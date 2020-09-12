cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]
# 먼저 짐 cargo를 ‘가격 $, 무게 kg’ 의 튜플 리스트로 정의.

def zero_one_knapsack(cargo):
    capacity = 15
    pack = []
    # 6 x 16 행렬의 중간 결과 테이블 생성
    # 이 테이블을 글자 그대로 타뷸레이션하는 다이나믹 프로그래밍 풀이.
    # 테이블 크기의 기준: 짐의 최대 개수(5개) + 1, 배낭의 최대 용량(15kg) +1  = 6 x 16
    # 테이블 각각의 셀에는 그 위치까지의 짐의 개수와 배낭의 용량에 따른 최댓값이 담기게 됨

    for i in range(len(cargo) + 1):   # 짐 개수  0 ~ 5개
        pack.append([])
        for c in range(capacity + 1):   # 배낭의 무게  0 ~ 15kg
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:  # 무게가 capacity 보다 작거나 같으면
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )
            else:
                pack[i].append(pack[i-1][c])  # capa 보다 크면  이전 값을 그대로 넣어줌.

    return pack[-1][-1]


r = zero_one_knapsack(cargo)

# 시간복잡도 = O(nW)   n: 짐의 개수, W: 배낭의 용량
