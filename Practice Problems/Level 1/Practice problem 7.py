#Using while

def seed_no(number,ref_no):
    n = number
    nn = 1
    while n>0:
        x = n%10
        n = n//10
        nn*=x
    if nn*number == ref_no:
        return True
    else:
        return False
        
number=125
ref_no=738
print(seed_no(number,ref_no))

# Using for 
def seed_no(number,ref_no):
    nn = number
    for i in str(number):
        nn*=int(i)
    return nn == ref_no
    
number=123
ref_no=738
print(seed_no(number,ref_no))
