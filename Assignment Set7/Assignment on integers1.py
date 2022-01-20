# Using for loop
def nearest_palindrome(number):
    for i in range(number+1, 10000000):
        if str(i) == str(i)[::-1]:
            return i
number=12331
print(nearest_palindrome(number))

# Using while loop
def nearest_palindrome(number):
    number+=1
    while str(number)!=str(number)[::-1]:
        number+=1
    return number
        
number=12331
print(nearest_palindrome(number))
