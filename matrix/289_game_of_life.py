# According to the Wikipedia's article:
# "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
# (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.
# The next state is created by applying the above rules simultaneously to every cell in the current state,
# where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

# Follow up:
#
# 1) Could you solve it in-place? Remember that the board needs to be updated at the same time:
# You cannot update some cells first and then use their updated values to update other cells.

# 2) In this question, we represent the board using a 2D array.
# In principle, the board is infinite,
# which would cause problems when the active area encroaches the border of the array.
# How would you address these problems?
import collections
from typing import List


class Solution:
    """
    문제:
    위키피디아의 기사에 따르면, "The game of life"는 단순히 Life으로도 알려져 있으며, 1970년 영국의 수학자 존 호튼 콘웨이가 고안한 세포자동화다."
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

    M x N cells가 있는 보드에 의해 각 셀은 초기 상태 살아있음(1) 또는 사망(0)을 가진다. 각 셀은 다음의 네 가지 규칙(위 위키백과 기사 참조)을 사용하여 8개의 이웃(수평, 수직, 대각선)과 상호작용한다.

    이웃이 둘도 안 되는 살아있는 세포는 인구 부족에 의한 것처럼 죽는다.
    2, 3명의 이웃이 살고 있는 어떤 "살아있는" 세포라도 다음 세대에 걸쳐 계속 생존한다.
    3명 이상의 이웃을 가진 살아있는 세포는 인구과잉에 의해 죽는다.
    정확히 3개의 이웃을 가진 "죽은" 세포는 생식을 통해 살아있는 세포가 된다.

    현재 상태가 지정된 보드의 다음 상태(한 번 업데이트 후)를 계산하는 함수를 작성하십시오. 다음 상태는 출생과 사망이 동시에 발생하는 현 상태의 모든 세포에 위의 규칙을 동시에 적용함으로써 생성된다.

    in-place에서 해결이 가능한가? 보드는 동시에 업데이트해야 한다. 일부 셀을 먼저 업데이트한 다음 업데이트된 값을 사용하여 다른 셀을 업데이트할 수 없음.
    이 질문에서 우리는 2D 배열을 사용하여 board를 표기한다. 원칙적으로 board가 무한대여서 활동 영역이 배열의 경계를 잠식할 때 문제가 발생한다. 이 문제들을 어떻게 해결할 것인가?

    ----------------------------
    풀이:

    참고: https://leetcode.com/problems/game-of-life/solution/

    만약 보드가 무한히 크면 어떻게 될까? 우리가 앞에서 본 것과 같은 솔루션을 여전히 사용할 수 있을까 아니면 우리가 다르게 해야 할 다른 방법이 있을까?
    보드가 무한히 커지면 현재 해결책은 다음과 같은 여러 가지 문제에 직면하게 된다.

    그렇게 큰 행렬을 반복하는 것은 계산적으로 불가능할 것이다.
    그 큰 행렬을 전적으로 메모리에 저장하는 것은 불가능할 것이다. 오늘날 우리는 수백 기가 바이트의 엄청난 메모리 용량을 가지고 있다.
    하지만, 그렇게 큰 매트릭스를 기억 속에 저장하는 것은 여전히 충분하지 않을 것이다.
    이렇게 거대한 board에 살아있는 세포가 몇 개만 있고 나머지는 모두 죽는다면 우리는 많은 공간을 낭비하고 있을 것이다.
    이런 경우, 우리는 매우 희박한 매트릭스를 가지고 있고 보드를 "매트릭스"로 저장하는 것은 말이 되지 않을 것이다.

    이러한 개방적인 문제는 프로그래밍 면접 시 설계 토론에 더 적합하며 면접관이 그러한 문제에 대해 이야기하는 데 관심이 있을 수 있으므로 문제의 확장성 측면을 고려하는 것이 좋은 습관이다.
    토론 부분은 이미 문제의 이 특정한 부분을 다루는 데 큰 역할을 한다. 우리는 토론 섹션에서 제공되었던 두 가지 다른 해결책에 대해 간략히 살펴보기로 한다.
    그들은 이 문제의 두 가지 주요 시나리오를 폭넓게 다루고 있기 때문이다.

    문제의 한 측면은 스테판 포흐만이 제공한 훌륭한 해결책에 의해 해결된다. 그래서 앞에서 언급했듯이, 우리가 살아있는 세포가 아주 적은 거대한 매트릭스를 가지고 있을 가능성이 있다.
    그럴 경우 판 전체를 있는 그대로 살리는 것은 어리석은 일일 것이다.

    만약 우리가 극도로 희박한 행렬을 가지고 있다면, 실제로 살아있는 세포의 위치를 저장한 다음 이 살아있는 세포만을 사용하여 4가지 규칙을 적용하는 것이 훨씬 더 타당할 것이다.

    스테판이 문제의 이러한 측면을 다루기 위해 제공한 샘플 코드를 살펴보자.

    본질적으로, 우리는 전체 보드에서 살아있는 세포만 얻은 다음 살아있는 세포만을 사용하여 다른 규칙을 적용하고 마지막으로 보드를 내부로 업데이트한다.
    이 해결책의 유일한 문제는 전체 보드가 메모리에 맞지 않을 때일 것이다. 만약 정말 그렇다면, 우리는 이 문제에 다른 방식으로 접근해야 할 것이다.
    이 시나리오의 경우, 매트릭스의 내용이 한 번에 한 행씩 파일에 저장된다고 가정한다.

    우리가 특정 세포를 업데이트하기 위해서, 우리는 본질적으로 그것의 위아래 줄에 놓여있는 8개의 이웃만 보면 된다. 따라서 행의 셀을 업데이트하려면 위 행과 아래 행만 있으면 된다.
    따라서, 우리는 파일에서 한 번에 한 행씩 읽으며, 최대 3개의 행을 메모리로 할 것이다. 우리는 처리된 행을 계속 폐기하고 파일에서 새로운 행을 한 번에 하나씩 계속 읽을 것이다.

    @beagle의 솔루션은 이 아이디어를 중심으로 회전하며, 토론 섹션의 코드를 참고하면 된다. 이 문제를 해결할 단 하나의 해결책은 없다는 점을 유념해야 한다.
    모든 사람들은 문제의 확장성 측면에 대해 다른 관점을 가지고 있을 수 있으며, 이 두 솔루션은 매트릭스 기반 문제를 규모에 맞게 처리할 때 가장 기본적인 문제를 다루고 있을 뿐이다.

"""

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)  # updated live
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)

    def gameOfLifeInfinite(self, live):
        counter = collections.Counter((I, J)
                                          for i, j in live
                                            for I in range(i - 1, i + 2)       # 위, 아래 총 3개 행만 메모리에 저장
                                                for J in range(j - 1, j + 2)   # 왼쪽, 오른쪽 총 3개 열만 메모리에 저장.
                                                    if I != i or J != j        # 값이 1인 셀의 주변 8개 셀마다 각자 카운트를 계산.
                                      )
        return {ij for ij in counter if counter[ij] == 3 or counter[ij] == 2 and ij in live}   #


# 23 / 23 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.2 MB
#
# Your runtime beats 92.78 % of python3 submissions.

