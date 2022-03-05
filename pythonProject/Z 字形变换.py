class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        res = ["" for n in range(numRows)]
        i = 0
        # ans = ""
        flag = -1

        for w in s:
            res[i] += w
            if i == numRows-1 or i == 0:
                # 若到达最底层则反转向上插入
                flag = -flag
            i += flag
        # for j in range(numRows):
        #     ans += res[j]
        # return ans
        return "".join(res)
