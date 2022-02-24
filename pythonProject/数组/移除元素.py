# 双指针法
class Solution:
    '''
    时间复杂度O(n)
    空间复杂度O(1)
    '''

    def removeElement(self, cls, nums: list[int], val: int) -> int:
        fast = slow = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            # 当fast指针遇到要删除的元素时停止赋值
            # slow指针停止移动，fast指针继续前进
            fast += 1
        return slow
