import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
import plotly.express as px

# Judul aplikasi
st.markdown('# Aplikasi Prediksi Tabular UAP')
st.markdown('## Nama: Fernanda Wawang Azraqi')
st.markdown('## NIM: 202110370311004')

# Load model dan encoder dengan error handling
try:
    rf_model = joblib.load('src/model/rf_model.pkl')
    xgb_model = joblib.load('src/model/xgb_model.pkl')
    encoder_area = joblib.load('src/model/encoder_area.pkl')
    encoder_item = joblib.load('src/model/encoder_item.pkl')
except FileNotFoundError as e:
    st.error("File model atau encoder tidak ditemukan. Pastikan semua file tersedia di folder 'src/model'.")
    st.stop()

# Judul aplikasi utama
st.title("Prediksi Produksi Pertanian")

# Input dari pengguna
st.header("Masukkan Data")
area = st.selectbox("Pilih Area", encoder_area.classes_)
item = st.selectbox("Pilih Komoditas", encoder_item.classes_)
year = st.number_input("Masukkan Tahun", min_value=1960, max_value=2023, step=1)

# Pilih model
model_choice = st.radio("Pilih Model Prediksi", ("Random Forest", "XGBoost"))

# Tombol prediksi
if st.button("Prediksi"):
    try:
        # Preprocessing input
        area_encoded = encoder_area.transform([area])[0]
        item_encoded = encoder_item.transform([item])[0]
        input_data = np.array([[area_encoded, item_encoded, year]], dtype=np.float32)

        # Prediksi berdasarkan model yang dipilih
        if model_choice == "Random Forest":
            model = rf_model
            prediction = model.predict(input_data)[0]
        else:
            model = xgb_model
            prediction = model.predict(input_data)[0]

        # Menampilkan hasil prediksi
        st.subheader("Hasil Prediksi")
        st.write(f"Prediksi Produksi untuk {item} di {area} pada tahun {year} adalah {prediction:.2f} ton.")

        # Visualisasi hasil prediksi
        st.subheader("Visualisasi Hasil Prediksi")
        fig = px.bar(x=[f'{item} - {year}'], y=[prediction], 
                     labels={'x': 'Item - Year', 'y': 'Produksi (ton)'}, 
                     color_discrete_sequence=['skyblue'])
        st.plotly_chart(fig)

        # Interpretasi model menggunakan SHAP
        st.subheader("Interpretasi Model")
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(input_data)
        shap.summary_plot(shap_values, input_data, feature_names=["Area", "Item", "Year"])
        st.pyplot(plt.gcf())

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

# Informasi tambahan
st.sidebar.title("Informasi Peningkatan Akurasi")
st.sidebar.markdown("""
- **Hyperparameter Tuning:** GridSearchCV digunakan untuk Random Forest dengan parameter `n_estimators`, `max_depth`.
- **Preprocessing:** Data dinormalisasi sebelum diterapkan ke model XGBoost.
- [Dokumentasi SHAP](https://shap.readthedocs.io)
- [XGBoost Documentation](https://xgboost.readthedocs.io)
""")
