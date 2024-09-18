from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


mylist = [1, 2, 3, 4, 5]
bruh = Solution()
print(bruh.getConcatenation(mylist))
