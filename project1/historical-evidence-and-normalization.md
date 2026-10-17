# Historical financial input and normalization ledger

**Status: source check required before final recommendation.** The following are *values used by the Python model*, not all independently verified reported figures. Dollar amounts in millions.

| Model line | Current code value | Required primary-source comparison / normalization |
|---|---:|---|
| FY2026 revenue | 713,163 | Walmart FY2026 Form 10-K consolidated income statements; confirm revenue vs net sales |
| Opening cash | 10,727 | FY2026 balance sheet; verify restrictions and short-term investments |
| Opening inventory | 58,851 | FY2026 balance sheet |
| Opening PP&E | 136,083 | Balance sheet and PP&E note |
| Opening other assets | 79,007 | Model **plug**; replace with named components and check each |
| Accounts payable in 'floor_plan' slot | 63,061 | Verify Walmart payables; rename in a future version for clarity |
| Interest-bearing long debt | 38,166 | Verify current maturities and long-term notes |
| Short-term borrowings ('revolver') | 6,596 | Verify not mistaken for financing facility availability |
| Other liabilities | 70,958 | Model **plug**; replace with mapped reported accounts |
| Total equity including NCI | 105,887 | Reconcile controlling equity and noncontrolling interest separately |
| Diluted shares in valuation | 7,972.4 | Current script describes shares outstanding; **do not claim diluted until verified** |
| Depreciation, capex, working-capital basis | Forecast | Trace cash flow note and normalize historic ratios |

## Week 2 contamination catalog (complete from filings before finalization)

| Potential contamination | Evidence/date/location | Reported amount | Proposed adjustment | Adjusted base | Decision effect |
|---|---|---|---|---|---|
| One-time litigation / restructuring | PENDING | PENDING | PENDING | PENDING | PENDING |
| Gains/losses on investments and disposals | PENDING | PENDING | PENDING | PENDING | PENDING |
| Accounting classification or changed presentation | PENDING | PENDING | PENDING | PENDING | PENDING |
| Period mismatch, currency, unit or diluted/basic share basis | PENDING | PENDING | PENDING | PENDING | PENDING |
| Discontinued business / acquisition effects | PENDING | PENDING | PENDING | PENDING | PENDING |

**Rule:** An unobserved one-time item is not automatically zero. If none exists, cite the reviewed filing note. Freeze the reported → adjustment → normalized mapping and record analyst judgment.
