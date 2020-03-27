import itertools
import math

x = []
N = 5
print math.factorial(N)
for i in range(N):
    x.append(i+1)
    
a = ''

for case in itertools.permutations(x):
    for i in range(N):
        a = a + str(case[i]) + ' '
    print a
    a = ''


