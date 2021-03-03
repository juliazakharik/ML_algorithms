"""
457. Circular Array Loop
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation:
There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
The cycle's length is 3.
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            pos = nums[i] > 0
            next_ind = i
            l = 0
            while True:
                l += 1
                
                if next_ind + nums[next_ind] >= len(nums):
                    next_ind  = (next_ind + nums[next_ind]) % len(nums)
                elif next_ind + nums[next_ind] < 0:
                    next_ind = len(nums) - abs(next_ind + nums[next_ind]) % len(nums)
                else:
                    next_ind += nums[next_ind]
                print(i, next_ind)
                
                if (nums[next_ind] >= 0) != pos:
                    break
                if next_ind == i and l > 1:
                    return True
                elif next_ind == i and l <= 1:
                    break
                if l >= len(nums):
                    break
        return False