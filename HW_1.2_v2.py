# after yesterday's discussion in telegram, I understand that my code is not so correct
# and I decided to fix it today
# Task 2.a
num_list = []
for num in range(1, 1000, 2):
    num_list.append(num**3)

sum_list = 0
for num in range(0, len(num_list)):
    if sum(int(digit) for digit in str(num_list[num])) % 7 == 0:
        sum_list += num_list[num]

print(num_list)
print(f"{sum_list} <---- 2.a")

# Task 2.b

num_list_2 = []
for num in range(0, len(num_list)):
    num_list_2.append(num_list[num] + 17)

print(num_list_2)
sum_list_2 = 0
for num in range(0, len(num_list_2)):
    if sum(int(digit) for digit in str(num_list_2[num])) % 7 == 0:
        sum_list_2 += num_list_2[num]

print(f"{sum_list_2} <---- 2.b")

# Task 2.c
for num in range(0, len(num_list)):
    num_list[num] += 17

print(num_list)

for num in range(0, len(num_list)):
    if sum(int(digit) for digit in str(num_list[num])) % 7 == 0:
        sum_list += num_list[num]

print(f"{num_list} <---- 2.c")

