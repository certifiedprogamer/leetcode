"""
58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only."""


class Solution(object):
    def lengthOfLastWord(self, s: str):
        lis = s.split(" ")
        for i in lis:
            if i == "":
                pass
            else:
                last_word = i
        return len(last_word)


print(Solution.lengthOfLastWord(1, "   fly me   to   the moon  "))
