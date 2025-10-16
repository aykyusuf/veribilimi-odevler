
# Soru 1

class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"Merhaba, benim adım {self.ad} ve {self.yas} yaşındayım.")

class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"Merhaba, ben {self.ad}, bir hocayım.")

    def ders_ver(self):
        print(f"{self.ad} ders veriyor.")

class Sekreter(Insan):
    def __init__(self, ad, yas, ofis_no):
        super().__init__(ad, yas)
        self.ofis_no = ofis_no

    def konus(self):
        print(f"Merhaba, ben {self.ad}, bir sekreterim.")

    def randevu_ayarla(self):
        print(f"{self.ad} randevu ayarlıyor.")

class Ogrenci(Insan):
    def __init__(self, ad, yas, ogrenci_no):
        super().__init__(ad, yas)
        self.ogrenci_no = ogrenci_no

    def konus(self):
        print(f"Merhaba, ben {self.ad}, bir öğrenciyim.")

    def ders_calis(self):
        print(f"{self.ad} ders çalışıyor.")

# Soru 1 Kullanım Örneği
hoca1 = Hoca("Ahmet", 45, "12345")
hoca1.konus()
hoca1.ders_ver()

sekreter1 = Sekreter("Ayşe", 30, "A-101")
sekreter1.konus()
sekreter1.randevu_ayarla()

ogrenci1 = Ogrenci("Mehmet", 20, "67890")
ogrenci1.konus()
ogrenci1.ders_calis()


# Soru 2

# 1- Aşağıdaki kodu yorumlayınız

# Araba adında bir sınıf (class) tanımlanıyor.
class Araba:
    # Bu sınıfın yapıcı metodu (constructor). 
    # Bir Araba nesnesi oluşturulduğunda otomatik olarak çağrılır.
    # self, nesnenin kendisini temsil eder. marka ve model parametrelerini alır.
    def __init__(self, marka, model):
        # Nesnenin marka özelliğini (attribute) alınan marka değeri ile ayarlar.
        self.marka = marka
        # Nesnenin model özelliğini (attribute) alınan model değeri ile ayarlar.
        self.model = model

    # bilgileri_yazdir adında bir metot tanımlanıyor.
    def bilgileri_yazdir(self):
        # Nesnenin marka ve model bilgilerini ekrana yazdırır.
        print(f"Marka: {self.marka}, Model: {self.model}")

# Kullanım
# Araba sınıfından "Toyota" marka ve "Corolla" model bir nesne (araba1) oluşturuluyor.
araba1 = Araba("Toyota", "Corolla")
# araba1 nesnesinin bilgileri_yazdir metodu çağrılarak bilgileri ekrana yazdırılıyor.
araba1.bilgileri_yazdir()


# 2- Bir Dikdortgen sınıfı oluşturun.

class Dikdortgen:
    def __init__(self, genislik, yukseklik):
        self.genislik = genislik
        self.yukseklik = yukseklik

    def alan_hesapla(self):
        return self.genislik * self.yukseklik

# Kullanım
dikdortgen1 = Dikdortgen(5, 10)
alan = dikdortgen1.alan_hesapla()
print(f"Dikdörtgenin alanı: {alan}")


# 3- Bir Kare sınıfı oluşturun.

class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    def kareyi_yazdir(self):
        for i in range(self.kenar):
            print("* " * self.kenar)

# Kare sınıfından bir nesne oluşturma ve kareyi yazdırma
kare1 = Kare(5)
kare1.kareyi_yazdir()
