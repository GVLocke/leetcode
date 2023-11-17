from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        freq_dict = {}
        for num in nums_set:
            freq_dict[num] = 0
        for num in nums:
            freq_dict[num] += 1
        sorted_dict = dict(
            sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
        )
        output_list = []
        for key, value in list(sorted_dict.items())[:k]:
            output_list.append(key)
        return output_list


bruh = Solution()
myList = [1, 1, 1, 2, 2, 3, 5, 2, 3, 4, 5, 5, 4, 5, 4, 1, 1, 4, 4, 4, 4, 7, 8, 9]
print(bruh.topKFrequent(myList, 2))
