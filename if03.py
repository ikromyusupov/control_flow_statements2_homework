from if01 import mx
from if02 import mn

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
    kt = mx(a,b,c)
    kc = mn(a,b,c)
    if kt == a and kc == c:
        return b
    elif kt == b and kc == a:
        return c
    else :
        return a
