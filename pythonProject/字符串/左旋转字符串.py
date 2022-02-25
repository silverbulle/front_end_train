class Solution:

    # 使用切片
    def reverseLeftWords1(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]

    # 反转区间为前n的子串
    # 反转区间为n到末尾的子串
    # 反转整个字符串
    def reverseLeftWords2(self, s: str, n: int) -> str:
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n] = list(reversed(s[n:]))
        s.reverse()

        return ''.join(s)

    # 手写reverse
    def reverseLeftWords3(self, s: str, n: int) -> str:
        def reverse_sub(lst, left, right):
            while left < right:
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1

        ans = list(s)
        end = len(ans) - 1
        reverse_sub(ans, 0, n - 1)
        reverse_sub(ans, n, end)
        reverse_sub(ans, 0, end)
        return ''.join(ans)

    # 考虑不能用切片的情况下，利用模+下标实现
    def reverseLeftWords4(self, s: str, n: int) -> str:
        new_s = ''
        for i in range(len(s)):
            j = (i + n) % len(s)
            new_s = new_s + s[j]
        return new_s
