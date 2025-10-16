
# Page 5
print("sinan")
print("sinan","başarlan","T","B","M",sep='.')
a="ali"
b=5
type(a)
type(b)
# tek yorum satırı,
"string tanımlama"
"""
çoklu
Yorum satırı
"""
#veri tipleri
a= 5 #type(a) #integer veri tipi
b="sinan" #string
c= 3.5 #float
d='k' #karakter veri tipi
# Veri yapıları
# liste, (list) elemanları değiştirilebilir (mutable)
# tuple (demet) değiştirilemez (immutable)
# dictonary (key,value)
# set (aynı elemanı yazamazsın)
liste1=[1,3,3,5,4,5,4,"ali","canan"]
liste1[0] #indis,indexler 0 dan başlar
len(liste1) #sayma sayıları 1 den başlar
dir(liste1) #built in functions
liste2=[1,3,3,5,4,5,4]
liste2.sort()
print(liste2)
liste2[0]=100000 #mutable değişir
print(liste2[0])
print(liste2)
liste2.pop()
liste2.append(25)
liste2.insert(7,"25")
print(liste2)
print(liste2[7])
demet=("ali","ayşe")
print(demet)
len(demet)
print(demet[0])
dir(demet)
demet.count("ali")#sayma sayıları 1 den
demet.index("ali")

# Page 6
x="sinan"
type(x) #string ilkerl veri
x.capitalize()
def selam():
    print("selam")
help(print) # ?print
selam() #parametre almayan, değer döndürmeyen function
def selamGotur(isim):
    print("selam",isim)
selamGotur("sinan") #parametre alan değer döndürmeyen
def topla():
    print("toplama yapan fonks.")
def topla(deger,deger2):
    print("{}, {} degerlerini alır".format(deger,deger2))
def topla_parametre(parametre):
    print("alınan degerleri: ",parametre)
topla_parametre(5)
topla(3,5)
selam()
# selam("sinan") # This would cause an error as selam takes no arguments
def topla_return(a,b):
    c=a+b
    return c
topla_return(3,5)
def kareal(a):
    return a*a
sonuc=kareal(4)
print("istenilen değerin karesi {}: ".format(sonuc))
sonuc=kareal(8)
print("istenilen değerin karesi ",sonuc)

# Page 7
print("sinan")
def selam(d):
    print("grilen deger",d)
help(format) #?format
# a= int(input("1. sayıyı giriniz: "))
# b= int(input("2. sayıyı giriniz: "))
def cikar(x,y):
    # print("sonuc :",a-b) # 'a' and 'b' are not defined in this scope
    return x-y
# sonuc=cikar(a,b)
# kareal(a)
cikar(5,5)
def ceyrek(x):
    return x/4
def küpal(x):
    return x*x*x
küpal(3)
ceyrek(4)
küpal(ceyrek(12))
print(küpal(ceyrek(20)))
liste1=[1,2,3,4,5]
#liste tek artırma
liste2=[i*2 for i in liste1]
print(liste2)
kare=lambda x:x*x #kare al fonksiyonu yerine
def toplama(x,y):
    return x+y
toplama(5,5)
#lambda ile
toplama_lambda = lambda x,y: x+y
toplama_lambda(5,5)

# Page 8
import math as matematik
matematik.pow(2,2)
2**2
matematik.cos(60)
matematik.sin(60)
matematik.sqrt(4)
from math import * #tüm math library getirir
import time
import random
rastgele=random.randint(1,100)
print(rastgele)

# Page 9
import random
import time
# rastgele=random.randint(1,100)
# tahmin_hakki=5
# while True:
#     tahmin=int(input("tahmin gir 1-100 arası :"))
#     print("kontrol ediliyor")
#     if( tahmin==rastgele):
#         print("kontrol ediliyor")
#         time.sleep(1)
#         print("girilen sayi",tahmin)
#         break
#         print("tebrikler")
#     elif( tahmin<rastgele):
#         tahmin_hakki=tahmin_hakki-1
#         print("sayıyı büyült")
#     elif(tahmin>rastgele):
#         tahmin_hakki=tahmin_hakki-1
#         print("sayıyı küçült")
#     else:
#         print("1-100 de değer gir")
#     if(tahmin_hakki==0):
#         print("hak bitti")
#         break

# Page 11
class Calisan():
    #özellikler; yaş,adres,tc,ad,soyad........vs
    #metot/davranışlar; çalışma,terfi alma.....vss
    pass #içeriği sonra oluşturacağım
calisan1=Calisan() #nesne türetildi.

# Page 12
class Arac():
    renk="sarı"
    model="jeep"
    marka="kia"
a1=Arac()
print(a1) #a1 bir objedir çıktısı veriyor.
print(a1.marka)
print(a1.model)
print(a1.renk)
a1.marka="BMW"
print(a1.marka)
class Kare():
    kenar=10 #metre
    def alan(self):
        alan=self.kenar*self.kenar
        print("Alan",alan)
k1=Kare()
print(k1)
print(k1.kenar)
k1.alan()

# Page 15
class Isci():
    yas=20
    maas=1000
    def yasaGoreMaasOranla(self):
        print(self.yas/self.maas)
isci1=Isci()
isci1.yasaGoreMaasOranla()
def yasMaasOranı(yas,maas):
    a=yas/maas
    #print("oran:	",a)
    print("oran:	 {}".format(a))
yasMaasOranı(20,2000)

# Page 19
class Hayvan():
    def __init__(self,isim,yas): #yapıcı/constructor metot
        self.isim=isim
        self.yas=yas
    def getYas(self):
        return self.yas
    def getAd(self):
        return self.isim
h1=Hayvan("dog",2)
h1_yas=h1.getYas()
print("h1 in yaşı :",h1_yas)
h1_isim=h1.getAd()
print("h1 in isim :",h1_isim)
h2=Hayvan("cat",3)
h2_yas=h2.getYas()
print("h2 in yaşı :",h2_yas)

# Page 20
class Makine():
    "hesap makinesi"
    def __init__(self,a,b):
        "başlangıç değerlerini ayarlar"
        #öznitelik alır
        self.deger1=a
        self.deger2=b
    def topla(self):
        " toplama a+b = sonuc -> return sonucs"
        sonuc=self.deger1+self.deger2
        return sonuc
    def carp(self):
        "carpma a*b= sonuc -> return sonuc"
        sonuc=self.deger1*self.deger2
        return sonuc
    def cikar(self):
        return self.deger1-self.deger2
    def bol(self):
        return self.deger1/self.deger2
x=5
y=2
h = Makine(x,y)
tSonuc=h.topla()
cSonuc=h.carp()
print("toplama sonuc: {}, çarpma sonucu: {}".format(tSonuc,cSonuc))

# Page 22-23
class Banka():
    def __init__(self,isim,para,adres):
        self.isim=isim
        self.para=para
        self.adres=adres
hesap1=Banka("Sinan",1000,"istanbul")
hesap2=Banka("Ayşe",5000,"Erzurum")
hesap1.para
hesap2.para=hesap2.para+hesap1.para #sinan'ın parası kalmadı
hesap2.para
hesap1.para=0
hesap1.para
#bunu engellemek için public değişkenleri private yapmalıyız
class Banka2():
    def __init__(self,isim,para,adres):
        self.isim=isim
        self._para=para
        self.adres=adres
    #get ve set metotları
    def getPara(self):
        return self._para
    def setPara(self,miktar):
        self._para=miktar
    def islemSayisi(self):
        self._para=self._para-10
hes1=Banka2("Sinan",1000,"istanbul")
hes2=Banka2("Ayşe",5000,"Erzurum")
print("1. hesaptaki para: ",hes1.getPara())
hes1.setPara(100)
print("set işlemi sonrası 1. hesaptaki para değişimi :",hes1.getPara())
#hes1.islemSayisi()
#print("işlem ücreti :",hes1.getPara())

# Page 24
class Animal():
    def __init__(self):
        print("hayvan sınıfının yapıcı metotum")
    def sesCikar(self):
        print("hav,miyav,vak....")
    def hareket(self):
        print("zıplar,koşar, yürür..")
class kedi(Animal):
    def __init__(self):
        super().__init__() # yazmasakta olur ata sınıfın init metodunu ezeriz metot overriding!!
        print("kedi sınıfı oluşturuldu")
    def sesCikar(self):
        print("miyav")
    def DokuzCan(self): #diğer hayvanlardan ayrılan bir fonksiyon :D
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")
k1=kedi()
k1.sesCikar() #ata sınıfı ezer
k1.hareket()
k1.DokuzCan()
class kus(Animal):
    def __init__(self):
        print("kus sınıfı oluşturldu")
    def ucma(self):
        print("kanatları vardır uçarlar")
kus1=kus()
kus1.ucma()
kus1.hareket()

# Page 25
from abc import ABC, abstractmethod
class Animal(ABC): # super clas
    @abstractmethod
    def yurume(self): pass
    @abstractmethod
    def kosma(self): pass
class kus(Animal):
    def __init__(self):
        print("kuş oluşturuldu")
    def yurume(self):
        print("kuslar pek yürümez")
    def kosma(self):
        print("kuslar pek kosmazda")
#a=Animal() soyut sınıflardan nesne oluşturulmaz.
b=kus() #abstract clasın içeriği yavru sınıfta doldurulur.
b.kosma()
b.yurume()

# Page 26
class Animal():
    def sesVer(self):
        print("ses çıkarırlar")
class kedi(Animal):
    def sesVer(self): #ata sınıfı ezdi
        print("miyav")
a=Animal()
a.sesVer()
k=kedi()
k.sesVer()
class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim
    def tepki(self):
        raise NotImplementedError('HATA')
class Kedi(Hayvanlar):
    def tepki(self):
        return 'Miyav!'
class Kopek(Hayvanlar):
    def tepki(self):
        return 'Haav! Hav!'
hayvanlar = [Kedi('Boncuk'), Kedi('Tekir'), Kopek('Elmas')]
for hyvn in hayvanlar:
    print(hyvn.isim + ': ' + hyvn.tepki())

# Page 27
class Animal():
    def __init__(self, name): # Constructor of the class
        self.name = name
    def talk(self):
        # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
class Cat(Animal):
    def talk(self):
        return 'Meow!'
class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'
animals = [Cat('Missy'), Cat('Mr. Mistoffelees'), Dog('Lassie')]
for animal in animals:
    print (animal.name + ': ' + animal.talk())
