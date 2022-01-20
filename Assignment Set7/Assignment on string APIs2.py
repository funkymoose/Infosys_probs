

def remove_duplicates(value):
    re = []
    [re.append(i) for i in value if i not in re]
    s = ''
    for j in re:
        s+=j
    return s
    #start writing your code here

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
