'''
 Question: Given a list of integers, write a function to determine if any pair of numbers from the list adds up to a given target number.
   The function should return a boolean value indicating whether such a pair exists.
 '''

def pairs_sum( nums: list[int], target: int )-> bool:
    for i in range(nums):
        for j in range(i+1, len((nums))):
            if list[i]+ list[j] ==target:
                return True
            
    return False


def pairs_sum(nums: list[int], target: int)-> bool: 
   seen = () 
   for num in nums: 
       complement = target-num 
       if complement in seen: 
           return True 
       seen.add(num)
    
   return False