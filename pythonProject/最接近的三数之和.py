class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        def update(cur):
            nonlocal ans
            if abs(cur - target) < abs(ans - target):
                ans = cur
        
        nums.sort()
        n = len(nums)
        ans = 10**7

        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                cur = nums[i]+nums[left]+nums[right]
                if cur ==target:
                    return target
                if cur<target:
                    left += 1
                    update(cur)
                else:
                    right -= 1
                    update(cur)
        return ans