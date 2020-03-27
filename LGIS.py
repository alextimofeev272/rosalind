def maxs(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]]) 
    return max(l, key=len)

def mins(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] > d[i]] or [[]], key=len) 
                  + [d[i]]) 
    return max(l, key=len)
 
file = open('D:\\python\input.txt')
text = file.read().replace('\n',' ').split(' ')
text2 = []

for i in range(len(text)-2):
    text2.append(int(text[i]))

d = [5,1,4,2,3]
c = '';
a = maxs(d)
for i in range(len(a)):
    c = c + str(a[i]) + ' '
print c
c = '';
a = mins(d)
for i in range(len(a)):
    c = c + str(a[i]) + ' '
print c

file.close()

