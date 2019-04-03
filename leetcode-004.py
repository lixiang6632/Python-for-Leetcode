class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        nums_len = len(nums)
        if nums_len % 2 == 1:
            return nums[nums_len//2]
        else:
            return (nums[nums_len//2] + nums[nums_len//2 - 1]) / 2            ·