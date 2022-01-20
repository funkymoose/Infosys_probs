def check_anagram(data1,data2):
    x = data1.lower()
    y = data2.lower()
    d1 = [] 
    [d1.append(i)for i in x]
#or d1 = list(x)
    d2 = [] 
    [d2.append(i)for i in y]
#or d2 = list(x)
    d1.sort()
    d2.sort()
    if d1==d2:
        j = len(x)-1
        while j>=0:
            if x[j]==y[j]:
                return False
            else:
                if j==0:
                    return True
                else:
                    j-=1
    else:
        return False

print(check_anagram("paepl","apple"))


# Simplified

def check_anagram(data1,data2):
    if sorted(data1.lower())==sorted(data2.lower()):
        for i in range(len(data1)):
            if data1.lower()[i]==data2.lower()[i]:
                return False
    else:
        return False
    return  True

print(check_anagram("tea","eat"))
