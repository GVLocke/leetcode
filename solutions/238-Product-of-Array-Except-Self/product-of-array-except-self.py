from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            output[i] = nums[i - 1] * output[i - 1]

        # Calculate postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output


bruh = Solution()
print(bruh.productExceptSelf([1, 2, 3, 4]))
