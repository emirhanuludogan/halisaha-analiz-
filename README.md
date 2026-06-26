# Halı Saha Analiz Platformu (Football Analytics Pipeline)

Bu proje, bir futbol maçının video kayıtlarından oyuncuların hareketliliğini analiz eden uçtan uca (end-to-end) bir yazılımdır.

## Kullanılan Teknolojiler
- **YOLOv11**: Gerçek zamanlı oyuncu tespiti ve takibi.
- **OpenCV**: Saha zemin maskeleme ve perspektif işlemleri.
- **Pandas & Seaborn**: Hareket verilerinin işlenmesi ve görselleştirme.

## Proje Akışı
1. **Veri Toplama (analiz.py)**: Video işlenir, oyuncuların (x,y) koordinatları anlık olarak CSV dosyasına kaydedilir.
2. **Görselleştirme (analiz_paneli.py)**: Kaydedilen koordinatlar, saha planı üzerine bindirilerek taktiksel ısı haritaları oluşturulur.

## Proje Çıktıları
Analiz sürecinin ham görüntüden anlamlı veriye dönüşümü aşağıdaki görsel setinde özetlenmiştir:

| Ham Görüntü | Nesne Tespiti | Analiz Süreci | Isı Haritası (Sonuç) |
| :---: | :---: | :---: | :---: |
| ![Ham](assets/camera1.jpg) | ![Takip](assets/camera2.jpg) | ![Analiz](assets/camera3.jpg) | ![Sonuç](assets/camera4.jpg) |

*Not: Görseller, ham video kaydı ile analiz edilmiş çıktı arasındaki farkı ve sistemin sahadaki yoğunluğu nasıl tespit ettiğini göstermektedir.*

## Nasıl Çalıştırılır?
1. `pip install -r requirements.txt`
2. `python analiz.py` (Video analizi için)
3. `python analiz_paneli.py` (Sonuç raporu için)