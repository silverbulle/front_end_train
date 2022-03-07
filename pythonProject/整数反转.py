class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x

        str_x = str(x)
        if str_x[0] != "-":

            ans = str_x[::-1]
            ans = int(ans)
        else:
            ans = str_x[:0:-1]
            ans = int(ans)
            ans = -ans

        if - 2**31 < ans < 2**31 - 1:
            return ans
        else:
            return 0
