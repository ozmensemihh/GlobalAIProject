import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the data from the file
data = pd.read_csv("NetflixOriginals.csv",encoding="ISO-8859-1")
#Dataframe is created
df = pd.DataFrame(data)



#En uzun film listesi max 10 tane olan filmleri alıyor.
uzun_filmleri_max_10 = (df.sort_values(by=['Runtime'], ascending=False).head(10))
x = uzun_filmleri_max_10['Language']
y = uzun_filmleri_max_10['Runtime']
plt.bar(x,y)
plt.xlabel('Language')
plt.ylabel('Runtime')
plt.title('Uzun Soluklu Max 10 Film')
plt.show()


# 2019 Ocak - 2020 Haziran arasında Documentary filmlerin IMDB puanlarını grafik olarak gösteriyor.
IMDB = df[(df['Premiere'] >= "January 2019") & (df['Premiere'] <= "June 2020") & (df['Genre'] == 'Documentary')]
IMDB_puan = IMDB['IMDB Score']
plt.hist(IMDB_puan, bins=10)
plt.xlabel('IMDB_Rating')
plt.ylabel('Frequency')
plt.title('Documentary Filmlerin IMDB Puanları')
plt.show()


