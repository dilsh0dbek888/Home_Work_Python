
# with open("pi_million_digits.txt", "r") as file:
#     fayl = file.read()
#
# pi = ""
#
# for raqam in fayl:
#     if raqam.isdigit():
#         pi = pi + raqam
#
# print(pi)
# qidiruv = input("Qidirmoqchi bo'lgan sonni kiriting : ")
# if qidiruv in pi:
#     print("Natija : ", True)
# else:
#     print(False)
# if qidiruv.isdigit():
#     print(f"Siz qidirgan son bu faylda < {pi.count(qidiruv)} > marta qatnashgan ekan.")
# else:
#     print(f"Siz qidirgan < {qidiruv} > soni bu faylda topilmadi.")


with open("pi_million_digits.txt", "r") as file:
    fayl = file.read()

pi = "".join(raqam for raqam in fayl if raqam.isdigit())
pii = float(pi)

qidiruv = input("Qidirmoqchi bo'lgan sonni kiriting : ")
if qidiruv in pi:
    print("Natija : ", True)
else:
    print(False)
if qidiruv.isdigit():
    print(f"Siz qidirgan son bu faylda < {pi.count(qidiruv)} > marta qatnashgan ekan.")
else:
    print(f"Siz qidirgan < {qidiruv} > soni bu faylda topilmadi.")
print(type(pii))



import pickle
with open('pi_million', 'wb') as file:
    pickle.dump(pi, file)

with open('pi_million', 'rb') as file:
    fayl1 = pickle.load(file)

    print(fayl1)
