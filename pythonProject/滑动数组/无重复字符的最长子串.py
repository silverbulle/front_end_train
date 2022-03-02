class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_set = set()  # 哈希集合，记录每个字符是否出现过
        length = len(s)
        right = -1  # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        ans = 0

        for left in range(length):
            # 左指针向右移动一格，移除一个字符
            if left != 0:
                chr_set.remove(s[left - 1])

            while right + 1 < length and s[right + 1] not in chr_set:
                # 不断地移动右指针
                chr_set.add(s[right + 1])
                right += 1
            # 第 left 到 right 个字符是一个极长的无重复字符子串
            ans = max(ans, right - left + 1)

        return ans
