class Solution:
    def search(self, nums: List[int], target: int) -> int:
        //left pointer initialization
        l = 0 
        //right pointer initialization
        r = len(nums)-1
        //condition check (if left pointer is lesser than or equal to the right pointer)
        while l<=r:
        //calculating the average of the given array
         m = (l+r)//2
        //checking the array with the help of the middle value calcuated and matching it
         if target == nums[m]:
            return m
         elif target > nums[m]:
          l = m+1
         elif target < nums[m]:
          r = m-1
        //calculating the edge case
        return -1
