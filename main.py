import os
from pprint import pprint

current = os.getcwd()
folder = 'sorted'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_res = 'res.txt'

file_1 = os.path.join(current, folder, file_name_1)
file_2 = os.path.join(current, folder, file_name_2)
file_3 = os.path.join(current, folder, file_name_3)
file_res = os.path.join(current, folder, file_name_res)

with open(file_1, encoding='utf-8') as file1, open(file_2, encoding='utf-8') as file2,\
        open(file_3, encoding='utf-8') as file3, open(file_res, 'w', encoding='utf-8') as res:
    dict_files = {
        file1: [len(file1.readlines()), file_name_1],
        file2: [len(file2.readlines()), file_name_2],
        file3: [len(file3.readlines()), file_name_3]
    }

    dict_files_sorted = dict(sorted(dict_files.items(), key=lambda x: x[1]))

    file1.seek(0)
    file2.seek(0)
    file3.seek(0)

    for key, value in dict_files_sorted.items():
        res.writelines(f'{value[1]}\n')
        res.writelines(f'{value[0]}\n')
        for line in key.readlines():
            res.writelines(f'{line}')
        res.writelines(f'\n')