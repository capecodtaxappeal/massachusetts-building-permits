#!/usr/bin/env python3
"""Refresh the free Massachusetts building-permit sample from the public MassPermits feed.

Pulls https://masspermits.com/feed/permits.json (a masked public preview — town, trade,
project value, date), writes CSV/JSON/stats, and refreshes the README preview table.
No secrets, no scraping: it consumes MassPermits' own public feed. Runs weekly via
GitHub Actions so the sample is always fresh and the repo shows steady activity.
"""
import csv, io, json, re, subprocess, collections
from datetime import datetime, timezone
from pathlib import Path

FEED = "https://masspermits.com/feed/permits.json"
ROOT = Path(__file__).resolve().parent


def fetch(url: str) -> str:
    # curl (present on GitHub runners) — avoids any bot-fingerprint blocking of urllib.
    r = subprocess.run(["curl", "-fsS", "-A", "masspermits-sample-bot", url],
                       capture_output=True, text=True, timeout=60)
    r.check_returncode()
    return r.stdout


def money(v):
    try:
        return "${:,.0f}".format(float(v))
    except Exception:
        return "—"


def main():
    data = json.loads(fetch(FEED))
    rows = []
    for it in data.get("items", []):
        rows.append({
            "date": (it.get("date_published") or "")[:10],
            "town": it.get("_town", ""),
            "trade": it.get("_trade", ""),
            "value": it.get("_value") or "",
            "permit_page": it.get("url", ""),
        })
    rows.sort(key=lambda r: r["date"], reverse=True)

    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data" / "latest-permits.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")

    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=["date", "town", "trade", "value", "permit_page"])
    w.writeheader(); w.writerows(rows)
    (ROOT / "data" / "latest-permits.csv").write_text(buf.getvalue(), encoding="utf-8")

    by_town = collections.Counter(r["town"] for r in rows if r["town"])
    by_trade = collections.Counter(r["trade"] for r in rows if r["trade"])
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    (ROOT / "data" / "stats.json").write_text(json.dumps({
        "updated": updated, "sample_size": len(rows),
        "by_town": dict(by_town.most_common(15)), "by_trade": dict(by_trade.most_common()),
        "source": "https://masspermits.com/feed/permits.json",
    }, indent=1), encoding="utf-8")

    # Refresh the README preview table between the STATS markers.
    tbl = ["| Date | Town | Trade | Est. project value |", "|---|---|---|---|"]
    for r in rows[:15]:
        tbl.append(f"| {r['date']} | {r['town']} | {r['trade']} | {money(r['value'])} |")
    top_towns = ", ".join(f"{t} ({n})" for t, n in by_town.most_common(8))
    block = (f"**Updated {updated}** — {len(rows)} recent Massachusetts building permits in this sample. "
             f"Busiest towns: {top_towns}.\n\n" + "\n".join(tbl))
    readme_p = ROOT / "README.md"
    readme = readme_p.read_text(encoding="utf-8")
    readme = re.sub(r"<!--STATS-->.*?<!--/STATS-->",
                    "<!--STATS-->\n" + block + "\n<!--/STATS-->", readme, flags=re.S)
    readme_p.write_text(readme, encoding="utf-8")
    print(f"updated: {len(rows)} permits across {len(by_town)} towns, {len(by_trade)} trades")


if __name__ == "__main__":
    main()
