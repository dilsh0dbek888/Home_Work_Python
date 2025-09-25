"""1 - misol"""
# class User:
#     def __init__(self, first_name, last_name, email, password):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#         print(f"Ism : {self.first_name}, \tFamilya : {self.last_name}, \tEmail: {self.email}, \tKod: {self.password}")
#
#
# ism = input("Ismingizni kiriting : \n>>> ")
# familya = input("Familyangizni kiriting : \n>>> ")
# gmail = input("Email kiriting : \n>>> ")
# kod = input("Kodni kiriting : \n>>> ")
#
# if "@gmail.com" not in gmail:
#     print(f"Kiritilgan Email xato: {gmail}\nNamuna: abcdefg@gmail.com")
#     gmail = input("Email kiriting : \n>>> ")
#
# User(ism, familya, gmail, kod)


"""2 - misol"""
# class User:
#     def __init__(self, first_name, last_name, email, password):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#
#     def get_first_name(self):
#         return self.first_name
#
#     def get_last_name(self):
#         return self.last_name
#
#     def get_full_name(self):
#         return self.first_name + " " + self.last_name
#
#     def toliq_malumot(self):
#         return f"Ism : {self.first_name}, \tFamilya : {self.last_name}, \tEmail: {self.email}, \tKod: {self.password}"

# ism = input("Ismingizni kiriting : \n>>> ")
# familya = input("Familyangizni kiriting : \n>>> ")
# gmail = input("Email kiriting : \n>>> ")
# kod = input("Kodni kiriting : \n>>> ")
#
# if "@gmail.com" not in gmail:
#     print(f"Kiritilgan Email xato: {gmail}\nNamuna: abcdefg@gmail.com")
#     gmail = input("Email kiriting : \n>>> ")
#
# full_malumot = User(ism, familya, gmail, kod)
# print(f"Ism : {full_malumot.get_first_name()}")
# print(f"Familya : {full_malumot.get_last_name()}")
# print(f"Ism va Familya : {full_malumot.get_full_name()}")
# print(f"Siz kiritgan to'liq malumotlar: \n{full_malumot.toliq_malumot()}")


"""3 - misol"""
# class User:
#     def __init__(self, first_name, last_name, email, password):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#
#     def get_first_name(self):
#         return self.first_name
#
#     def get_last_name(self):
#         return self.last_name
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def toliq_malumot(self):
#         return (f"Ism: {self.first_name}, Familya: {self.last_name}, "
#                 f"Email: {self.email}, Kod: {self.password}")
#
#
#
# user1 = User("Ali", "Valiyev", "ali@gmail.com", "1234")
# user2 = User("Vali", "Aliyev", "valiyev@gmail.com", "abcd")
# user3 = User("Olim", "Qodirov", "Olim@gmail.com", "q1w2")
#
# print("User1 ismi:", user1.first_name)
# print("User2 familyasi:", user2.last_name)
# print("User3 emaili:", user3.email)
#
# print("User1 to'liq ismi:", user1.get_full_name())
# print("User2 to'liq ma'lumot:", user2.toliq_malumot())
# print("User3 ismi:", user3.get_first_name())
# print("User3 familyasi:", user3.get_last_name())
#
# users = [user1, user2, user3]
# print("\nBarcha foydalanuvchilar:")
# for user in users:
#     print(user.toliq_malumot())




class Avto:
    def __init__(self, model, color, karobka, km = None, year = None, price = None ):
        self.model = model
        self.color = color
        self.karobka = karobka
        self.km = km
        self.year = year
        self.price = price

    def get_model(self):
        return self.model

    def get_color(self):
        return self.color

    def get_karobka(self):
        return self.karobka

    def get_km(self):
        return self.km

    def get_year(self):
        return self.year
    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model
    def update_km(self, yangi_km):
        self.km = yangi_km

    def get_info(self):
        return (f"Model: {self.model}, Rang: {self.color}, "
                f"Karobka: {self.karobka},Km : {self.km}, Narx: {self.price}$, "
                f"Yili: {self.year} ")

avto1 = Avto("Chevrolet Malibu", "oq", "avto", 0, 2023, 25_000 )
avto2 = Avto("Chevrolet Cobalt", "qora", "avto", 0, 2025, 15_000)
avto3 = Avto("Kia K5", "qizil", "avto", 150_000, 2019, 20_000)
avto4 = Avto("Hyundai Sonata", "kulrang", "avto", 12_000)
avto5 = Avto("Tesla Model 3", "ko‘k", "avto", None, 2023)
print(avto1.get_model())
print(avto1.get_color())
print(avto1.get_karobka())
print(avto1.get_km())
print(avto1.get_year())
print(avto1.get_price())
print(avto1.get_info())

yangi_km = int(input("Yangi km : "))
avto1.update_km(yangi_km)
print(f"Yangi km : {avto1.get_km()}")
avto1.set_model("Chevrolet Malibu 2")
print(f"Yangi model : {avto1.get_model()}")
print(avto1.get_info())


class Avtosalon:
    def __init__(self, name, destinetion, tel , number_of_auto = None, model = []):
        self.name = name
        self.manzil = destinetion
        self.model = model
        self.tel = tel
        self.number_of_auto = number_of_auto
    def full_information(self):
        return (f"Firma nomi : {self.name}",
                f"Firma manzili : {self.manzil}",
                f"Telfon raqam :  {self.tel}",
                f"Mavjud avtomobillar soni : {self.number_of_auto}",
                f"Mavjud modellar : {self.model}")

    def add_model(self, new_model):
        """Avtosalonga yangi model qo'shadi"""
        self.model.append(new_model)
        # avtomobil sonini ham avtomatik yangilash (ixtiyoriy)
        if self.number_of_auto is not None:
            self.number_of_auto += 1
    def get_model(self):
        return self.model

salon = Avtosalon("Premium Auto", "Toshkent", "+998 90 123 45 67", 2, ['Nexia 3', 'Malibu 2'])
salon2 = Avtosalon("GM Motors", "Samarqand", "+998 88 888 88 88")
salon3 = Avtosalon("Asia Cars", "Namangan", "+998 93 111 22 33")
salon4 = Avtosalon("Elite Auto", "Buxoro", "+998 00 999 88 77")
salon5 = Avtosalon("Speed Motors", "Andijon", "+998 22 333 44 55")
print(salon.full_information())
for malumot in salon.full_information():
    print(malumot)
print(salon2.full_information())
for malumot in salon2.full_information():
    print(malumot)
print(salon3.full_information())
for malumot in salon3.full_information():
    print(malumot)
print(salon4.full_information())
for malumot in salon4.full_information():
    print(malumot)
print(salon5.full_information())
for malumot in salon5.full_information():
    print(malumot)
salon.add_model("Malibu")
salon.add_model("Cobalt")
salon.add_model("Gentra")
salon.add_model("Spark")
print(salon.get_model())
print(salon.full_information())
for model in salon.get_model():
    print(model)

print(dir(Avto))
for a in dir(Avto):
    if a.startswith("__") == False:
        print(a)
print(dir(Avtosalon))
for a in dir(Avtosalon):
    if a.startswith("__") == False:
        print(a)

print(dir(salon))
print(dir(str))
print(dir(int))