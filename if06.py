def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n % 10
    n //= 10
    x2 = n % 10
    n //= 10
    x3 = n % 10
    n //= 10
    x4 = n % 10
    n //= 10
    x5 = n % 10
    n //= 10
    ix = 1
    mx = x1
    if mx < x2:
        mx = x2
        ix = 2
    if mx < x3:
        mx = x3
        ix = 3
    if mx < x4:
        mx = x4
        ix = 4
    if mx < x5:
        mx = x5
        ix = 5
    
    return ix
