# Steam Price Scraper & Tracker 🎮

Bu proje, Python ve BeautifulSoup kullanılarak geliştirilmiş, Tkinter arayüzüne sahip bir Steam oyun fiyatı takip uygulamasıdır. Kullanıcıdan alınan oyun ismini Steam üzerinde aratır, dinamik HTML yapılarını (App ID'den bağımsız olarak) çözümler ve oyunun güncel veya indirimli fiyatını masaüstü arayüzünde gösterir.

## Özellikler
* **Dinamik Web Scraping:** Steam arama motoru entegrasyonu ile sadece oyun ismi girerek fiyat çekebilme.
* **Yaş Kısıtlamasını Aşma:** Korumalı oyunlar (Resident Evil vb.) için özel çerez (cookie) yönetimi.
* **Akıllı Etiket Taraması:** Eklenti veya DLC'leri filtreleyerek doğrudan ana oyunun fiyatını tespit etme.
* **Modern Masaüstü Arayüzü:** Tkinter ile tasarlanmış Steam renk paletine uygun GUI.

## Kurulum
Projeyi kendi bilgisayarınızda çalıştırmak için:

1. Repoyu klonlayın:
   `git clone https://github.com/segemens/Steam-Price-Scraper.git`
2. Gerekli kütüphaneleri kurun:
   `pip install -r requirements.txt`
3. Uygulamayı başlatın:
   `python scrapper.py`