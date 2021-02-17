"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.


Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
"""

 Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        i = 0
        summ = 0
        res = []
        for ch in S:
            summ = sum(shifts[i:])
            
            if ord(ch) + summ > 122:
                if (ord(ch) + summ - 122) % 26 == 0:
                       res.append('z')
                else:
                    res.append(chr((ord(ch) + summ - 122) % 26 + 96))
            else:
                res.append(chr(ord(ch) + summ))
            i += 1
        return "".join(res)