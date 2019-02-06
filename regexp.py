import re
#
regexp = 'a'
# str = 'papaklim@gmAil.com'
#
# match = re.match(regexp, str, re.IGNORECASE)
# search = re.search(regexp, str, re.IGNORECASE)
# findall = re.findall(regexp, str, re.IGNORECASE)
# # print ('RegExp:')
# # print (match)
# # print ('Other::')
# # print(str.find('a'))
#
# split = re.split('-','10-20-30-40-50')
# print(split)
#
# sub = re.subn('a', '-', str)
# print(sub)
#
# pattern = re.compile(regexp, re.IGNORECASE)
# pattern.match(str)
# pattern.search(str)
# pattern.findall(str)
# pattern.split(str)
# pattern.subn('-', str)

s = 'Python Programming. for Absolute. Winner was Beginner'

# r = re.findall(r'.', s) # find all symbols
# r1 = re.findall(r'\.', s) # find all dots
# r2 = re.findall(r'\w', s) # find all symbols without spaces: [a-zA-Z0-9]
# r3 = re.findall(r'w', s, re.I)
# r4 = re.findall(r'\w', s) #
# r5 = re.findall(r'for', s) # find 'for'
# r6 = re.findall(r'[for]', s) #
# r7  = re.findall(r'[^for]', s) #
# r8  = re.findall(r'[a-zA-Z0-9]', s) #
# r9  = re.findall(r'\w+', s) # [a-zA-Z0-9]
# split = re.split('\.', s)
sub = re.subn('Programming', 'хуйня', s)
print(sub)