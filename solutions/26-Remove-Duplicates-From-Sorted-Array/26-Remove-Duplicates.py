from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # the solution I came up with
        if len(nums) == 1:
            return 1
        for testPointer in range(len(nums)):
            while (
                len(nums) > testPointer + 1
                and nums[testPointer] == nums[testPointer + 1]
            ):
                nums.pop(testPointer + 1)
        return len(nums)

        # neetcode's solution
        # l = 1
        # for r in range(1, len(nums)):
        #     if nums[r] != nums[r - 1]:
        #         nums[l] = nums[r]
        #         l += 1
        # return l


test = Solution()
mylist = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
print(test.removeDuplicates(mylist))
