def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
A = [12, 24, 27, 30, 33]
res = A[0]
for c in A[1:]:
    res = gcd(res , c)
    print('inside', res)
print(res)