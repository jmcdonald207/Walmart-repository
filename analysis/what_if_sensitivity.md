# Walmart Pro Forma Sensitivity Analysis

**Company:** Walmart Inc. (WMT)  
**Model:** Five-year FCFE pro forma  
**Currency:** USD millions except per-share values  
**Final forecast year:** FY2031

## Sensitivity Inputs

| Driver | Case | FY2027 | FY2028 | FY2029 | FY2030 | FY2031 | Unit |
|---|---|---:|---:|---:|---:|---:|---|
| Gross margin | Lower | 23.75% | 23.80% | 23.85% | 23.90% | 23.95% | % of net sales |
| Gross margin | Base | 24.25% | 24.30% | 24.35% | 24.40% | 24.45% | % of net sales |
| Gross margin | Higher | 24.75% | 24.80% | 24.85% | 24.90% | 24.95% | % of net sales |
| SG&A ÷ gross profit | Lower | 85.20% | 84.90% | 84.60% | 84.30% | 84.00% | % of gross profit |
| SG&A ÷ gross profit | Base | 86.20% | 85.90% | 85.60% | 85.30% | 85.00% | % of gross profit |
| SG&A ÷ gross profit | Higher | 87.20% | 86.90% | 86.60% | 86.30% | 86.00% | % of gross profit |

## Results

| Driver | Case | FY2031 operating income | Δ from base | FY2031 FCFE | Δ from base | Value/share | Δ from base | Balance gap | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Gross margin | Lower | 40,112.4 | −638.4 | 14,389.3 | −613.9 | $27.73 | −$1.25 | 0.0 | Valid |
| Gross margin | Base | 40,750.8 | 0.0 | 15,003.2 | 0.0 | $28.98 | $0.00 | 0.0 | Valid |
| Gross margin | Higher | 41,389.1 | +638.4 | 15,617.1 | +613.9 | $30.23 | +$1.25 | 0.0 | Valid |
| SG&A ÷ gross profit | Lower | 42,831.9 | +2,081.2 | 16,891.6 | +1,888.4 | $32.72 | +$3.74 | 0.0 | Valid |
| SG&A ÷ gross profit | Base | 40,750.8 | 0.0 | 15,003.2 | 0.0 | $28.98 | $0.00 | 0.0 | Valid |
| SG&A ÷ gross profit | Higher | 38,669.6 | −2,081.2 | 13,114.8 | −1,888.4 | $25.24 | −$3.74 | 0.0 | Valid |

## Output Spans

| Driver | Operating-income span | FCFE span | Value/share span |
|---|---:|---:|---:|
| Gross margin | 1,276.8 | 1,227.8 | $2.51 |
| SG&A ÷ gross profit | 4,162.3 | 3,776.8 | $7.48 |

## Final Restored-Base Check

| FY2031 operating income | FY2031 FCFE | Value/share | Balance gap | Cash-floor gap | Status |
|---:|---:|---:|---:|---:|---|
| 40,750.8 | 15,003.2 | $28.98 | 0.0 | 0.0 | Valid |

## Reproduction

The sensitivity runner preserves separate base inputs, creates a fresh deep copy for every case, changes one independent driver per run, and restores and reruns the base at the end.

```powershell
python walmart_proforma.py
python walmart_sensitivity.py
```

Required repository files:

- `walmart_proforma.py`
- `walmart_sensitivity.py`
- `walmart_github_submission.md`
