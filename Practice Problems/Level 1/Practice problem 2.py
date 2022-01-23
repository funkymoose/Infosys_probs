

def bracket_pattern(input_str):
    count1=0 
    count2=0
    if input_str.startswith("(") and input_str.endswith(")") :
        for i in input_str:
            if i =="(":
                count1+=1
            else:
                count2+=1
    else:
        return False
    return count1==count2

    
input_str="()((())())"
print(bracket_pattern(input_str))
