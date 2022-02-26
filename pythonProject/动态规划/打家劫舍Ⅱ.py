class Solution:
    def rob(self, nums: list[int]) -> int:
        def get_rob(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])

            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second

        size = len(nums)

        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        if size == 2:
            return max(nums[0], nums[1])
        else:
          return max(get_rob(0, size - 2), get_rob(1, size - 1))
