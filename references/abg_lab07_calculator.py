"""Simple peer P/E valuation using only Python's standard library."""

from fractions import Fraction


# EDIT THESE INPUTS. Use numbers or decimal strings; use None for missing data.
TARGET = {
    "name": "Asbury Automotive (ABG)",
    "diluted_eps": "21.50",
}

PEERS = [
    {"name": "AutoNation (AN)", "price": "169.84", "diluted_eps": "16.92"},
    {"name": "Group 1 Automotive (GPI)", "price": "421.48", "diluted_eps": "36.81"},
]


def positive_fraction(value):
    """Return an exact positive Fraction, or None for missing/invalid values."""
    if value is None or isinstance(value, bool):
        return None
    try:
        number = Fraction(str(value).strip())
    except (ValueError, ZeroDivisionError):
        return None
    return number if number > 0 else None


def median(values):
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def format_fixed(value, places):
    """Format a Fraction with round-half-even, without changing stored precision."""
    scale = 10**places
    scaled_numerator = value.numerator * scale
    quotient, remainder = divmod(scaled_numerator, value.denominator)
    twice_remainder = remainder * 2
    if twice_remainder > value.denominator or (
        twice_remainder == value.denominator and quotient % 2
    ):
        quotient += 1
    whole, fraction = divmod(quotient, scale)
    if places == 0:
        return str(whole)
    return f"{whole}.{fraction:0{places}d}"


def dollar(value):
    sign = "-" if value < 0 else ""
    return f"{sign}${format_fixed(abs(value), 2)}"


def unique_peers(target_name, peers):
    target_key = str(target_name).strip().casefold()
    seen = set()
    result = []
    for index, peer in enumerate(peers, 1):
        name = str(peer.get("name", "")).strip()
        key = name.casefold()
        if not key:
            name = f"Unnamed peer {index}"
            key = name.casefold()
        if key == target_key:
            print(f"Excluded {name}: same as target.")
        elif key in seen:
            print(f"Excluded {name}: duplicate peer.")
        else:
            seen.add(key)
            result.append({**peer, "name": name})
    return result


def usable_multiples(peers):
    usable = []
    for peer in peers:
        price = positive_fraction(peer.get("price"))
        eps = positive_fraction(peer.get("diluted_eps"))
        if price is not None and eps is not None:
            usable.append((peer["name"], price / eps))
    return usable


def median_implied_price(peers, target_eps):
    multiples = [multiple for _, multiple in usable_multiples(peers)]
    if not multiples or target_eps is None:
        return None
    return median(multiples) * target_eps


def main():
    target_name = str(TARGET.get("name", "Target")).strip() or "Target"
    target_eps = positive_fraction(TARGET.get("diluted_eps"))
    peers = unique_peers(target_name, PEERS)

    print(f"\nTarget: {target_name}")
    if target_eps is None:
        print("Target diluted EPS: not meaningful (missing or nonpositive)")
    else:
        print(f"Target diluted EPS: {format_fixed(target_eps, 6)}")

    print("\nPeer P/E multiples:")
    usable = []
    for peer in peers:
        price = positive_fraction(peer.get("price"))
        eps = positive_fraction(peer.get("diluted_eps"))
        if price is None or eps is None:
            reasons = []
            if price is None:
                reasons.append("price")
            if eps is None:
                reasons.append("diluted EPS")
            print(
                f"  {peer['name']}: not meaningful "
                f"(missing or nonpositive {' and '.join(reasons)})"
            )
        else:
            multiple = price / eps
            usable.append((peer["name"], multiple))
            print(f"  {peer['name']}: {format_fixed(multiple, 6)}x")

    print("\nValuation:")
    if not usable:
        print("  No usable peers.")
    else:
        multiples = [multiple for _, multiple in usable]
        median_multiple = median(multiples)
        print(f"  Median peer P/E: {format_fixed(median_multiple, 6)}x")
        if target_eps is None:
            print("  Implied price calculation: not meaningful (target diluted EPS is missing or nonpositive).")
        elif len(multiples) == 1:
            print(f"  Reference estimate (no range): {dollar(median_multiple * target_eps)}")
        else:
            print(f"  Minimum implied price: {dollar(min(multiples) * target_eps)}")
            print(f"  Median implied price:  {dollar(median_multiple * target_eps)}")
            print(f"  Maximum implied price: {dollar(max(multiples) * target_eps)}")

    print("\nPeer-removal sensitivity (median-implied price):")
    if not peers:
        print("  No peers to remove.")
        return

    full_estimate = median_implied_price(peers, target_eps)
    for removed_index, peer in enumerate(peers):
        remaining = peers[:removed_index] + peers[removed_index + 1 :]
        remaining_usable = usable_multiples(remaining)
        if not remaining_usable:
            print(f"  Remove {peer['name']}: no estimate (no usable peers remain).")
            continue
        estimate = median_implied_price(remaining, target_eps)
        if estimate is None or full_estimate is None:
            print(
                f"  Remove {peer['name']}: estimate and dollar change not meaningful "
                "(target diluted EPS is missing or nonpositive)."
            )
            continue
        change = estimate - full_estimate
        descriptor = "reference estimate" if len(remaining_usable) == 1 else "estimate"
        change_sign = "+" if change > 0 else ""
        print(
            f"  Remove {peer['name']}: {dollar(estimate)} ({descriptor}); "
            f"change {change_sign}{dollar(change)}"
        )


if __name__ == "__main__":
    main()
