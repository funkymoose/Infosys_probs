

def find_duplicates(list_of_numbers):
    res = []
    [res.append(i) for i in list_of_numbers if list_of_numbers.count(i)>1 and i not in res]
    return res

list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
