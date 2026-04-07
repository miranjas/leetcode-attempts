class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # setting left and right pointers
        left = 0
        right = len(nums) - 1

        # using binary search to find the target or the position to insert it
        while left <= right:
            mid = (left+right) //2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -  1
        return left

