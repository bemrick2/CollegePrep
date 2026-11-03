"""The Stripe webhook endpoint subscribes to exactly the events the webhook handles (A4, docs/product/STRIPE_BILLING.md).

Unhandled types (disputes, reviews, Radar) can name a person without naming a customer or subscription, so a household
deletion could never de-identify them; the webhook stores any that arrive de-identified, but the endpoint must not
ask for them. scripts/stripe/setup_billing.mjs creates the endpoint from its EVENTS list.
"""
import re, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def string_list(text: str, start: str) -> set[str]:
    body = text[text.index(start):]
    body = body[:body.index(']') + 1]
    return set(re.findall(r"'([a-z_.]+)'", body))


class StripeWebhookEventsTests(unittest.TestCase):
    def test_endpoint_events_equal_handled_events(self):
        handled = string_list((ROOT / 'supabase/functions/_shared/billing.ts').read_text(), 'export const HANDLED_EVENTS')
        endpoint = string_list((ROOT / 'scripts/stripe/setup_billing.mjs').read_text(), 'const EVENTS')
        self.assertGreaterEqual(len(handled), 9)
        self.assertEqual(endpoint, handled)

    def test_webhook_marks_unhandled_events_for_deidentification(self):
        hook = (ROOT / 'supabase/functions/stripe-webhook/index.ts').read_text()
        self.assertIn('p_store_raw: storeRawBillingEvent(event.type)', hook)
        self.assertIn('if (hhError) throw hhError', hook)


if __name__ == '__main__':
    unittest.main()
