class Solution:
    # 双指针法
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]:
                    continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        ans.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1
                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1
                        p += 1
                        q -= 1
            return ans
