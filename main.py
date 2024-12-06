# импортируем модуль 
import json

numbers_path = "numbers.json"
operators_path = "operators.json"

# парсим файл
def parse_json(file):
    file_opened = open(file, 'r', encoding='utf-8')
    return json.load(file_opened)

# превращаем в числа
def convert_to_numbers(raw_array:list):
    numbers_array = []
    for x in user_input:
        if x in numbers.keys():
            numbers_array.append(numbers[x])
        elif x in operators.keys():
            numbers_array.append(operators[x])

    print(*numbers_array)
    return numbers_array

# режем на числа
def slice_arr(numbers_array):
    sliced_number_array = []
    pre_x_idx = 0
    x_idx = 0
    for x in numbers_array:
        if x in operators.values():
            sliced_number_array.append(numbers_array[pre_x_idx:x_idx])
            sliced_number_array.append([numbers_array[x_idx]])
            pre_x_idx = x_idx+1
        x_idx += 1 
    sliced_number_array.append([numbers_array[x_idx-1]])
    print(sliced_number_array)
    return sliced_number_array

     

# парсинг чисел и операторов
numbers = parse_json(numbers_path)
operators = parse_json(operators_path)

# отладка
# print(numbers)

# ввод и форматрование
user_input = input().split(sep=" ")
print(*user_input)

# превращаем в числа
numbers_array = convert_to_numbers(user_input)

# резняяяяяяяяя
sliced = slice_arr(numbers_array)
print(sliced)

for x in sliced:
    current_number = []
    for num in range(0, len(x)-1, 1):
        if x[num] < x[num+1]:
            current_number.append(x[num] * x[num+1])
        else:
            current_number.append(x[num])
    
print(current_number)