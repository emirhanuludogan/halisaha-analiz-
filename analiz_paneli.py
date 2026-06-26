import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2

df = pd.read_csv('oyuncu_takip.csv')
saha_img = cv2.imread('saha_plan.jpg')
saha_img = cv2.cvtColor(saha_img, cv2.COLOR_BGR2RGB)

height, width = saha_img.shape[:2]

df['Y'] = height - df['Y']
df['X'] = width - df['X']

fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(saha_img, extent=[0, width, height, 0])
ax.set_xlim(0, width)
ax.set_ylim(height, 0)

sns.kdeplot(x=df['X'], y=df['Y'], fill=True, cmap='Reds', alpha=0.5, thresh=0.05, levels=20, ax=ax)

plt.title("Maç Sonu Oyuncu Hareketlilik Paneli")
plt.axis('off')
plt.show()