# Task 2.a
# Create a list of odd numbers from 1 to 100
# and power them to 3
num_list_1 = []
for num in range(1, 1000, 2):
    num_list_1.append(num**3)

# calculate total digits of each element in the list
num_list_1_ready = []
for num in num_list_1:
    num1 = num % 10
    num_list_1_ready.append(num1)

print(num_list_1)
print(num_list_1_ready)

num_list_2 = []
for num in num_list_1:
    num2 = num // 10
    num_list_2.append(num2)

num_list_2_ready = []
for num in num_list_2:
    num3 = num % 10
    num_list_2_ready.append(num3)

print(num_list_2)
print(num_list_2_ready)

num_list_3 = []
for num in num_list_2:
    num4 = num // 10
    num_list_3.append(num4)

num_list_3_ready = []
for num in num_list_3:
    num5 = num % 10
    num_list_3_ready.append(num5)

print(num_list_3)
print(num_list_3_ready)

num_list_4 = []
for num in num_list_3:
    num6 = num // 10
    num_list_4.append(num6)

num_list_4_ready = []
for num in num_list_4:
    num7 = num % 10
    num_list_4_ready.append(num7)

print(num_list_4)
print(num_list_4_ready)

num_list_5 = []
for num in num_list_4:
    num8 = num // 10
    num_list_5.append(num8)

num_list_5_ready = []
for num in num_list_5:
    num9 = num % 10
    num_list_5_ready.append(num9)

print(num_list_5)
print(num_list_5_ready)

num_list_6 = []
for num in num_list_5:
    num10 = num // 10
    num_list_6.append(num10)

num_list_6_ready = []
for num in num_list_6:
    num11 = num % 10
    num_list_6_ready.append(num11)

print(num_list_6)
print(num_list_6_ready)

num_list_7 = []
for num in num_list_6:
    num12 = num // 10
    num_list_7.append(num12)

num_list_7_ready = []
for num in num_list_7:
    num13 = num % 10
    num_list_7_ready.append(num13)

print(num_list_7)
print(num_list_7_ready)
print("end of list 7")

num_list_8 = []
for num in num_list_7:
    num14 = num // 10
    num_list_8.append(num14)

num_list_8_ready = []
for num in num_list_8:
    num15 = num % 10
    num_list_8_ready.append(num15)

print(num_list_8)
print(num_list_8_ready)

num_list_9 = []
for num in num_list_8:
    num16 = num // 10
    num_list_9.append(num16)

num_list_9_ready = []
for num in num_list_9:
    num17 = num % 10
    num_list_9_ready.append(num17)

print(num_list_9)
print(num_list_9_ready)
print("end of list 9")

# Now all "ready" num_lists calculate elements and collect them in a single list
all_num_lists_in_one_list = []
for num in range(0, len(num_list_1_ready)):
    all_num_lists_in_one_list.append(num_list_1_ready[num] + num_list_2_ready[num]
                                     + num_list_3_ready[num] + num_list_4_ready[num]
                                     + num_list_5_ready[num] + num_list_6_ready[num]
                                     + num_list_7_ready[num] + num_list_8_ready[num]
                                     + num_list_9_ready[num])

print(all_num_lists_in_one_list)

# Now separate from all_num_lists_in_one_list only
# dividable to number "7" elements to new list
num_list_dividable_to_7 = []
num_list_sum = 0
for num in range(0, len(all_num_lists_in_one_list)):
    if (all_num_lists_in_one_list[num] % 7) == 0:
        num_list_dividable_to_7.append(all_num_lists_in_one_list[num])
        num_list_sum += all_num_lists_in_one_list[num]

print(str(num_list_dividable_to_7) + "   << 2.a Final result")
print(f"{ num_list_sum} <:::::  sum of numbers which are dividable to 7")

# Task 2.b
# I have not clearly understand the task 2.b but I tried to solve this task in two variants
# 2.b - 1st the variant

num_list_plus_17 = []
for num in range(0, len(num_list_dividable_to_7)):
    num_list_plus_17.append(num_list_dividable_to_7[num] + 17)

# print(num_list_plus_17)

num_list_plus_17_dv_7_v1 = []

for num in range(0, len(num_list_plus_17)):
    if (num_list_plus_17[num] % 7) == 0:
        num_list_plus_17_dv_7_v1.append(num_list_plus_17[num])

print(str(num_list_plus_17_dv_7_v1) + " 2.b - 1st variant ")

# 2.b - 2nd variant

num_list_plus_17_v2 = []

for num in range(0, len(all_num_lists_in_one_list)):
    num_list_plus_17_v2.append(all_num_lists_in_one_list[num] + 17)

# print(num_list_plus_17_v2)

num_list_plus_17_dv_7_v2 = []

for num in range(0, len(num_list_plus_17_v2)):
    if (num_list_plus_17_v2[num] % 7) == 0:
        num_list_plus_17_dv_7_v2.append(num_list_plus_17_v2[num])

print(str(num_list_plus_17_dv_7_v2) + " 2.b - 2nd variant")

# Task 2.c unfortunately not working ((
# for num in range(0, len(all_num_lists_in_one_list)):
#     all_num_lists_in_one_list[num] += 17
#     if (all_num_lists_in_one_list[num] // 7) != 0:
#         all_num_lists_in_one_list.pop(all_num_lists_in_one_list[num])
#
# print(all_num_lists_in_one_list)
# print(str(all_num_lists_in_one_list) + "<< 2.c")
