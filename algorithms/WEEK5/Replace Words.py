"""
648. Replace Words
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

"""

#Runtime: 5604 ms, faster than 7.10% of Python online submissions for Replace Words.
#Memory Usage: 22.4 MB, less than 99.35% of Python online submissions for Replace Words.
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        res = []
        for word in sentence.split(' '):
            flag = False
            prefix = ""
            for letter in word:
                prefix += letter
                if prefix in dictionary:
                    res.append(prefix)
                    flag = True
                    break
            if not flag:
                res.append(word)
        return " ".join(res)




#Runtime: 292 ms, faster than 19.35% of Python online submissions for Replace Words.
# Memory Usage: 22.6 MB, less than 96.77% of Python online submissions for Replace Words.

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        d = {}
        for di in dictionary:
            d[di] = 0
        res = []
        for word in sentence.split(' '):
            flag = False
            prefix = ""
            for letter in word:
                prefix += letter
                if prefix in d:
                    res.append(prefix)
                    flag = True
                    break
            if not flag:
                res.append(word)
        return " ".join(res)