# Su Kalitesi Analizi ve Tahmin Modeli

Bu projede, suyun içilebilirliğini (potability) tahmin eden bir makine öğrenmesi modeli geliştireceğiz. Adım adım ilerleyerek:

1. [Water - a Hugging Face Space by btulftma](https://huggingface.co/spaces/btulftma/water)
2. [Water Quality Analysis | Aman Kharwal](https://thecleverprogrammer.com/2021/08/19/water-quality-analysis/)

## Proje Hedefleri

- Veri setini yükleyip analiz etmek
- Görselleştirmeler yapmak
- Makine öğrenmesi modeli eğitmek
- Modeli bir Streamlit uygulaması haline getirmek
- Hugging Face'e deploy etmek

## 1. Veri Setinin Yüklenmesi ve Ön İşleme

İlk olarak, su kalitesi veri setini yükleyip analiz ediyoruz. Veri setinde 9 özellik ve 1 hedef değişken (Potability) bulunmaktadır. Eksik verilerle başa çıkmak için her sütunun medyanı ile doldurulmaktadır.

## 2. Veri Analizi ve Görselleştirme

Hedef değişkenin dağılımını görselleştiriyoruz. Özelliklerin dağılımını ve potability'ye göre ayrımını inceleyerek veri setinin dengesiz olup olmadığını değerlendiriyoruz. Korelasyon matrisini inceleyerek özellikler arasındaki ilişkileri gözlemliyoruz.

## 3. Model Eğitimi

Veri, eğitim ve test setlerine ayrılmakta ve Random Forest algoritması ile model eğitilmektedir. Modelin performansı doğruluk skoru ve sınıflandırma raporu ile değerlendirilmektedir.

## 4. Streamlit Uygulaması

Modeli bir Streamlit uygulaması olarak geliştiriyoruz. Kullanıcıdan su örneği özelliklerini alarak model tahminleri yapıyoruz. Tahmin sonuçları ve özelliklerin önem dereceleri kullanıcıya sunulmaktadır.

## 5. Hugging Face'e Deploy Etme

Proje dosyaları (app.py, water_quality_model.pkl, requirements.txt) bir GitHub reposuna yüklenmekte ve Hugging Face Spaces'de yeni bir space oluşturulmaktadır. Gerekli bağımlılıklar requirements.txt dosyasına eklenmektedir.

## Sonuç ve Değerlendirme

Bu projede su kalitesi analizi için bir makine öğrenmesi modeli geliştirdik ve bir web uygulaması haline getirerek Hugging Face üzerinde yayınladık. Modelimiz, su örneklerinin içilebilir olup olmadığını %67 doğrulukla tahmin edebilmektedir.

## Model İyileştirme Denemeleri

Model iyileştirme için mevcut veri seti ve özellikler ile sınırlı kalındığı gözlemlenmiştir. Gelecekte daha kapsamlı veri analizleri ve farklı özellik mühendisliği yöntemleri ile modelin performansını artırmayı hedeflemekteyiz.
