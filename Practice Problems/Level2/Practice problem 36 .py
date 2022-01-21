
def find_target_positions(input_string, target_word):
    target_list=[]
    string = input_string.split()
    for i in range(len(string)):
        if string[i]==target_word:
            target_list.append(i)
    return target_list

def find_inverted_index(input_string):
    target_dict={}
    string = input_string.split()
    for i in string:
        target_dict[i]=find_target_positions(input_string,i)
    return target_dict
    
    
input_string="we dont need no education we dont need no thought control no we dont"
result_dict=find_inverted_index(input_string)
print(result_dict)

# Much short code, using comprehensions

def find_target_positions(input_string, target_word):
    string = input_string.split()
    return [i for i in range(len(string)) if string[i] == target_word]

def find_inverted_index(input_string):
    string = input_string.split()
    return {i: find_target_positions(input_string, i) for i in string}


input_string = "we dont need no education we dont need no thought control no we dont"
result_dict = find_inverted_index(input_string)
print(result_dict)
