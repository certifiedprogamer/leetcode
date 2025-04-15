"""14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""."""


class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs)):
            strs[i] = list(strs[i])
        shortest_word = strs[0]
        for i in range(len(strs)):
            if len(shortest_word) > len(strs[i]):
                shortest_word = strs[i]
        strs.remove(shortest_word)
        prefix = ""
        if len(strs) == 0:
            for i in shortest_word:
                prefix += i
            return prefix
        for letter_indx in range(len(shortest_word)):
            for i in strs:
                if shortest_word[letter_indx] != i[letter_indx]:
                    return prefix
            prefix += shortest_word[letter_indx]
        return prefix


print(Solution.longestCommonPrefix(1, ["flower", "flow", "flight"]))
