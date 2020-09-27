# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
#
# Note:
#
# sx, sy, tx, ty will all be integers in the range [1, 10^9].


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # starting point  x, y
        # target point x, y

        #         while sx < tx and sy < ty:
        #             tx, ty = tx % ty, ty % tx

        #         return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
        #                sy == ty and sx <= tx and (tx - sx) % sy == 0

        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx = tx % ty
                else:  # ty == sy
                    return (tx - sx) % ty == 0
            else:  # tx < ty
                if tx > sx:
                    ty = ty % tx
                else:  # tx == sx
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


# 190 / 190 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 78.82 % of python3 submissions.
# Your memory usage beats 5.77 % of python3 submissions.
