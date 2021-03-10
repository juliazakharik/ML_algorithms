"""
1344. Angle Between Hands of a Clock
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.


Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 5:

Input: hour = 12, minutes = 0
Output: 0
"""

class Solution(object):
	#Runtime: 16 ms, faster than 70.21% 
	#Memory Usage: 13.4 MB, less than 69.50%
    def angleClock(self, hour, minutes):
    """
    :type hour: int
    :type minutes: int
    :rtype: float
    """
    mb_rotate = (abs(((5 * hour) % 60 + minutes / 12.0) % 60
                     - minutes) * 7.5) / 1.25
    if mb_rotate  < 360 - mb_rotate:
        return mb_rotate
    return 360 - mb_rotate