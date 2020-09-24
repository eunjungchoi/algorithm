# Given a robot cleaner in a room modeled as a grid.
#
# Each cell in the grid can be empty or blocked.
#
# The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
#
# When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
#
# Design an algorithm to clean the entire room using only the 4 given APIs shown below.
#
# interface Robot {
#   // returns true if next cell is open and robot moves into the cell.
#   // returns false if next cell is obstacle and robot stays on the current cell.
#   boolean move();
#
#   // Robot will stay on the same cell after calling turnLeft/turnRight.
#   // Each turn will be 90 degrees.
#   void turnLeft();
#   void turnRight();
#
#   // Clean the current cell.
#   void clean();
# }
# Example:
#
# Input:
# room = [
#   [1,1,1,1,1,0,1,1],
#   [1,1,1,1,1,0,1,1],
#   [1,0,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0,0],
#   [1,1,1,1,1,1,1,1]
# ],
# row = 1,
# col = 3
#
# Explanation:
# All grids in the room are marked by either 0 or 1.
# 0 means the cell is blocked, while 1 means the cell is accessible.
# The robot initially starts at the position of row=1, col=3.
# From the top left corner, its position is one row below and three columns right.
# Notes:
#
# The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
# The robot's initial position will always be in an accessible cell.
# The initial direction of the robot will be facing up.
# All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
# Assume all four edges of the grid are all surrounded by wall.


"""
격자로 모델링 된 실내에 로봇 청소기가 있다.
그리드의 각 셀은 비어있거나 막혀있다.
로봇 청소기에는 4개의 API가 있다. 앞으로 가거나, 왼쪽으로 돌거나, 오른쪽으로 돌 수 있다. 한 번 돌 때 90도씩 돈다.

막힌 셀로 이동하려고 하면, 범퍼 센서가 장애물을 감지해서 현재 셀에 머무른다.
아래의 4개 API만 사용해서 전체 룸을 청소할 수 있는 알고리즘을 설계하라.

방의 모든 격자는 0 또는 1로 표기된다.
0은 셀이 막혀있다는 뜻이고, 1은 셀에 접근할 수 있다는 뜻이다.
로봇은 row=1, col=3에서 시작한다.
"""


# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            # going clockwise: 0 : up, 1: right, 2: down, 3: left
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0],
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                # turn the robot following chosen direction: clockwise
                robot.turnRight()

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        visited = set()
        backtrack()


# 29 / 29 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Memory Usage: 15.2 MB
#
# Your runtime beats 85.63 % of python3 submissions.
# Your memory usage beats 40.75 % of python3 submissions.
