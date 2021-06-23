'''
    Utilize for para obter a inversão de uma cadeia de string. Exemplos:

    !
    d
    l
    r
    o
    W
     
    o
    l
    l
    e
    H
     
     
     
    !dlroW olleH
'''

string1='Hello World!'
for index in range(len(string1)-1,-1,-1):
    print(string1[index])
    
for index in range(len(string1)-1,-1,-1):
    print(string1[index],end='')