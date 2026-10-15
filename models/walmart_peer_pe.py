"""Peer P/E valuation for Walmart (standard library only).

Edit TARGET and PEERS below. Enter numeric values as strings so Decimal keeps
their exact entered precision. Price means current share price; diluted_eps
must be diluted EPS on the same basis and period for every company.
"""

from decimal import Decimal, InvalidOperation
from statistics import median


# ----------------------------- EDIT INPUTS HERE -----------------------------
TARGET = {
    "ticker": "WMT",
    # Latest annual diluted EPS public by the January 1, 2025 comparison date.
    "diluted_eps": "1.91",
    "eps_fiscal_period": "Fiscal year ended January 31, 2024",
    "eps_publication_date": "March 15, 2024",
}

# Walmart reverse DCF inputs copied from Reverse DCF.md. These use a later
# valuation date than the EPS above, so the program labels the dates clearly.
REVERSE_DCF = {
    "valuation_date": "September 9, 2026",
    "share_price": "105.83",
    "implied_share_price": "105.83",
    "implied_five_year_fcff_growth": "22.3",
    "terminal_growth_rate": "2.5",
    "wacc": "7.0",
}

PEERS = [
    # Replace None values with your chosen price and diluted EPS figures.
    {"ticker": "COST", "price": None, "diluted_eps": None},
    {"ticker": "TGT", "price": None, "diluted_eps": None},
    {"ticker": "DG", "price": None, "diluted_eps": None},
    {"ticker": "DLTR", "price": None, "diluted_eps": None},
    {"ticker": "BJ", "price": None, "diluted_eps": None},
]
# ---------------------------------------------------------------------------


def positive_decimal(value):
    """Return a positive finite Decimal, or None when it is not meaningful."""
    if value is None or isinstance(value, bool):
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        return None
    return number if number.is_finite() and number > 0 else None


def normalized_ticker(value):
    return str(value).strip().upper()


def unique_peers(peers, target_ticker):
    """Keep the first occurrence of each peer, case-insensitively."""
    result = []
    seen = set()
    for peer in peers:
        ticker = normalized_ticker(peer.get("ticker", ""))
        if not ticker or ticker == target_ticker or ticker in seen:
            continue
        seen.add(ticker)
        result.append(
            {
                "ticker": ticker,
                "price": peer.get("price"),
                "diluted_eps": peer.get("diluted_eps"),
            }
        )
    return result


def peer_multiple(peer):
    price = positive_decimal(peer["price"])
    eps = positive_decimal(peer["diluted_eps"])
    return None if price is None or eps is None else price / eps


def fmt_multiple(value):
    return f"{value:.6f}x"


def fmt_price(value):
    return f"${value:.2f}"


def fmt_signed_price(value):
    sign = "+" if value >= 0 else "-"
    return f"{sign}${abs(value):.2f}"


def print_side_by_side_dcf_and_eps(target_eps):
    """Print the reverse-DCF headline and historical EPS in adjacent columns."""
    dcf_price = positive_decimal(REVERSE_DCF.get("implied_share_price"))
    dcf_price_label = fmt_price(dcf_price) if dcf_price is not None else "not meaningful"
    eps_label = fmt_price(target_eps) if target_eps is not None else "not meaningful"
    left_width = 48

    rows = [
        ("Walmart reverse DCF", "Walmart diluted EPS"),
        (
            f"Implied share price: {dcf_price_label}",
            f"Diluted EPS: {eps_label}",
        ),
        (
            f"Valuation date: {REVERSE_DCF.get('valuation_date', 'unresolved')}",
            TARGET.get("eps_fiscal_period", "Fiscal period: unresolved"),
        ),
        (
            "Implied five-year FCFF growth: "
            f"{REVERSE_DCF.get('implied_five_year_fcff_growth', 'unresolved')}%",
            f"Publication date: {TARGET.get('eps_publication_date', 'unresolved')}",
        ),
        (
            f"Terminal growth: {REVERSE_DCF.get('terminal_growth_rate', 'unresolved')}%",
            "Different dates; no direct DCF/EPS multiple.",
        ),
    ]

    print("\nReverse DCF and EPS:")
    print(f"  {rows[0][0]:<{left_width}} | {rows[0][1]}")
    print(f"  {'-' * left_width}-+-{'-' * 43}")
    for left, right in rows[1:]:
        print(f"  {left:<{left_width}} | {right}")


def main():
    target_ticker = normalized_ticker(TARGET.get("ticker", "")) or "TARGET"
    target_eps = positive_decimal(TARGET.get("diluted_eps"))
    peers = unique_peers(PEERS, target_ticker)
    multiples = [(peer["ticker"], peer_multiple(peer)) for peer in peers]
    valid = [(ticker, multiple) for ticker, multiple in multiples if multiple is not None]

    print(f"Target: {target_ticker}")
    print(
        f"Target diluted EPS: {TARGET.get('diluted_eps')}"
        if target_eps is not None
        else "Target diluted EPS: not meaningful"
    )
    print_side_by_side_dcf_and_eps(target_eps)
    print("\nPeer P/E multiples:")
    if not peers:
        print("  No peer inputs after deduplication and target exclusion.")
    for ticker, multiple in multiples:
        label = fmt_multiple(multiple) if multiple is not None else "not meaningful"
        print(f"  {ticker}: {label}")

    print("\nValuation:")
    if not valid:
        print("  No usable peers.")
        full_estimate = None
    else:
        values = [multiple for _, multiple in valid]
        median_multiple = median(values)
        full_estimate = median_multiple * target_eps if target_eps is not None else None

        if len(values) == 1:
            print(f"  Peer P/E: {fmt_multiple(values[0])}")
            if full_estimate is None:
                print("  Reference estimate: not meaningful (target EPS is missing or nonpositive).")
            else:
                print(f"  Reference estimate: {fmt_price(full_estimate)} (no range)")
        else:
            minimum_multiple = min(values)
            maximum_multiple = max(values)
            print(f"  Minimum peer P/E: {fmt_multiple(minimum_multiple)}")
            print(f"  Median peer P/E:  {fmt_multiple(median_multiple)}")
            print(f"  Maximum peer P/E: {fmt_multiple(maximum_multiple)}")
            if target_eps is None:
                print("  Minimum implied price: not meaningful (target EPS is missing or nonpositive).")
                print("  Median implied price:  not meaningful (target EPS is missing or nonpositive).")
                print("  Maximum implied price: not meaningful (target EPS is missing or nonpositive).")
            else:
                print(f"  Minimum implied price: {fmt_price(minimum_multiple * target_eps)}")
                print(f"  Median implied price:  {fmt_price(full_estimate)}")
                print(f"  Maximum implied price: {fmt_price(maximum_multiple * target_eps)}")

    print("\nPeer-removal sensitivity:")
    if not peers:
        print("  No peers to remove.")
    for removed_peer in peers:
        remaining = [
            multiple
            for ticker, multiple in multiples
            if ticker != removed_peer["ticker"] and multiple is not None
        ]
        prefix = f"  Remove {removed_peer['ticker']}: "
        if not remaining:
            print(prefix + "no estimate")
        elif target_eps is None or full_estimate is None:
            print(prefix + "not meaningful (target EPS is missing or nonpositive)")
        else:
            removal_estimate = median(remaining) * target_eps
            dollar_change = removal_estimate - full_estimate
            print(
                prefix
                + f"{fmt_price(removal_estimate)}; change {fmt_signed_price(dollar_change)}"
            )


if __name__ == "__main__":
    main()
