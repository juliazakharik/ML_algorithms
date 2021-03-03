"""
1711. Count Good Meals
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.



"""


class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        twos = [pow(2, i) for i in range(23)]
        count = 0
        d_odd = {}
        d_not_odd = {}
        for n in deliciousness:
            if n in d_odd:
                d_odd[n] += 1
            else:
                d_odd[n] = 1
        for i in range(len(deliciousness)):
            if deliciousness[i] in d_odd:
                for j in range(len(twos)):
                    if (twos[j] - deliciousness[i]) in d_odd:
                        if (twos[j] - deliciousness[i]) == deliciousness[i]:
                            count += (d_odd[deliciousness[i]] * (d_odd[deliciousness[i]] - 1))//2 
                        else:
                            count += (d_odd[twos[j] - deliciousness[i]] * d_odd[deliciousness[i]])
                del d_odd[deliciousness[i]]
        return count