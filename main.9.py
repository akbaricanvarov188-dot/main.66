class Kompyuter:
    def __init__(self, nomi, ram, xotira):
        self.nomi = nomi
        self.ram = ram
        self.xotira = xotira

    def malumot(self):
        print("Nomi:", self.nomi)
        print("RAM:", self.ram)
        print("Xotira:", self.xotira)


kompyuter = Kompyuter("Lenovo", "8 GB", "512 GB")
kompyuter.malumot()

class Kitob:
    def __init__(self, nomi, muallif, narxi):
        self.nomi = nomi
        self.muallif = muallif
        self.narxi = narxi

    def malumot(self):
        print("Kitob:", self.nomi)
        print("Muallif:", self.muallif)
        print("Narxi:", self.narxi)


kitob = Kitob("Python", "Ali", 50000)
kitob.malumot()

class Telefon:
    def __init__(self, brend, model, batareya):
        self.brend = brend
        self.model = model
        self.batareya = batareya

    def zaryad(self, foiz):
        self.batareya += foiz

    def malumot(self):
        print("Brend:", self.brend)
        print("Model:", self.model)
        print("Batareya:", self.batareya)


telefon = Telefon("Samsung", "A52", 40)
telefon.zaryad(30)
telefon.malumot()

class Oyinchi:
    def __init__(self, ism, oyin, ochko):
        self.ism = ism
        self.oyin = oyin
        self.ochko = ochko

    def ochko_qoshish(self, son):
        self.ochko += son

    def malumot(self):
        print("Ism:", self.ism)
        print("Oyin:", self.oyin)
        print("Ochko:", self.ochko)


oyinchi = Oyinchi("Akbar", "Roblox", 100)
oyinchi.ochko_qoshish(50)
oyinchi.malumot()

