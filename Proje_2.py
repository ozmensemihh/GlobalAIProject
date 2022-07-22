
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 
from datetime import datetime as dt
import random
from matplotlib import style
import matplotlib as mpl


"""

@author: Maksut Yazar
@author: Ahmet Umut Gökdemir
@author: Semih Özmen


"""

#dosya okuma
netflix =pd.read_csv("NetflixOriginals.csv",sep=",",encoding="ISO-8859-1")

print(100*"*")

#1) Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
#Language değerlerini gruplandırıp ortalamalarını alalım
language={"Language":netflix[["Language","Runtime"]].groupby("Language").mean().index,"Runtime":netflix[["Language","Runtime"]].groupby("Language").mean()["Runtime"].values}
lan_df=pd.DataFrame(language).sort_values(by='Runtime', ascending=False)
#Sonuç
print("Ortalama sürelere bakıldığında, en uzun soluklu filmlerin dillerinde ilk 5:\n\n", lan_df.head())
#Grafik
plt.bar(x="Language", height="Runtime", data= lan_df,width=0.5)
plt.xticks(rotation=90)

print(100*"*")

#2) 2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
documentary=netflix[netflix.Genre=="Documentary"][["Genre","Premiere","IMDB Score","Title"]]
#2019 ve 2020 yıllarını seçmek için tarih tipine dönüştürme işlemi yapalım
documentary["Premiere"]=pd.to_datetime(documentary.Premiere)
# tarihi içeren bu sütunu index olarak kullanalım
documentary.index=documentary["Premiere"]
documentary.index.name="Date"
# Aynı Sütundan iki tane olmaması için premiere sütununu silelim index ile devam edelim
documentary.drop("Premiere", axis=1,inplace=True)
documentary= documentary.loc['2019':'2020']

#index olarak tarihi veridim, gerekli filitrelmeleri yaptım 
print("2019 - 2020 Yıllarında Documentary türünde yapılan filmlerin IMBD puanları:\n\n",documentary)

#Grafik
## Yıllara göre kaç adet documentary türünde film çekildiğini gösterelim 
data =documentary["Title"].resample("A").count().values
keys = documentary["Title"].resample("A").count().index
explode = [0.08,0.01]
palette_color = sb.color_palette('bright')
plt.pie(data, labels=keys, colors=palette_color,explode=explode, autopct='%.0f%%')
plt.title("2019-2020 Documentary Türündeki Yapımların YIllara Göre Dağılımı")

## Yıllara Göre IMBD puanları gösterimi
plt.bar(x=documentary.loc["2019":"2020"].index, height=documentary["IMDB Score"], data=documentary,width=2)
plt.xticks(rotation=90)
print(100*"*")

print(100*"*")
#3) İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?

Eng= netflix[netflix.Language =="English"][["Genre","IMDB Score","Title"]]
Eng_Top=pd.DataFrame(Eng.groupby("Genre").max().sort_values(by='IMDB Score', ascending=False).head()) 
#türleri array olarak ayırıyorum
genre=np.array(Eng_Top.index) 
print(f"ingilizce çekilen yapımlar arasında en yüksek IMBD puanına sahip ilk 5 şu şekildedir\n\n {Eng_Top}\n\nEn yüksek puanı alan tür: {genre[0:1]} ve puanı: {Eng_Top['IMDB Score'].max()}")
#Grafik
##En yüksek İMBD puanı olan ingilizce yapımların türleri
plt.bar(x=Eng_Top.index, height=Eng_Top["IMDB Score"], data=Eng_Top)
plt.xticks(rotation=90)
print(100*"*")

print(100*"*")
#4) 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?

hindi=pd.DataFrame({"Language":netflix[["Language","Runtime"]].groupby("Language").mean().index,"Runtime":netflix[["Language","Runtime"]].groupby("Language").mean()["Runtime"].values}) 
print("Hind Filmlerinin ortalama süresi: {}".format(hindi[hindi.Language=='Hindi']["Runtime"]))
print(100*"*")
#5) 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
genre=pd.DataFrame({"Genre":netflix[["Genre","Language"]].groupby("Genre").count().index,"Count":netflix[["Genre","Language"]].groupby("Genre").count()["Language"].values})
print("Genre Sütünundaki kategori sayısı :{0}".format(genre.Genre.count()))
#Grafik 
data=genre.sort_values(by='Count', ascending=False).head(10)["Count"]
keys = genre.sort_values(by='Count', ascending=False).head(10)["Genre"]
explode =[]
for i in range(10): 
    explode.append(random.uniform(0.01,0.1)) 
    palette_color = sb.color_palette('dark')
plt.title("Netflix'te En Çok Üretilen Yapım Türlerinin ilk 10 Tanesinin Dağılımı")
plt.pie(x=data, labels=keys, colors=palette_color,explode=explode, autopct='%.0f%%')

print(100*"*")

#6) Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.

language={"Language":netflix[["Language","Title"]].groupby("Language").count().index,"Count":netflix[["Language","Title"]].groupby("Language").count()["Title"].values}
lan_df=pd.DataFrame(language).sort_values(by='Count', ascending=False)
print("Netflix'teki yapımlarda en çok kullanılan 3 dil \n{0}".format(lan_df.head(3)))

#Grafik
data=lan_df.head(3)["Count"]
keys =lan_df.head(3)["Language"]
explode =[]
for i in range(3): 
    explode.append(random.uniform(0.01,0.1)) 
    palette_color = sb.color_palette('dark')
plt.title("Netflix'teki Yapımlarda En Çok kullanılan 3 Dilin Dağılımı")
plt.pie(x=data, labels=keys, colors=palette_color,explode=explode, autopct='%.0f%%')
print(100*"*")
#7) IMDB puanı en yüksek olan ilk 10 film hangileridir?
print("IMDB puanı en yüksek olan ilk 10 film:\n{}".format(netflix[["IMDB Score","Title"]].sort_values(by="IMDB Score",ascending=False).head(10))) 
print(100*"*")

#8) IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.

#Korelasyon ölçümü
cor = netflix[["IMDB Score","Runtime"]]
print("Runtime ve IMDB puanları arasındaki ilişkiye bakıldığında istatistiksel bir ilşki görülmemektedir. Korelasyon tablosu: \n{}".format(cor.corr()))


#grafik
sb.scatterplot(x="IMDB Score",y="Runtime",data=cor)
sb.lineplot(x="IMDB Score", y="Runtime", data=cor,palette="flare")
print(100*"*")
# 9) IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
print(" IMDB Puanı en yüksek olan ilk 10 'Genre': \n{0}".format(netflix[["IMDB Score","Genre"]].groupby("Genre").max().sort_values(by="IMDB Score",ascending=False).head(10)))
#grafik
sb.barplot(x=netflix[["IMDB Score","Genre"]].groupby("Genre").max().sort_values(by="IMDB Score",ascending=False).head(10).index,y=netflix[["IMDB Score","Genre"]].groupby("Genre").max().sort_values(by="IMDB Score",ascending=False).head(10)["IMDB Score"])
plt.xticks(rotation=90)

print(100*"*")
#10) 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
print("Runtime' değeri en yüksek olan ilk 10 film:\n{0}".format(netflix[["Runtime","Title"]].sort_values(by="Runtime",ascending=False).head(10)))
#Grafik
sb.barplot(x=netflix[["Runtime","Title"]].sort_values(by="Runtime",ascending=False).head(10)["Title"],y=netflix[["Runtime","Title"]].sort_values(by="Runtime",ascending=False).head(10)["Runtime"])
plt.xticks(rotation=90)
print(100*"*")

#11) Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
## Gerekli
date=netflix[["Premiere","Title"]].groupby("Premiere")["Title"].count()
date.index=pd.to_datetime(date.index)
date.index.name="Date"
date=date.resample("A").count().sort_values(ascending=False)
print("en fazla film yayımlanan yıl: \n{0}".format(date.head(1)))
sb.barplot(x=date.index,y=date)
plt.xticks(rotation=90)

print(100*"*")

#12) Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
print("En düşük ortalama IMBD puanına sahip yapımın dili ve IMDB puanı: \n{0}".format(netflix[["IMDB Score","Language"]].groupby("Language").mean().sort_values(by="IMDB Score",ascending=True).head(1)))
#Grafik
X=netflix[["IMDB Score","Language"]].groupby("Language").mean().sort_values(by="IMDB Score",ascending=True)
plt.bar(x=X.index, height=X["IMDB Score"], data=X)
plt.xticks(rotation=90)
print(100*"*")


#13) Hangi yılın toplam "runtime" süresi en fazladır?
date=netflix[["Premiere","Runtime"]].groupby("Premiere")["Runtime"].count()
date.index=pd.to_datetime(date.index)
date.index.name="Date"
date=date.resample("A").mean().sort_values(ascending=False)
print(" Yıllara göre 'runtime' ortalaması en fazla olan yıl ve ortalaması: \n{0}".format(date.head(1)))
#grafik

data=date.values

keys =date.index
explode =[]
for i in range(8): 
    explode.append(random.uniform(0.01,0.1)) 
    palette_color = sb.color_palette('dark')
plt.title("Yıllara göre 'runtime' ortalamasının Dağılımı")
plt.pie(x=data, labels=keys, colors=palette_color,explode=explode, autopct='%.0f%%')

print(100*"*")
#14) Her bir dilin en fazla kullanıldığı "Genre" nedir?
print("Netflix'teki yapımların dillere göre en fazla yayınladığı türler: \n{0}".format(netflix[["Language","Genre"]].groupby("Language").max()))
print(100*"*")


#15) Veri setinde outlier veri var mıdır? Açıklayınız.

# Runtime verisi için Outlier incelemesi
print("Runtime verisine bakıldığında, ortalamadan, standart sapmanın çok üstünde sapma gösteren değerler vardır. Bu değerlere bakıldığında 209 dakikalık bir yapımla 4 dakikaklık bir yapım olduğu görülüyor. Ortalamanın da yaklaşık 94 dakika olduğu görülebilir. Detaylar için: \n{0}".format(netflix.Runtime.describe()))
## Runtime Grafik
sb.boxenplot(netflix["Runtime"])

# IMDB Score outlier incelemesi
print("IMDB Score incelendiğinde ortalaması, standart sapması yaklaşık 1 olan bir dağılım görünüyor. Alt değeri 3 ve üst değeri 9'dur ve bunlar aşırı değerlerdir.Burada da Aşırı değerlerin olduğu görülmektedir  \n{0}".format(netflix["IMDB Score"].describe()))
##IMDB Score Grafik
sb.boxenplot(netflix["IMDB Score"])
