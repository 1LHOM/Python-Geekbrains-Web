# 2
input_num = int(input('write your number: '))
nums_generator = (num for num in range(1, input_num+1) if num % 2 == 1)
print(*nums_generator)
# 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]
result_3 = ((tutors[i], classes[i]) for i in range(len(tutors)))
print(*result_3)

# 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_4 = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
print(result_4)

# 5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_5 = [num for num in src if src.count(num) == 1]
print(result_5)
