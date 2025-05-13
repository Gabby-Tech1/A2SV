#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            new_row = [1] * (row + 1)

            for j in range(1, row):
                new_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(new_row)

        return triangle
        
# @lc code=end

