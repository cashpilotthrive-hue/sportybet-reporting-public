# Trillionbg SportyBet Reporting Package

**Status:** Public reporting workspace  
**Data:** Illustrative sample for review structure  
**Version:** 1.0.0  
**Last Updated:** 2026-09-27

---

## Executive Summary

This repository contains a professional reporting framework for disciplined, data-driven betting operations review. The package demonstrates a complete operational audit trail including:

- **Settlement Ledger** – Bet-by-bet tracking with NGN currency precision
- **Operational Dashboard** – Real-time KPI monitoring and risk metrics
- **Risk Compliance** – Automated control verification and loss-limit checks
- **Report Generator** – Reproducible, auditable CSV export pipeline

---

## Key Features

✅ **Transparent Risk Model**  
Fractional Kelly at 20% with hard stop-loss limits  

✅ **Compliance-Ready**  
All risk controls automated and logged  

✅ **Reproducible**  
Sample data clearly labeled; replace with verified exports for operational use  

✅ **Professional Grade**  
Investor-ready formatting and documentation  

---

## Files

| File | Purpose |
|------|----------|
| `scripts/alert_action_csv_generation.py` | Core report generator |
| `exports/Settlement_Ledger.csv` | Transaction-level audit trail |
| `exports/Operational_Dashboard.csv` | KPI summary and health checks |
| `exports/Risk_Compliance.csv` | Risk control verification |
| `INVESTOR_BRIEF.md` | Professional summary for stakeholders |
| `ZIP_EXPORT.py` | Package generator for distribution |

---

## Getting Started

### Generate Reports

```bash
python scripts/alert_action_csv_generation.py
```

Outputs to `exports/` directory.

### Create Distribution Package

```bash
python ZIP_EXPORT.py
```

Creates `trillionbg-sportybet-reporting-[DATE].zip`

---

## Important Disclaimers

⚠️ **Sample Data Only**  
This repository uses illustrative sample data. Replace values with verified account exports before operational use.

⚠️ **No Live Betting**  
This package does not connect to SportyBet, execute bets, or settle live transactions.

⚠️ **Not Financial Advice**  
Betting and sports wagering involve real risk of financial loss. Consult regulatory guidance.

---

## Client Profile

| Field | Value |
|-------|-------|
| Client | Trillionbg |
| Market | SportyBet |
| Currency | NGN (Nigerian Naira) |
| Risk Model | Fractional Kelly @ 20% |
| Opening Bankroll | ₦5,000,000 |
| Max Daily Loss | ₦250,000 |
| Confidence Floor | 75+ |
| Min Edge Required | 5%+ |

---

## Support & Documentation

- **Report Specs:** See `INVESTOR_BRIEF.md`
- **Data Import:** Provide verified account CSV exports
- **Customization:** Modify `scripts/alert_action_csv_generation.py`
- **Issues:** Use GitHub Issues

---

## License

MIT License – See LICENSE file

---

**Repository:** https://github.com/cashpilotthrive-hue/sportybet-reporting-public
