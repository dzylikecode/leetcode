"""

## summary

利用极值原理来剪枝

多多看看自己失败的案例, 多思考一下, 
不要被立马的想到的答案给满足了.
多思考一下所代表的集合, 也许就水落石出了

"""

def notSolveBySelf(cls):
    return cls


@notSolveBySelf
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        官方解答, 考虑极值, 边界

        针对最长的序列, 则 x-1或者说 x+1一定不在剩余的
        可以用来剪枝

        同时不妨加强假设条件, 从起点考虑

        于是变成考虑以 x 为起点的最长序列, 然后考虑所有的 x
        """
        nums = set(nums) # 优化去重
        longest = 0
        for x in nums:
            if x-1 in nums:
                continue
            x_prime = x
            x_longest = 1
            while x_prime+1 in nums:
                x_longest += 1
                x_prime += 1
            longest = max(x_longest, longest)

        return longest

@notSolveBySelf
class Solution_divide_border_simplify:
# class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        分支可以统一表达
        """
        nums = set(nums)
        state_longest = 0
        state_consecutive:dict[int, int] = {}
        for x in nums:
            x_plus_1 = (state_consecutive[x+1]
                        if x+1 in state_consecutive 
                        else 0)
            x_minus_1 = (state_consecutive[x-1]
                        if x-1 in state_consecutive 
                        else 0)
            ## 发现分支可以统一
            length = x_minus_1 + x_plus_1 + 1
            state_consecutive[x]           = 1 #length # 表面存在
            state_consecutive[x-x_minus_1] = length
            state_consecutive[x+x_plus_1]  = length

            state_longest = max(length, state_longest)
        return state_longest


@notSolveBySelf
class Solution_divide_border:
# class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        多分析一下失败的那个案例, 我没有思考清楚

        ```
            x Consecutive | Consecutive x
        x+1, x-1 指向对应的序列, 长度就可以代表序列了
        ```

        **对应的序列**没有思考清楚

        (x+1, x+1+length) 其实就是代表了那个序列

        我已经在思考 x+1, x-1 这种边界了, 
        但是没有进一步意识到, Consecutive 可以用边界来定义
        """
        nums = set(nums)
        state_longest = 0
        state_consecutive:dict[int, int] = {}
        for x in nums:
            x_plus_1 = (state_consecutive[x+1]
                        if x+1 in state_consecutive 
                        else 0)
            x_minus_1 = (state_consecutive[x-1]
                        if x-1 in state_consecutive 
                        else 0)
            length = 0
            match (x_minus_1 != 0, x_plus_1 != 0):
                case (False, False): # 都不存在
                    state_consecutive[x] = 1
                    length = 1
                case (True, True): # 都存在
                    length = x_minus_1 + x_plus_1 + 1
                    state_consecutive[x-x_minus_1] = length
                    state_consecutive[x]           = length
                    state_consecutive[x+x_plus_1]  = length
                case (True, False): 
                    length = x_minus_1 + 1
                    state_consecutive[x-x_minus_1] = length
                    state_consecutive[x]           = length
                case (False, True): 
                    length = x_plus_1 + 1
                    state_consecutive[x]          = length
                    state_consecutive[x+x_plus_1] = length

            state_longest = max(length, state_longest)
        return state_longest

class Solution_divide:

    class Consecutive:
        def __init__(self, length:int):
            self.length = length


    def longestConsecutive(self, nums: list[int]) -> int:
        """
        引用那个集合
        问题
            在合并的时候, 将另一边全部替换成同一个集合
            这个导致复杂度难分析
        """
        nums = set(nums)
        state_longest = 0
        state_consecutive:dict[int, Solution_divide.Consecutive] = {}
        for x in nums:
            ## 利用集合去重
            # if x in state_consecutive: # 重复的没影响
            #     continue
            x_plus_1 = (state_consecutive[x+1]
                        if x+1 in state_consecutive 
                        else None)
            x_minus_1 = (state_consecutive[x-1]
                        if x-1 in state_consecutive 
                        else None)
            length = 0
            match (x_minus_1 != None, x_plus_1 != None):
                case (False, False): # 都不存在
                    state_consecutive[x] = Solution_divide.Consecutive(1)
                    length = 1
                case (True, True): # 都存在
                    length = x_minus_1.length + x_plus_1.length + 1
                    consecutive = state_consecutive[x-1]
                    consecutive.length = length

                    state_consecutive[x-1] = consecutive
                    state_consecutive[x]   = consecutive
                    # x+1 代表的集合要全部指向同一集合
                    x_prime = x
                    while x_prime+1 in state_consecutive:
                        state_consecutive[x_prime+1] = consecutive
                        x_prime += 1
                case (True, False): 
                    length = x_minus_1.length + 1
                    consecutive = state_consecutive[x-1]
                    consecutive.length = length

                    state_consecutive[x-1] = consecutive
                    state_consecutive[x]   = consecutive
                case (False, True): 
                    length = x_plus_1.length + 1
                    consecutive = state_consecutive[x+1]
                    consecutive.length = length

                    state_consecutive[x]   = consecutive
                    state_consecutive[x+1] = consecutive
            state_longest = max(length, state_longest)
        return state_longest

class Solution_divide_failed:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        采用递归来思考, 思考每个步骤

        添加一个元素
                        原来的 -> 新的
                            这个过程连续序列的影响

        连续
                    x Consecutive | Consecutive x
        即判断 x+1 开始的序列 | x-1 结束的序列是否存在
        存在: 更新序列 (*特别的* 可能都存在, 那就是合并)
        否则: 创建新序列

        进一步的技巧就是
        x+1, x-1 指向对应的序列, 长度就可以代表序列了

        核心
            分治
        """
        state_longest = 0
        state_consecutive:dict[int, int] = {}
        for x in nums:
            if x in state_consecutive: # 重复的没影响
                continue
            x_plus_1 = (state_consecutive[x+1]
                        if x+1 in state_consecutive 
                        else 0)
            x_minus_1 = (state_consecutive[x-1]
                        if x-1 in state_consecutive 
                        else 0)
            length = 0
            match (x_minus_1 != 0, x_plus_1 != 0):
                case (False, False): # 都不存在
                    state_consecutive[x] = 1
                    length = 1
                case (True, True): # 都存在
                    length = x_minus_1 + x_plus_1 + 1
                    state_consecutive[x-1] = length
                    state_consecutive[x]   = length
                    state_consecutive[x+1] = length
                case (True, False): 
                    length = x_minus_1 + 1
                    state_consecutive[x-1] = length
                    state_consecutive[x]   = length
                case (False, True): 
                    length = x_plus_1 + 1
                    state_consecutive[x]   = length
                    state_consecutive[x+1] = length

            state_longest = max(length, state_longest)
        return state_longest


def test_longestConsecutive_divide_failed():
    sol = Solution_divide_failed()
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

def test_longestConsecutive():
    sol = Solution()
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert sol.longestConsecutive([-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2]) == 12