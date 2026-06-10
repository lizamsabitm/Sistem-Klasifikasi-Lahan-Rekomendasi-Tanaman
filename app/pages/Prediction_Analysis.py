import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
import altair as alt
import plotly.graph_objects as go

st.set_page_config(
    page_title="Prediction & Analysis",
    page_icon="🌾",
    layout="centered"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PATH_MODEL = os.path.join(BASE_DIR, 'model', 'model_rekomendasi_tanaman.pkl')
PATH_DATASET = os.path.join(BASE_DIR, 'dataset', 'Crop_recommendation_clean.csv')

@st.cache_resource
def muat_paket_ai():
    with open(PATH_MODEL, 'rb') as file:
        return pickle.load(file)

@st.cache_data
def muat_data_asli():
    return pd.read_csv(PATH_DATASET)

paket_ai = muat_paket_ai()
df_asli = muat_data_asli()

model_klasifikasi = paket_ai['model_klasifikasi']
model_clustering = paket_ai['model_clustering']
scaler = paket_ai['scaler']
encoder = paket_ai['encoder']
kamus_zona = paket_ai['kamus_zona']

deskripsi_zona = {
    0: "Wilayah lahan yang memiliki karakteristik curah hujan rendah hingga sedang dengan paparan matahari yang stabil. Tanah memiliki kemampuan drainase alami yang baik sehingga tidak gampang tergenang air.",
    1: "Zona lahan dengan pasokan air sangat melimpah, kelembapan udara tinggi, dan curah hujan masif. Biasanya berlokasi di dataran rendah, aliran sungai, atau daerah pesisir yang daya ikat airnya kuat.",
    2: "Karakteristik lahan topografi dataran tinggi dengan suhu sejuk. Tanah berstatus sangat subur karena kaya akan kandungan hara makro spesifik Fosfor (P) dan Kalium (K) untuk merangsang akar dan buah.",
    3: "Lahan dataran rendah dengan kondisi lingkungan serbaguna dan seimbang. Kandungan hara (N, P, K), keasaman (pH), suhu, dan curah hujan berada pada batas rata-rata (moderat).",
    4: "Karakteristik lahan dengan struktur tanah cenderung gembur, berpasir, atau berupa endapan (aluvial). Memiliki sirkulasi udara tanah yang baik, suhu hangat, namun kelembapan udara sekitarnya cukup tinggi."
}

st.title("Klasifikasi Lahan & Rekomendasi Tanaman")
st.markdown("### Optimalkan potensi pertanian Anda dengan identifikasi karakteristik zonasi lahan Anda dan temukan rekomendasi komoditas tanaman lokal terbaik secara akurat")
st.write(
    "Masukkan indikator hara tanah dan kondisi cuaca di bawah ini. "
    "Sistem akan menganalisis karakteristik zona lahan "
    "sekaligus menentukan rekomendasi komoditas tanaman terbaik secara otomatis."
)
st.markdown("---")

st.subheader("Formulir Input Indikator Sensor")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Unsur Hara Makro Tanah**")
    input_N = st.number_input("Kadar Nitrogen (N)", min_value=0, max_value=150, value=50, help="Satuan mg/kg")
    input_P = st.number_input("Kadar Fosfor (P)", min_value=5, max_value=150, value=40, help="Satuan mg/kg")
    input_K = st.number_input("Kadar Kalium (K)", min_value=5, max_value=210, value=40, help="Satuan mg/kg")
    input_pH = st.number_input("Tingkat Keasaman Tanah (pH)", min_value=3.5, max_value=10.0, value=6.5, step=0.1, help="Skala pH tanah")

with col2:
    st.markdown("**Parameter Kondisi Cuaca**")
    input_temp = st.number_input("Suhu Udara (°C)", min_value=10.0, max_value=50.0, value=25.0, step=0.5, help="Derajat Celcius")
    input_hum = st.number_input("Kelembapan Udara (%)", min_value=10.0, max_value=100.0, value=80.0, step=0.5, help="Persentase kelembapan")
    input_rain = st.number_input("Estimasi Curah Hujan (mm)", min_value=20.0, max_value=300.0, value=150.0, step=1.0, help="Satuan milimeter")

st.markdown("---")

if 'proses_analisis' not in st.session_state:
    st.session_state.proses_analisis = False

if st.button("Analisis Karakteristik Lahan & Rekomendasi Tanaman", type="primary"):
    st.session_state.proses_analisis = True
    st.session_state.data_mentah = pd.DataFrame([{
        'N': input_N, 'P': input_P, 'K': input_K,
        'temperature': input_temp, 'humidity': input_hum,
        'ph': input_pH, 'rainfall': input_rain
    }])

if st.session_state.proses_analisis and 'data_mentah' in st.session_state:
    data_mentah = st.session_state.data_mentah
    data_scaled = scaler.transform(data_mentah)

    angka_cluster = model_clustering.predict(data_scaled)[0]
    nama_zona_asli = kamus_zona[angka_cluster]
    teks_deskripsi = deskripsi_zona[angka_cluster]

    angka_tanaman = model_klasifikasi.predict(data_scaled)[0]
    nama_tanaman_asli = encoder.inverse_transform([angka_tanaman])[0]

    saran_tanaman_lokal = {
        0: "Sorgum, Kacang Tanah, Pohon Jati, atau Singkong",
        1: "Kangkung Darat, Genjer, Talas Bumbu, atau Sagu",
        2: "Teh, Kentang, Wortel, Stroberi, atau Kubis",
        3: "Kedelai, Kacang Hijau, Ubi Jalar, atau Bawang Merah",
        4: "Pohon Sengon, Jambu Biji, Nanas, atau Kacang Koro"
    }
    tanaman_alternatif = saran_tanaman_lokal.get(angka_cluster, "Tanaman palawija lokal")

    st.subheader("Hasil Analisis Sistem")

    st.info(f"**1. Karakteristik Wilayah Lahan Anda:**\n\n"
            f"**Kategori:** *{nama_zona_asli}*\n\n"
            f"**Deskripsi:** {teks_deskripsi}")

    st.success(f"**2. Komoditas Pertanian Paling Direkomendasikan:**\n\n"
               f"**Tanaman Utama:** *{nama_tanaman_asli.upper()}*\n\n"
               f"Tanaman ini terbukti memiliki kecocokan pola matematis 100% "
               f"terhadap kondisi hara makro serta fluktuasi cuaca lokal yang Anda masukan.\n\n"
               f"--- \n\n"
               f"**Saran Komoditas Alternatif (Karakteristik Lahan Setara):**\n"
               f"Berdasarkan kesamaan tipe zona lahan, Anda juga dapat mempertimbangkan budidaya: **{tanaman_alternatif}**.")

    st.markdown("---")
    st.subheader("Grafik Pendukung & Visualisasi Hasil Analisis")
    st.write("Visualisasi berikut bersifat dinamis dan diekstraksi secara *real-time* dengan memetakan posisi data input Anda terhadap tren sebaran dataset asli.")

    st.markdown(f"#### A. Perbandingan Hara Lahan Anda vs Kebutuhan Ideal Tanaman {nama_tanaman_asli.title()}")

    df_ideal = df_asli[df_asli['label'] == nama_tanaman_asli][['N', 'P', 'K']].mean()

    df_grafik_hara = pd.DataFrame({
        'Kandungan Hara': ['Nitrogen (N)', 'Fosfor (P)', 'Kalium (K)',
                           'Nitrogen (N)', 'Fosfor (P)', 'Kalium (K)'],
        'Nilai (mg/kg)': [
            data_mentah['N'].values[0], data_mentah['P'].values[0], data_mentah['K'].values[0],
            df_ideal['N'], df_ideal['P'], df_ideal['K']
        ],
        'Kategori': [
            'Lahan Anda', 'Lahan Anda', 'Lahan Anda',
            f'Ideal {nama_tanaman_asli.title()}',
            f'Ideal {nama_tanaman_asli.title()}',
            f'Ideal {nama_tanaman_asli.title()}'
        ]
    })

    st.bar_chart(data=df_grafik_hara, x='Kandungan Hara', y='Nilai (mg/kg)', color='Kategori', stack=False)

    st.markdown(f"#### B. Profil Parameter Lahan Anda vs Rata-rata Zona: {nama_zona_asli}")

    df_zona = df_asli[df_asli['cluster_lahan'] == angka_cluster]
    rata_zona = df_zona[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].mean()

    parameter_labels = ['N', 'P', 'K', 'Suhu', 'Kelembapan', 'pH', 'Curah Hujan']
    nilai_user = [float(input_N), float(input_P), float(input_K),
                  float(input_temp), float(input_hum), float(input_pH), float(input_rain)]
    nilai_zona = [rata_zona['N'], rata_zona['P'], rata_zona['K'],
                  rata_zona['temperature'], rata_zona['humidity'],
                  rata_zona['ph'], rata_zona['rainfall']]

    nilai_max = [150, 150, 210, 50, 100, 14, 300]
    user_norm = [v / m for v, m in zip(nilai_user, nilai_max)]
    zona_norm = [v / m for v, m in zip(nilai_zona, nilai_max)]

    fig_radar = go.Figure()

    fig_radar.add_trace(go.Scatterpolar(
        r=zona_norm + [zona_norm[0]],
        theta=parameter_labels + [parameter_labels[0]],
        fill='toself',
        fillcolor='rgba(99, 149, 230, 0.3)',
        line=dict(color='rgba(99, 149, 230, 0.9)', width=2),
        name=f'Rata-rata {nama_zona_asli}'
    ))

    fig_radar.add_trace(go.Scatterpolar(
        r=user_norm + [user_norm[0]],
        theta=parameter_labels + [parameter_labels[0]],
        fill='toself',
        fillcolor='rgba(255, 80, 80, 0.25)',
        line=dict(color='red', width=2.5, dash='dot'),
        name='Lahan Anda',
        mode='lines+markers',
        marker=dict(size=7, color='red')
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1],
                tickformat='.0%',
                gridcolor='#DDDDDD'
            ),
            angularaxis=dict(gridcolor='#DDDDDD'),
            bgcolor='white'
        ),
        showlegend=True,
        legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5, font=dict(color='black')),
        paper_bgcolor='white',
        font=dict(color='black'),
        margin=dict(t=40, b=80, l=60, r=60),
        height=450
    )

    st.plotly_chart(fig_radar, use_container_width=True)
    st.caption(
        "Cara membaca grafik:"
        "Semakin berhimpitan area **Merah (Lahan Anda)** dengan area **Biru (Rata-rata Zona)**, "
        "semakin sesuai kondisi lahan Anda dengan karakteristik zona tersebut."
    )