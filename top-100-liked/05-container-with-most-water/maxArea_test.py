class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        通过对最优解的考察, 容易考虑边界

        对于 left
            一定不会存在 i < j & height[i] > height[j]
        对于 right
            一定不会存在 i < j & height[i] < height[j]

        直接从剪枝思考, 减少思考成本
        """
        if len(height) == 2:
            return min(height[0], height[1]) # * 1

        left_queue = [height[0]]
        right_queue = [height[1]]

        for i, h in height:
            pass
