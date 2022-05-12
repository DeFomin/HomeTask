import PySimpleGUI as sg
import table_for_cars
import random
 
arrray_choice = ['Занят', 'Свободен']
second_arr = []

contact_inf_arr = []

head_Off = ['Тип', 'Бронь', 'Номер данного транспорта']
head_for_table = ['Тип', 'Номер данного транспорта']
# print(Ref)
# for i in range(random.randint(5, 21)):
#     Ref_new.append(random.choice(Ref))
Ref_new = [['MAN-10', 'Свободен', 32264], ['MAN-10', 'Свободен', 32265],
            ['MAN-10', 'Свободен', 32266], ['MAN-10', 'Свободен', 32267],
            ['Газель', 'Свободен', 33890], ['Фура', 'Занят', 33037],
            ['Фура', 'Занят', 33807], ['MAN-10', 'Свободен', 32066],
            ['Газель', 'Свободен', 33800], ['Газель', 'Свободен', 33890],
            ['Газель', 'Свободен', 32090], ['MAN-10', 'Свободен', 32166],
            ['Газель', 'Свободен', 33490], ['Газель', 'Свободен', 33890],
            ['Бычок', 'Свободен', 24249], ['Фура', 'Занят', 33837],
            ['Фура', 'Занят', 32837], ['Фура', 'Занят', 33817],
            ['Бычок', 'Свободен', 24249], ['MAN-10', 'Свободен', 32066], ['Фура', 'Занят', 30837]]
# print(Ref_new)

inf_table = [
    [sg.Table(values=Ref_new,
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

Car_Add = [
[sg.Text("Введите характеристики транспорта, который хотите добавить: "), sg.Text(size=(10, 1), key = "-TOUT-")],
[sg.Text("Введите тип транспорта: "), sg.Input(key='-Тип-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите номер данного автомобиля: "), sg.Input(key='-Номер данного транспорта-', do_not_clear=True, size=(10, 1))],
[sg.Button('Submit Information'), sg.Button('Show Table')]
]


Group = [
                [sg.TabGroup(
                    [[sg.Tab('Available transport', inf_table, element_justification= 'right'),
                    sg.Tab('Add Car', Car_Add)]],
                    tab_location='centertop')]
            ]


#Define Window

def Second():
    ww = sg.Window("Cars", Group)
    while True:
        event, values = ww.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Submit Information':
            contact_inf = [values['-Тип-'], values['-Номер данного транспорта-']]
            contact_inf_arr.append(contact_inf)
            sg.popup("Contact Submitted!")
        elif event == 'Show Table':
            table_for_cars.create(contact_inf_arr, head_for_table)

# Second()
second_arr = contact_inf_arr

# Second()
# print(second_arr)
# import PySimpleGUI as sg
# import table
# Ref = [
#     ['Газель', 2, 3, 2, '1.7-2.2'],
#     ['Бычок', 3, '4.2-5', '2-2.2', '2-2.4'],
#     ['MAN-10', 10, '6-8', 2.45, '2.3-2.7'],
#     ['Фура', 20, 13.6, 2.46, '2.5-2.7']
# ]
#
# head = ['Грузоподъемность, тонн', 'Длина', 'Ширина', 'Высота']
#
# inf_table = [
#     [sg.Table(values=Ref,
#         headings=head,
#         max_col_width=20,
#         auto_size_columns=True,
#         display_row_numbers=True,
#         justification='right',
#         num_rows=10,
#         alternating_row_color='#808080',
#         key='-CONTACT_TABLE-',
#         row_height=20,
#         tooltip='This is a table')],
#     [sg.Button('Exit')]
# ]
#
# Car_Add = [
# [sg.Text("Введите ваш габариты вашего груза: "), sg.Text(size=(10, 1), key = "-TOUT-")],
# [sg.Text("Введите вес груза:"), sg.Input(key='-Вес-', do_not_clear=True, size=(10, 1))],
# [sg.Text("Введите длину груза:"), sg.Input(key='-Длина-', do_not_clear=True, size=(10, 1))],
# [sg.Text("Введите ширину груза:"), sg.Input(key='-Ширина-', do_not_clear=True, size=(10, 1))],
# [sg.Text("Введите высоту груза:"), sg.Input(key='-Высота-', do_not_clear=True, size=(10, 1))],
# [sg.Button('Submit Information'), sg.Button('Show Table'), sg.Button('Exit')]
# ]
#
#
# Group = [
#                 [sg.TabGroup(
#                     [[sg.Tab('Ref', inf_table, element_justification= 'right'),
#                     sg.Tab('Car_Add', Car_Add)]],
#                     tab_location='centertop')]
#             ]
#
#
# #Define Window
# window =sg.Window("Freight transport accounting", Group)
#
# while True:
#     event, values = window.read()
#     if event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     elif event == 'Submit Information':
#         contact_inf = [values['-Вес-'], values['-Длина-'], values['-Ширина-'], values['-Высота-']]
#         contact_inf_arr.append(contact_inf)
#         sg.popup("Contact Submitted!")
#     elif event == 'Show Table':
#         table.create(contact_inf_arr, head)

# Inf = Inf_1 = 0
# array = ()
# def begin(s):
#     global Inf
#     alf = '123'
#     t = s
#     # Inf = 0
#     count = 0
#     for i in range(len(t)):
#         if (t[i] in alf):
#             count += 1
#             if (count == len(t)):
#                 Inf = 1
#         else:
#             print(IntFloatValueError(s))
#             print('Попробуйте еще раз:')
#             break
#
#
# def input_main():
#     global inp; global Inf
#     while (Inf == 0):
#         print('\nВведите нужную цифру:')
#         inp = str(input())
#         begin(inp)
