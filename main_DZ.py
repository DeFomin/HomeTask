import sys
from peewee import *
import sqlite3
from abc import ABC, abstractmethod
import PySimpleGUI as sg
import table
import second_phase
from second_phase import *
from second_phase import second_arr, Ref_new
import Add
import Delete
from Delete import del_arr
import time
from threading import *
from threading import Thread
from peewee import *
import asyncio

# ---------------------------------------------------------------------
final_tmp = Ref_new
t_start = time.perf_counter()
# ---------------------------------------------------------------------
num_proverka = ['да', 'ДА', 'Да', 'НЕТ', 'Нет', 'нет', 'if']
num_proverka_not = ['НЕТ', 'Нет', 'нет']
num_proverka_da = ['да', 'ДА', 'Да', 'if']
contact_information_array = []
arr = []
set_arr = ()
tmp = []
# new_array = []
# ---------------------------------------------------------------------
# sg.theme('DarkBlack')
Reference = [
    ['Газель', 2, 3, 2, '1.7-2.2'],
    ['Бычок', 3, '4.2-5', '2-2.2', '2-2.4'],
    ['MAN-10', 10, '6-8', 2.45, '2.3-2.7'],
    ['Фура', 20, 13.6, 2.46, '2.5-2.7']
]
head_f = ['Тип', 'Бронь', 'Номер данного транспорта']
headings = ['Тип', 'Грузоподъемность, тонн', 'Длина', 'Ширина', 'Высота']
headings_Application = ['Грузоподъемность, тонн', 'Длина', 'Ширина', 'Высота']

information_table_window = [
    [sg.Table(values=Reference,
        headings=headings,
        max_col_width=20,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='right',
        num_rows=10,
        alternating_row_color='#808080',
        key='-CONTACT_TABLE-',
        row_height=20,
        tooltip='This is a table')],
]

Application = [
[sg.Text("Введите габариты вашего груза: "), sg.Text(size=(10, 1), key = "-TOUT-")],
[sg.Text("Введите вес груза:"), sg.Input(key='-Вес-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите длину груза:"), sg.Input(key='-Длина-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите ширину груза:"), sg.Input(key='-Ширина-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите высоту груза:"), sg.Input(key='-Высота-', do_not_clear=True, size=(10, 1))],
[sg.Button('Submit Information'), sg.Button('Show Table')]
]
tab_group = [
                [sg.TabGroup(
                    [[sg.Tab('Reference', information_table_window, element_justification= 'right'),
                    sg.Tab('Application', Application)]],
                    tab_location='centertop')]
            ]



# ---------------------------------------------------------------------
def Main_Table():
    window = sg.Window("Freight transport accounting", tab_group)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Submit Information':
            contact_information = [values['-Вес-'], values['-Длина-'], values['-Ширина-'], values['-Высота-']]
            contact_information_array.append(contact_information)
            sg.popup("Contact Submitted!")
        elif event == 'Show Table':
            table.create(contact_information_array, headings_Application)

arr = contact_information_array



# ---------------------------------------------------------------------
class Basic(ABC):
    @abstractmethod
    def first(self):
        print('__________Freight transport accounting__________')

class Advanced(Basic):
    def first(self):
        super().first()
        print()
        print('Если вы хотите посмотреть справочный материал и создать заявку на перевоз груза, нажмите (1);\n' \
        'Если хотите посмотреть добавить авто, нажмите (2);\n' \
        'Если хотите посмотреть удалить авто, нажмите (3)')

a = Advanced()
a.first()

# ---------------------------------------------------------------------
class IntFloatValueError(Exception): # Исключения
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '"{}" не является верным вводом, принимаются только значения от 1 до 3 включительно'.format(self.value)

def input_main():
    global inp
    print('\nВведите нужную цифру:')
    print('| ', end = '')
    inp = input()
    alf = ['1', '2', '3']
    if (inp.replace('.', '', 1).replace(',', '', 1).isdigit() == 1) and (str(inp) in alf):
        return inp
    else:
        print(IntFloatValueError(inp))
        input_main()
# ---------------------------------------------------------------------
def dal():
    question_exit = input()
    while (question_exit not in num_proverka): # Прооверка на правильный ввод
        print('Попробуйте еще раз (Да/Нет): ')
        print('| ', end = '')
        question_exit = input()

    if (question_exit in num_proverka_not):
        print('Работа программы продолжается')
        question_exit = 'end'

    return question_exit
# ---------------------------------------------------------------------
def If_continue():
    global inp
    if (inp == '1'):
        print('Хотите ли вы добавить/удалить свой транспорт? (Да/Нет)')
        print('| ', end = '')
    if (inp == '2'):
        print('Хотите ли вы создать заявку на перевоз груза или удалить транспорт? (Да/Нет)')
        print('| ', end = '')
    if (inp == '3'):
        print('Хотите ли вы создать заявку на перевоз груза или добавить транспорт? (Да/Нет)')
        print('| ', end = '')
    up = 0
    question_exit = dal()
    if (question_exit in num_proverka_da) and (inp == '2'): # Для вариантов 213 и 231
        up += 1
        print('Продолжим...')
        result = input_main()
        if (result == '1') and (inp != '2'):
            Main_Table()
            print('Хотите ли вы удалить транспорт? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                Delete.Third()
        elif (result == '3') and (inp != '2'):
            Delete.Third()
            print('Хотите ли вы создать заявку на перевоз груза? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                Main_Table()
        else:
            print('Извините, вернуться невозможно')
            If_continue()


    if (question_exit in num_proverka_da) and (inp == '1') and (up == 0): # Для варивнтов 123 и 132
        up += 1
        print('Продолжим...')
        result = input_main()
        if (result == '2') and (inp != '1'):
            second_phase.Second()
            print('Хотите ли вы удалить транспорт? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                Delete.Third()
        elif (result == '3') and (inp != '1'):
            Delete.Third()
            print('Хотите ли вы добавить транспорт? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                second_phase.Second()
        else:
            print('Извините, вернуться невозможно')
            If_continue()

    if (question_exit in num_proverka_da) and (inp == '3') and (up == 0): # Для варивнтов 312 и 321
        up += 1
        print('Продолжим...')
        result = input_main()
        if (result == '1') and (inp != '3'):
            Main_Table()
            print('Хотите ли вы добавить транспорт? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                second_phase.Second()
        elif (result == '2') and (inp != '3'):
            second_phase.Second()
            print('Хотите ли вы создать заявку на перевоз груза? (Да/Нет)')
            print('| ', end = '')
            new = dal()
            if (new in num_proverka_da):
                Main_Table()
        else:
            print('Извините, вернуться невозможно')
            If_continue()


# ---------------------------------------------------------------------

input_main()

if (inp == '1'):
    Main_Table()
    If_continue()
elif (inp == '2'):
    second_phase.Second()
    If_continue()
else:
    Delete.Third()
    If_continue()


# ---------------------------------------------------------------------
def main_exit(): # Возможность выйти из программы
    print('Завершить программу (Да/Нет)?')
    print('| ', end = '')
    question_exit = input()

    while (question_exit not in num_proverka): # Прооверка на правильный ввод
        print('Попробуйте еще раз (Да/Нет): ')
        print('| ', end = '')
        question_exit = input()

    if (question_exit in num_proverka_da):
        print('Досрочное завершение программы')
        # file_out.write('Итоговая таблица:\n') # Запись в файл
        # file_out.write(str(result))
        sys.exit()

    if (question_exit in num_proverka_not):
        print('Продолжим')
        print()
# ---------------------------------------------------------------------
# print(arr)
# new_array = second_arr
# print(second_arr)

apple = 'Заявка Add'
apple_del = 'Заявка Delete'

for i in range(len(second_arr)):
    qwerty = second_arr[i][1]
    second_arr[i][1] = apple
    second_arr[i].append(qwerty)
for i in range(len(second_arr)):
    Ref_new = [second_arr[i]] + Ref_new


for i in range(len(del_arr)):
    qw = del_arr[i][1]
    del_arr[i][1] = apple_del
    del_arr[i].append(qw)
for i in range(len(del_arr)):
    Ref_new = [del_arr[i]] + Ref_new


# print(second_arr)
# print(Ref_new)
print('Подождите окончания работы программы...')

for i in range(3):
    time.sleep(i)
    print(i + 1, '...')

Add.create(Ref_new, head_Off)
print()
# ---------------------------------------------------------------------

# print(Ref_new)
# print(second_arr)
# print(del_arr)
app_new = 'Свободен'
array_end_ref = []
if (len(second_arr) != 0):
    for i in range(len(second_arr) + len(del_arr)):
        if (Ref_new[i][1] == 'Заявка Add'):
            Ref_new[i][1] = app_new
            array_end_ref = [Ref_new[i]] + array_end_ref
            Ref_new[i] = ['0', 'Заявка Delete', '0']

# print(del_arr)
if (len(del_arr) != 0):
    # del_arr.sort(key = lambda x: x[2])
    # del_arr.reverse()
    for i in range(len(del_arr)):
        for j in range(len(Ref_new)):
            if (int(del_arr[i][2]) != int(Ref_new[j][2])) and (str(Ref_new[j][1]) != 'Заявка Delete'):
                array_end_ref.append(Ref_new[j])
                # print(int(del_arr[i][2]), int(Ref_new[j][2]), Ref_new[j])
            else:
                # print(del_arr[i], Ref_new[j])
                Ref_new[j] = ['0', 'Заявка Delete', '0']
else:
    array_end_ref = array_end_ref + Ref_new[len(second_arr):]
# print(del_arr)


# print(Ref_new, '\n', array_end_ref)
# print('------', second_arr)
last_a = []
busy_a = []
last_a_2 = []
busy_a_2 = []
for i in range(len(array_end_ref)):
    if (array_end_ref[i][1] == app_new):
        last_a.append(array_end_ref[i])
    else:
        busy_a.append(array_end_ref[i])

for i in range(len(final_tmp)):
    if (final_tmp[i][1] == app_new):
        last_a_2.append(final_tmp[i])
    else:
        busy_a_2.append(final_tmp[i])
print('Подождите...')
for i in range(3):
    time.sleep(i)
    print(i + 1, '...')
# print(array_end_ref)
if (len(second_arr) != 0) or (len(del_arr) != 0):
    Add.create(array_end_ref, head_Off)

print()

# ---------------------------------------------------------------------
if (len(last_a) != 0):
    temporary = last_a
    temporary_del = busy_a
else:
    temporary = last_a_2
    temporary_del = busy_a_2
cont = []
inf_table = [
    [sg.Table(values=temporary,
        headings=head_Off,
        max_col_width=30,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='right',
        num_rows=20,
        alternating_row_color='#808080',
        key='-CONTACT_TABLE-',
        row_height=25,
        tooltip='This is a table')],
    [sg.Button('Exit')]
]
inf_table_right = [
    [sg.Table(values=temporary_del,
        headings=head_Off,
        max_col_width=30,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='right',
        num_rows=20,
        alternating_row_color='#808080',
        key='-CONTACT_TABLE-',
        row_height=25,
        tooltip='This is a table')],
    [sg.Button('Exit')]
]
book_new = [[sg.Text("Введите характеристики транспорта, который хотите забронировать: "), sg.Text(size=(10, 1), key = "-TOUT-")],
[sg.Text("Введите тип транспорта: "), sg.Input(key='-Тип-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите номер данного автомобиля: "), sg.Input(key='-Номер данного транспорта-', do_not_clear=True, size=(10, 1))],
[sg.Button('Submit Information'), sg.Button('Show Table')]]
Group_last = [
            [sg.TabGroup(
                [[sg.Tab('Available transport for book', inf_table, element_justification = 'left'),
                sg.Tab('Transport Busy', inf_table_right, element_justification = 'right'),
                sg.Tab('Book Car', book_new)]],
                tab_location='centertop')]
]
def Book_fun():
    ww = sg.Window("Cars", Group_last)
    while True:
        event, values = ww.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Submit Information':
            contact_i = [values['-Тип-'], values['-Номер данного транспорта-']]
            cont.append(contact_i)
            sg.popup("Contact Submitted!")
        elif event == 'Show Table':
            table_for_cars.create(cont, head_for_table)

print('Вы хотите забронировать свободный транспорт?')
print('| ', end = '')
new = dal()
if (new in num_proverka_da):
    Book_fun()
    book_arr = cont
    # print(book_arr, cont, second_arr, del_arr)
    str_new = 'Забронирован'
    print('Обработка...\n')
    # print(temporary, book_arr)
    for i in range(len(book_arr)):
        for j in range(len(temporary)):
            if (int(book_arr[i][1]) == int(temporary[j][2])):
                # print(book_arr[i], temporary[j])
                temporary[j][1] = str_new
    # print(temporary)
    Add.create(temporary, head_Off)

# print(book_arr)
# ---------------------------------------------------------------------








print('----------------------------------------------------------------')
# ---------------------------------------------------------------------
for i in range(len(arr)):
    set_arr = (*arr[i], )
    tmp.append(set_arr)
# print(tmp)
# print(Ref_new)
print()
# ---------------------------------------------------------------------
for i in range(len(arr)):
    if (int(float(arr[i][0])) <= 2) and (int(float(arr[i][1])) <= 3) and (int(float(arr[i][2])) <= 2) and (0 <= int(float(arr[i][3])) <= 2.2):
        print('| ', end = '')
        print('Для груза №{} вам подойдет Газель'. format(i))
        res = 'Газель'
        tmp[i] += (res, )
    elif (2 < int(float(arr[i][0])) <= 3) and (3 <= int(float(arr[i][1])) <= 5) and (0 < int(float(arr[i][2])) <= 2.2) and (0 <= int(float(arr[i][3])) <= 2.4):
        print('| ', end = '')
        print('Для груза №{} вам подойдет Бычок'. format(i))
        res = 'Бычок'
        tmp[i] += (res, )
    elif (3 < int(float(arr[i][0])) <= 10) and (6 <= int(float(arr[i][1])) <= 8) and (0 < int(float(arr[i][2])) <= 2.45) and (0 <= int(float(arr[i][3])) <= 2.7):
        print('| ', end = '')
        print('Для груза №{} вам подойдет MAN-10'. format(i))
        res = 'MAN-10'
        tmp[i] += (res, )
    elif (10 < int(float(arr[i][0])) <= 20) and (8 <= int(float(arr[i][1])) <= 13.6) and (0 < int(float(arr[i][2])) <= 2.46) and (0 <= int(float(arr[i][3])) <= 2.7):
        print('| ', end = '')
        print('Для груза №{} вам подойдет Фура'. format(i))
        res = 'Фура'
        tmp[i] += (res, )
    else:
        print('| ', end = '')
        print('Транспорт не определен')
        res = '-'
        tmp[i] += (res, )
# print(arr)
# print(tmp)

print()
# main_exit()
ArrForLast = []
ArrForLast = array_end_ref
# print(ArrForLast)
for i in range(len(ArrForLast)):
    if (ArrForLast[i][0] == 'Газель'):
        ArrForLast[i] += Reference[0][1:]
    if (ArrForLast[i][0] == 'Бычок'):
        ArrForLast[i] += Reference[1][1:]
    if (ArrForLast[i][0] == 'MAN-10'):
        ArrForLast[i] += Reference[2][1:]
    if (ArrForLast[i][0] == 'Фура'):
        ArrForLast[i] += Reference[3][1:]
# print('\n', ArrForLast)
if (del_arr == 0):
    for i in range(len(ArrForLast)):
        ArrForLast[i] = ArrForLast[i][7:]
print(ArrForLast)
# ---------------------------------------------------------------------
try:
    connection = SqliteDatabase('Freight__transport__accounting.sqlite')
    cursor = connection.cursor()
    print('База данных успешно создана и подключена к Sqlite')
    print()
    # ---------------------------------------------------------------------
    sql = "DROP TABLE IF EXISTS BaseOfAllCars"
    cursor.execute(sql)

    cursor.execute("""CREATE TABLE IF NOT EXISTS BaseOfAllCars(
    Type INT,
    Status_of_book STRING,
    Number INT,
    Weight INT,
    Length INT,
    Width INT,
    Height INT);
    """)

    cursor.executemany("INSERT INTO BaseOfAllCars VALUES(?, ?, ?, ?, ?, ?, ?);", ArrForLast)
    connection.commit()
    # ---------------------------------------------------------------------
    sql = "DROP TABLE IF EXISTS Base"
    cursor.execute(sql)

    cursor.execute("""CREATE TABLE IF NOT EXISTS Base(
    Weight INT,
    Length INT,
    Width INT,
    Height INT,
    Recommend STRING);
    """)

    cursor.executemany("INSERT INTO Base VALUES(?, ?, ?, ?, ?);", tmp)
    connection.commit()
    # ---------------------------------------------------------------------
    class BaseModel(Model):
        class Meta:
            database = connection


    class Base(BaseModel):
        Weight = AutoField(column_name='Weight')
        Length = TextField(column_name='Length', null=True)
        Width = TextField(column_name='Width', null=True)
        Height = TextField(column_name='Height', null=True)
        Recommend_Car = TextField(column_name='Recommend', null=True)

        class Meta:
            table_name = 'Base'

    class BaseOfAllCars(BaseModel):
        Type = AutoField(column_name='Type')
        Status_of_book = TextField(column_name='Status_of_book', null=True)
        Number = TextField(column_name='Number', null=True)
        Weight = TextField(column_name='Weight', null=True)
        Length = TextField(column_name='Length', null=True)
        Width = TextField(column_name='Width', null=True)
        Height = TextField(column_name='Height', null=True)

        class Meta:
            table_name_all = 'BaseOfAllCars'

    print('Обработка базы данных...')
    async def goodbye(): # Асинхронность
        k = 0
        for i in range(2):
            k += 1
            await asyncio.sleep(i)
            print(k, '...')
        print('Представлена информация из базы данных с помощью ORM:')

    async def main():
        print('Подождите окончания работы программы...')
        await goodbye()
        query = Base.select().order_by(Base.Weight.desc())
        art = query.dicts().execute()
        print('\nИнформация из первой таблицы:')
        # print(list(sea))
        for i in range(len(art)):
            print('Cargo {}: '.format(i), art[i])

        all_car = BaseOfAllCars.select().order_by(BaseOfAllCars.Type.desc())
        sea = all_car.dicts().execute()

        print('\nИнформация из второй таблицы:')
        for i in range(len(sea)):
            print('Car {}: '.format(i), sea[i])
        print('----------------------------------------------------------------')
            # print('Cargo(s): ', *list(art), '\n')
    asyncio.run(main())
    cursor.close()


except sqlite3.Error as error:
    print()
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print()
        print("Соединение с Sqlite закрыто")
