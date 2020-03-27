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

for i in range(len(s)):
        s1 = s[i];
        otv = ''
        for j in range(len(s)):
            a = 0
            s2 = s[j];
            for k in range(len(s[0])):
                if s1[k]<>s2[k]:
                    a = a + 1
            otv += "%.5f" % (float(a)/len(s[0])) + ' '
        print otv
