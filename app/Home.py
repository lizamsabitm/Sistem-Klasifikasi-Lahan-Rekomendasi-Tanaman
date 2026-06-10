import streamlit as st

st.set_page_config(
    page_title="Rekomendasi Lahan & Tanaman",
    page_icon="🌾",
    layout="centered"
)

st.title("Sistem Klasifikasi Lahan & Rekomendasi Tanaman")
st.markdown(
    "### Sistem penunjang keputusan pertanian presisi yang mengintegrasikan dua algoritma, "
    "yaitu **K-Means Clustering** untuk mengidentifikasi karakteristik zonasi kesuburan lahan, "
    "dan **XGBoost Classifier** untuk menentukan rekomendasi komoditas tanaman terbaik. "
    "Analisis otomatis ini bekerja berdasarkan kombinasi indikator hara makro tanah "
    "(Nitrogen, Fosfor, Kalium, pH Tanah) serta parameter cuaca lokal "
    "(suhu, kelembapan, curah hujan)."
)
st.write(
    "Optimalkan potensi pertanian Anda dengan identifikasi karakteristik zonasi lahan "
    "dan temukan rekomendasi komoditas tanaman lokal terbaik secara akurat."
)

st.markdown("---")

st.subheader("Ringkasan Proyek")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Tanaman", "14 Komoditas")
col2.metric("Fitur Sensor", "7 Parameter")
col3.metric("Zona Lahan", "5 Zona")
col4.metric("Akurasi Model", "100%")

st.markdown("---")

st.subheader("Zona Lahan yang Diidentifikasi")
st.write("Sistem mengelompokkan lahan ke dalam **5 zona** berdasarkan pola sensor tanah dan cuaca:")

zona = {
    "Lahan Kering Alami & Tropis Hangat": "Curah hujan rendah–sedang, drainase alami baik, paparan matahari stabil.",
    "Lahan Basah": "Pasokan air melimpah, kelembapan tinggi, curah hujan masif. Cocok untuk dataran rendah dan pesisir.",
    "Lahan Subur Dataran Tinggi": "Suhu sejuk, kaya Fosfor (P) dan Kalium (K), sangat subur untuk tanaman buah dan sayur.",
    "Lahan Moderat Dataran Rendah": "Kondisi seimbang dan serbaguna. Semua parameter berada di kisaran rata-rata.",
    "Lahan Aluvial": "Struktur tanah gembur, sirkulasi udara baik, suhu hangat dengan kelembapan cukup tinggi."
}

for nama_zona, deskripsi in zona.items():
    with st.expander(nama_zona):
        st.write(deskripsi)

st.markdown("---")

st.subheader("Komoditas Tanaman yang Didukung")
st.write("Sistem mendukung **14 komoditas tanaman lokal Indonesia:**")

tanaman = [
    "Padi", "Jagung", "Pisang", "Mangga",
    "Semangka", "Jeruk", "Pepaya", "Kelapa",
    "Kopi", "Anggur", "Apel", "Delima",
    "Melon", "Kacang Hijau"
]

cols = st.columns(4)
for i, t in enumerate(tanaman):
    cols[i % 4].markdown(f"- {t}")

st.markdown("---")

st.subheader("Fitur Aplikasi")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("**1️. Dataset Overview**\n\nEksplorasi informasi dan statistik dataset.")
with col2:
    st.success("**2️. Prediction & Analysis**\n\nInput parameter sensor lahan dan klik Analisis.")
with col3:
    st.warning("**3️. Visualization**\n\nLihat grafik hasil analisis secara dinamis.")
with col4:
    st.error("**4️. About**\n\nPelajari metode dan informasi proyek.")

st.markdown("---")

st.subheader("Identitas Mahasiswa")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Nama**")
    st.info("Lizam Sabit Mafaiz")
    st.markdown("**NIM**")
    st.info("24051214106")

with col2:
    st.markdown("**Kelas**")
    st.info("KDD1")
    st.markdown("**Mata Kuliah**")
    st.info("Data Mining")

st.markdown("**Dosen Pengampu**")
st.info("Dr. Wiyli Yustanti, S.Si., M.Kom.")

st.markdown("---")
st.caption("© 2026 · Sistem Klasifikasi Lahan & Rekomendasi Tanaman · Data Mining · Sistem Informasi · UNESA")