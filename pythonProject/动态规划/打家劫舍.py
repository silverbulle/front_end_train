class Solution:
    def rob(self, nums: list[int]) -> int:
        s = len(nums)

        if not nums:
            return 0
        if s == 1:
            return nums[0]
        dp = [0] * s

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, s):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[len(nums) - 1]

    # 优化,减少存储
    def rob2(self,nums:list[int])->int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second