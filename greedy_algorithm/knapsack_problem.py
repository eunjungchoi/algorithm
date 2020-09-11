# 배낭 문제 knapsack problem은 조합 최적화 combination optimization 분야의 매우 유명한 문제로,
# 배낭에 담을 수 있는 무게의 최댓값 (15kg)이 정해져있고,
# 각각 짐의 가치와 무게가 있는 짐을 배낭에 넣을 때 가치의 합이 최대가 되도록, 즉 $ 달러의 가치가 최대가 되도록 짐을 고르는 방법을 찾는 문제다.
# 배낭 문제는 짐을 쪼갤 수 잇는 경우인 분할 가능 배낭문제( 그리디 알고리즘으로 해결) 와  짐을 쪼갤 수 없는 배낭문제 (다이내믹 프로그래밍으로 해결) 로 나뉜다.
# 짐을 쪼갤 수 있는 분할 가능 배낭 문제
# 이 경우 단가가 가장 높은 짐부터 차례대로 채워나가면 된다.
#
# 먼저 짐 cargo를 ‘가격, 무게’ 의 튜플 리스트로 정의하고, 함수 fractional_knapsack()을 호출한다.
# 앞서 단가 기준으로 알고리즘을 설명한 그대로 구현하기 위해 단가를 계산하고 역순으로 정렬한다. 즉 단가가 높은 짐이 맨 위에 오도록 다음과 같이 구현한다.
# 이제 단가 순으로 그리디 알고리즘으로 계산하면 된다

# 코드로 구현해보면 다음과 같다.

cargo = [
    (4, 12),
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2)
]


def fractional_knapsack(cargo):
    capacity = 15
    pack = []

    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)

    # 단가순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break

    return total_value


r = fractional_knapsack(cargo)


