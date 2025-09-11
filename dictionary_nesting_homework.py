"""Dictionary vazifa"""
"""1-topshiriq"""
# izohli_lugatlar = {
#     'bool': 'Mantiqiy qiymat',
#     'float' : "O'nlik son",
#     'for' : 'biror amalni qayta qayta bajarish tsikli',
#     'if' : 'Shartni tekshirish tsikli',
#     'integer' : 'Butun son',
#     'sort()' : 'Tartib bilan saralash metodi',
#     'find()' : 'Matnda qiymatni birinchi uchragan indeksini qaytaradi. Agar topilmasa -1',
#     'index()' : 'find()ga o‘xshaydi, lekin qiymat topilmasa xato beradi (ValueError)',
#     'replace()': 'Matndagi eski qiymatni yangisiga almashtiradi',
#     'split()' : 'Matnni bo‘lib ro‘yxat qilib beradi'
# }
# print("Izohli lug'atlar")
# for kalit, qiymat in sorted(izohli_lugatlar.items()):
#     print(f"{kalit} - {qiymat}")

"""2-topshiriq"""
# davlat_poyytaxt = {
#     'Tojikiston' : 'Dushanbe',
#     'AQSH' : 'Vashington',
#     'Rossiya' : 'Moskva',
#     'Italiya' : 'Rim',
#     "O'zbekiston" : 'Toshkent',
#     'Malaziya' : 'Kuala-Lumpur',
#     'Qozogiston' : 'Nursulton',
#     'Singapur' : 'Singapur',
#     'Qirgiziston' : 'Bishkek'
# }
# print("Dunyo poytaxtlari")
# for key in sorted(davlat_poyytaxt.keys()):
#     print(f"{key}")
# print("\nDavlatlarning paytaxti")
# for qiymat in sorted(davlat_poyytaxt.values()):
#     print(f"{qiymat}")

"""3-topshiriq"""
# davlat_poyytaxt = {
#     'Tojikiston' : 'Dushanbe',
#     'AQSH' : 'Vashington',
#     'Rossiya' : 'Moskva',
#     'Italiya' : 'Rim',
#     "O'zbekiston" : 'Toshkent',
#     'Malaziya' : 'Kuala-Lumpur',
#     'Qozogiston' : 'Nursulton',
#     'Singapur' : 'Singapur',
#     'Qirgiziston' : 'Bishkek'
# }
# davlat = input("Qaysi davlatni poytaxtini bilishni xoxlaysiz ? \n>>>> ")
# for key in davlat_poyytaxt.keys():
#     if davlat == key:
#         print(f"{key} poytaxti {davlat_poyytaxt[key]} ")
# else:
#     print(f"Bizda '{davlat}' haqida malimot yo'q")


"""Nesting vazifa"""
"""1-topshiriq"""

# sevimli_kino = {
#     'Ali' : ['Terminator', 'Rambo', 'Titanic'],
#     'Vali' : ['Tenet', 'Inception', 'Interstellar'],
#     'Hasan' : ['Abdullajon', 'Bomba', 'Shaytanat'],
#     'Husan' : ['Maxallada duv-duv agp', 'John Wick'],
#     'Dilshod' : ['Matrissa', 'Qasoskorlar', 'Interstellar']
# }
# for ism, kinolar in sevimli_kino.items():
#     print(f"\n{ism}ning Sevimli kinolari : ")
#     for kino in kinolar:
#         print( kino.upper())

"""2-topshiriq"""
# davlatlar = {
#     'Uzbekiston' : {
#         'poytaxt' : 'Toshkent',
#         'hududi' : '448 978 kv.km',
#         'axolisi' : 38_000_000,
#         'pul birligi' : "so'm"
# },
#     'Rassiya' : {
#         'poytaxt' : 'Moskva',
#         'hududi' : '17 098 246 kv.km',
#         'axolisi' : 144_000_000,
#         'pul birligi' : "rubl"
# },
#     'AQSH' : {
#         'poytaxt' : 'Vashington',
#         'hududi' : '9 631 418 kv.km',
#         'axolisi' : 327_000_000,
#         'pul birligi' : "dollar"
# },
#     'Malayziya' : {
#         'poytaxt' : 'Kuala-Lumpur',
#         'hududi' : '326 750 kv.km',
#         'axolisi' : 25_000_000,
#         'pul birligi' : "rinngit"
# }
# }
#
# for kalit, qiymat in davlatlar.items():
#     print(f"\n {kalit}ning poytaxti {davlatlar[kalit]['poytaxt']}\n"
#           f" hududi {qiymat['hududi']}\n"
#           f" axolisi {qiymat['axolisi']}\n"
#           f" pul birligi {qiymat['pul birligi']}")



"""Dictionary metodlari va misollar"""

d = {"a": 1, "b": 2}
d1 = {"ism" : "Dilshod", "familya" : "Saidov"}
d2 = {"viloyat" : "Xorazm", "tuman" : "Qo'shko'pir"}


# clear() – lug‘atdagi barcha elementlarni o‘chiradi.

# d.clear()
# print(d)
#
# d1.clear()
# print(d1)
#
# d2.clear()
# print(d2)

# copy() – lug‘atning nusxasini qaytaradi.

# d3 = d.copy()
# print(d3)
#
# d4 = d1.copy()
# print(d4)
#
# d5 = d2.copy()
# print(d5)

# fromkeys() – berilgan kalitlardan yangi lug‘at yaratadi, qiymat hammasi uchun bir xil bo‘ladi.

# keys = ["a", "b", "c"]
# d = dict.fromkeys(keys, 0)
# print(d)
#
# kalitlar = ['1', '2', '3']
# k = dict.fromkeys(kalitlar, "salom")
# print(k)
#
# salom = ["salom_1", "salom_2", "salom_3"]
# s = dict.fromkeys(salom, "Assalom aleykum")
# print(s)
#
# get() – kalit qiymatini qaytaradi, agar bo‘lmasa None yoki berilgan default qiymatni qaytaradi.

# print(d.get("a"))
# print(d.get("c", 0))
#
# print(d1.get("familya"))
# print(d1.get("c", 0))
#
# print(d2.get("Viloyat"))
# print(d2.get("Tuman"))

# items() – lug‘atdagi barcha juftliklarni (kalit, qiymat) qaytaradi.

# print(list(d.items()))
#
# print(d1.items())
#
# print(dict(d2.items()))

# keys() – faqat kalitlarni qaytaradi.

# print(list(d.keys()))
#
# print(d1.keys())
#
# print(list(d2.keys()))

# pop() – berilgan kalitni o‘chiradi va qiymatini qaytaradi.

print(d.pop("a"))
print(d)

print(d1.pop("familya"))
print(d1)

print(d2.pop("viloyat"))
print(d2)

# popitem() – oxirgi qo‘shilgan kalit-qiymat juftligini o‘chiradi va qaytaradi.

# print(d.popitem())
# print(d)
#
# d1.popitem()
# print(d1)
#
# d2.popitem()
# print(d2)

# setdefault() – kalit mavjud bo‘lsa, qiymatini qaytaradi; agar bo‘lmasa, yangi qiymat qo‘shib qaytaradi.

# d_ = {"a": 1}
# print(d_.setdefault("a", 10))
# print(d_.setdefault("b", 20))
# print(d_)
#
# d_1 = {"ism" : "Dilshod"}
# d_1.setdefault("ism", 10)
# print(d_1.setdefault("familya", "Saidov"))
# print(d_1)
#
# d_2 = {"tuman" : "Qo'shko'pir"}
# print(d_2.setdefault("viloyat", "Xorazm"))
# d_2.setdefault("tuman" , "Qo'shko'pir")
# print(d_2)

# update() – lug‘atni boshqa lug‘at yoki juftliklar bilan yangilaydi.

# d_ = {"a": 1}
# d_.update({"b": 2})
# print(d_)
#
# d_1 = {"ism" : "Dilshod"}
# d_1.update({"ism" : "Dilshodbek"})
# print(d_1)
#
# d_2 = {"tuman" : "Qo'shko'pir"}
# d_2.update({"viloyat": "Xorazm"})
# print(d_2)

# values() – lug‘atdagi barcha qiymatlarni qaytaradi.





