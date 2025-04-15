class Solution(object):
    def longestCommonPrefix(self, strs: list):
        for i in range(len(strs)):
            strs[i] = list(strs[i])
        shortest_word = strs[0]
        for i in range(len(strs)):
            if len(shortest_word) > len(strs[i]):
                shortest_word = strs[i]
        strs.remove(shortest_word)
        prefix = ""
        for letter_indx in range(len(shortest_word)):
            for i in strs:
                if shortest_word[letter_indx] != i[letter_indx]:
                    return prefix
            prefix += shortest_word[letter_indx]


print(Solution.longestCommonPrefix(1, ["flower", "flow", "flight"]))
