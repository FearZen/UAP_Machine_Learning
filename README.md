# 🌱 Aplikasi Prediksi Tabular UAP

### 👤 Nama: Fernanda Wawang Azraqi
### 🌐 NIM: 202110370311004

---

## 🔍 Table of Contents

1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Dataset](#dataset)
3. [Repository](#repository)
4. [Langkah Instalasi](#langkah-instalasi)
5. [Deskripsi Model](#deskripsi-model)
6. [Hasil dan Analisis](#hasil-dan-analisis)
7. [Kontak](#kontak)

---

## 🔎 Deskripsi Proyek <a id="deskripsi-proyek"></a>

Proyek ini adalah aplikasi web berbasis **Streamlit** untuk memprediksi hasil produksi pertanian berdasarkan dataset yang tersedia. Proyek ini bertujuan untuk memberikan wawasan kepada pengguna tentang prediksi produksi berbagai komoditas pertanian menggunakan model machine learning. Aplikasi ini menyediakan opsi untuk menggunakan model **Random Forest** atau **XGBoost** sebagai prediktor.

---

## 📊 Dataset <a id="dataset"></a>

Dataset yang digunakan berasal dari Kaggle: [Crop Production Dataset](https://www.kaggle.com/datasets/imtkaggleteam/crop-production).

Dataset ini mencakup data historis produksi pertanian untuk berbagai area dan komoditas.

---

## 🔧 Repository <a id="repository"></a>

Repository proyek dapat ditemukan di GitHub: [FearZen/UAP_Machine_Learning](https://github.com/FearZen/UAP_Machine_Learning)

---

## 📚 Langkah Instalasi <a id="langkah-instalasi"></a>

Ikuti langkah-langkah berikut untuk menjalankan proyek ini secara lokal:

1. Clone repository ini:

   ```bash
   git clone https://github.com/FearZen/UAP_Machine_Learning.git
   ```

2. Pindah ke direktori proyek:

   ```bash
   cd UAP_Machine_Learning
   ```

3. Buat virtual environment dan aktifkan:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/Mac
   venv\Scripts\activate   # Untuk Windows
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Unduh Model:

   [Model .pkl](https://drive.google.com/drive/folders/1j2BQImV6ftljZWBKmDrB56UcvHTgrXvz?usp=sharing)

6. Jalankan aplikasi Streamlit:

   ```bash
   streamlit run app.py
   ```

---

## 🔢 Deskripsi Model <a id="deskripsi-model"></a>

Proyek ini menggunakan dua model machine learning:

1. **Random Forest**
   - Parameter utama: `n_estimators`, `max_depth`.
   - Dioptimalkan menggunakan GridSearchCV.

2. **XGBoost**
   - Model dengan boosting gradient berbasis pohon keputusan.
   - Data dinormalisasi sebelum digunakan untuk pelatihan.

---

## 🎨 Hasil dan Analisis #<a id="hasil-dan-analisis"></a>

Berikut adalah perbandingan performa antara model **Random Forest** dan **XGBoost**:

| Model         | MSE       | R²   | MAE        |
| ------------- | --------- | ---- | ---------- |
| Random Forest | 4.447e+12 | 0.53 | 248,478.72 |
| XGBoost       | 2.921e+12 | 0.69 | 331,333.03 |

Dari hasil di atas, **XGBoost** memiliki performa yang lebih baik dibandingkan **Random Forest**, khususnya dalam metrik R².

---

## 📢 Kontak <a id="kontak"></a>

Terima kasih telah menggunakan aplikasi ini! Jika Anda memiliki pertanyaan atau saran, jangan ragu untuk membuka isu di repository GitHub.

