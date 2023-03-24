#print("hi world")
#print("hello user")
#print(30-10)
#print(10 * 10)
#print(10/2) 
#print(1//2)
#print( 7 % 3)
#print( 3 + 6 / 9)
#print(3**4)
#name ="bagget777"
#print(name)
#number_one=1
#print(number_one)
#hi = "bagget studio"
#print(hi)
#number = 10.5
#print(number * 8.2)
#print(number / 4)
#one_1 = 1
#print(one_1)
#print(type(12))
#print(type(15.0))
#print(type("Osh"))
#print("hi world" + "10") #Контатинация
#методы строк 
#title маленький текст
#upper большой текст
# name = "bagget777"
#print(name.upper())
#print(name.title())
#print(name.count('n'))
#print('gEEks'.title())
#print("gEEks".upper())
#it = "Geeks"
#print(it[4])
#it_company = "Google"
             #012345
#print(it_company[4])
#print(it_company[0:2])
#print(it_company[3:6])
#print(10 + 4.0)
#print(5.0 + 10)
#print(True + 1)
#print(True + 2)
#print(False + 1)
#print(False + 3)
#print(10 + int("5"))
#print(float(3) + int ("100"))
#print(10 + int("5"))
#print(int("10")) + (int("10))
#name = "bagget777"
#age = 14
#language = "python"
#developer = True
#height = 176.3
#print ("Hello I'm " + name + "and my age " + str(age) + ". My language is " + language)
#print("Hello, I'm ",  name,  "and my age ",  age,  ". My language is ",  language)
#print(f"Hello, I'm {name} and my age {age}. My Language is {language}")
#name = input("Введите своё имя")
#print("Здравствуйте", name)
#num1 = input("Num1:")
#num2 = input("Num2:")
#print(int(num1) + int(num2))
#mil = float(input("Введите мили:"))
#print("Ответ:", mil * 123410, "lm")
#Операторы сравнения
#print(4 == 4)
#print(10 == 11)
#print("Hello" == "hello")

#print(400 != 400)
#print(500 != 5)

#print(10 > 1)
#print(3 > 7)

#print(1 < 29)
#print( 100<3 )

#print(10 <= 11)
#print(12 <= 1)

#print(10 >= 12)
#print(321 >= 172)
#num1 = 100
#num2 = 100
#if num1 > num2:
    #print ("Первое число больше")
#else:
    #print("Второе число больше")
#number1 = int(input("Первое число:"))
#operator = input("+, -, /,:")
#number2 = int(input("Второе число:"))
#if operator == "+":
    #print("Ответ:", number1 + number2)
#elif operator == "-":
    #print ("Ответ:", number1 - number2)
#elif operator == "*":
    #print ("Ответ:", number1 * number2)
#elif operator == "/":
    #print ("Ответ:", number1 / number2)
#else: 
   # print("Оператор не найден")
  
# from random import choice
# def choice_name(names:list)->str:
#     res = choice(names)
#     return res
from moduls import fun2
def fun1():
    return "Function one"
print(fun1())
print(fun2())