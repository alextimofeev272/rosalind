ss = open('D:\\python\input.txt').read().strip().split('\n')
n = len(ss)
db = dict([(s[:-1], s[1:]) for s in ss])
k = db.iterkeys().next()
s = ''
print db
while len(s) < n:
    print db[k][-1],db[k],k
    s += db[k][-1]
    k = db[k]
print (s)
