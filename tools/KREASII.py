import streamlit as st
import random
from PIL import Image, ImageOps
from io import BytesIO

# Daftar gambar
image_urls = [
    "https://drive.google.com/uc?export=view&id=1uTojWTp3nOwNQWYiRuXjHlFcFlfyfWuM",
    "https://drive.google.com/uc?export=view&id=1dFUcmq51LN9T65_GKBHrRh2r6YMbJhVY",
    "https://drive.google.com/uc?export=view&id=13r8HA6B9mSgs32uXs7WLrHG9KY3KFicg",
    "https://drive.google.com/uc?export=view&id=1RyHarV3gSFq5oDyiZk8CU_tDTcuBZY4X",
    "https://drive.google.com/uc?export=view&id=1pdWy7eGALG7jQYjI-jo7M8u465wX2G-P",
    "https://drive.google.com/uc?export=view&id=1H2FvUXOqWS88WNlP1KBfMoEyxraYbFmr",
    "https://drive.google.com/uc?export=view&id=11EsaipCjA-2VDkibzGldSvNob62GU7wm",
    "https://drive.google.com/uc?export=view&id=1DtWLKoErKoTrq5x8LsA60kOblwZp8TlW",
    "https://drive.google.com/uc?export=view&id=14Q0kTnxMZTq3Lk5RiCER6SAhHNT4Oumx",
    "https://drive.google.com/uc?export=view&id=12Ziv1YeqgRyzYAWURx1p6RGdrGLStj-h",
    "https://drive.google.com/uc?export=view&id=1DCDH-MVLJsnosadIpEIWoPQ0WdgkDeyE",
    "https://drive.google.com/uc?export=view&id=1qfpceOSKfC21ryfPPcvZmlYECTriTGpa",
    "https://drive.google.com/uc?export=view&id=14bcqk8dfCJrqPk6xChc5m7JBrtsM5G3P",
    "https://drive.google.com/uc?export=view&id=1P5hhBReMUAV2k5jJbs7VdhOhMPkZehUx",
    "https://drive.google.com/uc?export=view&id=1XzZTgrIUKJ3f1_GNsfeSl2KS6xGZRNB5",
    "https://drive.google.com/uc?export=view&id=1DUUMrI3_UklpW0gldodR-ZzA0AjNbgFM",
    "https://drive.google.com/uc?export=view&id=1IGQ1bsVHvQG1LRaF04GZiqd2IvTDmp3b",
    "https://drive.google.com/uc?export=view&id=1qYrVAACBO5QECt1sjTrFthxgaRuKsHWV",
    "https://drive.google.com/uc?export=view&id=11FXHqnfaxVVU-_2EJooiVYlZv7qkbG-V",
    "https://drive.google.com/uc?export=view&id=1_mGbJs-wUS_39MqM3pX7B_h9d3gVWKHZ",
    "https://drive.google.com/uc?export=view&id=1parpmeDm1tSRxBuNbEaF0HeX6bV3qzHD",
    "https://drive.google.com/uc?export=view&id=1_Lc7DWvaGYwYtgN_ANYtEam9k_3oUwhc",
    "https://drive.google.com/uc?export=view&id=1GANT7dB9FgwWphdvAzp10an5MxLDNakH",
    "https://drive.google.com/uc?export=view&id=1xRRNCTohmt39mV2qekCU7UQ0KKJ-0fer",
    "https://drive.google.com/uc?export=view&id=1G1V33pdmvDWfY48VXlRbxWFzpj0s4g_q",
    "https://drive.google.com/uc?export=view&id=1CkQ5rDvhZdJvhPV4DrcKB_O00zidJaF2",
    "https://drive.google.com/uc?export=view&id=1IOpqBhMd0yX1kTgz8Hn-2GQlOCGaelAu",
    "https://drive.google.com/uc?export=view&id=1OFn2Sl0-IlvkTBRByt4d3wMtgVu5-hQ_",
    "https://drive.google.com/uc?export=view&id=19x1WINsa7pzowK2iV7z_rjbQzkAKdrxw",
    "https://drive.google.com/uc?export=view&id=1rStwbjBreYZmm8fs_XniDP3Dv6ZL21Vv",
    "https://drive.google.com/uc?export=view&id=1ooNX4qt938_mqwa3-1cZWCMcCFxxFzl-",
    "https://drive.google.com/uc?export=view&id=1My0HpjrG-TEa73o0uJwVbmMdfvdw-jX7",
    "https://drive.google.com/uc?export=view&id=19x5D0YfDpTe2u9M76tuno2W4d6eCJDZH",
    "https://drive.google.com/uc?export=view&id=1Vo2ll8ei4RrRx-Sx3Wis36C_XQ86lCiC",
    "https://drive.google.com/uc?export=view&id=185YLv_FnagP2nC-1YRDiVpBsuDPVvk6E",
    "https://drive.google.com/uc?export=view&id=1RnZHP2am0P5c3_T22SCY3mmsoQp3cPLY",
    "https://drive.google.com/uc?export=view&id=1zvFAgtR2CU0Z6ajH_-c5D3c9N_2-0FbN",
    "https://drive.google.com/uc?export=view&id=1NzZtarvSbczaRlBwGv6yeTUxb2q2fAEQ",
    "https://drive.google.com/uc?export=view&id=1IPp3x5IZMifIRwm3z9vK4_lDx5bZuk2h",
    "https://drive.google.com/uc?export=view&id=1rox9bvGmU_u0MrMeUsUuKec7w2BQ7I95",
    "https://drive.google.com/uc?export=view&id=1rO1uBcdKHRUXjlBAgSQQcsPDguW_s5VL",
    "https://drive.google.com/uc?export=view&id=1Pkma6Z6WvoGfx0PPCZ9GiDU-8EFNfURB",
    "https://drive.google.com/uc?export=view&id=1100-k00heWrdUnJm2La7hUoHfjIMQyFR",
    "https://drive.google.com/uc?export=view&id=1__r574xamgY0eVV_qSwcu4KUJmqH-3yV",
    "https://drive.google.com/uc?export=view&id=1ZTUAOYLCVi2j9t0WnAxKohFW6u-uT0bg",
    "https://drive.google.com/uc?export=view&id=1Fkoyz1rDo0aJ-jq1jMyh1JeSjbCYJ15_",
    "https://drive.google.com/uc?export=view&id=1qvCr6lRo-Wd0lvEY8W457mLYYtiejFpO",
    "https://drive.google.com/uc?export=view&id=1yILSQ5mmx5UHHPJj9hJOHmcVpTMRoipA",
    "https://drive.google.com/uc?export=view&id=1OFTUiw3wfNnjLGrDaLY5pDiCwvKlHkMK",
    "https://drive.google.com/uc?export=view&id=1OAOWAcTMgWgliRThq6cXuqG1rt8ZnS4v",
    "https://drive.google.com/uc?export=view&id=1gMGUrtdrgM_N3lcawCSXFBlDwcgaSLU7",
    "https://drive.google.com/uc?export=view&id=1we7hdH_L96KJuG8-je6SniQNs31Lwgyj",
    "https://drive.google.com/uc?export=view&id=1kw6x3hyANWNTrvq55mcDQiWJARttNGMx",
    "https://drive.google.com/uc?export=view&id=1ZW8UaKo6LdO3wm1qKUzTCOrShqhHnuC-",
    "https://drive.google.com/uc?export=view&id=1_zOqRw0ND8BO-EY14gmMswppO-TYrtGm"
]

# Menyimpan state dari gambar yang terpilih
if 'image_terpilih' not in st.session_state:
    st.session_state.image_terpilih = random.choice(image_urls)

# Fungsi untuk menampilkan gambar baru secara acak
def tampilkan_gambar_baru():
    st.session_state.image_terpilih = random.choice(image_urls)

# Judul 
st.title("Uniform Pamer Mobil")

# Tombol untuk menampilkan gambar baru
if st.button('Tampilkan Gambar Mobil Baru'):
    tampilkan_gambar_baru()

# Menampilkan gambar terpilih
st.image(st.session_state.image_terpilih, caption="Gambar Mobil", use_column_width=True)
