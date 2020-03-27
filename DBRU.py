file = open('D:\\python\input.txt')
s = []
for i in file.readlines():
        s.append(i.replace('\n',''))
d = [];
#k = len(s[0])-1
#print len(s[0]),k
k = 3 

def reverse(s):
        s1 = ''
        for i in s:
                if i=='A': s1 = 'T'+s1
                if i=='G': s1 = 'C'+s1
                if i=='C': s1 = 'G'+s1
                if i=='T': s1 = 'A'+s1
        return s1

for i in s:
        d.append(reverse(i))
        
q = set(s)|set(d)
print q

for i in q:
        otv = '('+i[:k]+', '+i[1:k+1]+')'
        print otv
        
