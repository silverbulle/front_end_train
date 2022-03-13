class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int) -> List[str]:
            if index == len(digits):
                ans.append(''.join(temp))

            else:
                digit = digits[index]
                for i in phoneMap[digit]:
                    temp.append(i)
                    backtrack(index + 1)
                    temp.pop()

        temp = list()
        ans = list()
        backtrack(0)
        return ans