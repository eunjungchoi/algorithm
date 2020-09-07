
# 퀵 소트

# 영국의 컴퓨터 과학자 토니 호어가 1959년에 고안한 알고리즘
# 피벗을 기준으로 좌우를 나누는 특징
# 파티션 교환 정렬이라고도 불림
# 분할 정복 알고리즘
# 피벗이라는 개념을 통해 피벗보다 작으면 왼쪽, 크면 오른쪽과 같은 방식으로 파티셔닝하면서 쪼개 나감.
# N.Lomuto 가 구현한 '파티션 계획 partition scheme' 버전이 유명
# = 항상 맨 오른쪽의 피벗을 택하는 방식.


def quicksort(A, low, high):
    def partition(low, high):
        pivot = A[high]
        left = low

        for right in range(low, high):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1

        A[left], A[high] = A[high], A[left]
        return left

    if low < high:
        pivot = partition(low, high)
        quicksort(A, low, pivot - 1)
        quicksort(A, pivot + 1, high)
