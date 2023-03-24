# # Множества set, frozentset
# # emails = {"geeks@edu.kg", "nur@gmail.com", "kurmanbek@gmail.com",} удаляет повтор
# # print(emails)

# # st = {10, 1.0, True, "Hello",}
# # print(st)

# #  haa = set('hello')
# #  print(haa)

# # company = {"Google", "Netflix","Meta"}
# # company.add('Geeks')#добавляет
# # print(company)
# # company.remove('Meta')#Удаляет
# # print(company)
# # company.pop()#случайно удаляет
# # print(company)

# # num1 = [10,20,30,40,50]
# # num2 = [10,25,30,35,60]
# # print(set(num1 + num2))

# # frozset = frozenset({10,20,30,30,20})
# # print(frozset)

# #Dictionary - словари
# # student = {'name' : 'Nurbolot', 'age' : 18}
# # print(student['name'])
# # nums = [5, 3, 14, 53, 62]
# # print(len(nums))
# # print(student['age'])
# # student.setdefault('job', 'Python Developer')
# # print(student)
# # student.pop('age')#удаляет по указанию
# # print(student)
# # student.popitem()#удаляет последнию строку
# # print(student)
# # student['age'] = '16'
# # print(student)

# # osh = {
# #     'name' : 'osh',
# #     'year' : 2023,
# #     'population' : 2131231
# #     #правая часть перменная : левая ключи
# # }
# # print(osh.keys())#левая строка
# # print(osh.values())#правая строка
# # print(osh.items())#в одну линию

# # for k, v in osh.items():
# #     print(k, v)

# # name = (
# #     'ads',
# #     'sada'  'asd',
# #     'home'
# # )
# # print(name)

# contact = {'MHCS' : 112}
# while True:
#     command = input("1 - Посмотреть 2 - Добавить, 3 - удалить, 4 - обновить: ")
#     #while = input (но while бесконечный)
#     if command == '1':
#         print(contact)
#     elif command == '2':
#         add_name = input("Имя которое надо обавить: ")
#         add_number = input("Номер который надо добавить: ")
#         contact.setdefault(add_number, add_name)
#         print("Успешно добавлен")
#     elif command == "3":
#         delete_number = input("кого удалить: ")
#         contact.pop(delete_name)
#         print("Успешно удалено")
#     elif command == "4":
#         update_name = input("Кого обновить: ")
#         new_number = input("Новый номер: ")
#         contact[update_name] = new_number
#         print("успешно обновлен")
