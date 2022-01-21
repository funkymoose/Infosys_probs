#lex_auth_01269445968039936095

def validate_credit_card_number(card_number):
    l1 = []
    l2 = []
    sum = 0
    for i in range(len(str(card_number))):
        if i%2==0:
            l1.append(int(str(card_number)[i]))
        else:
            l2.append(int(str(card_number)[i]))
    for i in l1:
        temp = i*2
        if temp<10:
            sum+=temp
        else:
            sum+=(int(str(temp)[0])+int(str(temp)[1]))
    for i in l2:
        sum+=i
    if sum%10==0:
        return True
    else:
        return False

card_number=   4539869650133101 #1456734512345698   #1456734512345698 # #5239512608615007 #try uncommenting each value
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
    
#     Using Comprehensions

def validate_credit_card_number(card_number):
    l1 = [(int(str(card_number)[i])) for i in range(len(str(card_number))) if i%2==0]
    l2 = [(int(str(card_number)[i])) for i in range(len(str(card_number))) if i%2!=0]
    sum = 0
    for i in l1:
        temp = i*2
        if temp<10:
            sum+=temp
        else:
            sum+=(int(str(temp)[0])+int(str(temp)[1]))
    for i in l2:
        sum+=i
    return sum%10==0

card_number=   4539869650133101 #1456734512345698   #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
