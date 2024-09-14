import streamlit as st
from streamlit_option_menu import option_menu # type: ignore
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width=True, width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>This Is Uniform</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Uniform adalah kelompok kaderisasi HMSD Adyatama ke-9. Nama "Uniform" berasal dari distribusi seragam dalam statistika, 
            di mana setiap hasil memiliki peluang yang sama untuk terjadi. Ini mencerminkan prinsip kesetaraan dan keadilan, 
            dengan kata lain setiap anggota kelompok memiliki peran yang sama pentingnya, 
            dan setiap ide serta kontribusi dianggap setara..</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1Rnu9pJsPjzRTbWu901GfM0dxFFRp3os0"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Meski setiap anggota memiliki peran yang berbeda, 
            semua bersatu dalam satu tujuan, seperti halnya distribusi seragam yang memberikan peluang yang sama untuk setiap nilai. Ini menekankan pentingnya kerja sama dan sinergi dalam mencapai hasil yang optimal dalam sebuah tim. Meskipun kami adalah kelompok terakhir, 
            tapi kami percaya dengan kata-kata "Save the best for the last". This is Uniform. Unity of Many Form.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QEBEvPJpvsnVDdIe7Vlxv8bhRKO6G9iP", #labo
            "https://drive.google.com/uc?export=view&id=1dY7vnoPEeLtA_VEyQpT8m2fvjj2Azm0v", #dea
            "https://drive.google.com/uc?export=view&id=1tVijdOoz6T6sC2hJWcE27zb4FO8pd0gO", #Ale
            "https://drive.google.com/uc?export=view&id=1hRD_DucFPJPTgZBscZNyNOxwaB1KTQ-I", #Nadya
            "https://drive.google.com/uc?export=view&id=17Q_PJzifqxHsLF5vr5TJNrf7O58mH20e", #Tesa
            "https://drive.google.com/uc?export=view&id=1S_FtbEO8iQGvyUZ9hp3M19aDvToLr9Zs", #Efi
            "https://drive.google.com/uc?export=view&id=1wKuzDS0oQfb9GL6LBub7kKKp1LscBCPf", #Lutfia
            "https://drive.google.com/uc?export=view&id=1ih4tjMqUAhyA6wPibNUkhq_J_f7HJAfi", #Lia
            "https://drive.google.com/uc?export=view&id=16Vhr7cRwiSWHD8CIN63h0EByJPIIdgEt", #Rafi
            "https://drive.google.com/uc?export=view&id=1GCl8uI-GB7tcHypdhEoBt5Y4ZxWxapGM", #Aisyah
            "https://drive.google.com/uc?export=view&id=1gcAZp0gojhbMgs7bS-3bK6fOHsvZMMFC", #Ariel
            "https://drive.google.com/uc?export=view&id=1yXw5sa22zovTeaO0fy5SJFRkXBM-IxT6", #Fikri
        ]
        
        data_list = [
            {
                "nama": "Labo Napitupulu",
                "sebagai": "Pak Lurah",
                "nim": "123450037",
                "fun_fact": "Metabolisme tergolong cepat",
                "motto_hidup": "Jangan meninggal sebelum ke Banda Neira",
            },
            {
                "nama": "Dea Amanda",
                "sebagai": "Bu Lurah",
                "nim": "123450006",
                "fun_fact": "belibet ngomong E",
                "motto_hidup": "Hidup cuma sekali",
            },
            {
                "nama": "Aliya Ammara Ananta",
                "sebagai": "Anggota",
                "nim": "123450075",
                "fun_fact": "menghapal sangat cepat",
                "motto_hidup": "semangat terus sampai mampus",
            },
            {
                "nama": "Nadya Ratu Anjani",
                "sebagai": "Anggota",
                "nim": "123450083",
                "fun_fact": "tidak bisa mengendarai sepeda",
                "motto_hidup": "just keep pushing, just keep pushing",
            },
            {
                "nama": "Tesalonika Hutajulu",
                "sebagai": "Anggota",
                "nim": "123450033",
                "fun_fact": "ga bisa coding tapi masuk data",
                "motto_hidup": "jalanin dulu",
            },
            {
                "nama": "Efi Defiyati",
                "sebagai": "Anggota",
                "nim": "123450005",
                "fun_fact": "mengarang cerita sebelum tidur",
                "motto_hidup": "jalanin aja atau jalan-jalan",
            },
            {
                "nama": "Lutfia Aisyah Putri",
                "sebagai": "Anggota",
                "nim": "123450074",
                "fun_fact": "Panikan level akut",
                "motto_hidup": "Terwujud tidak terwujud, tetaplah bersujud",
            },
            {
                "nama": "Lia Hana Ichisasmita",
                "sebagai": "Anggota",
                "nim": "123450089",
                "fun_fact": "Pengamat yang baik",
                "motto_hidup": "Ikuti alurnya, nikmati prosesnya",
            },
            {
                "nama": "Rafi Diva Efangga",
                "sebagai": "Anggota",
                "nim": "123450001",
                "fun_fact": "suka gabut tengah malam",
                "motto_hidup": "selalu bersyukur apapun yang terjadi",
            },
            {
                "nama": "Aisyah Musfirah",
                "sebagai": "Anggota",
                "nim": "123450084",
                "fun_fact": "ENTJ tapi introvert",
                "motto_hidup": "Focus on your study and make Joshua proud",
            },
            {
                "nama": "Arielva Simon Siahaan",
                "sebagai": "Anggota",
                "nim": "123450105",
                "fun_fact": "ujian ya sks",
                "motto_hidup": "dengan sks dapatkan nilai a",
            },
            {
                "nama": "Abdillah Fikri Al Pome",
                "sebagai": "Anggota",
                "nim": "123450062",
                "fun_fact": "saya bisa berjalan",
                "motto_hidup": "jangan sombong aee",
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
