import streamlit as st
from PIL import Image
from io import BytesIO
import requests


image_url = "https://drive.google.com/uc?export=download&id=1uTojWTp3nOwNQWYiRuXjHlFcFlfyfWuM"

response = requests.get(image_url)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    st.image(image, caption="Gambar Mobil dari Google Drive", use_column_width=True)
else:
    st.error("Gambar tidak bisa diambil dari URL. Status code: {}".format(response.status_code))
