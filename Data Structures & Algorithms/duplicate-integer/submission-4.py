class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=0
        for i in range(len(nums)):
            d[nums[i]]+=1
        for i in range(len(nums)):
            if d[nums[i]]>1:
                return True
        return False