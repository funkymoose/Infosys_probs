
def close_number(num1,num2,num3):
    mylist = [num1,num2,num3]
    l1 = []
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            l = [mylist[i], mylist[j]]
            l1.append(max(l)-min(l))

    l1.sort()
    if l1[0]<=1 and l1[1]>=2 and l1[2]:
        return True
    else:
        return False
    
print(close_number(5,4,2))

# Using Itertools
from itertools import combinations

def close_number(num1,num2,num3):
    mylist = [num1,num2,num3]
    l1 = [(max([i,j])-min([i,j])) for i,j in combinations(mylist,2)]
    l1.sort()
    return l1[0]<=1 and l1[1]>=2 and l1[2]>=2
print(close_number(5,4,2))
