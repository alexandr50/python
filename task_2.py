numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def translate_adv(num):
    if num[0] == num[0].upper():
        num = num.lower()
        return numbers[num].capitalize()
    else:
        return numbers[num]


print(translate_adv('nine'))
print(translate_adv('One'))
