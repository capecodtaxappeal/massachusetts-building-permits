# Massachusetts Building Permits — Free Weekly Sample

A free, auto-updated sample of **Massachusetts building-permit data** — the earliest public signal of upcoming construction, renovation, roofing, solar, HVAC, electrical, plumbing and remodeling work across the state.

Every building permit is a homeowner who was *just approved to spend money* on their property. For contractors, that's the best lead there is — reach them before five competitors do.

This repo publishes a **masked weekly preview** (town, trade, project value, date). The **full leads** — exact street address, property owner, and the contractor on file — live at **[masspermits.com](https://masspermits.com)**.

> 👉 **[Get a free sample of the full Massachusetts permit data →](https://masspermits.com)**

## This week's sample

<!--STATS-->
**Updated 2026-07-06** — 100 recent Massachusetts building permits in this sample. Busiest towns: Boston (34), Dorchester (12), Braintree (10), Roslindale (6), Roxbury (6), Jamaica Plain (6), Mattapan (5), Hyde Park (5).

| Date | Town | Trade | Est. project value |
|---|---|---|---|
| 2026-07-06 | Braintree | Other | — |
| 2026-07-06 | Hingham | Electrical | — |
| 2026-07-06 | Hingham | Other | — |
| 2026-07-05 | Braintree | Other | — |
| 2026-07-05 | Braintree | Windows/Doors/Siding | — |
| 2026-07-05 | Braintree | Kitchen/Bath | — |
| 2026-07-04 | Braintree | Other | — |
| 2026-07-04 | Braintree | Roofing | — |
| 2026-07-04 | Braintree | Plumbing | — |
| 2026-07-03 | Brighton | Electrical | $16,000 |
| 2026-07-03 | Brighton | Plumbing | $5,000 |
| 2026-07-03 | Braintree | Kitchen/Bath | — |
| 2026-07-03 | Braintree | Plumbing | — |
| 2026-07-03 | Braintree | HVAC | — |
| 2026-07-02 | Charlestown | Electrical | $5,000 |
<!--/STATS-->

Full files: [`data/latest-permits.csv`](data/latest-permits.csv) · [`data/latest-permits.json`](data/latest-permits.json) · [`data/stats.json`](data/stats.json)

## Free sample vs. full lead

| Field | This free sample | Full lead at masspermits.com |
|---|---|---|
| Town, trade, date, project value | ✅ | ✅ |
| Exact street address | 🔒 masked | ✅ |
| Property owner name | 🔒 | ✅ |
| Contractor on file | 🔒 | ✅ |
| Sortable file, refreshed weekly | — | ✅ |

- 🆓 **Free sample:** [masspermits.com](https://masspermits.com)
- 📦 **One-time lead pack:** $49
- 🔁 **Live weekly feed:** $99/mo

## Browse by town & trade

Every Massachusetts town and trade has its own page and machine-readable feed:

- **All towns & trades:** https://masspermits.com/permits/
- **RSS feed:** https://masspermits.com/feed.xml
- **JSON API:** https://masspermits.com/feed/permits.json

## How this updates

A weekly [GitHub Action](.github/workflows/update.yml) pulls the public [MassPermits JSON feed](https://masspermits.com/feed/permits.json) and regenerates the sample files above — no scraping, no keys, fully automated.

## About

Data is compiled from **public municipal building-permit records** across Massachusetts (Greater Boston, Cape Cod, and expanding). Not affiliated with any municipality.

**[MassPermits](https://masspermits.com)** — building-permit leads for Massachusetts contractors: roofers, solar installers, HVAC, electricians, plumbers, remodelers, GCs and more.

## License

Sample data and code are released under the [MIT License](LICENSE). The underlying permit records are public records.
