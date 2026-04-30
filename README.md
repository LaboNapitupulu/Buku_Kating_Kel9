# 📖 Interactive Organization Portal & Data Analytics Dashboard (Buku Kating Kel 9)
> **Live Web Application:** [bukukatinguniform.streamlit.app](https://bukukatinguniform.streamlit.app/)

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-yellow.svg)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-indigo.svg)](https://plotly.com/python/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-lightblue.svg)](https://seaborn.pydata.org/)

## 📌 Executive Summary
Proyek ini adalah aplikasi web interaktif berbasis **Streamlit** yang dikembangkan sebagai sistem informasi dan *dashboard* analitik untuk Himpunan Mahasiswa Sains Data (HMSD) ITERA. 

Lebih dari sekadar buku profil digital, repositori ini mendemonstrasikan implementasi praktik *Data Science* yang komprehensif—mulai dari rekayasa perangkat lunak dasar (*web routing*, *caching*), *Data Cleaning* menggunakan RegEx, hingga visualisasi statistik (*Exploratory Data Analysis*) untuk mengukur performa organisasi.

---

## 🛠️ Arsitektur & Fitur Teknis Utama

### 1. Interactive Web Routing & State Management
Membangun pengalaman *user* yang mulus (tanpa *reload* berlebih) menggunakan arsitektur multipage Streamlit.
*   **Routing Dinamis:** Menggunakan modul `st.navigation` dan `st.Page` di `main.py` untuk mengelola puluhan halaman profil (*routing*) secara modular.
*   **Session Management:** Memanfaatkan `st.session_state` untuk menjaga konsistensi data dan logika perpindahan halaman selama sesi aktif pengguna.

### 2. Cloud Integration & Performance Optimization
*   **API/URL Image Fetching:** Memuat seluruh aset gambar secara dinamis dari Google Drive menggunakan modul `requests` dan `PIL` (Pillow).
*   **Data Caching:** Menggunakan dekorator `@st.cache_data` pada fungsi pemuatan gambar untuk memori lokal sementara, sehingga meminimalisir beban jaringan dan mempercepat waktu *render* aplikasi secara signifikan.

### 3. Data Cleaning & Feature Extraction (`tools/KREASII.py`)
Mendemonstrasikan proses pra-pemrosesan data mentah yang krusial di dunia nyata menggunakan **Pandas**.
*   **RegEx Implementation:** Mengekstrak nilai numerik tersembunyi dari format teks yang kotor (misal: "10,5 jam kerja") menggunakan RegEx `r'(\d+[,\.]?\d*)'`, mengganti koma dengan titik, dan mengonversinya ke tipe data `float`.
*   **Data Imputation & Normalization:** Menangani entri teks tidak standar (seperti "Belum ada sejauh ini") dengan mengubahnya menjadi nilai kuantitatif yang relevan (0), serta menstandarisasi nama kategori divisi.

### 4. Exploratory Data Analysis (EDA) & Visualization
Menyajikan *insight* organisasi melalui grafik statistik tingkat lanjut menggunakan kombinasi **Matplotlib**, **Seaborn**, dan **Plotly**.
*   **Analisis Sentralitas & Persebaran:** Menampilkan ringkasan statistik deskriptif dan visualisasi **Boxplot** untuk mengidentifikasi anomali (*outliers*) distribusi jam kerja.
*   **Kepadatan & Tren:** Menggunakan **Density Plot (KDE)** dan **Histogram** untuk menemukan sentralitas beban kerja di berbagai divisi organisasi.
*   **Spatial & Time-Series Data:** Integrasi **Plotly Express** untuk membuat peta interaktif (*Choropleth*) pengguna internet global dan grafik garis (*line chart*) untuk data tren historis.

### 5. Containerized Development (`.devcontainer/devcontainer.json`)
Aplikasi ini dikembangkan dengan arsitektur *container-ready* menggunakan Docker (berbasis `[mcr.microsoft.com/devcontainers/python:1-3.11-bullseye](https://mcr.microsoft.com/devcontainers/python:1-3.11-bullseye)`).
*   Menjamin **reproduksibilitas 100%** di berbagai perangkat pengembangan.
*   Skrip otomatis untuk pembaruan *package* sistem (`apt`) dan instalasi dependensi Python (`requirements.txt`) pada saat instalasi lingkungan (*post-attach*).

---

## 📂 Struktur Repositori (Ringkasan)
Pendekatan modular (*Separation of Concerns*) digunakan untuk menjaga kode tetap terstruktur.
```text
Buku_Kating_Kel9/
├── .devcontainer/             # Konfigurasi containerized environment
├── .streamlit/                # Pengaturan tema global (config.toml)
├── Buku Kating/               # Kumpulan skrip untuk modul halaman profil
├── Halaman Utama/             # Landing page aplikasi
├── tools/                     # Modul inti untuk Data Science (EDA & Visualisasi)
│   ├── KREASI.py              # Visualisasi interaktif dengan Plotly
│   └── KREASII.py             # Data Cleaning & Statistical Analysis dengan Pandas & Seaborn
├── main.py                    # Entry point & sistem routing navigasi Streamlit
└── requirements.txt           # Daftar dependensi library Python
```

---

## 🚀 Cara Menjalankan secara Lokal

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/LaboNapitupulu/Buku_Kating_Kel9.git
   cd Buku_Kating_Kel9
   ```

2. **Instal dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan aplikasi Streamlit:**
   ```bash
   streamlit run main.py
   ```

*(Aplikasi akan otomatis terbuka di browser melalui `http://localhost:8501`)*

---
*Proyek ini merupakan representasi implementasi Data Science dalam manajemen organisasi, dikembangkan sebagai bagian dari penugasan kaderisasi himpunan (HMSD ITERA).*

***
