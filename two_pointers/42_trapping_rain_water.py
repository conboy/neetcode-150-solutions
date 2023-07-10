class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        lmax = height[l]
        rmax = height[r]

        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                water = min(lmax, rmax) - height[l]
                lmax = max(lmax, height[l])
            else:
                r -= 1
                water = min(lmax, rmax) - height[r]
                rmax = max(rmax, height[r])
            if water > 0:
                res += water
        return res