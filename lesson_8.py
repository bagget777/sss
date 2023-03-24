#модули
# import moduls
# print(moduls.add(30,53))
# print(moduls.hello())
# print(moduls.it)
# print(moduls.lambda_add(40, 50))

#########################

# from moduls import add
# # print(add(30, 40))
# ################################
# from moduls import *
# print(add(30, 432))
# print(it)
# print(lambda_add(10,32))
# ##############################

# from main import choice_name
# from moduls import ist_name
# print(choice_name(ist_name))

#работа с файлами
# f = open('python.txt', 'w')
# # f.write('Geeks Python Files')
# f.close()

# r = open('python.txt')
# print(r.read())
# r.close()

# py = open('hello.py', 'w')
# py.write("print('Hello world)")
# py.close

# # py_r = open('lesson_8.py')
# # print(py_r.read())
# # py_r.close

# #
# with open('Geeks.py', 'w') as f:
#     f.write('it = "Geeks"')

# with open('geeks.py') as r:
#     print(r.read())

while True:
    commands = input("1-добавить, 2-удалить: ")
    if commands == "1":
        add_name = input("Имя: ")
        add_number = input("Номер: ")
        with open('contacts.txt', 'w') as contacts:
         contacts.write(f'{add_name} {add_number}')
        print("успешно добавлено")
    # elif commands == "2":
    #    with open('contacts.txt') as read_contacts:
    #       print(read_contacts.read())
    else:
        add_name = input("Имя: ")
    add_number = input("Номер: ")
    print("контакт удалён")
