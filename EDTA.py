import numpy

def string(text):
    results = []
    strings = text.strip().split('>')
    for s in strings:
        if len(s):
            parts = s.split()
            k = parts[0]
            v = ''.join(parts[1:])
            results.append(v)
    return results

file = open('D:\\python\input.txt')
text = file.read()
s = string(text)

s1 = s[0]#'PRETTY'
s2 = s[1]#'PRTTEIN'

dist=[[0]*(len(s2)+1) for i in xrange(len(s1)+1)]
for i in xrange(len(s1)+1):
    dist[i][0]=i
for j in xrange(len(s2)+1):
    dist[0][j]=j

def editDistance(s1,s2,dist):
    for i in xrange(1,len(s1)+1):
        for j in xrange(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dist[i][j]=dist[i-1][j-1]
            else:
                dist[i][j]=min(dist[i-1][j-1], dist[i-1][j], dist[i][j-1])+1
    return dist[len(s1)][len(s2)]

def traceback(dist,s1,s2):
    t1, t2, i, j = '', '', len(s1), len(s2)
    while not (i==0 and j==0):
        l, d, t = dist[i][j-1], dist[i-1][j-1], dist[i-1][j]
        if s1[i-1] == s2[j-1] or (d==min(l,d,t) and d<l and d<t):
            t1, t2, i, j = s1[i-1]+t1, s2[j-1]+t2, i-1, j-1
        elif t == min(l,d,t):
            t1, t2, i, j = s1[i-1]+t1, '-'+t2, i-1, j
        elif l == min(l,d,t):
            t1, t2, i, j='-'+t1, s2[j-1]+t2, i, j-1
    return t1, t2

print editDistance(s1,s2,dist)
#print traceback(dist,s1,s2)

