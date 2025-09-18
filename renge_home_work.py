import random

# seed() – tasodifiy son generatorini boshlang‘ich qiymat bilan ishga tushiradi
# random.seed(10)
# a = random.random()
# print("seed a:", a)
# random.seed(1)
# a_1 = random.random()
# print("seed a_1:", a_1)

# # getstate() – generatorning joriy holatini qaytaradi
# b = random.getstate()
# print("getstate b:", b)
# b_1 = random.getstate()
# print( b_1)
# b_2 = type(b_1)
# print(b_2)

# getrandbits() – tasodifiy bitlardan iborat butun son qaytaradi
# a = random.getrandbits(8)
# print("getrandbits a:", a)
# a_1 = random.getrandbits(16)
# print("getrandbits a_1:", a_1)

# randrange() – berilgan oraliqdan tasodifiy butun son qaytaradi
# b = random.randrange(1, 10)
# print("randrange b:", b)
# b_1 = random.randrange(0, 100, 5)
# print("randrange b_1:", b_1)

# randint() – berilgan oraliqdagi tasodifiy butun son qaytaradi
# c = random.randint(1, 10)
# print("randint c:", c)
# c_1 = random.randint(50, 100)
# print("randint c_1:", c_1)

# choice() – berilgan ketma-ketlikdan bitta element tanlaydi
# a = random.choice([1, 2, 3, 4, 5])
# print("choice a:", a)
# a_1 = random.choice("python")
# print("choice a_1:", a_1)

# choices() – ketma-ketlikdan bir nechta elementni (takrorlanuvchi) tanlaydi
# b = random.choices([1, 2, 3, 4], k=2)
# print("choices b:", b)
# b_1 = random.choices("abcdef", k=3)
# print("choices b_1:", b_1)

# shuffle() – berilgan ketma-ketlik elementlarini aralashtiradi
# lst = [1, 2, 3, 4]
# random.shuffle(lst)
# c = lst
# print("shuffle c:", c)
# lst2 = ["a", "b", "c", "d"]
# random.shuffle(lst2)
# c_1 = lst2
# print("shuffle c_1:", c_1)

# sample() – ketma-ketlikdan elementlarni (takrorlanmas) tanlab qaytaradi
# a = random.sample(range(10), 3)
# print("sample a:", a)
# a_1 = random.sample("abcdef", 3)
# print("sample a_1:", a_1)

# random() – 0 va 1 orasida tasodifiy float qaytaradi
# b = random.random()
# print("random b:", b)
# b_1 = random.random()
# print("random b_1:", b_1)

# uniform() – berilgan ikkita son orasida float qaytaradi
# c = random.uniform(1, 10)
# print("uniform c:", c)
# c_1 = random.uniform(-5, 5)
# print("uniform c_1:", c_1)

# triangular() – uchburchak taqsimot asosida float qaytaradi
# a = random.triangular(10, 20)
# print("triangular a:", a)
# a_1 = random.triangular(10, 20, 15)
# print("triangular a_1:", a_1)

# betavariate() – Beta taqsimotiga asosan float qaytaradi
# b = random.betavariate(2, 5)
# print("betavariate b:", b)
# b_1 = random.betavariate(5, 1)
# print("betavariate b_1:", b_1)

# expovariate() – eksponensial taqsimot bo‘yicha float qaytaradi
# c = random.expovariate(1/5)
# print("expovariate c:", c)
# c_1 = random.expovariate(1/10)
# print("expovariate c_1:", c_1)

# gammavariate() – Gamma taqsimoti bo‘yicha float qaytaradi
# a = random.gammavariate(2, 5)
# print("gammavariate a:", a)
# a_1 = random.gammavariate(5, 1)
# print("gammavariate a_1:", a_1)

# gauss() – Gauss taqsimotiga asosan float qaytaradi
# b = random.gauss(0, 1)
# print("gauss b:", b)
# b_1 = random.gauss(100, 20)
# print("gauss b_1:", b_1)

# lognormvariate() – log-normal taqsimot asosida float qaytaradi
# c = random.lognormvariate(0, 0.25)
# print("lognormvariate c:", c)
# c_1 = random.lognormvariate(1, 0.5)
# print("lognormvariate c_1:", c_1)

# normalvariate() – normal taqsimot bo‘yicha float qaytaradi
# a = random.normalvariate(0, 1)
# print("normalvariate a:", a)
# a_1 = random.normalvariate(100, 15)
# print("normalvariate a_1:", a_1)

# vonmisesvariate() – von Mises taqsimoti bo‘yicha float qaytaradi
# b = random.vonmisesvariate(0, 4)
# print("vonmisesvariate b:", b)
# b_1 = random.vonmisesvariate(1, 1)
# print("vonmisesvariate b_1:", b_1)

# paretovariate() – Pareto taqsimoti bo‘yicha float qaytaradi
# c = random.paretovariate(2)
# print("paretovariate c:", c)
# c_1 = random.paretovariate(3)
# print("paretovariate c_1:", c_1)

# weibullvariate() – Weibull taqsimoti bo‘yicha float qaytaradi
# a = random.weibullvariate(1, 1.5)
# print("weibullvariate a:", a)
# a_1 = random.weibullvariate(2, 5)
# print("weibullvariate a_1:", a_1)