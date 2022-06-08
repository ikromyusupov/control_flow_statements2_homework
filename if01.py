def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mx = a

    if mx < b:
        mx = b
        
    if mx < c:
        mx = c

    return mx