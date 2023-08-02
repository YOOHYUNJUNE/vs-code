#정수 n의 각 자리 숫자 합

def solution(n):
    a = list(map(int,str(n)))
    return sum(a)

print(solution(123456789))
