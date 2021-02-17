"""
68. Text Justification
Hard

Given an array of words and a width maxWidth, format the text such that each 
line has exactly maxWidth characters and is fully (left and right) justified.


Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""

import math
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        width_left = maxWidth
        res = []
        res_line = []
        for word in words:
            if len(word) < width_left + 1:
                width_left -= len(word)
                width_left -= 1
                res_line.append(word)
            else:
                extra_spaces = []
                width_left += 1
                delim = len(res_line) - 1
                if delim != 0:
                    aa = width_left // delim 
                else:
                    aa = 0
                for i in range(delim):
                    extra_spaces.append(aa)
                    width_left -= aa
                if width_left > 0:
                    #print(width_left, " ", extra_spaces, " ", delim)
                    for i in range(width_left):
                        if len(extra_spaces) > i:
                            extra_spaces[i] += 1
                
                res_str = ''
                i = 0
                if len(res_line)  == 1:
                        res_str += res_line[0]
                        sp = " "*width_left
                        res_str += sp
                else:
                    for word1 in res_line:
                        res_str += word1

                        if i < len(res_line) -1:
                            sp = " "*int(extra_spaces[i] + 1)
                            res_str += sp

                        i += 1
                res.append(res_str)
                res_line = []
                res_line.append(word)
                width_left = maxWidth - len(word) - 1
        final_line = " ".join(res_line)
        final_line += (" " * (maxWidth - len(final_line)))
        res.append(final_line)
        return res
        
        