def is_palindrome(word):
    string = word.lower()
    return string == string[::-1]

#Provide different values for word and test your program
result=is_palindrome("stocks")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
