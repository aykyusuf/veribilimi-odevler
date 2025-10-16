
import random
import math

# 1. Kullanıcıdan Alınan Metni Ekranda Gösterme
def metni_goster():
    """Kullanıcıdan bir metin alır ve ekranda gösterir."""
    metin = input("Bir metin giriniz: ")
    print("Girdiğiniz metin:", metin)

# 2. Kullanıcının Girdiği İki Sayıyı Toplama
def iki_sayiyi_topla():
    """Kullanıcıdan iki sayı alır ve toplamını ekranda gösterir."""
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
        print(f"Sayıların toplamı: {sayi1 + sayi2}")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

# 3. Girilen Sayının Tek veya Çift Sayı Olduğunu Belirleme
def tek_mi_cift_mi():
    """Kullanıcıdan bir sayı alır ve tek mi çift mi olduğunu belirler."""
    try:
        sayi = int(input("Bir sayı giriniz: "))
        if sayi % 2 == 0:
            print(f"{sayi} bir çift sayıdır.")
        else:
            print(f"{sayi} bir tek sayıdır.")
    except ValueError:
        print("Lütfen geçerli bir tam sayı giriniz.")

# 4. İki Sayı ile İşlem Yapan Basit Hesap Makinesi
def basit_hesap_makinesi():
    """İki sayı ve bir işlem alarak basit bir hesap makinesi işlevi görür."""
    try:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        operator = input("İşlemi giriniz (+, -, *, /): ")
        sayi2 = float(input("İkinci sayıyı giriniz: "))

        if operator == '+':
            print(f"Sonuç: {sayi1 + sayi2}")
        elif operator == '-':
            print(f"Sonuç: {sayi1 - sayi2}")
        elif operator == '*':
            print(f"Sonuç: {sayi1 * sayi2}")
        elif operator == '/':
            if sayi2 == 0:
                print("Bir sayı sıfıra bölünemez.")
            else:
                print(f"Sonuç: {sayi1 / sayi2}")
        else:
            print("Geçersiz işlem.")
    except ValueError:
        print("Lütfen geçerli sayılar giriniz.")

# 5. Hesap Makinesinde Kullanıcı Hatalarını Önleme
# (4. sorudaki basit_hesap_makinesi fonksiyonuna try-except blokları eklenmiştir.)

# 6. +/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma
def artir_azalt(sayi, isaret):
    """Verilen sayıyı belirtilen işarete göre artırır veya azaltır."""
    if isaret == '+':
        return sayi + 1
    elif isaret == '-':
        return sayi - 1
    else:
        return sayi

# 7. +10 ile -10 Arasındaki Sayıları Ekrana Yazma
def on_ile_eksi_on_arasi():
    """-10 ile +10 arasındaki sayıları ekrana yazar."""
    for sayi in range(-10, 11):
        print(sayi, end=" ")
    print()

# 8. Metindeki Her Harfin Arasına Virgül Koyma
def harflerin_arasina_virgul_koy(metin):
    """Verilen metnin her harfinin arasına virgül koyar."""
    return ",".join(metin)

# 9. 1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme
def rastgele_sayi_dizisi_olustur():
    """1 ile 100 arasında rastgele 10 tam sayı üretip bir listeye ekler."""
    return [random.randint(1, 100) for _ in range(10)]

# 10. -100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme
def bese_tam_bolunenler():
    """-100 ile +100 arasındaki 5'e tam bölünen sayıları gösterir."""
    for sayi in range(-100, 101):
        if sayi % 5 == 0:
            print(sayi, end=" ")
    print()

# 11. Üç Adet Sayıyı Karşılaştırıp Sıralama
def uc_sayiyi_sirala(a, b, c):
    """Verilen üç sayıyı küçükten büyüğe sıralar."""
    sayilar = [a, b, c]
    sayilar.sort()
    return sayilar

# 12. Faktöriyel Hesaplama ve Açılımını Yazdırma
def faktoriyel_hesapla(n):
    """Bir sayının faktöriyelini hesaplar ve açılımını yazdırır."""
    if n < 0:
        return "Negatif sayıların faktöriyeli olmaz."
    elif n == 0:
        return "0! = 1"
    else:
        sonuc = 1
        aciklama = f"{n}! = "
        for i in range(n, 0, -1):
            sonuc *= i
            aciklama += str(i)
            if i != 1:
                aciklama += " * "
        return f"{aciklama} = {sonuc}"

# 13. Metindeki İlk Kelime ile Son Kelimeyi Bulma
def ilk_ve_son_kelimeyi_bul(metin):
    """Verilen metindeki ilk ve son kelimeyi bulur."""
    kelimeler = metin.split()
    if len(kelimeler) > 0:
        return kelimeler[0], kelimeler[-1]
    else:
        return None, None

# 14. Girilen Sayıların Toplamını ve Ortalamasını Bulma
def toplam_ve_ortalama_bul():
    """Kullanıcıdan alınan sayıların toplamını ve ortalamasını bulur."""
    girdi = input("Sayıları aralarında boşluk bırakarak giriniz: ")
    sayilar_str = girdi.split()
    try:
        sayilar = [float(s) for s in sayilar_str]
        toplam = sum(sayilar)
        ortalama = toplam / len(sayilar)
        print(f"Toplam: {toplam}, Ortalama: {ortalama}")
    except ValueError:
        print("Lütfen geçerli sayılar giriniz.")

# 15. Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme
def harf_buyuklugunu_degistir(metin):
    """Verilen metindeki harflerin büyüklüğünü değiştirir."""
    return metin.swapcase()

# 16. Personel Maaşından Yüzdesel Zam Hesaplama
def zam_hesapla(maas, zam_orani):
    """Verilen maaşa belirtilen oranda zam uygular."""
    yeni_maas = maas * (1 + zam_orani / 100)
    return yeni_maas

# 17. Sayı Değerlerinin Toplamını Hesaplama
def sayi_degerleri_toplami(sayi):
    """Bir sayının basamaklarındaki rakamların toplamını hesaplar."""
    toplam = 0
    for rakam in str(sayi):
        toplam += int(rakam)
    return toplam

# 18. Kullanıcının Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma
def sonsuz_tek_cift():
    """Kullanıcıdan sürekli sayı alır ve tek/çift olduğunu belirtir. 'q' ile çıkılır."""
    while True:
        girdi = input("Bir sayı giriniz (çıkmak için 'q'): ")
        if girdi.lower() == 'q':
            break
        try:
            sayi = int(girdi)
            if sayi % 2 == 0:
                print(f"{sayi} - Çift")
            else:
                print(f"{sayi} - Tek")
        except ValueError:
            print("Lütfen geçerli bir tam sayı giriniz.")

# 19. 1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma
def onbire_bolunenler():
    """1 ile 300 arasındaki 11'e tam bölünen sayıları bulur."""
    return [sayi for sayi in range(1, 301) if sayi % 11 == 0]

# 20. Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama
def final_notu_hesapla(vize_notu, gecme_notu, vize_etkisi=0.4):
    """Vize notu ve geçme notuna göre alınması gereken final notunu hesaplar."""
    final_etkisi = 1 - vize_etkisi
    gereken_final = (gecme_notu - (vize_notu * vize_etkisi)) / final_etkisi
    return gereken_final

# 21. Üç Kenarı Girilen Üçgenin Alanını Hesaplama
def ucgenin_alanini_hesapla(a, b, c):
    """Üç kenarı verilen üçgenin alanını Heron formülü ile hesaplar."""
    s = (a + b + c) / 2
    alan = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return alan

# 22. Metindeki Sesli Harf Sayısını Hesaplama
def sesli_harf_sayisi(metin):
    """Verilen metindeki sesli harf sayısını hesaplar."""
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"
    sayac = 0
    for harf in metin:
        if harf in sesli_harfler:
            sayac += 1
    return sayac

# 23. Her Sayıyı Kendisi Kadar Yan Yana Yazdırma
def sayiyi_kendisi_kadar_yazdir(sayi):
    """Bir sayıyı kendisi kadar yan yana yazdırır."""
    print(str(sayi) * sayi)

# 24. Tekrarsız Rastgele Sayı Üretme
def tekrarsiz_rastgele_sayi_uret(adet, min_val, max_val):
    """Belirtilen aralıkta tekrarsız rastgele sayılar üretir."""
    return random.sample(range(min_val, max_val + 1), adet)

# 25. Asal Çarpanlarını Bulma
def asal_carpanlari_bul(n):
    """Bir sayının asal çarpanlarını bulur."""
    carpanlar = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            carpanlar.append(d)
            n //= d
        d += 1
    if n > 1:
       carpanlar.append(n)
    return carpanlar

# 26. Metindeki En Uzun Kelimeyi Bulma
def en_uzun_kelimeyi_bul(metin):
    """Verilen metindeki en uzun kelimeyi bulur."""
    kelimeler = metin.split()
    if not kelimeler:
        return None
    return max(kelimeler, key=len)

# 27. Girilen Bir Notun Harf Karşılığını Bulma
def harf_notu_bul(not_):
    """Girilen nota göre harf karşılığını bulur."""
    if 90 <= not_ <= 100:
        return "AA"
    elif 85 <= not_ < 90:
        return "BA"
    elif 80 <= not_ < 85:
        return "BB"
    elif 75 <= not_ < 80:
        return "CB"
    elif 65 <= not_ < 75:
        return "CC"
    elif 58 <= not_ < 65:
        return "DC"
    elif 50 <= not_ < 58:
        return "DD"
    elif 40 <= not_ < 50:
        return "FD"
    else:
        return "FF"

# 28. Cümledeki Her Kelimeyi Tersten Yazdırma
def kelimeleri_tersten_yazdir(cumle):
    """Bir cümledeki her kelimeyi tersten yazdırır."""
    kelimeler = cumle.split()
    tersten_kelimeler = [kelime[::-1] for kelime in kelimeler]
    return " ".join(tersten_kelimeler)

# 29. Metni Mors Alfabesine Çevirme
def metni_morsa_cevir(metin):
    """Verilen metni Mors alfabesine çevirir."""
    mors_alfabesi = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.' ,
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--','X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    }
    mors_metni = ""
    for harf in metin.upper():
        if harf in mors_alfabesi:
            mors_metni += mors_alfabesi[harf] + " "
    return mors_metni.strip()

# 30. Kümülatif Toplam Hesaplama
def kumulatif_toplam_hesapla(sayilar):
    """Bir sayı listesinin kümülatif toplamını hesaplar."""
    kumulatif_toplam = []
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
        kumulatif_toplam.append(toplam)
    return kumulatif_toplam

if __name__ == '__main__':
    # Örnek kullanımlar
    # 1. metni_goster()
    # 2. iki_sayiyi_topla()
    # 3. tek_mi_cift_mi()
    # 4. basit_hesap_makinesi()
    
    print("6. +/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma:")
    sayi = 5
    sayi = artir_azalt(sayi, '+')
    print(f"Sayı artırıldı: {sayi}")
    sayi = artir_azalt(sayi, '-')
    print(f"Sayı azaltıldı: {sayi}")
    
    print("\n7. +10 ile -10 Arasındaki Sayıları Ekrana Yazma:")
    on_ile_eksi_on_arasi()
    
    print("\n8. Metindeki Her Harfin Arasına Virgül Koyma:")
    print(harflerin_arasina_virgul_koy("Python"))
    
    print("\n9. 1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme:")
    print(rastgele_sayi_dizisi_olustur())
    
    print("\n10. -100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme:")
    bese_tam_bolunenler()
    
    print("\n11. Üç Adet Sayıyı Karşılaştırıp Sıralama:")
    print(uc_sayiyi_sirala(5, 2, 8))
    
    print("\n12. Faktöriyel Hesaplama ve Açılımını Yazdırma:")
    print(faktoriyel_hesapla(5))
    
    print("\n13. Metindeki İlk Kelime ile Son Kelimeyi Bulma:")
    ilk, son = ilk_ve_son_kelimeyi_bul("Bu bir deneme cümlesidir")
    print(f"İlk kelime: {ilk}, Son kelime: {son}")
    
    # 14. toplam_ve_ortalama_bul()
    
    print("\n15. Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme:")
    print(harf_buyuklugunu_degistir("PyThOn PrOgRaMlAmA"))
    
    print("\n16. Personel Maaşından Yüzdesel Zam Hesaplama:")
    print(f"Yeni maaş: {zam_hesapla(5000, 20)}")
    
    print("\n17. Sayı Değerlerinin Toplamını Hesaplama:")
    print(f"Sayı değerleri toplamı: {sayi_degerleri_toplami(12345)}")
    
    # 18. sonsuz_tek_cift()
    
    print("\n19. 1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma:")
    print(onbire_bolunenler())
    
    print("\n20. Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama:")
    print(f"Gereken final notu: {final_notu_hesapla(50, 60)}")
    
    print("\n21. Üç Kenarı Girilen Üçgenin Alanını Hesaplama:")
    print(f"Üçgenin alanı: {ucgenin_alanini_hesapla(3, 4, 5)}")
    
    print("\n22. Metindeki Sesli Harf Sayısını Hesaplama:")
    print(f"Sesli harf sayısı: {sesli_harf_sayisi('Merhaba Dünya')}")
    
    print("\n23. Her Sayıyı Kendisi Kadar Yan Yana Yazdırma:")
    sayiyi_kendisi_kadar_yazdir(4)
    
    print("\n24. Tekrarsız Rastgele Sayı Üretme:")
    print(tekrarsiz_rastgele_sayi_uret(5, 1, 20))
    
    print("\n25. Asal Çarpanlarını Bulma:")
    print(f"Asal çarpanlar: {asal_carpanlari_bul(90)}")
    
    print("\n26. Metindeki En Uzun Kelimeyi Bulma:")
    print(f"En uzun kelime: {en_uzun_kelimeyi_bul('Python programlama dili')}")
    
    print("\n27. Girilen Bir Notun Harf Karşılığını Bulma:")
    print(f"Harf notu: {harf_notu_bul(88)}")
    
    print("\n28. Cümledeki Her Kelimeyi Tersten Yazdırma:")
    print(kelimeleri_tersten_yazdir("Merhaba Dünya"))
    
    print("\n29. Metni Mors Alfabesine Çevirme:")
    print(metni_morsa_cevir("HELLO WORLD"))
    
    print("\n30. Kümülatif Toplam Hesaplama:")
    print(kumulatif_toplam_hesapla([1, 2, 3, 4, 5]))
