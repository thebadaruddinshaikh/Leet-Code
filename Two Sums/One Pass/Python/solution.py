class Solution:
   
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if(complement in ha.keys() and ha.get(complement) != i ):
                return [i,ha.get(complement)]
            ha[nums[i]] = i
        