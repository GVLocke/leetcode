class Solution(object):
    def __self__(self):
        pass

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return True
            else:
                nums_set.add(i)
        return False


nums2 = [1, 2, 3, 4]
bruh = Solution()
print(bruh.containsDuplicate(nums2))
