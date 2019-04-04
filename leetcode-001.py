class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        hashmap = {}
        for index, num in enumerate(nums):
            target_num = target - num
            if target_num in hashmap:
                return [hashmap[target_num], index]
            hashmap[num] = index