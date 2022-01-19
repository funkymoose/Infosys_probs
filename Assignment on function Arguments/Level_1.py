# Method 1 without using list(less space complexity)
def find_pairs_of_numbers(num_list,n):
    pairs = 0 
    for i in num_list:
        for j in num_list:
            if i != j and i+j == n:
                pairs+=1 
    if pairs>0:
        return pairs//2
    else:
        return pairs
      
num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))

# Method 2 Using lists(less code complexity)
def find_pairs_of_numbers(num_list, n):
    l = [(i,j)for i in num_list for j in num_list if i!=j and i + j == n]
    return len(l)//2 if len(l) > 0 else 0
  
num_list = [1, 2, 7, 4, 5, 6, 0, 3]
n = 6
print(find_pairs_of_numbers(num_list, n))
