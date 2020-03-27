#coding: utf_8
#ищет надстроку
s1='ATCTGAT'
s2='TGCATA'


S = [ [""]*(len(s2)+1) for _ in xrange(len(s1)+1) ]

for i in xrange(1,len(s1)+1):
    S[i][0] = s1[:i]
for j in xrange(1,len(s2)+1):
    S[0][j] = s2[:j]
for i in xrange(len(s1)+1):
    print S[i]

for i in xrange(1,len(s1)+1):
    for j in xrange(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            print i,j,S[i-1][j-1] + s1[i-1]
            S[i][j] = S[i-1][j-1] + s1[i-1]
        else:
            print i,j,S[i][j-1] + s2[j-1], S[i-1][j] + s1[i-1]
            S[i][j] = min([ S[i][j-1] + s2[j-1], S[i-1][j] + s1[i-1]], key = len)

print S[len(s1)][len(s2)]


















