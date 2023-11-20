class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    """

    def encode(self, strs):
        return_string = ""
        for string in strs:
            return_string += str(len(string)) + "#" + string
        return return_string

    """
    @param: str: a string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        output_list, string_pointer = [], 0
        while string_pointer < len(str):
            length_pointer = string_pointer
            while str[length_pointer] != "#":
                length_pointer += 1
            length = int(str[string_pointer:length_pointer])
            output_list.append(str[length_pointer + 1 : length_pointer + 1 + length])
            string_pointer = length_pointer + length + 1
        return output_list


bruh = Solution()
mylist = ["test", "this", "th#t", "blah", "blah"]
print(bruh.decode(bruh.encode(mylist)))
