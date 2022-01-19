# Method1 

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func ==None:
        return(sum(list_of_num))
    else:
        x = filter_func(list_of_num)
        return (sum(x))

def even(data):
    even_list = [i for i in data if i%2==0]
    return even_list

def odd(data):
    odd_list = [i for i in data if i%2!=0]
    return odd_list

sample_data = range(1,11)

print(sum_of_numbers(sample_data,"odd"))

# More simplified code

def sum_of_numbers(list_of_num,filter_func=None):
    return(sum(list_of_num)) if filter_func ==None else (sum(filter_func(list_of_num)))

def even(data):
    return [i for i in data if i%2==0]

def odd(data):
    return [i for i in data if i%2!=0]

sample_data = range(1,11)
print(sum_of_numbers(sample_data,even)) #write the function name directly, dont write it in strings 
