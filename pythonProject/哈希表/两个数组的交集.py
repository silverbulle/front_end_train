class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # 两个数组先变成集合，求交集后还原为数组
        return list(set(nums1) & set(nums2))
