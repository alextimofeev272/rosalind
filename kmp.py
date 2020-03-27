def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] <> s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

o=''
#file1 = open('D:\\python\input.txt')
#file2 = open('D:\\python\output.txt','w')
s = 'CAGCATGGTATCACAGCAGAG'#.join(file1.read().split('\n'))
a = prefix(s)

for i in a:
    o = o + str(i) + ' '

print o


#file1.close()
#file2.close()

#print 'end'
