class Solution(object):
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
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        for i in range(len(strs)):
            output_addition = []
            output_addition.append(strs[i])
            for j in range(len(strs)):
                if i!=j:
                    if self.isAnagram(strs[i], strs[j]):
                        output_addition.append(strs[j])
                        strs.remove(strs[j])
            output.append(output_addition)
            strs.remove(strs[i])
        for i in strs:
            output.append([i])
        return output

bruh = Solution()
bruh.groupAnagrams(["", ""])