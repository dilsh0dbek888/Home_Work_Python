"""1. Ob-havo Tavsifi:"""
# ob_havo = float(input("Ob havo haroritini kiriting : "))
# if ob_havo < 0:
#     print(f"havo sovuq ")
# elif ob_havo >= 0 and ob_havo <= 20:
#     print(f"havo salqin ")
# elif ob_havo > 20 and ob_havo <= 30:
#     print(f"havo iliq ")
# else:
#     print(f"havo issiq ")

"""2. Internet-do'kon Chegirmasi:"""
# harid_summa = float(input("Xaridlaringiz summasini kiriting: "))
# if harid_summa < 50_000:
#     print(f"Sizga chegirma yo'q. Siz {harid_summa} so'm to'lov qilasiz ")
# elif harid_summa >= 50_000 and harid_summa <= 100_000:
#     print(f"Sizga 5% chegima bor. Siz {harid_summa - (harid_summa*0.05)} so'm to'lov qilasiz")
# elif harid_summa > 100_000:
#     print(f"Sizga 10% chegima bor. Siz {harid_summa - (harid_summa*0.01)} so'm to'lov qilasiz")

"""3. Tizimga Kirish:"""
# login = input("Login kiriting : ")
# password = input("Parol kiriting : ")
# if login == "admin" and password == "12345":
#     print("Xush kelibsiz ! Admin")
# else :
#     print("Kechirasiz login yoki parol xato")

"""4. Film Yosh Cheklovi:"""
# yosh = int(input("Yoshingizni kiriting : "))
# if yosh > 0 and yosh < 13:
#     print("Sizga ushbu filim taklif etilmaydi. ")
# elif yosh >= 13 and yosh <= 17:
#     print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin.")
# elif yosh >= 18:
#     print("Siz filmni tomasha qilishingiz mumkun")

"""5. Restoran Menyusi:"""
# menu = ["osh", "mastava", "shashlik"]
# print(menu)
# zakaz = input("Zakas kiriting : ")
# if zakaz == "osh":
#     (f"{zakaz} narxi 40 000 so'm. 5 minutda tayyor bo'ladi.")
# elif zakaz == "mastava":
#     print(f"{zakaz} narxi 30 000 so'm. 3 minutda tayyor bo'ladi.")
# elif zakaz == "shashlik":
#     print(f"{zakaz} narxi 15 000 so'm. 10 minutda tayyor bo'ladi.")
# else:"Bizda bunday taom yo'q"

"""6. Email Tekshiruvi: """
# email = input("Emailni kiriting : ")
# if email.find("@") != -1 and email.find(".com", -4) != -1:
#     print("To'g'ri email manzil")
# else:
#     print("Noto'g'ri email manzil")

"""7. Talaba Baholash Tizimi:"""
# talaba_baho = float(input("Talabani yig'gan balini kiriting : "))
# if talaba_baho >= 86 and talaba_baho < 100:
#     print("5 baxo")
# elif talaba_baho <= 85 and talaba_baho >= 70:
#     print("4 baxo")
# elif talaba_baho <= 69 and talaba_baho >= 55:
#     print("3 baxo")
# else:
#     print("2 baxo")

"""8. Bankomat Pul Yechish:"""
# kartadagi_summa = float(input("Kartangizdagi pul miqdorin kiriting : "))
# yechib_ol_summa = float(input("Yechib olmoqchi bo'lgan summmangiz miqdorin kiriting : "))
# if kartadagi_summa < yechib_ol_summa:
#     print("Hisobingizda yetarli mablag' mavjud emas. ")
# elif yechib_ol_summa < 5_000:
#     print("Minimal yechish summasi 5 000 so'm")
# else:
#     print(f"Pul muvoffaqiyatli yechildi. Kartangizda {kartadagi_summa - yechib_ol_summa} So'm pul qoldi.")

"""9. Ish Jadvalini Tekshirish: """
# hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma"]
# hafta_kuni = input("Hafta Kunini kiriting : ")
# if hafta_kuni in hafta_kunlari:
#     print("bugun ish kuni")
# elif hafta_kuni == "Yakshanba" or hafta_kuni == "Shanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bunaqa hafta kuni yo'q")

"""10. Mobil Tarif Tanlash:"""
# mobil_trafik = float(input("Oyiga nechi GB mobil internet ishlatasiz : "))
# if mobil_trafik <= 1:
#     print("Sizga 'MINI' tarif rejasi mos keladi")
# elif mobil_trafik > 1 and mobil_trafik <= 5:
#     print("Sizga 'Standart' tarif rejasi keladi")
# else:
#     print("Sizga 'Unlimited' tarif rejasi keladi")
