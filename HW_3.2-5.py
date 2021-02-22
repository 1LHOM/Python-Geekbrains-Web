# ####################  2   #######################
def num_translate_adv(word=input()):
    en_ru_dict = {
        'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
    }
    if word[0].isupper():
        word = word.lower()
        return en_ru_dict[word].capitalize()
    else:
        return en_ru_dict[word]


print('(2) ===> advanced translator ')
print(num_translate_adv())


# 3
def thesaurus(*args):
    sorted(args)
    my_dict = {}
    my_dict2 = {}
    for i in args:
        n, s = i.split()
        s_letter = s[0]
        n_letter = n[0]
        if n_letter not in my_dict:
            my_dict[n_letter] = []
        if n_letter in my_dict:
            my_dict[n_letter].append(i)

    return my_dict


print('(3) ===> ')
print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))

# 5
from random import choice


def get_jokes(num):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []

    while num != 0:
        ch_n = choice(nouns)
        ch_adv = choice(adverbs)
        ch_adj = choice(adjectives)
        joke.append(f'{ch_n} {ch_adv} {ch_adj}')
        num -= 1
    return joke


print(get_jokes(5))
