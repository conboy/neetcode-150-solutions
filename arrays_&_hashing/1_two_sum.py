class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in visited_nums:
                return [visited_nums[diff], i]
            else:
                visited_nums[n] = i