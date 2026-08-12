class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_nums = nums
        nums=sorted(nums)
        i=0
        j=len(nums)-1
        while(i<j):
            if nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                idx1 = original_nums.index(nums[i])
                idx2 = original_nums.index(nums[j]) if nums[i] != nums[j] else original_nums.index(nums[j], idx1 + 1)
                return sorted([idx1, idx2])