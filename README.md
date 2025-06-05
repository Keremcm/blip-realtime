# 🎥 Anlık Görüntü Yorumlama – BLIP ile Webcam Açıklaması

Bu proje, **Salesforce BLIP (Bootstrapped Language Image Pretraining)** modeli kullanarak webcam'den alınan görüntüler üzerine gerçek zamanlı açıklamalar üretir.

## 🚀 Özellikler

- Gerçek zamanlı webcam görüntüsü
- Görüntülere otomatik açıklama oluşturma (captioning)
- Flask tabanlı sade bir web arayüzü
- Basit ve genişletilebilir altyapı

## 🖼️ Demo

![Demo](demo.png) <!-- Demo gif veya ekran görüntüsü eklersen buraya koy -->

## 🧠 Kullanılan Teknolojiler

- Python
- Flask
- OpenCV
- HuggingFace Transformers
- BLIP (Large) – `Salesforce/blip-image-captioning-large`

## ⚙️ Kurulum

### Gereksinimler
- Python 3.8+
- pip ile:

```bash
pip install flask transformers pillow opencv-python
```
## Çalıştırma

```bash
python app.py
```
Ardından tarayıcınızdan http://localhost:5000 adresine gidin.

## 📂 Proje Yapısı

.
├── app.py              # Flask backend ve görüntü işleme
├── templates/
│   └── index.html      # Web arayüzü
├── requirements.txt    # Açıklama
├── .gitignore          # Git ignore dosyası
└── README.md           # README dosyası
