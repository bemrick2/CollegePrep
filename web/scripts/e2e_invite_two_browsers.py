"""
Cross-browser invitation regression against a real deployment (staging) and its real Supabase backend.

Two isolated browser contexts stand in for two devices: nothing is shared between them except the backend.

  A (parent):  create account -> create household -> add a child -> read the invite code/link
  B (student): open the invite link -> create a separate account -> join -> lands on the student app
  A again:     Household shows the child as "Has login"; still exactly one student
  B again:     reusing the same code is refused as "Already used"

Run by the project owner (it creates real accounts):

  pip install playwright
  E2E_BASE=https://college-optimizer-staging.netlify.app \
  E2E_EMAIL_PREFIX=you+pp-e2e \
  E2E_EMAIL_DOMAIN=example.com \
  E2E_PASSWORD='a long test password' \
  E2E_INVITE_EMAIL=student-inbox@example.com   # optional: also send the invitation email
  python web/scripts/e2e_invite_two_browsers.py

Requires email confirmation to be off for the project (or pre-confirmed accounts); the script stops with a clear
message if sign-up asks to confirm by email. It prints the two emails so the backend rows can be checked.
"""
import asyncio
import os
import sys
import time

from playwright.async_api import async_playwright, expect

BASE = os.environ.get("E2E_BASE", "https://college-optimizer-staging.netlify.app").rstrip("/")
PREFIX = os.environ.get("E2E_EMAIL_PREFIX", "pp-e2e")
DOMAIN = os.environ.get("E2E_EMAIL_DOMAIN")
PASSWORD = os.environ.get("E2E_PASSWORD")
STAMP = time.strftime("%Y%m%d%H%M%S")


async def sign_up(page, name, email):
    await page.get_by_label("Your first name").fill(name)
    await page.get_by_label("Email").fill(email)
    await page.get_by_label("Password").fill(PASSWORD)
    await page.get_by_role("button", name="Create account").click()
    try:
        await page.wait_for_url(lambda u: "/auth" not in u, timeout=15_000)
    except Exception:
        if await page.get_by_text("Check your email to confirm").count():
            sys.exit("Sign-up requires email confirmation; turn it off for staging or use pre-confirmed accounts.")
        raise


async def main():
    if not (DOMAIN and PASSWORD):
        sys.exit("Set E2E_EMAIL_DOMAIN and E2E_PASSWORD (see the docstring).")
    parent_email = f"{PREFIX}-parent-{STAMP}@{DOMAIN}"
    student_email = f"{PREFIX}-student-{STAMP}@{DOMAIN}"
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        a = await (await browser.new_context()).new_page()
        b = await (await browser.new_context()).new_page()  # separate storage: a second device

        # A: parent
        await a.goto(f"{BASE}/auth?role=parent")
        await expect(a.get_by_role("button", name="Create account")).to_be_visible()
        assert await a.get_by_text("Demo mode").count() == 0, "staging is running in demo mode"
        await sign_up(a, "E2E Parent", parent_email)
        await a.wait_for_url("**/onboarding/parent")
        await a.get_by_label("Household name").fill("E2E household")
        await a.get_by_role("button", name="Continue").click()
        await a.get_by_label("Student's first name").fill("Riley")
        await a.get_by_role("button", name="9", exact=True).click()
        await a.get_by_role("button", name="Continue").click()
        await a.get_by_role("button", name="Create household").click()
        invite_to = os.environ.get("E2E_INVITE_EMAIL")
        if invite_to:
            # Emails the student (server-side); the page still shows the link/code as a fallback.
            await a.get_by_label("Recipient email").fill(invite_to)
            await a.get_by_role("button", name="Send invitation").click()
            await expect(a.get_by_text("Invitation sent").or_(a.get_by_text("We couldn't send the email"))).to_be_visible(timeout=20_000)
            print("email:", "sent" if await a.get_by_text("Invitation sent").count() else "NOT sent (invite still valid)")
        else:
            await a.get_by_role("button", name="Copy invite link or code instead").click()
        code = (await a.get_by_test_id("invite-code").inner_text(timeout=20_000)).strip()
        assert len(code) == 64, f"expected a 64-character live code, got {code!r}"
        await expect(a.get_by_text("Valid for 72 hours")).to_be_visible()

        # B: student on their own device, via the invite link
        await b.goto(f"{BASE}/join?code={code}")
        await b.wait_for_url("**/auth?**")
        await sign_up(b, "Riley", student_email)
        await b.wait_for_url("**/join?code=*")
        await b.get_by_role("button", name="Join").click()
        await b.wait_for_url(lambda u: "/student" in u or "/onboarding/student" in u, timeout=20_000)

        # A: the child now has a login; still one student
        await a.goto(f"{BASE}/parent/household")
        await expect(a.get_by_text("Has login")).to_have_count(1, timeout=15_000)
        await expect(a.get_by_text("Not linked yet")).to_have_count(0)

        # B: the code cannot be used again
        await b.goto(f"{BASE}/join?code={code}")
        await b.get_by_role("button", name="Join").click()
        await expect(b.get_by_text("Invitation already used")).to_be_visible()

        # Invalid link
        await b.goto(f"{BASE}/join?code={'0' * 64}")
        await b.get_by_role("button", name="Join").click()
        await expect(b.get_by_text("Invalid invitation")).to_be_visible()

        await browser.close()
    print("PASS")
    print("parent:", parent_email)
    print("student:", student_email)


asyncio.run(main())
