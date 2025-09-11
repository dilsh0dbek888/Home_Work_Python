sonlar = [1, 1, 2, 1, 3, 4, 1, 8]
son = [6, 7, 8, 10, 10, 12]
ism = ["Dilshod" , "akmal", "akbar"]
salom = ["salom", "alik"]
mevalar = ["olma" , "anjir" , "shaftoli" , "nok", "olma"]
alphabet = ["a", "b", "c", "c", "d", "d", "g", "c"]


#"""//////////////////////////////////////////////////////////"""

# clear()    Listni bo‘shatadi.

# print (salom.clear())
#
# print (ism.clear())
#
# meva = mevalar.clear()
# print (meva)
#
# #"""//////////////////////////////////////////////////////////"""

# # copy()    Listning nusxasini qaytaradi.

# nusxa = ism.copy()
# print (nusxa)
#
# nusxa = mevalar.copy()
# print (nusxa)
#
#
# nusxa = salom.copy()
# print (nusxa)

#"""//////////////////////////////////////////////////////////"""

# # count()     Listda berilgan qiymat nechta ekanini sanaydi.

# soni = mevalar.count("olma")
# print (soni)
#
# print(sonlar.count(1))
#
# print(alphabet.count("c"))

#"""//////////////////////////////////////////////////////////"""

# extend()    Bir list elementlarini boshqa list oxiriga qo‘shadi.

# mevalar.extend(alphabet)
# print(mevalar)
#
# sonlar.extend(son)
# print(sonlar)
#
# alphabet.extend(son)
# print(alphabet)

#"""//////////////////////////////////////////////////////////"""

# index()    Elementning birinchi uchragan indeksini qaytaradi.
#
# print(mevalar.index("olma"))
#
# print(alphabet.index("d"))
#
# print(son.index(10))
# reverse()     List elementlarini teskari tartibda qiladi.

# son.reverse()
# print(son)
#
# alphabet.reverse()
# print(alphabet)
#
# ism.reverse()
# print(ism)

# """//////////////////////////////////////////////////////////"""

# sort()     Listni tartiblaydi (default: o‘sish tartibida).
# ism.sort()
# print(ism)
#
# alphabet.sort()
# print(alphabet)
#
son.sort()
print(son)
#
# alphabet.sort()
# print(alphabet)