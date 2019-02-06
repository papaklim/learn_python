# -*- coding: utf8 -*-


# with open ('text.txt', 'r', encoding='utf-8') as f:
#     line = f.readline()
#     for s in line:
#         while s in ['(', ')', '.']:
#             new_line = line.replace(s, '')
#             print(new_line)

fish="qwer,asdf.zxcv!"

def del_chars(text):
    for char in text:
        if char in [',','.','!']:
           fotmated_text=text.replace(char,'')
    return fotmated_text




print(del_chars(fish))