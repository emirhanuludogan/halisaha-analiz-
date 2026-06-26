import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2

# 1. Veriyi oku
df = pd.read_csv('oyuncu_takip.csv')

# 2. Saha görüntüsünü arka plan olarak yükle (Video karelerinden birini alabilirsin)
# Eğer elinde boş bir saha görüntüsü yoksa, sadece haritayı da çizebilirsin
plt.figure(figsize=(10, 6))

# 3. Isı haritasını oluştur
# 'X' ve 'Y' sütunlarını yoğunluk haritası olarak çizdiriyoruz
sns.kdeplot(x=df['X'], y=df['Y'], fill=True, cmap='coolwarm', thresh=0.05, levels=20)

plt.title("Oyuncu Hareketlilik Isı Haritası")
plt.xlabel("X Koordinatı")
plt.ylabel("Y Koordinatı")

# Koordinatları videodaki gibi ters çevir (Görüntü işleme mantığına uygun)
plt.gca().invert_yaxis() 

plt.show()