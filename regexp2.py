import re

str = 'Python Programming for Absolute Winner was Beginner  '

#Квантификаторы
# + от 1 и больше вхождений = {1,}
# * от 0 и больше вхождений = {0,}
# {0,} => *
# {1,} => +
# {0,1} => ?


r = re.findall(r'\w+$', str)

mail = 'papaklim@gmail.com'

date = '3-3-qwer asd 12-5-1985 abc 12-05-2017, qwe 42-54 23-12-2019, xyz 01-09-2019, qwe 1-12-1789, qwqw 9-05-1212'
# [a-zA-Z0-9] => /w
# [^a-zA-Z0-9] => /W
# [0-9] => /d
# [^0-9] => /D
regexp = re.findall(r'@\w+.+', mail)
regexp1 = re.findall(r'\.\w+$', mail)
regexp2 = re.findall(r'[0-3]{0,}\d+-[0-1]*\d+-(\d{4})', date)

print(regexp)
print(regexp1)
print(regexp2)
print(regexp2)