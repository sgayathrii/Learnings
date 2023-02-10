
def list123(nums):
    for items in range(0,len(nums)-1):
        if nums[items]==1:
            if nums[items+1]==2:
                if nums[items+2]==3:
                    return True
       
    return False 
  

print(list123([1, 1, 2, 3, 1]))
print(list123([1, 1, 2, 4, 1]))
print(list123([1, 1, 2, 1, 2, 3]))



"""
def list123(nums, desired=[1, 2, 3]):
    return str(desired)[1:-1] in str(nums)
"""


"""
def list123(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==1:
            if nums[i+1]==2:
                if nums[i+2]==3:
                    return True

    return False 

nums=[1, 2, 1, 3, 1, 2, 1]
print(list123(nums))

"""