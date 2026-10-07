"""Fail before credentials/network work while the owner hold is active."""
import json
from pathlib import Path

def require_live_writes():
    path = Path(__file__).resolve().parents[1] / '.operations/supabase-live-hold.json'
    try:
        state = json.loads(path.read_text())
    except (OSError, ValueError):
        raise SystemExit('Live write control missing or invalid; refusing database writes.')
    if state.get('hold') is not False:
        raise SystemExit('CollegePrep live database writes are on hold. See docs/SUPABASE_PAUSE.md.')

if __name__ == '__main__':
    require_live_writes()
