"""
https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked

## issue

python 与 js 不一样, 不存在的key会报错, 需要提前检查: `num not in table`

## summary

利用 hash 表的查询

宏观地观看算法步骤, 比如先记忆再查询和先查询再记忆, 比如一边查询一边记忆

"""

def notSolveBySelf(func):
    return func

class Solution:
    @notSolveBySelf
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        官方: 把 twoSum_hash_merge 进一步修改
        
        不要把先放入记忆, 而是先查找记忆

        因此, 不需要存储多个 index:
            比如 3 + 3 = 6, 在考虑第二个 3 的时候, 立即可以判断
            否则直接替换
        """
        ### num: index[]
        table:dict[int, int] = {}
        for i, num in enumerate(nums):
        ## 先不建立记忆
            # if num not in table:
            #     table[num] = []
            # table[num].append(i) # 先不放入
        ## 查找
            diff = target - num
            if diff in table:
                return [i, table[diff]]
        ## 建立记忆
            table[num] = i


    def twoSum_hash_merge(self, nums: list[int], target: int) -> list[int]:
        """
        进一步的就是一边建立hash, 一边查找, 如同翻找记忆

        不需要等完全建立hash后再执行
        """
        ### num: index[]
        table:dict[int, list[int]] = {}
        ## 建立表
        for i, num in enumerate(nums):
            if num not in table:
                table[num] = []
            table[num].append(i)
        ## 查找
        # for i, num in enumerate(nums): # 合并这个过程
            diff = target - num
            if diff not in table:
                continue
            position = table[diff]
            if diff == num:
                if len(position) < 2:
                    continue
                return [position[0], position[1]]
            return [i, position[0]]

    
    def twoSum_hash(self, nums: list[int], target: int) -> list[int]:
        """
        利用 hash 表的查询
        """
        ### num: index[]
        table:dict[int, list[int]] = {}
        ## 建立表
        for i, num in enumerate(nums):
            if num not in table:
                table[num] = []
            table[num].append(i)
        ## 查找
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in table:
                continue
            position = table[diff]
            if diff == num:
                if len(position) < 2:
                    continue
                return [position[0], position[1]]
            return [i, position[0]]
            

                

    def twoSum_enum(self, nums: list[int], target: int) -> list[int]:
        """
        枚举
        """
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                if a + b == target:
                    return [i, j]
                

def test_sol():
    sol = Solution()
    assert sorted(sol.twoSum([2,7,11,15], 9)) == [0,1]
    assert sorted(sol.twoSum([3,2,4], 6)) == [1,2]
    assert sorted(sol.twoSum([2,5,5,11], 10)) is not None
