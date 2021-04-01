"""
657. Robot Return to Origin
Easy

There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
"""

# Runtime: 24 ms, faster than 90.48% of Python online submissions for Robot Return to Origin.
# Memory Usage: 13.6 MB, less than 71.16% of Python online submissions for Robot Return to Origin.  
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") - moves.count("D") == 0 and moves.count("L") - moves.count("R") == 0

# Runtime: 68 ms, faster than 40.56% of Python online submissions for Robot Return to Origin.
# Memory Usage: 13.5 MB, less than 91.95% of Python online submissions for Robot Return to Origin.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        coord = [0, 0]
        for letter in moves:
            if letter == "U":
                coord[1] += 1
            elif letter == "D":
                coord[1] -= 1
            elif letter == "R":
                coord[0] += 1
            else:
                coord[0] -=1
        return coord == [0, 0]


# Runtime: 56 ms, faster than 74.38% of Python online submissions for Robot Return to Origin.
# Memory Usage: 13.7 MB, less than 42.90% of Python online submissions for Robot Return to Origin
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        coordX = 0
        coordY = 0
        for letter in moves:
            if letter == "U":
                coordY += 1
            elif letter == "D":
                coordY -= 1
            elif letter == "R":
                coordX += 1
            else:
                coordX -=1
        return coordX == 0 and coordY == 0