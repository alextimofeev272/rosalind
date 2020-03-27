from Bio.SubsMat.MatrixInfo import blosum62

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
a = 11
b = 1

s1 ='WDHEDGMLCLHLLVKCFGKYKKDTLDVMEGSVWQFIAPHMPSSISWYAGRTTFMYTFRICIFITMHSITVNLKSRWFI'
s2 ='WDHEDHLLVKCFGKYKKWTLDVMEQFIAPYMPSSISWYAGRTTFMYTYEQYFRIFNLKQRWFI'

m = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]
ix = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]
iy = [[0]*(len(s2)+1) for i in xrange(len(s1)+1)]

for i in xrange(1,len(s1)+1):
    m[i][0] = -100;ix[i][0]=-b-(i-1)*a;iy[i][0]=-100;
for j in xrange(1,len(s2)+1):
    m[0][j] = -100;ix[0][j]=-100;iy[0][j]=-b-(j-1)*a;

l1, l2 = len(s1), len(s2)

for i in xrange(1,l1+1):
    for j in xrange(1,l2+1):
        sc = blosum62.get((s1[i-1], s2[j-1]))
        if sc == None:
            sc = blosum62.get((s2[j-1], s1[i-1]))
        m[i][j]  =max(m[i-1][j-1]+sc,ix[i-1][j-1]+sc,iy[i-1][j-1]+sc)
        ix[i][j] =max(m[i-1][j]-b,ix[i-1][j]-a,iy[i-1][j]-b)
        iy[i][j] =max(m[i][j-1]-b,ix[i-1][j]-b,iy[i][j-1]-a)
       
                         
print max(m[l1][l2],ix[l1][l2],iy[l1][l2])

def traceback(dist,s1,s2):
    t1, t2, i, j = '', '', len(s1), len(s2)
    while not (i==0 and j==0):
        l, d, t = dist[i][j-1], dist[i-1][j-1], dist[i-1][j]
        if s1[i-1] == s2[j-1] or (d==max(l,d,t) and d>l and d>t):
            t1, t2, i, j = s1[i-1]+t1, s2[j-1]+t2, i-1, j-1
        elif t == max(l,d,t):
            t1, t2, i, j = s1[i-1]+t1, '-'+t2, i-1, j
        elif l == max(l,d,t):
            t1, t2, i, j='-'+t1, s2[j-1]+t2, i, j-1
    return t1, t2

t1,t2 = traceback(m,s1,s2)
print t1
print t2






