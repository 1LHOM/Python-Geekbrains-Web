# 2
# input_num = int(input('write your number: '))
# nums_generator = (num for num in range(1, input_num+1) if num % 2 == 1)
# print(*nums_generator)
# 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
result = (word for word in zip(tutors, classes))
print(*result)