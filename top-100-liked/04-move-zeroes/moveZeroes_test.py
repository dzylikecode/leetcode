"""


## summary

在此题, 体会到双指针是特殊的队列, 可以推导出队列的某种表达当作指针

"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        官方: 更简洁地找到需要成本操作的地方

        换了一个视角考虑操作, 从非0视角考虑:
            一个数非0说明就存在交换的可能, 不交换其实就是和自己交换

        其实和队列很像, left 就是队列的 head, 
        只不过刻画了关系就是下一个,
        不需要真正的队列
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


class Solution_combine:
# class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        综合考虑前面两个方案
                slot = slots.pop(0)
                slots.append(i)
        具有长度不变

        再考虑
                zero_i ~ nzero_i 都是 0

        所以可以用 0 的个数来刻画 slots
        也就是 nzero_i - zero_i = slots
        """
        slots = 0
        for i, num in enumerate(nums):
            if num == 0:
                slots += 1
            else:
                nums[i-slots] = num
        n = len(nums)
        for i in range(n-slots, n):
            nums[i] = 0
        



class Solution_pointer:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        考虑极值, 出现 0 的时候才会处理
        处理时立马找非0

        从需要操作的成本开始考虑

                nums[zero_i] = nums[nzero_i]

        接下来就是
                zero_i += 1
                nzero_i = find_nzero()

        细节就是 zero_i ~ nzero_i 都是 0

        然后是用状态机来思考
             for i, num in enumerate(nums)
             本质上是这么一个循环的状态转移

        本质上感觉是对 queue 的优化
        """
        zero_i: int | None = None
        nzero_i:int | None = None
        for i, num in enumerate(nums):
            ## 用状态机更好理解, 就是为了到达需要考虑成本的操作
            if zero_i is None and num != 0:
                continue
            if zero_i is None and num == 0: # 找到 0 开始考虑
                zero_i = i
                continue
            if num == 0:    # 此时 zero_i is not 0
                continue    # 需要找到非0
            nzero_i = i     # 找到非0
            ## 真正的成本处理
            nums[zero_i] = nums[nzero_i]
            ## 接下来
            zero_i += 1
        if zero_i is not None:
            while zero_i < len(nums):
                nums[zero_i] = 0
                zero_i += 1


class Solution_queue:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        0 这个信息是冗余的, 可以任意给别人占用, 最后补足就行

        相当于 0 是一块内存, 如何把离散的内存变连续
        一旦发现空白的内存就可以给其他数字用
        """
        slots = []
        for i, num in enumerate(nums):
            if num == 0:
                slots.append(i)
            elif len(slots) > 0:
                slot = slots.pop(0)
                nums[slot], num[i] = num, 0
                slots.append(i)



class Solution_bubble:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        第一想法是冒泡
        """
        length = len(nums)
        for i in range(length):
            bubbled = False
            for j in range(length-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    bubbled = True
            if not bubbled:
                break

def test_moveZeroes():
    sol = Solution()
    args = [1]
    sol.moveZeroes([1])
    assert args == [1]