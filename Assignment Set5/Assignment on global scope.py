
def find_more_than_average():
    average = sum(list_of_marks)/len(list_of_marks)
    count = 0
    for i in list_of_marks:
        if i>average:
            count+=1
    return ((count*100)/len(list_of_marks))
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    return [list_of_marks.count(j)for j in range(26)] 
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
