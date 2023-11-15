class Solution(object):
    def __self__(self):
        pass

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        return s_list == t_list


text = "bruh"
text2 = "rubt"
bruh = Solution()
print(bruh.isAnagram(text, text2))
