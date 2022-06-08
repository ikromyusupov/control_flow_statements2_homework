# from if01 import mx
# from if02 import mn

def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """

    if a <= b <= c or a >= b >= c:
        return b
    elif b <= a <= c or b >= a >= c:
        return a
    elif a <= c <= b or a >= c >= b:
        return c
    # kt = mx(a,b,c)
    # kc = mn(a,b,c)
    # if kt == a and kc == c:
    #     return b
    # elif kt == b and kc == a:
    #     return c
    # else :
    #     return a
