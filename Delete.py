import PySimpleGUI as sg
import table_for_cars
from second_phase import *
import random

arrray_choice = ['Занят', 'Свободен']
second_arr = []
del_arr = []

contact_inf_arr = []

head_Off = ['Тип', 'Бронь', 'Номер данного транспорта']
Car_Delete = [
[sg.Text("Введите характеристики транспорта, который хотите удалить: "), sg.Text(size=(10, 1), key = "-TOUT-")],
[sg.Text("Введите тип транспорта: "), sg.Input(key='-Тип-', do_not_clear=True, size=(10, 1))],
[sg.Text("Введите номер данного автомобиля: "), sg.Input(key='-Номер данного транспорта-', do_not_clear=True, size=(10, 1))],
[sg.Button('Submit Information'), sg.Button('Show Table')]
]

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

Group = [
                [sg.TabGroup(
                    [[sg.Tab('Available transport', inf_table, element_justification= 'right'),
                    sg.Tab('Delete Car', Car_Delete)]],
                    tab_location='centertop')]
            ]

def Third():
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

del_arr = contact_inf_arr

# Third()
# print(contact_inf_arr)
