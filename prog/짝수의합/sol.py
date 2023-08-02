# def solution(n):
#     answer = 0

#     for i in range(n+1):
#         if i % 2 == 0:
#             answer += i

#     return answer


# 2. 짝수 리스트를 만든 후 리스트 내 수를 전부 더하는 방법

# def solution(n):
#     answer = []

#     for i in range(n+1):
#         if i % 2 == 0:
#             answer.append(i)

#     return sum(answer)


# 3. 더 간단한 방법

def solution(n):

    answer = range(2, n+1, 2)

    return sum(answer)