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
        st.image(load_image(url), use_column_width="True", width=350)
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
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
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
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #dea
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Ale
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Nadya
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Tesa
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Efi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Lutfia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Lia
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Rafi
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Aisyah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Ariel
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Fikri
        ]
        
        data_list = [
            {
                "nama": "Labo Napitupulu",
                "sebagai": "Pak Lurah",
                "nim": "123450037",
                "fun_fact": "Metabolimse tergolong cepat",
                "motto_hidup": "Jangan meninggal sebelum ke Banda Neira",
            },
            {
                "nama": "Dea Amanda",
                "sebagai": "Bu Lurah",
                "nim": "123450006",
                "fun_fact": "belibet ngomong E",
                "motto_hidup": "hidup cuma sekali",
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
            
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
