# #Function функции
# def calc():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1 + num2)

# def welcome():
#     name = input("Ваше имя: ")
#     print("Здравствуйте", name)


# def add(num1, num2): #num1 num2 параметры функции add
#     print(num1 +num2)
# add(10, 40)#Вызываем функцию add и передаем аргументы 10, 40

# def cas(ist:list) -> str:
#     for num in ist:
#      if num % 2 == 0:
#         print(num, "Четный")
#      else:
#         print(num, "Нечетный")

# numbers = [10, 20, 30, 50, 21, 12, 231, 324]
# cas(numbers)
# cas([10,20,12,32,40,32,43])

# def add(num1:int, num2:int) -> int:
#     print(num1 + num2)

# def cool(num1:int, num2:int) -> int:
#     print(num1 - num2)

# def doll(num1:int, num2:int) -> int:
#     print(num1 * num2)

# def pro(num1:int, num2:int) -> float:
#     print(num1 / num2)

# def main(number1:int, number2:int, operator:str) -> int:
#     if operator == "+":
#         add(number1, number2)

#     elif operator == "-":
#         cool(number1, number2)

#     elif operator == "*":
#         add(number1, number2)

#     elif operator == "/":
#         pro(number1, number2)
#     else:
#         print("Такого оператора не существует")
# main(10,20, "+")
# main(10,20, "-")
# main(10,20, "*")
# main(10,20, "/")

# def get_name(name:str="defolt"):
#     print(name)
# get_name()
# print()

# def add(num1:int=1, num2:int=2) -> int:
#     return num1 + num2
# print(add(20, 20))

# def hello():
#     while True:
#         print('hello')
#         return "hello"
# hello()

# try:
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 / num2)
#  except ZeroDivisionError:
#      print("Деление на ноль")
#  except ValueError:
#      print("пишите только цифры")
# except Exception: #отвечает за все виды ошибок но не показывает какой, остальные указываею ошибки своего типа
#     print("Fatal error 404")