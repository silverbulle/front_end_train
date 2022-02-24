class Solution:
    def teoSum(self, nums: list[int], target: int) -> list[int]:
        record = dict()
        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for idx, val in enumerate(nums):
            if target - val in dict.keys():
                record[val] = idx
            else:
                # 如果存在就返回字典记录索引和当前索引
                return [record[target - val], idx]
