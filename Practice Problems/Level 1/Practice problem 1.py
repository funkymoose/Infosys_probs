

def add_string(str1):
    if len(str1)>=3:
        if str1.endswith("ing"):
            return(str1+"ly")
        else :
            return(str1+"ing")
    else:
        return str1

  

str1="com"
print(add_string(str1))
