import PySimpleGUI as sg

def create(contact_information_array, headings):
    contact_information_window_layout = [
        [sg.Table(values=contact_information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    enable_events=True,
                    key='-CONTACT_TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')]
    ]
 
    contact_information_window = sg.Window("Contact Information Window",
    contact_information_window_layout, modal=True)

    while True:
        event, values = contact_information_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == '-CONTACT_TABLE-':
            selected_index = values['-CONTACT_TABLE-'][0]
            selected_row = contact_information_array[selected_index]
            popup_message = "Вес: " + selected_row[0] + "\n" + "Длина: " + selected_row[1] + "\n" + "Ширина: " + selected_row[2] + "\n" + "Высота: " + selected_row[3]
            sg.popup(popup_message)
            print(selected_row)


    contact_information_window.close()
