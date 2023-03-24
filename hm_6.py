#1)
# def my_best_work(mbw:str) -> str:
#     split_mbw = mbw.split()
#     res = ""
#     for i in split_mbw:
#         res += i[0].upper()
#     return res       
# print(my_best_work("Моё Лучшее Задания"))
# ######### 3)
# def izogramma(word:str) ->str:
#     if len(word) == len(set(word)):
#         return True
#     else:
#         return False
# print(izogramma("HEKKI"))
# print(izogramma("HEKKI"))
# print(izogramma("hi"))
######## 4)
# def reverse_int(num:int=23) -> int:
#     return int(str(num)[::-1])
# print(reverse_int(27))
#########2)
# def count_words(word:str)->str:
#     word_split = word.lower().replace(',', '').split()
#     res = {}
#     for n in word_split:
#         res[n] = word_split.count(n)
#     return res
# print(count_words("Money, money, money, it's always sunny, in the richmen's world"))
