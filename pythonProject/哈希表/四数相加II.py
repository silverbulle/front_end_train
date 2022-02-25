class Solution:
    def fourSumCount(self, nums1: list, nums2: list, nums3: list, nums4: list) -> int:
        hashmap = dict()
        # 遍历大A和大B数组，统计两个数组元素之和，和出现的次数，放到map中
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1 + n2] += 1
                else:
                    hashmap[n1 + n2] = 1
        # 在遍历大C和大D数组，找到如果 0-(c+d) 在map中出现过的话，
        # 就把map中key对应的value也就是出现次数统计出来。
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = -n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count
