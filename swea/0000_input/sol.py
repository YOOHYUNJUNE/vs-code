import sys
sys.stdin = open('input.txt')

# 1차원 리스트
N = int(input())

if N % 2 == 1:
    print('홀수')
else:
    print('짝수')


N = int(input())

if N % 2 == 1:
    print('홀수')
else:
    print('짝수')

TC = int(input())

for i in range(TC):
    N = int(input())

    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')


N = int(input())

for i in range(N):
    numbers = list(map(int, input().split()))
    print(numbers)

for m in matrix:
    print(m)


N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.appen(numbers)
    

for row in matrix:
# print(row)
    for item in row:
        if item == 5:
                print('5가 있습니다.')