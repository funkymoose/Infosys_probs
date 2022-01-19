#Using number as int

def check_double(number):
    nl = []
    nno = number * 2
    nnl=[]
    count = 0
    while number>0:
        r = number%10
        number = number//10
        nl.append(r)
    while nno>0:
        r = nno%10
        nno = nno//10
        nnl.append(r)
    if (len(nl)==len(nnl)):
        for i in nl:
            if i in nnl:
                count+=1
        if count==len(nnl):
            return True
        else:
            return False

    else:
        return False
print(check_double(125874)) #True

# Using Counter function

from collections import Counter
def check_double(number):
    nl = []
    nno = number * 2
    nnl=[]
    count = 0
    while number>0:
        r = number%10
        number = number//10
        nl.append(r)
    while nno>0:
        r = nno%10
        nno = nno//10
        nnl.append(r)
    if Counter(nl)==Counter(nnl):
        return True
    else:
        return False

    #Remove pass and write your logic here
print(check_double(142857)) #True


# Treating number as a string

#lex_auth_01269441810970214471

def check_double(number):
    num = str(number)
    dou_num = str(number * 2)
    count = 0
    for i in num:
        if i in dou_num:
            count+=1
    return count==len(num)
print(check_double(125874))
