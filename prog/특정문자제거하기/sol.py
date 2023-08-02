def solution(my_string, letter):
    return my_string.replace(letter, '')

print(solution('hello world!', ' world'))

# def solution(my_string, letter):
#     answer = ''

#     for string in my_string:
#         if string != letter:
#             answer += string

#     return answer

# print(solution('hello world!', 'wor'))