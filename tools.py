def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)

def find_gcd(list):
    A = [12, 24, 27, 30, 33]
    res = list[0]
    for elm in list[1:]:
        res = gcd(res , elm)
    return res