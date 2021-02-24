# Homework 4_5
# We can get several currency rates at the same time through console
# f. eg. python HW_4_5.py USD EUR UZS
import datetime
import time

from requests import get, utils


def currency_rates(argv):

    program, *args = argv
    start_time = time.perf_counter()
    print(f'\n{program} <---- this is what "program" received')
    print(f'{args} <---- this is what "args" received')
    print(f'{argv} <---- this is what "argv" received\n')
    for char_code in args:
        response = get('http://www.cbr.ru/scripts/XML_daily.asp')
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        char_code = char_code.upper()
        if char_code not in content:
            return print(f'Ввлюта не найдена "{char_code}"\n{datetime.datetime.now()}')
            # If we don't want to stop cycle when something get wrong
            # we can solve it by just removing 'return' here
        else:
            start_index = content.find(f'{char_code}')
            data = content[(content.find('Date')+5):(content.find('name')-1)]
            name_of_currency = content[(content.find('Name', start_index)+5):(content.find('</Name>', start_index))]
            nominal = content[(content.find('Nominal', start_index)+8):(content.find('</Nominal>', start_index))]
            rub, kop = content[(content.find('Value', start_index)+6):(content.find('</Value>', start_index))].split(',')
            rub = int(rub)
            kop = int(kop)
            currency_rate = float(f'{rub}.{kop}')
            print(f'Дата: {data}\nКурс валюты: {nominal} {name_of_currency}'
                  f'\nВ рублях: {currency_rate}\n')
    end_time = time.perf_counter()
    end_process = datetime.datetime.now()
    speed_of_process = (end_time - start_time)
    print(f'Время завершения: {end_process}')
    print(f'Запрос выполнен за: {speed_of_process} секунд')
    return 0


if __name__ == '__main__':
    import sys
    print(currency_rates(sys.argv))