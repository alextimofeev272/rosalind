#coding: utf_8
N = 10
S = 'AG'
p = [0.25,0.5,0.75]
otv=''
for i in p:
    pr = 1
    for j in S:
        if j == 'A' or j == 'T':
            pr = pr*((1-i)/2)
        if j == 'C' or j == 'G':
            pr = pr*((i)/2)
    if pr<>0:
        a = 1/pr
        #так как возможно пересечение N+1-len(s)
        otv = otv + str(round((N+1-len(S))/a, 3)) + ' '
    else:
        otv = otv + str(0.000) + ' '
    
print otv
