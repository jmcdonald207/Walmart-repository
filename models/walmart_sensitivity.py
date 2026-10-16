"""Lab 11: reproducible one-driver-at-a-time Walmart sensitivity.
Uses the actual pro-forma engine; no invented output numbers.
Run from repository root: python models/walmart_sensitivity.py
"""
import copy
import importlib.util
from pathlib import Path

source = Path(__file__).with_name("walmart_proforma.py")
spec = importlib.util.spec_from_file_location("walmart_proforma", source)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)

BASE = copy.deepcopy(model.A)
# Judgement ranges are illustrative until supported by historical evidence.
SHIFTS = {"gross_margin": 0.005, "sga_ratio": 0.01}

def evaluate(assumptions):
    model.A = copy.deepcopy(assumptions)
    rows = model.project()
    model.assert_balanced(rows)
    equity, terminal_share, price = model.value(rows)
    return {
        "operating_income": rows[-1]["op_income"],
        "fcfe": rows[-1]["fcfe"],
        "price": price,
        "balance_gap": max(abs(r["gap"]) for r in rows),
        "terminal_share": terminal_share,
    }

def main():
    try:
        baseline = evaluate(BASE)
        print("BASE", baseline)
        for key, shift in SHIFTS.items():
            print("\nDRIVER:", key, "shift", shift, "absolute ratio points")
            cases = {}
            for name, direction in (("lower", -1), ("base", 0), ("higher", 1)):
                inputs = copy.deepcopy(BASE)
                inputs[key] = [v + direction * shift for v in BASE[key]]
                result = evaluate(inputs)
                cases[name] = result
                print(name, "values:", inputs[key])
                print(" outputs:", result)
                print(" changes from base:", {
                    k: result[k] - baseline[k]
                    for k in ("operating_income", "fcfe", "price")
                })
            print("OUTPUT SPANS:", {
                k: max(v[k] for v in cases.values()) - min(v[k] for v in cases.values())
                for k in ("operating_income", "fcfe", "price")
            })
        restored = evaluate(BASE)
        for key in ("operating_income", "fcfe", "price"):
            if abs(restored[key] - baseline[key]) > 1e-6:
                raise AssertionError("Base restoration mismatch: " + key)
        print("\nRESTORED BASE PASS", restored)
    finally:
        model.A = BASE

if __name__ == "__main__":
    main()
