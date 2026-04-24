# 1
class Odam:
    def __init__(self, name, age):
        self.ism = name
        self.yosh = age

    def salom(self):
        print("Salom", end="")

class Talaba(Odam):
    def salom(self):  # bu yerda tuzatildi
        super().salom()
        print(", men talaba")

a = Talaba("Bunyod", 19)
a.salom()

# 2
class Hayvon:
    def __init__(self, name):
        self.nomi = name

    def ovoz(self):
        print("ovoz chiqardi")


class Mushuk(Hayvon):
    def ovoz(self):
        super().ovoz()
        print("Miyav")

a = Mushuk("Sobr")
a.ovoz()

# 3
class Transport:
    def __init__(self, model):
        self.model = model

    def harakat(self):
        print("Harakatlanmoqda")


class Mashina(Transport):
    def harakat(self):
        print("Mashina yurmoqda")

a = Mashina("cobolt")
a.harakat()

# 4
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def info(self):
        print(self.nomi)


class Darslik(Kitob):
    def info(self):
        super().info()
        print(f"Bu darslik")

a = Darslik(123, "456")
a.info()

# 5
class Ishchi:
    def __init__(self, name, maosh):
        self.nomi = name
        self.moash = maosh

    def ishla(self):
        print("Ishlamoqda")


class Dasturchi(Ishchi):
    def ishla(self):
        print("Code yozmoqda")

a = Dasturchi("Bunyod", 1234567)
a.ishla()
