a = ['1 2 32342\n', '4 5 6213\n']
print(len(ans))
for i in range(len(ans)):
    print(ans[i][:len(ans[i])-1])

# array = []
# root = 1
# array.append((root, -100000000, 1000000000))
#
#
# prov = array.pop(0)
# node = prov[0]
# print(prov, node)





















# array_end_ref = [['MAN-10', 'Свободен', 32265], ['MAN-10', 'Свободен', 32266], ['MAN-10', 'Свободен', 32267],
# ['Газель', 'Свободен', 33890], ['Фура', 'Занят', 33037], ['Фура', 'Занят', 33807],
# ['MAN-10', 'Свободен', 32066], ['Газель', 'Свободен', 33800], ['Газель', 'Свободен', 33890],
# ['Газель', 'Свободен', 32090], ['MAN-10', 'Свободен', 32166], ['Газель', 'Свободен', 33490],
# ['Газель', 'Свободен', 33890], ['Бычок', 'Свободен', 24249], ['Фура', 'Занят', 33837],
# ['Фура', 'Занят', 32837], ['Фура', 'Занят', 33817], ['Бычок', 'Свободен', 24249],
# ['MAN-10', 'Свободен', 32066], ['Фура', 'Занят', 30837], ['MAN-10', 'Свободен', 32265],
# ['MAN-10', 'Свободен', 32267], ['Газель', 'Свободен', 33890], ['Фура', 'Занят', 33037],
# ['Фура', 'Занят', 33807], ['MAN-10', 'Свободен', 32066], ['Газель', 'Свободен', 33800],
# ['Газель', 'Свободен', 33890], ['Газель', 'Свободен', 32090], ['MAN-10', 'Свободен', 32166],
# ['Газель', 'Свободен', 33490], ['Газель', 'Свободен', 33890], ['Бычок', 'Свободен', 24249],
# ['Фура', 'Занят', 33837], ['Фура', 'Занят', 32837], ['Фура', 'Занят', 33817], ['Бычок', 'Свободен', 24249],
# ['MAN-10', 'Свободен', 32066], ['Фура', 'Занят', 30837]]
#
#
# Reference = [
#     ['Газель', 2, 3, 2, '1.7-2.2'],
#     ['Бычок', 3, '4.2-5', '2-2.2', '2-2.4'],
#     ['MAN-10', 10, '6-8', 2.45, '2.3-2.7'],
#     ['Фура', 20, 13.6, 2.46, '2.5-2.7']
# ]
# ArrForLast = array_end_ref
# for i in range(len(ArrForLast)):
#     if (ArrForLast[i][0] == 'Газель'):
#         ArrForLast[i] += Reference[0][1:]
#     if (ArrForLast[i][0] == 'Бычок'):
#         ArrForLast[i] += Reference[1][1:]
#     if (ArrForLast[i][0] == 'MAN-10'):
#         ArrForLast[i] += Reference[2][1:]
#     if (ArrForLast[i][0] == 'Фура'):
#         ArrForLast[i] += Reference[3][1:]
# print(ArrForLast)
