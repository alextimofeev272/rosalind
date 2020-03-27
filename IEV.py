file = open('D:\python\input.txt')
a = file.read().split()

p = [1,1,1,0.75,0.5,0]
middle = 0; middle2 = 0;

sum = 0
for i in range(6):
    sum = sum + 2*p[i]*int(a[i])

print sum

file.close()
