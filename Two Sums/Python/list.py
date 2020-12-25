class Solution:
   
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if(complement in nums and nums.index(complement) != i ):
                return [i,nums.index(complement)]
            
        