def factor(number):
    l = [i for i in range(1, number+1) if number%i==0 ]
    return len(l)

def find_smallest_number(num):
    i=1
    while (True):
        if factor(i)==num:
            break
        else:
            i+=1
    return i

num=7
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
