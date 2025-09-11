#
# """//////////////////////////////////////////////////////////////////////////////"""
# # capitalize()    Gapdagi faqat birinchi so‘zning birinchi harfini katta qilib beradi.
# matn = "salom dunyo"
# print(matn.capitalize())
#
# matn = "python darsi"
# print(matn.capitalize())
#
# matn = "123abc"
# print(matn.capitalize())
# """//////////////////////////////////////////////////////////////////////////////"""
# # casefold()
# matn = "BaRcha belGILarni kichik Harf BIlAn qaytaradi"
# print(matn.casefold())
#
# matn = "SALom ALEYkum"
# print(matn.casefold())
#
# matn = "BUgun KImdaRSda yo'Q"
# print(matn.casefold())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # center()
# matn = "banan"
# print(matn.center(10)) # matn uzunligidan katta o'lcham kiritish kerak
# matn = "BUgun KImdaRSda yo'Q"
# print(matn.center(50))
# matn = "yaxshi"
# print(matn.center(8))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # count()
# matn = "salom, salom men keldim"
# print(matn.count("salom")) #kiritgan so'z matinda nechi marta qatnashganini hisoblaydi
#
# matn = "yaxshi yaxshi yaxshi"
# print(matn.count("yaxshi"))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # encode()  Matnni bayt (bytes) ko‘rinishga o‘tkazadi.
# matn = "salom, salom men keldim"
# print(matn.encode())
#
# matn = "yaxshi yaxshi yaxshi"
# print(matn.encode())
#
# matn = "ozodov"
# print(matn.encode())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # endswith()    Matn berilgan qiymat bilan tugasa True, aks holda False qaytaradi.
# matn = "salom, salom men keldim."
# print(matn.endswith("."))
#
# matn = "yaxshi yaxshi yaxshi"
# print(matn.endswith(","))
#
# matn = "ozodov."
# print(matn.endswith("."))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # expandtabs()      \t belgilarini bo‘sh joy bilan almashtiradi, uzunligi sizega teng bo‘ladi.
# txt = "S\ta\tl\to\tm"
# x =  txt.expandtabs(4)
# print(x)
#
# matn = "123\t45"
# print(matn.expandtabs(8))
#
# matn = "py\tthon"
# print(matn.expandtabs(2))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # find() Matnda qiymatni birinchi uchragan indeksini qaytaradi. Agar topilmasa -1.
# matn = "salom, salom men keldim."
# print(matn.find("men"))
#
# matn = "salom"
# print(matn.find("l"))
#
# matn = "alik"
# print(matn.find("x"))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # format()     Matn ichiga qiymatlarni {} joyiga qo‘yadi.
# txt = "For only {price:.3f} dollars!"
# print(txt.format(price = 49))
#
# matn = "{}, {}, {}"
# print(matn.format("A", "B", "C"))
#
# matn = "mening ismim{}"
# print(matn.format("Dilshodbek"))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # format_map(dict)     dict yordamida {} joylarini to‘ldiradi.
# matn = "My name is {name}, age {age}"
# print(matn.format_map({"name": "Ali", "age": 25}))
#
#
# matn = "{x} + {y}"
# print(matn.format_map({"x": 5, "y": 10}))
#
# matn = "{first} {last}"
# print(matn.format_map({"first": "John", "last": "Doe"}))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # index() find()ga o‘xshaydi, lekin qiymat topilmasa xato beradi (ValueError).
# matn = "banan"
# print(matn.index("banan"))
#
# matn = "salom"
# print(matn.index("salom"))
#
# matn = "salom, salom men keldim."
# print(matn.index("men"))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isalnum()    Agar matn faqat harf yoki raqamlardan iborat bo‘lsa True.
# txt = "Company12"
# x = txt.isalnum()
# print(x)
#
# matn = "abc!"
# print(matn.isalnum())
#
# matn = "2025"
# print(matn.isalnum())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isalpha()    Agar matn faqat harflardan iborat bo‘lsa True.
# txt = "Company9"
# x = txt.isalpha()
# print(x)
#
# matn = "hello"
# print(matn.isalpha())
#
# matn = "abc123"
# print(matn.isalpha())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isascii()    Matndagi barcha belgilar ASCII bo‘lsa True.
# txt = "Company12л3"
# x = txt.isascii()
# print(x)
#
# matn = "123"
# print(matn.isascii())
#
# matn = "лоло"
# print(matn.isascii())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isdecimal()    Agar matn faqat decimal raqam bo‘lsa True.
# matn = "12345"
# print(matn.isdecimal())
#
# matn = "&12"
# print(matn.isdecimal())        # True
#
# matn = "12sa"
# print(matn.isdecimal())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isdigit()   Agar matn faqat raqam belgilaridan iborat bo‘lsa True.
# matn = "1230.45"
# print(matn.isdigit())
#
# matn = "abc"
# print(matn.isdigit())
# """//////////////////////////////////////////////////////////////////////////////"""
# # isidentifier()    Matn Python identifikatori bo‘la oladimi, tekshiradi.
# matn = "Assalom"
# print(matn.isidentifier())
#
# matn = "123abc"
# print(matn.isidentifier())
#
# matn = "_name"
# print(matn.isidentifier())
#
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # islower()    Matnning barcha harflari kichik bo‘lsa True.
# matn = "Assalom"
# print(matn.islower())
#
# matn = "hello"
# print(matn.islower())
#
# matn = "world123"
# print(matn.islower())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isnumeric()     Agar matn faqat raqam yoki matematik belgidan iborat bo‘lsa True.
# matn = "123045"
# print(matn.isnumeric())
#
# matn = "123a"
# print(matn.isnumeric())
#
# matn = "abc"
# print(matn.isnumeric())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isprintable()    Agar matn faqat ekranga chiqarib bo‘ladigan belgilar bo‘lsa True.
#
# matn = "salom, salom men keldim "
# print(matn.isprintable())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # isspace()    Agar matn faqat bo‘sh joy yoki tab belgilaridan iborat bo‘lsa True.
# matn = "   "
# print(matn.isspace())
#
# matn = " \n  "
# print(matn.isspace())          # True
#
# matn = "\t"
# print(matn.isspace())
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # istitle()    Har bir so‘zning birinchi harfi katta bo‘lsa True.
# matn = "Salom, Salom Men Keldim "
# print(matn.istitle())
#
# matn = "Salom ALekum "
# print(matn.istitle())
#
# matn = "Ha Yaxshi"
# print(matn.istitle())
# """//////////////////////////////////////////////////////////////////////////////"""
# # isupper()    Matnning barcha harflari katta bo‘lsa True.
# matn = "SALOM "
# print(matn.isupper())
#
# matn = "XAYR "
# print(matn.isupper())
#
# matn = "Salom, Salom Men Keldim "
# print(matn.isupper())
# """//////////////////////////////////////////////////////////////////////////////"""
# # join()      Berilgan ro‘yxat (yoki iterable) elementlarini matn yordamida birlashtiradi.
# myTuple = ("John", "Peter", "Vicky")
# x = " / ".join(myTuple)
# print(x)
#
# matn = ("Salom", "Salom",  "Men Keldim ")
# print("=".join(matn))
#
# """//////////////////////////////////////////////////////////////////////////////"""
# # ljust()   Matnni chapga tekislab, o‘ngini to‘ldiradi.
# txt = "banana"
# x = txt.ljust(20)
# print(x, "is my favorite fruit.")
#
# matn = "dog"
# print(matn.ljust(10, "-"))
#
# matn = "hi"
# print(matn.ljust(5, "*"))

# """//////////////////////////////////////////////////////////////////////////////"""
# translate     maketrans() bilan yaratilgan jadvalga asoslanib matnni almashtiradi.
# txt = "Hello Sam!"
# mytable = str.maketrans("H", "P")
# print(txt.translate(mytable))
#
# matn = "hello"
# table = str.maketrans("aeiou", "12345")
# print(matn.translate(table))

# """//////////////////////////////////////////////////////////////////////////////"""
# # partition()      Matnni birinchi uchragan sep bo‘yicha 3 qismga ajratadi.
# txt = "I could eat bananas all day"
# x = txt.partition("eat")
# print(x)
# matn = "hello world"
# print(matn.partition(" "))
#
# matn = "python=dars"
# print(matn.partition("="))

# """//////////////////////////////////////////////////////////////////////////////"""
# # replace()     Matndagi eski qiymatni yangisiga almashtiradi.
# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)
#
# matn = "banana"
# print(matn.replace("a", "o"))
#
# matn = "banana"
# print(matn.replace("a", "o", 2))

# """//////////////////////////////////////////////////////////////////////////////"""
# # rindex()    index()ga o‘xshaydi, oxiridan qidiradi, agar topilmasa xato beradi.
# txt = "Mi casa, su casa."
# x = txt.rindex("casa")
# print(x)
#
# matn = "banana"
# print(matn.rindex("a"))
#
# matn = "hello"
# print(matn.rindex("l"))

# """//////////////////////////////////////////////////////////////////////////////"""
# # split()   Matnni bo‘lib ro‘yxat qilib beradi.
# txt = "welcome to the jungle"
# x = txt.split()
# print(x)
#
# matn = "a b c d"
# print(matn.split(" ", 2))
#
# matn = "python darsi"
# print(matn.split())

# """//////////////////////////////////////////////////////////////////////////////"""
# # splitliness()   Matnni satr bo‘yicha bo‘ladi.
# txt = "Thank you for the music \nWelcome to the jungle"
# x = txt.splitlines()
# print(x)
#
# matn = "line1\r\nline2"
# print(matn.splitlines())
#
# matn = "one\ntwo\nthree"
# print(matn.splitlines(True))

# """//////////////////////////////////////////////////////////////////////////////"""
# # startswith()   Matn berilgan qiymat bilan boshlansa True.
# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")
# print(x)
#
# matn = "world"
# print(matn.startswith("wo"))  # True
#
# matn = "python"
# print(matn.startswith("Java"))

# """//////////////////////////////////////////////////////////////////////////////"""
#
# #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83:  88}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

# """//////////////////////////////////////////////////////////////////////////////"""
# # zfill()    Matnni berilgan uzunlikka teng qilish uchun chapidan nol bilan to‘ldiradi.
# txt = "50"
# x = txt.zfill(10)
# print(x)
#
# matn = "42"
# print(matn.zfill(5))
#
# matn = "-89"
# print(matn.zfill(5))