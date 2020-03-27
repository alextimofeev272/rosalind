#coding: utf_8
#Данн набор строк ДНКа
#Собрать общую строку

def string(text):
    results = [];
    strings = text.strip().split('>');#pазделяет строку по >,убирает пробелы
    for s in strings:
        if len(s):#если не нулевая длинна строки
            parts = s.split();
            k = parts[0];#название
            v = ''.join(parts[1:]);#объеденяет строки(последоваельности амин)
            results.append(v);#добавляет название и строку в один элемент
    return results;

def superstring(string,strings):#string - ; strings - набор строк днка
    if len(strings) == 0:return string;#если все строки присоеденили даст ответ
    else:
        for i in range(len(strings)):#для всех оставшихся строк        
            for j in range(len(strings[i])/2):#половина условие задачи
                if string.startswith(strings[i][j:]):
                    Istr = strings[i];strings.pop(i);#.pop(i) удаляет i элемент
                    return superstring(Istr[:j] + string,strings)
                if string.endswith(strings[i][:len(strings[i])-j]):
                    Istr = strings[i];strings.pop(i);
                    return superstring(string + Istr[len(Istr)-j:],strings);

file = open('D:\\python\input.txt')
text = file.read();
s1 = string(text);
s2 = s1[0];s1.pop(0);
print superstring(s2,s1)
file.close()
