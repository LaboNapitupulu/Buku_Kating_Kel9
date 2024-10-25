import streamlit as st

# URL gambar dari Google Drive (gunakan direct link Google Drive)
image_url = "https://drive.google.com/uc?export=view&id=1uTojWTp3nOwNQWYiRuXjHlFcFlfyfWuM"

# Judul aplikasi
st.title("Tes Gambar Mobil dari Google Drive")

# Menampilkan gambar
st.image(image_url, caption="Gambar Mobil", use_column_width=True)
