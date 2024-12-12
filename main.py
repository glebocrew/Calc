# импортируем модуль 
import json

numbers_path = "numbers.json"
operators_path = "operators.json"

# парсим файл
def parse_json(file):
    file_opened = open(file, 'r', encoding='utf-8')
    return json.load(file_opened)

parsed_numbers = parse_json(numbers_path)
parsed_operators = parse_json(operators_path)

def slice_string(string: str):
    string = string.split(sep=" ")
    sliced = []

    start = 0
    end = 0
    for part in string:
        if part in parsed_operators:
            sliced.append(string[start:end])
            start = end
            start += 1
            sliced.append([string[end]])
        end += 1

    sliced.append(string[end-1:])
    return sliced


def numirise(nums_list:list):
    # print(nums_list)

    for big_number in range(0, len(nums_list)):
        if nums_list[big_number][0] not in parsed_operators.keys():
            for small_number in range(0, len(nums_list[big_number])):
                for number in parsed_numbers.keys():
                    if nums_list[big_number][small_number].find(number) != -1 and abs(len(nums_list[big_number][small_number]) - len(number)) <= 2:
                        nums_list[big_number][small_number] = parsed_numbers[number]
                        break
        else:
            nums_list[big_number] = [parsed_operators[nums_list[big_number][0]]]

    return nums_list


def realise(numbers_list:list):
    outlist = []
    
    def real_numerisation(number:list):
        # print(number)
        real_num = 0
        max_id = number.index(max(number))
        for x in number[:max_id]:
            real_num += x
        if real_num == 0:
            real_num += 1
        real_num *= number[max_id]


        # print(real_num)
        try:
            if len(number[max_id+1:]) > 1:
                return real_num + real_numerisation(number[max_id+1:])
            else:
                return real_num + number[max_id+1]

        except:
            return real_num        
    for big_number in numbers_list:
        if big_number[0] in parsed_operators:
            outlist.append(big_number[0])
        else:
            if len(big_number) > 1:
                outlist.append(real_numerisation(big_number))
            else:
                outlist.append(big_number[0])

    return outlist


                

user_input = input()

sliced = slice_string(user_input)
# print(*sliced)

numirised = numirise(sliced)
# print(*numirised)

realised = realise(numirised)
print(*realised, end=" ")