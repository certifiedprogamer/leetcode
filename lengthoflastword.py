class Solution(object):
    def lengthOfLastWord(self, s):
        lis = s.split(" ")
        for i in lis:
            if i == "":
                pass
            else:
                last_word = i
        return len(last_word)


print(Solution.lengthOfLastWord(1, "   fly me   to   the moon  "))
