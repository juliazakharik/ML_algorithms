"""
Given an array of strings strs, 
group the anagrams together. You can return the answer in any order.


Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = []
        anagram_set = []
        for string in strs:
            sort_str = sorted(string)
            if sort_str in anagram_set:
                i = 0
                for anagram in anagram_set:
                    if anagram == sort_str:
                        anagrams[i].append(string)
                    i += 1
            else:
                anagram_set.append(sort_str)
                anagrams.append([string])
                    
        return anagrams