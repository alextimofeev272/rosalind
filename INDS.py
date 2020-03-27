import math

def binom(n,k,p):
    C = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    P = C*(p**k)*((1-p)**(n-k))
    return P

n = 43; b = 0; o = []; st = '';
for k in range(2*n):
    b += binom(2*n,k,0.5)
    o.append(math.log(b,10))
for i in range(len(o)-1,-1,-1):
    st = st + '%.3f'%o[i] + ' '

print st
    
