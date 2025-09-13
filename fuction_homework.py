# #  1  -  misol
# def user_data(first_name,last_name,age):
#     print(f"Ism : {first_name} \nFamilya : {last_name} \nYosh : {age} yoshda")
#
# first_name = input("Ismingizni kiriting : ")
# last_name = input("Familyangizni kiriting : ")
# age = int(input("Yoshingizni kiriting : "))
# user_data(first_name,last_name,age)
#
#
#
# def user_data(first_name,last_name,age):
#     toliq_ism = f"Ism : {first_name} \nFamilya : {last_name} \nYosh : {age} yoshda"
#     return toliq_ism
#
# first_name = input("Ismingizni kiriting : ")
# last_name = input("Familyangizni kiriting : ")
# age = int(input("Yoshingizni kiriting : "))
# toliq_ism = (user_data(first_name,last_name,age))
# print(toliq_ism)


# #  2  -  misol
# def find_max(a, b, c):
#     katta = max(a, b, c)
#     if a != b and b != c and a != c:
#         print(f"Kiritilgan sonlardan eng kattasi : ", katta)
#     elif a == b and b != c:
#         print(f"Kiritilgan sonlardan eng kattasi : A va B = {a} ")
#     elif a == c and b != c:
#         print(f"Kiritilgan sonlardan eng kattasi : A va C = {a} ")
#     elif b == c and a != c:
#         print(f"Kiritilgan sonlardan eng kattasi : B va C = {b} ")
#     else:
#         print(f"Kiritilgan sonlardan eng kattasi : A va B va C = {a} ")
#
# a = input("A ga qiymat bering : A = ")
# b = input("B ga qiymat bering : B = ")
# c = input("C ga qiymat bering : C = ")
# find_max(a, b, c)


# 3 - misol

# def find_letter_count(word, letter):
#     count = 0
#     i = 0
#     while i < len(word):
#         if word[i] == letter:
#
#             count += 1
#         i += 1
#     print(f'"{word}" so‘zida "{letter}"  {count} ta.')
# word = input("Ixtiyoriy so'z yoki matin kiriting : \n>>>")
# letter = input("Berilgan gapdan izlamoqchi bo'lgan ma'lumotingizni kiriting : \n>>>")
#
# find_letter_count(word, letter)


# 4-misol
# def list_sum(my_list):
#     print(f"Kiritgan sonlaringizni yig'indisi : {sum(my_list)} ")
#
# soni = int(input("Nechta sonni yigindisi kerak ? \nSonini kiriting  : "))
# a = 0
# my_List = []
# while a < soni:
#     number = int(input(f"{a + 1} - raqamni kiriting : "))
#     a += 1
#     my_List.append(number)
# list_sum(my_List)

# 5-misol
# def daraja(a, b):
#     print(a ** b)
#
# a = int(input("A ni kirit. a = "))
# b = int(input("B ni kirit. b = "))
# daraja(a, b)

# 6-misol
# def daraja(a, b, c, d):
#     print(a ** b)
#     print(a ** c)
#     print(a ** d)
# a = int(input("A ni kirit. a = "))
# b = int(input("B ni kirit. b = "))
# c = int(input("A ni kirit. c = "))
# d = int(input("B ni kirit. d = "))
# daraja(a, b, c, d)



# # 7-misol
# def digit_count_sum(word):
#     print(f" yig'indi = {sum(word)}\nraqamlar soni {len(word)} ta")
#
# word = input("ixtiyoriy matin kiriting : ")
# raqam = []
# for belgi in word:
#     if belgi.isdigit():
#         raqam.append(int(belgi))
# digit_count_sum(raqam)


# 8-misol
# def add_right(a, b):
#     print(a, b, sep='')
#     print(str(a) + str(b))
# a = int(input("A ni kirit. a = "))
# b = int(input("B ni kirit. b = "))
# add_right(a, b)


# 9-misool
# def add_left(a, b):
#     print(b, a, sep='')
#     print(str(b) + str(a))
#
# a = int(input("A ni kirit. a = "))
# b = int(input("B ni kirit. b = "))
# add_left(a, b)


# 10 - misol
# def work_with_lidt(a):
#     c = []
#     for i in a:
#         print(f"{kichik_son * i}")
#     print(c)
#
#
# a = []
# kirit = int(input("nechta son kiritasiz : son = "))
# son = 1
# while son <= kirit:
#     b = int(input(f'{son} - son = '))
#     a.append(b)
#     son += 1
# kichik_son = min(a)
# work_with_lidt(a)


# 11- misol
# def big_sales(sales):
#
#     max_daromad = max( sales.values())
#     return max_daromad
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
#     }
# print(big_sales(sales))


# 12-misol
# def min_max(numbers, max_num, min_num):
#     if min_qiymat == min(my_list):
#         min_num = "minimal qiymatni to'g'ri kiritdingiz"
#     else:
#         min_num = f"{min_qiymat} bu minimal qiymat emas. minimal qiymat {min(numbers)}"
#     if max_qiymat == max(my_list):
#         max_num = ("maximal qiymatni to'g'ri kiritingiz")
#     else:
#         max_num = f"{max_qiymat} bu maximal qiymat emas.  maximal qiymat {max(numbers)}"
#     return min_num, max_num
# my_list = []
# list_elements = int(input("Listga nechta element kiritasiz : \nson = "))
# a = 0
# while a < list_elements:
#     element = int(input(f"{a +1} - element = "))
#     my_list.append(element)
#     a += 1
# min_qiymat = int(input("minimal qiymat nechiga teng ? \n>>>"))
# max_qiymat = int(input("maximal qiymat nechiga teng ? \n>>>"))
# print(min_max(my_list, max_qiymat, min_qiymat))


# 13 - misol
# def expensiveProduct(products):
#     eng_qimmat_telefon = max(products)
#     return eng_qimmat_telefon
#
# products  =[
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ]
# qiymatlar = []
# for item in products:
#     narx = item['price']
#     qiymatlar.append(narx)
# print(expensiveProduct(qiymatlar))
