import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Modeli yükle
model = joblib.load('water_quality_model.pkl')

# Özellik sütun isimlerini tanımla (model eğitimindekiyle aynı sırada)
feature_columns = [
    'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate',
    'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'
]

# Başlık
st.title("Su Kalitesi Tahmin Uygulaması")
st.markdown("""
Bu uygulama, su örneklerinin içilebilir olup olmadığını tahmin eder.
Lütfen aşağıdaki formu doldurun.
""")

# Kullanıcı girişi
with st.form("su_verileri"):
    st.header("Su Özellikleri")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ph = st.number_input("pH Değeri", min_value=0.0, max_value=14.0, value=7.0)
        hardness = st.number_input("Sertlik (mg/L)", min_value=0.0, value=150.0)
        solids = st.number_input("Çözünmüş Katılar (ppm)", min_value=0.0, value=20000.0)
    
    with col2:
        chloramines = st.number_input("Kloraminler (ppm)", min_value=0.0, value=5.0)
        sulfate = st.number_input("Sülfat (mg/L)", min_value=0.0, value=300.0)
        conductivity = st.number_input("İletkenlik (μS/cm)", min_value=0.0, value=400.0)
    
    with col3:
        organic_carbon = st.number_input("Organik Karbon (ppm)", min_value=0.0, value=10.0)
        trihalomethanes = st.number_input("Trihalometanlar (μg/L)", min_value=0.0, value=60.0)
        turbidity = st.number_input("Bulanıklık (NTU)", min_value=0.0, value=3.0)
    
    submitted = st.form_submit_button("Tahmin Et")

# Tahmin yap
if submitted:
    try:
        # Girdileri DataFrame'e çevir
        input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, 
                                  conductivity, organic_carbon, trihalomethanes, turbidity]],
                                columns=feature_columns)
        
        # Tahminleri yap
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)
        
        # Sonuçları göster
        st.subheader("Sonuç")
        if prediction[0] == 1:
            st.success(f"✅ Bu su örneği İÇİLEBİLİR (Olasılık: %{probability[0][1]*100:.2f})")
        else:
            st.error(f"❌ Bu su örneği İÇİLEMEZ (Olasılık: %{probability[0][0]*100:.2f})")
        
        # Özellik önemleri
        st.subheader("Özellik Önemleri")
        feature_importance = pd.DataFrame({
            'Özellik': feature_columns,
            'Önem': model.feature_importances_
        }).sort_values('Önem', ascending=False)
        
        st.bar_chart(feature_importance.set_index('Özellik'))
        
    except Exception as e:
        st.error(f"Bir hata oluştu: {str(e)}")

# Yan bilgi çubuğu
st.sidebar.header("Hakkında")
st.sidebar.info("""
Bu uygulama, Random Forest algoritması kullanarak su kalitesini tahmin eder.

**Kullanılan Teknolojiler:**
- Python
- Scikit-learn
- Streamlit
- Pandas
""")