

"""1-masala elektron pochta manzillarini tekshirish"""

# pochtalar = ['user1@gmail.com', "user2yahoo.com", "user3@outlook.com", "admin@123.com"]
# for pochta in pochtalar:
#     if pochta.find("@") != -1:
#         print(f"to'g'ri email: {pochta}  ")
#     else:
#         print(f"noto'g'ri email: {pochta}  ")


"""2-masala parol kuchini tekshirish"""
# parollar = ["password123", "qwerty", "admin", "strongpass1!@#$%^&*()", "strongkod1", "asrgethdj"]
# for parol in parollar:
#     if len(parol) < 8:
#         print(f"berilgan parol:  {parol} juda qisqa")
#     elif parol.isalpha() or parol.isdigit():
#         print(f"berilgan parol {parol} zaif")
#     else:
#         print(f"berilgan parol {parol} juda kuchli")


"""3-masala ob havo malumotlarini tahlil qilish"""
# ob_havo = [ 20, 22, 19, 24, 25, 23, 21]
# havo = 0
# ortacha_harrorat = sum(ob_havo) / len(ob_havo)
# print(f"o'rtacha harorat {ortacha_harrorat} ga teng")
# for harorat in ob_havo:
#     havo += harorat
#     if harorat > 22:
#         print(f"{ob_havo.index(harorat)+1} - kun {harorat} gradus Iliq kun")
#     else:
#         print(f"{ob_havo.index(harorat)+1} - kun {harorat} gradus Salqin kun")
# print(f"O'rtacha harorat : {havo / len(ob_havo) } gradusga teng")


"""4- masala Restaron buyurtmalari"""

menu = ["osh", "shashlik", "manti", "lag'mon", "somsa", "norin", "sho'rva", "barak"]
buyurtma = []
soni = int(input("nechta buyurtma qilas? \n>>>>>"))
# zakaz = input("Buyurtmangizni bering")
for i in range(soni):
    zakaz = input(f"{i+1} - Buyurtmangizni bering\n>>>>>")
    buyurtma.append(zakaz.lower())
print(f"Sizning buyurtmalarangiz {buyurtma}")
for b in buyurtma:
    if b in menu:
        print(f"Bizda {b} bor")
    else:
        print(f"Bizda {b} yo'q")


"""5- masala anketa tahlili"""
# yoshlar = [16, 21, 17, 30, 25]
# for yosh in yoshlar:
#     if yosh >= 18:
#         print(f"Siz {yosh} yoshda ekansiz.     Xush kelibsiz!")
#     else:
#         print(f"Siz {yosh} yoshda ekansiz. Siz hali detiski ekansiz.    {18-yosh} yildan keyin qayta harakat qilib ko'ring.")


"""6-masala mobil ilova bildirishnomalari"""

xabarlar = ["Yangi habarlar", "Batareyaeya past", "Yangilanish mavjud"]
sarlavha = input("sarlavha kiriting: ")
for xabar in xabarlar:
    if xabar.lower() == sarlavha:
        print("Telefoningizni quvvatlang")


"""7 - masala Fayillarni guruhlash"""

files = ["kitob.jpg", "kok_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphon_16.jpg"]
image = []
mp3 = []
for file in files:
    if file.find(".jpg") != -1:
        image.append(file)
    else:
        mp3.append(file)
print(f" rasm ko'rinishidagi fayillar   >>>   {image}, \n musiqa ko'rinishidagi fayillar  >>>  {mp3}" )
