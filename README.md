# Sistem Klasifikasi Lahan & Rekomendasi Tanaman

Aplikasi web interaktif berbasis Streamlit yang mengintegrasikan metode Machine Learning untuk melakukan zonasi karakteristik lahan pertanian (K-Means Clustering) sekaligus memberikan rekomendasi tanaman lokal yang paling optimal (XGBoost Classifier). Proyek ini disusun untuk memenuhi Tugas Akhir / UAS mata kuliah Data Mining.

## Identitas Mahasiswa
Nama: Lizam Sabit Mafaiz
NIM: 24051214106
Kelas: KDD1

- **Mata Kuliah:** Data Mining
- **Dosen Pengampu:** Dr. Wiyli Yustanti, S.Si., M.Kom.
- **Program Studi:** Sistem Informasi
- **Universitas:** Universitas Negeri Surabaya (UNESA)

---

## Deskripsi Proyek

Sistem ini membantu petani dan praktisi pertanian dalam:
1. Mengidentifikasi **zona karakteristik lahan** berdasarkan data sensor hara tanah dan cuaca
2. Mendapatkan **rekomendasi komoditas tanaman** yang paling sesuai secara otomatis

Input sistem berupa 7 parameter sensor:
- **N** — Kadar Nitrogen dalam tanah (mg/kg)
- **P** — Kadar Fosfor dalam tanah (mg/kg)
- **K** — Kadar Kalium dalam tanah (mg/kg)
- **Temperature** — Suhu udara (°C)
- **Humidity** — Kelembapan udara (%)
- **pH** — Tingkat keasaman tanah
- **Rainfall** — Estimasi curah hujan tahunan (mm)

---

## Metode yang Digunakan

| Metode | Fungsi |
|---|---|
| K-Means Clustering (K=5) | Mengelompokkan lahan ke dalam 5 zona karakteristik |
| XGBoost Classifier | Merekomendasikan komoditas tanaman terbaik |
| StandardScaler | Normalisasi fitur sebelum pemodelan |
| Label Encoding | Konversi label tanaman ke format numerik |

**Metodologi:** CRISP-DM (Cross Industry Standard Process for Data Mining)

**Evaluasi Model:**
- Naive Bayes (Baseline) — Akurasi: 100%
- Random Forest (Ensemble) — Akurasi: 100%
- XGBoost (Advanced, Model Terpilih) — Akurasi: 100%

XGBoost dipilih karena lebih robust terhadap korelasi antar fitur dan memiliki skalabilitas terbaik.

---

## Dataset

- **Nama:** Crop Recommendation Dataset
- **Sumber:** [Kaggle — Atharva Ingle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- **Jumlah Tanaman:** 14 komoditas lokal Indonesia (Padi, Jagung, Pisang, Mangga, Semangka, Jeruk, Pepaya, Kelapa, Kopi, Anggur, Apel, Delima, Melon, Kacang Hijau)

---

## Struktur Folder

```text
UAS_DataMining_106_Lizam/
│
├── dataset/
│   |── Crop_recommendation_clean.csv
|   |_Crop_recommendation.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── model/
│   └── model_rekomendasi_tanaman.pkl
│
├── app/
│   ├── Home.py
│   ├── pages/
│   │   ├── Dataset_Overview.py
│   │   ├── Prediction_Analysis.py
│   │   └── About.py 
│   └── assets/
│       └── visualisasi_curah_hujan.png
|       └── visualisasi_distribusi.png
|       └── visualisasi_korelasi_hara.png
|
├── laporan/
│   └── laporan.pdf
│
├── requirements.txt
└── README.md
```

---

## Cara Menjalankan Aplikasi
- SECARA LOKAL
1. Clone atau download repository ini
2. Install semua dependensi:
```bash
pip install -r requirements.txt
```
3. Jalankan aplikasi Streamlit:
```bash 
streamlit run app/Home.py
```
4. Buka browser dan akses `http://localhost:8501`

- Atau bisa langsung akses di https://sistem-klasifikasi-lahan-dan-rekomendasi-tanaman.streamlit.app
---

## Requirements

```text
streamlit
pandas
numpy
scikit-learn
xgboost
plotly
altair
matplotlib
seaborn
pickle5
```
Catatan:
1. Jika Ingin Menjalankan Aplikasi Ini Secara Lokal Dengan Repository Ini, Tambahkan Modul pickle5 Terlebih Dahulu Di File requirements.txt Atau Copy(Salin) Isi File requirements.txt Secara Lengkap Diatas
2. Untuk Deploy Menggunakan Platform Streamlit (https://streamlit.io/), modul pickle5 tidak perlu dimasukkan ke requirements.txt
---

## Lisensi

Proyek ini dibuat untuk keperluan akademik — Tugas Akhir / UAS mata kuliah Data Mining, Sistem Informasi, Universitas Negeri Surabaya (UNESA), 2026.
