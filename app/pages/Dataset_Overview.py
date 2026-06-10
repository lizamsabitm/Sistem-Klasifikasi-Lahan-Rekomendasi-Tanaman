import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Dataset Overview",
    page_icon="🌾",
    layout="centered"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_DATASET = os.path.join(BASE_DIR, 'dataset', 'Crop_recommendation.csv')
DIR_ASSETS = os.path.join(BASE_DIR, 'app', 'assets')

@st.cache_data
def muat_data():
    return pd.read_csv(PATH_DATASET)

df_tanaman = muat_data()

st.title("Dataset Overview")
st.markdown("---")

st.subheader("Informasi Dataset")
st.write(
    "Dataset yang digunakan dalam proyek ini adalah **Crop Recommendation Dataset** yang bersumber dari platform Kaggle. "
    "Dataset ini dirancang untuk membangun sistem rekomendasi pertanian presisi berdasarkan parameter lingkungan lokal."
)
st.markdown("**Sumber Resmi:** [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)")

col_meta1, col_meta2 = st.columns(2)
with col_meta1:
    st.metric("Jumlah Baris Data (Instances)", f"{df_tanaman.shape[0]} Baris")
with col_meta2:
    st.metric("Jumlah Kolom Fitur (Attributes)", f"{df_tanaman.shape[1]} Kolom")

st.markdown(
    "Dataset ini bersifat *Balanced Dataset* (Seimbang Sempurna), yang mencakup **22 jenis komoditas tanaman berbeda** "
    "(seperti padi, jagung, kopi, buah-buahan, dll). Masing-masing tanaman memiliki tepat **100 sampel data** hara dan cuaca. "
    "Terdiri dari 8 kolom, yang terbagi menjadi 7 fitur prediktor (input) dan 1 fitur target (output). Fitur-fitur ini merupakan "
    "indikator hara tanah dan parameter cuaca yang dimasukkan oleh pengguna melalui formulir sensor untuk dianalisis oleh sistem:\n\n"
    "**1. Nitrogen (N)**: Kadar kandungan unsur hara makro Nitrogen di dalam tanah (satuan: mg/kg)\n\n"
    "**2. Fosfor (P)**: Kadar kandungan unsur hara makro Fosfor di dalam tanah (satuan: mg/kg)\n\n"
    "**3. Kalium (K)**: Kadar kandungan unsur hara makro Kalium di dalam tanah (satuan: mg/kg)\n\n"
    "**4. Suhu Udara (Temperature)**: Derajat panas lingkungan sekitar lahan (satuan: °C)\n\n"
    "**5. Kelembapan Udara (Humidity)**: Persentase kandungan air di udara lingkungan sekitar lahan (satuan: %)\n\n"
    "**6. Tingkat Keasaman (pH)**: Skala keasaman atau kebasaan dari struktur tanah (skala: 0–14)\n\n"
    "**7. Curah Hujan (Rainfall)**: Estimasi volume curah hujan tahunan di wilayah lahan tersebut (satuan: mm)"
)

st.markdown("---")
st.subheader("Statistik Sederhana")
st.write(
    "Tabel berikut menampilkan ringkasan matriks statistik deskriptif dari seluruh parameter sensor tanah dan cuaca di dalam dataset. "
    "Matriks ini mencakup nilai rata-rata (*mean*), standar deviasi (*std*), nilai minimum, kuartil, hingga nilai maksimum."
)

st.dataframe(df_tanaman.describe().T, use_container_width=True)

st.markdown("---")
st.subheader("Visualisasi Analisis Data")
st.write("Berikut adalah visualisasi grafis hasil pra-proses dan eksplorasi data yang telah diekstraksi dari model pengujian:")

st.markdown("#### 1. Sebaran Target Komoditas Tanaman")
st.image(os.path.join(DIR_ASSETS, 'visualisasi_distribusi.png'), caption="Grafik Batang Distribusi Jumlah Sampel Data per Komoditas", use_container_width=True)
st.info(
    "**Analisis Grafik:**\n\n"
    "Grafik batang (*bar chart*) di atas menggambarkan sebaran jumlah sampel data untuk setiap komoditas tanaman yang ada di dalam dataset. "
    "Hasil visualisasi menunjukkan bahwa dataset ini merupakan **Balanced Dataset (Dataset Seimbang Sempurna)**. "
    "Terdapat total 22 jenis komoditas tanaman berbeda, di mana masing-masing tanaman memiliki tepat **100 baris sampel data**, sehingga membentuk total keseluruhan 2.200 data. "
    "Karakteristik data yang seimbang seperti ini sangat ideal untuk proses *training* model *Machine Learning* (XGBoost), karena mencegah model mengalami bias atau hanya condong pintar memprediksi satu jenis tanaman tertentu saja."
)

st.markdown("---")

st.markdown("#### 2. Karakteristik Pola Klaster Hara Tanah")
st.image(os.path.join(DIR_ASSETS, 'visualisasi_korelasi_hara.png'), caption="Grafik Scatter Plot Hubungan Kadar Nitrogen (N) vs Kalium (K)", use_container_width=True)
st.info(
    "**Analisis Grafik:**\n\n"
    "Grafik sebaran (*scatter plot*) ini memetakan hubungan antara dua unsur hara makro utama tanah, yaitu Nitrogen (N) dan Kalium (K), untuk beberapa sampel tanaman ikonik (*Rice, Maize, Apple, Coffee, Grapes*). "
    "Dari sebaran titik-titik koordinat tersebut, terlihat jelas adanya **pola pengelompokan alami (clustering)** yang unik:\n"
    "* Tanaman **Grapes (Anggur)** dan **Apple (Apel)** berkumpul membentuk kelompok di area atas, yang menandakan bahwa kedua tanaman buah ini membutuhkan asupan Kalium (K) yang sangat tinggi (berkisar antara 140–205 mg/kg) namun dengan kadar Nitrogen yang sangat rendah.\n"
    "* Tanaman **Rice (Padi)** dan **Coffee (Kopi)** berkerumun di area kanan bawah, mengindikasikan karakteristik lahan yang kaya akan Nitrogen (N) tetapi rendah Kalium (K).\n\n"
    "Pola sebaran yang terpisah secara berkelompok inilah yang menjadi dasar kuat mengapa algoritma **K-Means Clustering** sangat relevan dan akurat dalam mendefinisikan zonasi karakteristik lahan pada sistem ini."
)

st.markdown("---")

st.markdown("#### 3. Analisis Rentang Toleransi Curah Hujan")
st.image(os.path.join(DIR_ASSETS, 'visualisasi_curah_hujan.png'), caption="Grafik Box Plot Distribusi Rentang Kebutuhan Curah Hujan per Komoditas", use_container_width=True)
st.info(
    "**Analisis Grafik:**\n\n"
    "Grafik kotak-garis (*box plot*) di atas digunakan untuk menganalisis rentang serta sebaran kebutuhan estimasi curah hujan (dalam satuan milimeter) bagi seluruh komoditas tanaman. "
    "Melalui visualisasi ini, kita dapat mengidentifikasi batas toleransi air untuk setiap tanaman:\n"
    "* Tanaman **Rice (Padi)** memiliki posisi kotak paling tinggi, yang membuktikan secara valid bahwa padi membutuhkan volume curah hujan paling masif (berkisar antara 200–300 mm) karena karakteristik habitatnya berupa lahan basah/sawah.\n"
    "* Sebaliknya, komoditas seperti **Muskmelon** atau **Chickpea** memiliki kotak yang berada di area bawah, menandakan rentang kebutuhan air yang sangat minim (di bawah 100 mm).\n\n"
    "Visualisasi ini memperlihatkan bahwa variabilitas parameter cuaca, khususnya curah hujan, memegang peranan krusial bagi model keputusan **XGBoost** dalam mengklasifikasikan jenis tanaman yang paling aman untuk direkomendasikan pada kondisi iklim tertentu."
)