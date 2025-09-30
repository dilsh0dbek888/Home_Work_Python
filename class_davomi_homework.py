
class Shaxs:
    __odamlar_soni = 0  # klassga oid (class variable)

    def __init__(self, ism, familya, yosh, tyil):

        self.ism = ism
        self.familya = familya
        self.yosh = yosh
        self.__tyil = tyil
        Shaxs.__odamlar_soni += 1

    def get_tyil(self):
        return self.__tyil

    def set_tyil(self, yangi_tyil):
            self.__tyil = yangi_tyil



    def get_info(self):
        return f"{self.ism} {self.familya}, {self.yosh} yoshda"

    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def __str__(self):
        return self.nomi


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init__(self, ism, familya, yosh, tyil, universitet, bosqich):
        super().__init__(ism, familya, yosh, tyil)
        self.universitet = universitet
        self.fanlar = []
        self.__bosqich = bosqich
        Talaba.talabalar_soni += 1


    def get_bosqich(self):
        return self.__bosqich

    def set_bosqich(self, yangi_bosqich):
        if 1 <= yangi_bosqich <= 4:
            self.__bosqich = yangi_bosqich
 


    def fanga_yozil(self, fan):
        if fan not in self.fanlar:
            self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return f"Siz {fan} faniga yozilmagansiz"


    def get_info(self):
        fanlar = ", ".join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Fanlar yo‘q"
        return (f"Talaba: {self.ism} {self.familya}, {self.yosh} yoshda, "
                f"{self.universitet}, {self.__bosqich}-bosqich. Fanlar: {fanlar}")

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni



class Professor(Shaxs):
    def __init__(self, ism, familya, yosh, tyil, mutaxassisligi):
        super().__init__(ism, familya, yosh, tyil)
        self.mutaxassisligi = mutaxassisligi

    def get_info(self):
        return f"Professor: {self.ism} {self.familya}, mutaxassisligi: {self.mutaxassisligi}"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familya, yosh, tyil, username):
        super().__init__(ism, familya, yosh, tyil)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.ism} {self.familya}, login: {self.username}"


class Admin(Foydalanuvchi):
    def __init__(self, ism, familya, yosh, tyil, username):
        super().__init__(ism, familya, yosh, tyil, username)

    def ban_user(self, foydalanuvchi):
        print(f"Foydalanuvchi {foydalanuvchi.username} bloklandi")

    def get_info(self):
        return f"Admin: {self.ism} {self.familya}, login: {self.username}"


class Sotuvchi(Shaxs):
    def __init__(self, ism, familya, yosh, tyil, dokon):
        super().__init__(ism, familya, yosh, tyil)
        self.dokon = dokon

    def get_info(self):
        return f"Sotuvchi: {self.ism} {self.familya}, do‘kon: {self.dokon}"


class Mijoz(Shaxs):
    def __init__(self, ism, familya, yosh, tyil, balans):
        super().__init__(ism, familya, yosh, tyil)
        self.balans = balans

    def get_info(self):
        return f"Mijoz: {self.ism} {self.familya}, balans: {self.balans} so‘m"


matematika = Fan("Oliy Matematika")
fizika = Fan("Fizika")
tarix = Fan(" Jaxon Tarix")


talaba1 = Talaba("Ali", "Valiyev", 21, 2004, "TATU", 2)
talaba1.fanga_yozil(matematika)
talaba1.fanga_yozil(fizika)

print(talaba1.get_info())
print("Tug‘ilgan yili:", talaba1.get_tyil())
talaba1.set_bosqich(3)
print("Yangi bosqich:", talaba1.get_bosqich())


prof = Professor("Javlon", "Asadov", 45, 1979, "Fizika")
print(prof.get_info())


user1 = Foydalanuvchi("Dilshod", "Saidov", 25, 2000, "dilshod25")
admin1 = Admin("Akbar", "Akmalov", 30, 1995, "admin_aziz")
print(user1.get_info())
print(admin1.get_info())
admin1.ban_user(user1)


sotuvchi1 = Sotuvchi("Akmal", "Akbarov", 28, 1996, "A_A Market")
mijoz1 = Mijoz("Asad", "Axadov", 22, 2003, 150000)
print(sotuvchi1.get_info())
print(mijoz1.get_info())


print("Umumiy odamlar soni:", Shaxs.get_odamlar_soni())
print("Talabalar soni:", Talaba.get_talabalar_soni())

