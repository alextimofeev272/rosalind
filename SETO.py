#coding: utf_8
#операции над множества в питоне

#из sset: кол-во подмножеств 2**N
#множества задаются фигурными скобками

def f(D):
    D=D.replace('{','').replace('}','')
    D=D.replace(' ','').replace('\n','')
    S=D.split(',')
    E={int(S[0])}
    for i in range(1,len(S)):
        E.add(int(S[i]))
    return E
def w(A):
    s = '{'
    for elem in A:
        s = s+str(elem)+', '
    s = s[:len(s)-2]+'}\n'
    return s

file1 = open('D:\\python\input.txt')
file2 = open('D:\\python\output.txt','w')
S1 = file1.readline()
S2 = file1.readline()

A = f(S1);B = f(S2);
U = {i for i in range(1,17547)}


file2.write(w(A|B)) #сложение(объеденение) множеств
file2.write(w(A&B))#пересечение множеств
file2.write(w(A - B))#разность множеств
file2.write(w(B - A))#разность множеств
file2.write(w(U - A))
file2.write(w(U - B))

file1.close()
file2.close()
print 'end'

    


