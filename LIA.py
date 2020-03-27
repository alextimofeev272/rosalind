import math
                             
def P(n, k):
    return (math.factorial(2**k)/(math.factorial(n) * math.factorial((2**k) - n)))*(0.25**n) * (0.75)**((2**k) - n)

def problem(k, N):
    p = 1
    for n in range(N):
        p = p - P(n, k)
    return p

k = 7
N = 36
print problem(k,N)

