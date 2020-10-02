# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
#
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
#
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
#
# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
#
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
#
# Example:
#
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
# Snake snake = new Snake(width, height, food);
#
# Initially the snake appears at position (0,0) and the food at (1,2).
#
# |S| | |
# | | |F|
#
# snake.move("R"); -> Returns 0
#
# | |S| |
# | | |F|
#
# snake.move("D"); -> Returns 0
#
# | | | |
# | |S|F|
#
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
#
# | |F| |
# | |S|S|
#
# snake.move("U"); -> Returns 1
#
# | |F|S|
# | | |S|
#
# snake.move("L"); -> Returns 2 (Snake eats the second food)
#
# | |S|S|
# | | |S|
#
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
from collections import deque
from typing import List


class SnakeGame:
    """
    스네이크 게임을 디자인한다.

    화면 크기 = 너비 x 높이의 장치에서 플레이한다.
    뱀은 처음에 길이 = 1 인 상태로, 왼쪽 상단 모서리에 위치한다.
    음식의 위치 목록을 행-열 순서대로 받는다. 뱀이 음식을 먹으면 길이와 게임의 점수가 모두 1씩 증가한다.
    각각의 음식이 화면에 하나씩 나타난다. 첫 번째 음식을 뱀이 먹으면 두 번째 음식이 나타난다.
    화면에 음식이 나타날 때, 뱀이 점유한 블록에는 음식이 나타나지 않는다.
    """

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width - 1
        self.height = height - 1
        self.food = deque(food)
        self.snake = deque([[0, 0]])

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        i, j = self.snake[0]
        if direction == 'U':
            i -= 1
        elif direction == 'R':
            j += 1
        elif direction == 'L':
            j -= 1
        elif direction == 'D':
            i += 1

        if i < 0 or i > self.height or j < 0 or j > self.width:  # 바운더리를 벗어남
            return -1

        if self.food and [i, j] == self.food[0]:  # 음식을 먹으면
            self.food.popleft()  # 음식을 목록에서 제거
        else:
            self.snake.pop()  # 꼬리 제거
            if (i, j) in self.snake:  # 몸에 부딪힘
                return -1

        self.snake.appendleft((i, j))  # 새로운 곳으로 head가 이동.
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)


# 539 / 539 test cases passed.
# Status: Accepted
# Runtime: 260 ms
# Memory Usage: 15.4 MB
#
# Your runtime beats 99.73 % of python3 submissions.
# Your memory usage beats 14.61 % of python3 submissions.
