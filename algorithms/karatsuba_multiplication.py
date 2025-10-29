def karatsuba(x, y):
    """Multiply two integers."""

    # Only use automatic multplication for two single digit numbers
    if x < 10 and y < 10:
        return x * y
    
    x_str, y_str = str(x), str(y)
    max_len = max(len(x_str), len(y_str))

    # Zero-pad from left to same length
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)
    midpoint = max_len // 2

    # Split from right, as the powers of 10 only make sense if both numbers
    # are split at the same "digit position" from the right side, e.g.:
    #   x=12345, y=678
    #   splitting from left: a=12, b=345, c=6, d=78 -> a corresponds to 10**3, c to 10**2
    #   splitting from right: a=123, b=45, c=6, d=78 -> both a and c correspond to 10**2
    a, b = int(x_str[:-midpoint]), int(x_str[-midpoint:])
    c, d = int(y_str[:-midpoint]), int(y_str[-midpoint:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    q = karatsuba(a + b, c + d)
    ad_plus_bc = q - ac - bd

    return 10 ** (2 * midpoint) * ac + 10 ** midpoint * ad_plus_bc + bd
