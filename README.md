# 🧮 Basit Python Hesap Makinesi (Pytest + Ortam Yapılandırması)

Bu proje, temel dört aritmetik işlemi gerçekleştiren **komut satırı tabanlı bir hesap makinesi** uygulamasıdır. Amaç sadece hesaplama yapmak değil, aynı zamanda:

- ✔️ Ortam yönetimi (test vs development)
- ✔️ `pytest` ile birim testi yazımı
- ✔️ Hata yönetimi (exception handling)
- ✔️ Temiz modüler Python mimarisi

gibi profesyonel yazılım geliştirme pratiklerini de göstermektir.

---

## 🚀 Özellikler

- Toplama, çıkarma, çarpma ve bölme işlemleri
- Sıfıra bölme hatası kontrolü
- Ortam değişkenine göre çalıştırma (örn. `development`)
- `pytest` ile kapsamlı testler
- Ortam kontrolü ile testlerin izole çalışması

---

## 🗂️ Proje Yapısı

calculator/
│

├── calculator/

│ └── operations.py # Aritmetik işlemler

├── config/

│ └── settings.py # Ortam yönetimi (ENV değişkeni)

├── tests/

│ └── test_operations.py # Pytest ile birim testleri

├── main.py # CLI hesap makinesi

├── requirements.txt

└── .pytest_cache/ # pytest çalıştırıldığında oluşur

---

## ⚙️ Kurulum ve Çalıştırma

### Ortam değişkenini ayarla

```export ENV=development```

### Projeyi çalıştır

```python main.py```

⚠️ Uygulama sadece development ortamında çalışır. settings.py dosyasındaki kontrol sayesinde test ortamında main.py çalışmaz.

🧪 Testler

### ENV değişkeni test ortamına alınmalı

```export ENV=test```

### Testleri çalıştır

```python -m pytest -v```

📦 requirements.txt

pytest~=8.4.1

📃 Lisans: MIT Lisansı

👩‍💻 Geliştirici: Sena Çetinkaya

📧 [cetinkayasena96@gmail.com](cetinkayasena96@gmail.com)

🌐 GitHub: [https://github.com/sena-cetinkaya](https://github.com/sena-cetinkaya)
