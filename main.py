# импортируем модуль 
import json
from colorama import Fore, Back, Style



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

    # print(string)

    start = 0
    end = 0
    for part in string:
        if part in parsed_operators.keys():
            sliced.append(string[start:end])
            start = end + 1
            sliced.append([string[end]])
        end += 1

    sliced.append(string[start:])
    return sliced


def numirise(nums_list:list):
    # print(nums_list)

    for big_number in range(0, len(nums_list)):
        if nums_list[big_number][0] not in parsed_operators.keys():
            for small_number in range(0, len(nums_list[big_number])):
                for number in parsed_numbers.keys():
                    if nums_list[big_number][small_number].find(number) != -1 and abs(len(nums_list[big_number][small_number]) - len(number)) <= 2 and number[0] == nums_list[big_number][small_number][0]:
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

def signal_handler(signum, frame):
    raise RuntimeError("Слишком Долго!")

commands_dictionary = {
    "/cmd": "показать допустимые команды",
    "/help": "показать допустимые значения и операторы",
    "/end": "закончить выполнение программы"
}

commands_dictionary_actions = {
    "/cmd": "cmds()",
    "/help": "help()",
    "/end": "loop = False"
}

commands = []
for cmd in commands_dictionary.keys():
    commands.append(cmd)

def cmds():
    for cmd_key, cmd_val in commands_dictionary.items():
        print(f"{Fore.CYAN}{cmd_key}{Style.RESET_ALL} - {Fore.BLUE}{cmd_val}{Style.RESET_ALL}")
    
def help():
    print(f"\n{Back.MAGENTA}ДОПУСТИМЫЕ ЧИСЛА{Style.RESET_ALL}\n")
    for number in parsed_numbers.keys():
        print(number)
    print(f"\n{Back.MAGENTA}ДОПУСТИМЫЕ ОПЕРАЦИИ{Style.RESET_ALL}\n")
    for operation in parsed_operators.keys():
        print(operation)

print(
f'''Здравствуйте!
Вы используете тестовый калькулятор {Fore.GREEN}GCalc (Glebocrew Pakostin Corporation){Style.RESET_ALL}
Начните писать свои примеры после данного сообщения в окне ввода.
Если вы хотите ознакомиться с допустимыми специальными командами приложения напишите /cmd
Если вы хотите ознакомиться с допустимыми числами и операторами напишите команду /help'''
)

ERROR_MSG = f"\n{Fore.RED}{Back.LIGHTYELLOW_EX}Runtime Error: {Style.RESET_ALL}{Fore.RED}Что-то пошло не так. Скорее всего вы ввели такое число, которое интерпретатор не позволяет посчитать из за большого размера.{Style.RESET_ALL}"
USER_ERROR_MSG = f"\n{Fore.RED}{Back.LIGHTYELLOW_EX}User Query Error: {Style.RESET_ALL}{Fore.RED}К сожалению, вы ввели неправильный формат входных данных. Попробуйте ещё раз. Чтобы ознакомится с допустимыми значениями ввода напишите {Fore.MAGENTA}/help{Style.RESET_ALL}"

def polling():
    sliced = slice_string(user_input)
    # print(*sliced)
    numirised = numirise(sliced)
    # print(*numirised)
    # print(numirised)
    try:
        realised = realise(numirised)
        print(*realised, "=", end=" ")
        query = ""
        for element_of_str in realised:
            query += str(element_of_str)                
        exec(f"print({query})")
    except NameError:
        print(USER_ERROR_MSG)
    except TypeError:
        print(USER_ERROR_MSG)
    except RuntimeError:
        print(ERROR_MSG)
    except ValueError:
        print(ERROR_MSG)

loop = True
while loop:
    user_input = input(f">>>{Fore.LIGHTCYAN_EX}")
    print(f"{Style.RESET_ALL}", end="")
    if user_input.lower() in commands:
        exec(commands_dictionary_actions[user_input.lower()])
    else:
        polling()
