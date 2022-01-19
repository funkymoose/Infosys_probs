# More detailed version

def validate_name(name):
    if len(name)>0 and len(name)<16 and name.isalpha():
        return True
    else:
        return False
    #Start writing your code here

def validate_phone_no(phno):
    if len(phno)==10 and phno.isdigit():
        if str(phno) != str(phno)[0] * len(str(phno)):
            return True
        else:
            return False
    else:
        return False
    #Start writing your code here

def validate_email_id(email_id):
    
    if email_id.endswith("@gmail.com"):
        if email_id[:-10].isalnum():
            return True
        else :
            return False
    elif email_id.endswith("@yahoo.com"):
        if email_id[:-10].isalnum():
            return True
        else :
            return False
    elif email_id.endswith("@hotmail.com"):
        if email_id[:-12].isalnum():
            return True
        else :
            return False
    else :
        return False
    #Start writing your code here

def validate_all(name,phone_no,email_id):
    if validate_name(name):
        if validate_phone_no(phone_no):
            if validate_email_id(email_id):
                print("All the details are valid")
            else:
                print("Invalid email id")
        else:
            print("Invalid phone number")
    else:
        print("Invalid Name")
    

    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")

# Comprehensions and less lines
def validate_name(name):
    return (len(name)>0 and len(name)<16 and name.isalpha())
    #Start writing your code here

def validate_phone_no(phno):
    return len(phno)==10 and phno.isdigit() and str(phno) != str(phno)[0] * len(str(phno))

def validate_email_id(email_id):
    if email_id.endswith("@gmail.com") or email_id.endswith("@yahoo.com") or email_id.endswith("@hotmail.com"):
        if email_id[:-10].isalnum():
            return True
        elif email_id.endswith("@hotmail.com") and email_id[:-12].isalnum():
            return True
        else:
            return False
    else :
        return False
    #Start writing your code here

def validate_all(name,phone_no,email_id):
    if validate_name(name):
        if validate_phone_no(phone_no):
            if validate_email_id(email_id):
                print("All the details are valid")
            else:
                print("Invalid email id")
        else:
            print("Invalid phone number")
    else:
        print("Invalid Name")
validate_all("Tina", "9994599998", "tina@yahoo.com")
