class Solution:
    def repaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
        ans = list(s)
        ans.extend([' '] * counter * 2)

        # 原始字符串的末尾，拓展后的末尾
        left, right = len(s) - 1, len(ans) - 1

        while left >= 0:
            if ans[left] != ' ':
                ans[right] = ans[left]
                right -= 1
            else:
                ans[right - 2:right + 1] = '%20'
                right -= 3
            left -= 1
        return ''.join(ans)
