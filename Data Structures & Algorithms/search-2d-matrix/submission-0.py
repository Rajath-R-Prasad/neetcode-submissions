class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(nums,t):
            low=0
            high=len(nums)-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==t:
                    return mid
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1

        for row in matrix:
            if bsearch(row,target)!=-1:
                return True
        return False