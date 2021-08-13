def translate_num(num):
    if num in numbers:
        print(numbers[num])
    else:
        print(numbers.get(num))


numbers = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять'
}
translate_num('one')
