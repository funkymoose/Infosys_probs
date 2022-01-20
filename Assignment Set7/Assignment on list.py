def check_perfect_number(number):
    sum = 0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum == number:
        return True
    else:
        return False
    
    #start writing your code here

def check_perfectno_from_list(no_list):
    nl = []
    for i in no_list:
        if type(i)==int and i>0:
            if check_perfect_number(i):
                nl.append(i)
                
    return nl
            
    #start writing your code here

perfectno_list=check_perfectno_from_list([18,6,52,12,28])
print(perfectno_list)

# Same code using comprehensions
# lex_auth_01269446533799116898

def check_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

def check_perfectno_from_list(no_list):
    return [i for i in no_list if type(i) == int and i > 0 if check_perfect_number(i)]

perfectno_list = check_perfectno_from_list([18, 6, 52, 12, 28])
print(perfectno_list)
