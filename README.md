# Halı Saha Analiz Platformu (Football Analytics Pipeline)

Bu proje, bir futbol maçının video kayıtlarından oyuncuların hareketliliğini analiz eden uçtan uca (end-to-end) bir yazılımdır.

## Kullanılan Teknolojiler
- **YOLOv11**: Gerçek zamanlı oyuncu tespiti ve takibi.
- **OpenCV**: Saha zemin maskeleme ve perspektif işlemleri.
- **Pandas & Seaborn**: Hareket verilerinin işlenmesi ve ısı haritası (heatmap) üretimi.

## Proje Akışı
1. **Veri Toplama (analiz.py)**: Video işlenir, oyuncuların (x,y) koordinatları anlık olarak CSV dosyasına kaydedilir.
2. **Görselleştirme (analiz_paneli.py)**: Kaydedilen koordinatlar, saha planı üzerine bindirilerek taktiksel ısı haritaları oluşturulur.

## Nasıl Çalıştırılır?
1. `pip install ultralytics opencv-python pandas seaborn matplotlib`
2. `python analiz.py` (Video analizi için)
3. `python analiz_paneli.py` (Sonuç raporu için)


## Örnek Çıktı
![Isı Haritası Analizi](BURAYA_GORSEL_DOSYASININ_ADI.jpg)
*Bu görsel, maç boyunca oyuncuların sahada en çok vakit geçirdiği bölgeleri temsil etmektedir.*