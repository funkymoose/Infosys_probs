
def list123(nums):
    s = ""
    for i in nums:
        s+=str(i)
    return "123" in s
        
nums=[1,2,3,4,5]
print(list123(nums))
