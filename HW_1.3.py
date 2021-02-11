permanent_word = "Протцент"
input_num = int(input("Введите число: "))
suffixes = ['', 'а', 'у', '', 'ом', 'е', 'ы', 'ов', 'ам', 'ы', 'ами', 'ах', 'а', 'у', '', 'ом', 'е', 'ы', 'ов', 'ам', 'а']
if input_num <= 20:
    print(f"{input_num} {permanent_word}{suffixes[input_num]}")
else:
    print(f"Вы ввели слишком большое число !\nВаша число {input_num}"
          f"\nДиапазон принимаемых чисел 0 - 20")
