#!/usr/bin/python3.8
import numpy as np
import pandas as pd

def veri_girdisi():
    öğrenci_verileri = []
    #öğrenci girdilerinin tamamlanmadığına dair önerme
    öğrenci_girdisi_tamamlandı = False
    #Öğrenci verilerinin kullanıcıdan alınması
    while not öğrenci_girdisi_tamamlandı:
        dummy_list = []
        print("Lütfen öğrencinin adını giriniz: ")
        isim = str(input())
        dummy_list.append(isim)
        print("Lütfen öğrencinin soyismini giriniz: ")
        soyisim = str(input())
        dummy_list.append(soyisim)
        print("Lütfen öğrencinin okul numarasını giriniz: ")
        numara = int(input())
        dummy_list.append(numara)
        print("Lütfen öğrencinin notunu giriniz: ")
        ders_notu = float(input())
        dummy_list.append(ders_notu)
        print(dummy_list)
        #Oluşturulan öğrenci veri kimliğini depola
        öğrenci_verileri.append(dummy_list)
        while True:
            #Kullanıcıdan girilecek verinin bitip-bitmediğinin sorulması
            print("Başka öğrenci sisteme eklemek istiyor musunuz ? (e/h)")
            yanıt = str(input())
            #Kullanıcı girdinin yorumlanması
            #Eğer son veri ise bilgi almayı durdur
            if yanıt == "H" or yanıt == "h" or yanıt == "hayır":
                print("Sisteme veri girilmesi tamamlandı.")
                öğrenci_girdisi_tamamlandı = True
                break
                #Eğer girdi için başka veri varsa devam et
            elif yanıt == "E" or yanıt == "e" or yanıt == "evet":
                print("Lütfen sıradaki öğrencinin bilgilerini giriniz")
                break
                #Yanıt tanımlanamıyorsa tekrar iste
            else:
                print("Girdiğiniz yanıt geçersizdir, tekrar deneyiniz. Lütfen bunlardan birini deneyiniz: \nE,e,evet,H,h,hayır")
    return öğrenci_verileri

print("*"*10,"Öğrenci not bilgi sistemine hoş geldiniz","*"*10)
print("Öğrencilerin İsim,Soyisim ve ders notu girildikten sonra harf notları ve başarı durumları bir excel dosyası olarak kayıt edilecektir.")
öğrenci_verileri = veri_girdisi()
print(öğrenci_verileri)
df = pd.DataFrame(öğrenci_verileri,columns = ['İsim','Soyisim','Numara','Not'])
#print(df)
# Harf notu limitleri
not_limitleri = [
    (df['Not']<=39),
    (df['Not'] > 39) & (df['Not']<=49),#FD
    (df['Not'] > 49) & (df['Not'] <= 54),#DD
    (df['Not'] > 54) & (df['Not'] <= 59),#DC
    (df['Not'] > 59) & (df['Not'] <= 69),#CC
    (df['Not'] > 69) & (df['Not'] <= 79),#CB
    (df['Not'] > 79) & (df['Not'] <= 84),#BB
    (df['Not'] > 84) & (df['Not'] <= 89),#BA
    (df['Not'] > 89)#AA
    ]

# Not limitlerine karşılık gelen harf notları
harf_notları = ['FF', 'FD','DD','DC','CC','CB','BB','BA', 'AA']
# DataFrame'de tutulan sayısal notları, verilen not limitlerine göre değerlendir
df['Harf'] = np.select(not_limitleri, harf_notları)

# display updated DataFrame
print(df)
