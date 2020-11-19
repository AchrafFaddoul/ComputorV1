def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

def find_gcd(list):
    res = list[0]
    for elm in list[1:]:
        if (elm % 1):
            return False
        res = gcd(res , elm)
    return res