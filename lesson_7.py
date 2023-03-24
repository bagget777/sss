#lambda функции
# def mult_two(number:int) -> int:
#    return number * number
# print(mult_two(10))
###########
# lambda_mult_two =lambda number: number * number
# print(lambda_mult_two(10))

# print((lambda number: number + number)(10))

# def add(num1:int=10, num2:int=10) -> int:
#     return num1 + num2
# print(add(23))
# lambda_add = lambda num1=10, num2=20: num1 + num2 
# print(lambda_add(20, 30))
# print(lambda_add())

# print((lambda num1, num2: num1 + num2)(30, 30))
##########
# numbers = [10, 20, 30, 40, 50]
# new_numbers = []
# def mult_two_list(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n * 2)
#     return new_numbers
# print(mult_two_list(numbers))

# numbers = [10,20,30,40]
# lambda_new_numbers = list(map(lambda numbers:numbers * 2, numbers))
# print(lambda_new_numbers)

# numbers = [10,20,30,40,50]
# print(list(map(lambda numbs: numbs * 2, numbers)))
# ########## 
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20,]
# chet = []
# def chet_nams(m:list) -> list:
#     for n in m:
#         if n % 2 == 0:
#             chet.append(n)
#     return chet
# print(chet_nams(nums))
# #####
# nums = [10,20,30,40,50,60]
# lambda_a = list(filter(lambda numbers: numbers % 2 == 0, nums))
# print(lambda_a)
# #####
# nums = [10,20,30,20,3,4,342,523,231,342,5436,294]
# print(list(filter(lambda nums: nums % 2 == 0, nums)))
# ########################
# print(list(filter(lambda nums: nums % 2 == 0, [10,20,41,436,21494,436,32984,564,328523,85438583,])))

#args,, kwargs
# print("Fake","True","Index")
# print("Hello world")

# def bagget(*s:str):
#    # print(s)
#    for n in s:
#       print("Приветствую", n)
# bagget("baget_top","hii")
########
# def student(name:str, *points:int) -> str:
#     print(name, round(sum(points) / len(points)))
# student("bagget", 2, 5, 5, 4, 2, 4, 5)
# student("good", 5, 4, 5, 4, 3, 4, 5, 3, 2)
################
# def translate(**words):
#     print(words)
# translate(Apple = "Яблоко", Phone = "Телефон")

