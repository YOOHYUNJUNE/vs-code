# 새로운 명단을 추가해도 계산되게 하는 방법

location_list = ['서울', '부산', '서울', '서울', '대전', '제주', '광주', '부산', 'LA', '도쿄']
                
location_dict = {}

for location in location_list:
    # 이미 기록은 한 경우
    if location in location_dict.keys():
        location_dict[location] += 1
    # 처음 등장한 경우
    else:
        location_dict[location] = 1
        
print(location_dict)


# data = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# result = {}
# for blood_type in data:
#     if blood_type in result:
#         result[blood_type] += 1
#     else:
#         result[blood_type] = 1

# print(result)