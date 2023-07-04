class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max = 0
        for n in num_set:
            count = 1
            if n - 1 not in num_set:
                for i in range(1, len(num_set)):
                    if n + i in num_set:
                        count += 1
                    else:
                        break
                if count > max:
                    max = count
        return max