class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(S: list, left: int, right: int):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans

    def generateParenthesis(self, n: int) -> list[str]:
        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left:
                return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res
