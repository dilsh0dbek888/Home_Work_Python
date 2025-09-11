# ranglar = ['qizil', 'sariq', 'yashil']
# qiymat = True
# while qiymat:
#     svetafor_rangi = input('sevtafor qaysi rangda ?\n>>>').lower()
#     if svetafor_rangi in ranglar:
#         print("raxmat to'g'ri keladi ")
#         break
#     else:
#         print("bu xato rang ")
#         continue


# import random
# imkoniyat = 1
# son = random.randint(1, 10)
# while True:
#     a = int(input(f'1 dan 10 raqam kiriting \n>>>' ))
#     if a == son:
#         print(f"tabriklaymiz siz to'g'ri topdingiz. Bu son {son} edi")
#         print(f"urinishlar soni {imkoniyat} ta")
#         break
#     else:
#         print("xato")
#     imkoniyat += 1


# dustlar = []
# ishora = True
# while ishora:
#     ismlar = input("Do'stingiz ismini kiriting \n>>>")
#     dustlar.append(ismlar)
#     kiritish = input("Yana bitta do'stinizni ismini kiritasizmi \n"
#                      "Kiritishni xoxlamasangiz 'STOP' deb yozing \n>>>").upper()
#     if kiritish == "STOP":
#         ishora = False
# print(f"Do'stlaringiz to'yxati \n{dustlar}")
# print("Do'stlaringiz")
# for ism in dustlar:
#     print(ism)


valyuta_kursi = 12_500
print("Qanaqa amaliyot bajarmoqchisiz ?"
      "\n1 - usd -> sum   \n2 - sum -> usd")
ishora = True
while  ishora:
    amaliyot = input("amaliyot turini kiriting \n>>>")
    if amaliyot == str(1):
        usd = float(input("USD miqdorini kiriting \n>>>"))
        print(f"{usd} usd {usd * valyuta_kursi} so'm bo'ladi")
    elif amaliyot == str(2):
        sum = float(input("Summani kiriting \n>>>"))
        print(f"{sum} so'm {sum / valyuta_kursi} usd bo'ladi")
    kirit = input("Yana amalyot amalga oshirasizmi \n"
                  "Dastur tugashi uchun 'EXIT' deb yozing").upper()
    if kirit == "EXIT":
        ishora = False
