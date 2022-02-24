class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        res = float("inf")  # 定义一个无限大的数
        s_um = 0
        index = 0
        for i in range(len(nums)):
            s_um += nums[i]
            while s_um >= s:
                res = min(res, i - index + 1)
                s_um -= nums[index]
                index += 1
            return 0 if res == float("inf") else res
