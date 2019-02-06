# try:
#     long=20
#     short=2
#     total=long*3+short*2
#     x = 'a' > 1
#     print(total)
# except TypeError:
#     print('Ощибка типа')
# except NameError:
#     print('Ощибка имени')
#
# print('The End!')
# -------------------------------
# try:
#     age = input("Введите свой возраст: ")
#     age = int(age)
#     if age < 18:
#         raise Exception ('Не подходите по возрасту')
#     print('Всё хорошо')
# except ValueError as e:
#     print(e)
# except (EOFError, KeyboardInterrupt) as e:
#     if type(e) == EOFError:
#         print('Вы сделали EOF')
#     else:
#         print('Вы отменили операцию')
# except Exception as e:
#     print(e)
# finally:
#     print('The End!')
# -------------------------------
# try:
#     n=1
#     try:
#         s = 'a' > 1
#     except:
#         print('inner')
#     finally:
#         print('ok')
# except:
#     print('outer')
# finally:
#     print('The End')

