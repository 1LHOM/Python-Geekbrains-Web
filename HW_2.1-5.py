Type_of_item = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for i in Type_of_item:
    print(type(i))

# 2

My_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
New_list = []

for item in My_list:
    if item.isdigit():
        New_list.append(f'"{int(item):02}"')
    else:
        New_list.append(item)

print(New_list)
print(" ".join(New_list))

# 4
list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
list2 = []
for item in list1:
    list2.append(item.split())

for i in list2:
    print(f"Hello {i[-1].capitalize()}.")

# 5 a, b, c, d
# 5b add price_list.sort()
# 5c add price_list.sort(reverse=True)
# 5d add while loop to print only
price_list = [54.89, 23.6, 5.65, 47.35, 78.25, 1.06, 43.65, 72.41, 53.86, 15.7]
price_list.sort(reverse=True)
max_print = 1
for num in price_list:
    rubles = num // 1
    kopeyki = num % 1
    print(f"{max_print} place - {int(rubles):02d} руб {int(round(kopeyki*100))} коп")
    max_print +=1
    if max_print > 5:
        break

# our list is sorted and everything is working correctly))
print(f"Checking our list - {price_list}")
print(f"Checking our list reversed - {sorted(price_list, reverse=False)}")

