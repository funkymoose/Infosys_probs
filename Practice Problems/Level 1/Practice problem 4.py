def find_nine(nums):
    if len(nums)<=4:
        if 9 in nums:
            return True
        else:
            return False
    else:
        if 9 in nums[:4]:
            return True
        else:
            return False	

nums=[1,9,4,5,6]
print(find_nine(nums))

# Consise code

def find_nine(nums):
    if len(nums)<=4:
        return 9 in nums
    else:
        return 9 in nums[:4]
	

nums=[1,9,4,5,6]
print(find_nine(nums))
