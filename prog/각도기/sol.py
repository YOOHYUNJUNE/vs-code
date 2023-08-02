def solution(angle):
    if 0 < angle < 90:
        return '예각'
    elif angle == 90:
        return '직각'
    elif 90 < angle < 180:
        return '둔각'
    else:
        return '평각'
    
    '예각' : 1
    '직각' : 2
    '둔각' : 3
    '평각' : 4

    print(angle(88, 120))

