#coding: utf_8
alf = ['T','A','G','C']#переменная считается заданной для всех кто ниже

def vocab(s, n):
    m = n - 1
    for i in alf:
        print s
        print s + i
        if m <> 0:
            vocab(s + i, m)

vocab("", 2)




            
    


        

        
