def mn(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mn = a
    if mn > b:
        mn = b

    if mn > c:
        mn = c
    return mn
