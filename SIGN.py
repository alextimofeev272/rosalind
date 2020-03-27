import itertools, math

N = 5
c = ''

a = list(itertools.permutations(range(1,N+1)))
b = list(itertools.product('-+', repeat=N))
print len(a)*len(b)
for i in b:
    for j in a:
        s = i
        d = j
        for k in range(N):
            if s[k] == '-':
                c = c + s[k] + str(d[k]) + ' '
            else:
                c = c + str(d[k]) + ' '
        print c
        c = ''
            
        



