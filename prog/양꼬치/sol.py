def solution(n, k):
    # n : 양꼬치 n인분 / n = 10
    # K : 음료수 k개 / k = 3
    answer = 0

    service = n // 10

    answer = (n * 12000) + (k - service) * 2000

    return answer

