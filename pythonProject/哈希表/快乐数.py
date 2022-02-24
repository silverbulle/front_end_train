class Solution:
    def isHappy(self, n: int) -> bool:
        def calaulate_happy(num):
            sum_ = 0

            # 从个位开始依次取，平方求和
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        # 记录中间结果
        record = set()

        while True:
            n = calaulate_happy(n)
            if n == 1:
                return True

            # 如果中间结果重复出现，说明进入死循环，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)
