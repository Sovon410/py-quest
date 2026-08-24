class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        max_water = 0

        while(lp < rp):
            width = rp - lp
            ht = min(height[lp], height[rp])
            curr_water = width * ht
            max_water = max(max_water, curr_water)

            lp, rp = (lp + 1, rp) if height[lp] < height[rp] else (lp, rp - 1)

        return max_water