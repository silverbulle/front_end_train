class Solution:
    # 使用数组作为哈希表
    def canConstruct1(self, ransom: str, magazine: str) -> bool:
        arr = [0] * 26

        for x in magazine:
            arr[ord(x) - ord("a")] += 1

        for x in ransom:
            if arr[ord(x) - ord("a")] == 0:
                return False
            else:
                arr[ord(x) - ord("a")] -= 1

        return True

    # 使用defaultdict
    def canConstruct2(self, ransom: str, magazine: str) -> bool:
        from collections import defaultdict

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1
        for x in ransom:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1
        return True

    # 使用dict
    def canConstruct3(self, ransom: str, magazine: str) -> bool:
        hashmap = dict()

        for x in ransom:
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        for x in magazine:
            if x in hashmap:
                hashmap[x] -= 1

        for key in hashmap:
            if hashmap[key] > 0:
                return False
        return True

