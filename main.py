import os.path
import re

time_mask = re.compile(r'^\d{2}:\d{2}$')
grn_mask = re.compile(r'^\d+₴$')

file_path = "ticket_sales.txt"


def check_existence(path: str):
    return os.path.exists(path)


def check_template(lines_list: list[list]):
    for line in lines_list:
        flag = True
        if len(line) != 6:
            print(f"Недостатня кількість заповнених полів у {lines_list.index(line) + 1} рядку.")
            flag = False
        else:
            for item in line[:2]:
                if not item.isdigit():
                    print(f"Нечисловий або порожній запис у {line.index(item) + 1} полі, {lines_list.index(line) + 1} рядку.")
                    flag = False
            for item in line[2:4]:
                if not item.isalpha():
                    print(f"Небуквений або порожній запис у {line.index(item) + 1} полі,"
                          f" {lines_list.index(line) + 1} рядку.")
                    flag = False
            if not re.match(time_mask, line[4]):
                print(f"Хибний формат поля \"Час відправлення\" під номером 5, {lines_list.index(line) + 1} рядку.")
                flag = False
            if not re.match(grn_mask, line[5]):
                print(f"Хибний формат поля \"Ціна\" під номером 6, {lines_list.index(line) + 1} рядку.")
                flag = False

        if flag is True:
            print(f"Дані у {lines_list.index(line) + 1} рядку записані коректно.")


def check_data_correctness(path: str):
    columns_list = []
    with open(path, 'r', encoding="utf-8") as mainFile:
        for i, line in enumerate(mainFile.readlines()):
            columns = line.split('\t')
            columns_list.append(columns)
        check_template(columns_list)
        check_for_repeat(columns_list)


def check_for_repeat(lines_list: list[list]):
    sec_row = [row[1] for row in lines_list]
    if len(sec_row) != len(set(sec_row)):
        print(f"Помилка!\n"
              f"Файл містить неунікальні поля \"Номер рейсу\"")


if not check_existence(file_path):
    print("Помилка відкриття файлу!")
else:
    check_data_correctness(file_path)

