import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="🌾",
    layout="centered"
)

st.title("Tentang Proyek Ini")
st.markdown("---")

st.subheader("Deskripsi Proyek")
st.write(
    "Proyek ini merupakan sistem berbasis Machine Learning yang dirancang untuk membantu "
    "petani dan praktisi pertanian dalam mengidentifikasi karakteristik zona lahan serta "
    "mendapatkan rekomendasi komoditas tanaman yang paling sesuai berdasarkan kondisi "
    "hara tanah dan parameter cuaca secara otomatis."
)

st.markdown("---")

st.subheader("Informasi Dataset")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Nama Dataset**")
    st.info("Crop Recommendation Dataset")
    st.markdown("**Sumber**")
    st.info("[Kaggle — Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)")

with col2:
    st.markdown("**Jumlah Fitur Input**")
    st.info("7 Parameter Sensor (N, P, K, Suhu, Kelembapan, pH, Curah Hujan)")
    st.markdown("**Jumlah Kelas Tanaman**")
    st.info("14 Komoditas Tanaman Lokal Indonesia")

st.markdown("**Fitur-fitur Dataset:**")
st.table({
    "Fitur": ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"],
    "Keterangan": [
        "Kadar Nitrogen dalam tanah (mg/kg)",
        "Kadar Fosfor dalam tanah (mg/kg)",
        "Kadar Kalium dalam tanah (mg/kg)",
        "Suhu udara lingkungan (°C)",
        "Kelembapan udara (%)",
        "Tingkat keasaman tanah (pH)",
        "Estimasi curah hujan tahunan (mm)"
    ]
})

st.markdown("---")

st.subheader("Metodologi: CRISP-DM")
st.write(
    "Proyek ini menggunakan kerangka kerja **CRISP-DM (Cross Industry Standard Process "
    "for Data Mining)** sebagai panduan alur pengembangan sistem secara sistematis."
)

tahapan = {
    "1. Business Understanding": "Membangun sistem yang mampu mengelompokkan karakteristik lahan pertanian ke dalam zona-zona lahan dan merekomendasikan komoditas tanaman yang paling cocok berdasarkan kondisi sensor hara tanah dan cuaca.",
    "2. Data Understanding": "Eksplorasi dataset Crop Recommendation yang mencakup 7 parameter sensor. Dilakukan pengecekan struktur data, nilai kosong, keseimbangan kelas, dan analisis korelasi antar fitur menggunakan heatmap.",
    "3. Data Preparation": "Penyaringan 14 tanaman lokal Indonesia, penerjemahan label dari Bahasa Inggris ke Indonesia, pembersihan outlier berbasis IQR per kelas tanaman, label encoding target, dan feature scaling menggunakan StandardScaler.",
    "4. Modeling": "Dua tahap pemodelan: (1) K-Means Clustering (K=5) untuk mengelompokkan lahan menjadi 5 zona, ditentukan menggunakan Elbow Method dan Silhouette Score. (2) Komparasi tiga algoritma klasifikasi: Naive Bayes (baseline), Random Forest (ensemble), dan XGBoost (advanced).",
    "5. Evaluation": "Evaluasi model klasifikasi menggunakan Accuracy Score, Classification Report (precision, recall, F1-score per kelas), dan Confusion Matrix. Model terbaik dipilih berdasarkan akurasi tertinggi.",
    "6. Deployment": "Model terbaik dikemas dalam file .pkl dan di-deploy sebagai aplikasi web interaktif menggunakan Streamlit, dilengkapi form input sensor, hasil prediksi zona lahan, rekomendasi tanaman, dan visualisasi dinamis."
}

for tahap, deskripsi in tahapan.items():
    with st.expander(tahap):
        st.write(deskripsi)

st.markdown("---")

st.subheader("Metode Machine Learning yang Digunakan")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Clustering")
    st.success(
        "**K-Means Clustering**\n\n"
        "Digunakan untuk mengelompokkan data lahan ke dalam **5 zona lahan** "
        "berdasarkan kemiripan pola sensor. Jumlah klaster optimal (K=5) ditentukan "
        "melalui **Elbow Method** dan divalidasi dengan **Silhouette Score**."
    )

with col2:
    st.markdown("#### Klasifikasi")
    st.info(
        "**XG Boost (Model Terpilih)**\n\n"
        "Dipilih sebagai model final karena lebih robust terhadap korelasi "
        "antar fitur dibandingkan Naive Bayes, dan lebih efisien secara komputasi "
        "dibandingkan Random Forest."
    )

st.markdown("**Perbandingan Model yang Diuji:**")
st.table({
    "Model": ["Naive Bayes", "Random Forest", "XGBoost"],
    "Tipe": ["Baseline", "Ensemble", "Advanced (Model Terpilih)"],
    "Akurasi": ["100%", "100%", "100%"],
    "Keterangan": [
        "Akurasi sempurna namun berasumsi fitur independen — tidak ideal karena antar fitur berkorelasi",
        "Akurasi sempurna, lebih robust namun lebih lambat secara komputasi",
        "Akurasi sempurna, dipilih karena lebih robust terhadap korelasi fitur dan skalabilitas terbaik"
    ]
})

st.markdown("---")

st.subheader("Tools & Library yang Digunakan")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Pengembangan Model**")
    st.table({
        "Library": ["Scikit-learn", "XGBoost", "NumPy", "Pandas"],
        "Fungsi": [
            "K-Means, preprocessing, evaluasi",
            "Model klasifikasi XGBoost",
            "Operasi numerik array",
            "Manipulasi & analisis data"
        ]
    })

with col2:
    st.markdown("**Visualisasi**")
    st.table({
        "Library": ["Matplotlib", "Seaborn", "Plotly", "Altair"],
        "Fungsi": [
            "Grafik dasar & plot",
            "Heatmap & visualisasi statistik",
            "Radar chart interaktif",
            "Scatter chart interaktif"
        ]
    })

with col3:
    st.markdown("**Deployment**")
    st.table({
        "Library": ["Streamlit", "Pickle", "Google Colab", "Python 3"],
        "Fungsi": [
            "Framework aplikasi web",
            "Simpan & muat model .pkl",
            "Environment pelatihan model",
            "Bahasa pemrograman utama"
        ]
    })

st.markdown("---")

st.subheader("Informasi Proyek")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Mata Kuliah**")
    st.info("Data Mining")
    st.markdown("**Dosen Pengampu**")
    st.info("Dr. Wiyli Yustanti, S.Si., M.Kom.")

with col2:
    st.markdown("**Kelas**")
    st.info("KDD1")
    st.markdown("**Program Studi**")
    st.info("Sistem Informasi")

st.markdown("**Identitas Mahasiswa:**")
st.table({
    "Nama": ["Lizam Sabit Mafaiz"],
    "NIM": ["24051214106"],
    "Kelas": ["KDD1"]
})

st.markdown("---")
st.caption("© 2026 · Sistem Klasifikasi Lahan & Rekomendasi Tanaman · Data Mining · Sistem Informasi · UNESA")