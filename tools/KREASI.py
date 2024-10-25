import streamlit as st
import random

# Daftar kutipan dalam bahasa Inggris
kutipan = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "The secret of getting ahead is getting started. - Mark Twain"
]

# Judul aplikasi dalam bahasa Indonesia
st.title("Penghasil Kutipan Acak")

# Menyimpan state dari kutipan yang dihasilkan
if 'kutipan_terpilih' not in st.session_state:
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tombol untuk menghasilkan kutipan baru
if st.button("Tampilkan Kutipan Baru"):
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tampilkan kutipan dengan tulisan besar dan font yang unik
st.markdown(
    f"""
    <div style="text-align: center; font-size: 30px; font-family: 'Courier New', Courier, monospace;">
        {st.session_state.kutipan_terpilih}
    </div>
    """,
    unsafe_allow_html=True
)
