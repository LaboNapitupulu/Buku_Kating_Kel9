import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
            "Departemen MEDKRAF",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobi: {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iOQLQe7biXtCxRuYXmyMa1vRTHE8ojM_",
            "https://drive.google.com/uc?export=view&id=1dLzo4Am4yobPY-jAMXT5KukNpNol5uP6",
            "https://drive.google.com/uc?export=view&id=1hJIz9KdSIt4xhkQsdy3yBRhGXOkLdcT9",
            "https://drive.google.com/uc?export=view&id=14kQFzU_QcbOJgwhGg7RWAipDfWR-tQNS",
            "https://drive.google.com/uc?export=view&id=1iY5fptVh8QtVo1OWxmJLimp8yq6HbWa0",
            "https://drive.google.com/uc?export=view&id=1vETWfqKdLBQo4kDiCoQ_5jOWIo3ecizR",

        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar ",
                "hobi": "Main Bola, Belajar",
                "sosmed": "@gumilsngkharisma",
                "kesan": "Abang ini tegas banget",  
                "pesan":"Semangat ya bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jalan Bawean 2, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Wah tetangga saya",  
                "pesan":"Semangat ya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Cantik euy",  
                "pesan":"Semangat nyekre nya"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Jalan Nangka IV",
                "hobi": "Dengarin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "1121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "-",  
                "pesan":"-"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Membaca",
                "sosmed": "nadillaandr26",
                "kesan": "-",  
                "pesan":"-"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VGLljCBu1W4FlHJmaZUAwSMoCKf-xrZ3",
            "https://drive.google.com/uc?export=view&id=1p1HvT0_NwCFiEwYEeall1AMv3QV_Wf5E",
            "https://drive.google.com/uc?export=view&id=1cTPnjWmbijw2No1nYk_OC-vE2GluRpDW",
            "https://drive.google.com/uc?export=view&id=11hi02LB-SdI9ej9BXbCZmsec2UMvAGcF",
            "https://drive.google.com/uc?export=view&id=1tfcp_NHfqJrgUgD8_nexVtv0XDQUyC2J",
            "https://drive.google.com/uc?export=view&id=14N-C2x-y8puLO9Rh0Xb4g6w6kKhJke1O",
            "https://drive.google.com/uc?export=view&id=142SZI0IjVt7lKhK5AYzWL3Py2Nz-fIbI",
            "https://drive.google.com/uc?export=view&id=1k2ZwZlnlsUdQHRhGukrz75bKHMsNRps4",
            "https://drive.google.com/uc?export=view&id=1pufL9stOQVwQgl0_UAA7GtbD0nqqPtUW",
            "https://drive.google.com/uc?export=view&id=1P0_R6vL0hWmA4Bf3n8jLcQkC27Mz0P16",
            "https://drive.google.com/uc?export=view&id=1Oi39BhNnLrQ4U1ki3l2R5wUrGILi9o--",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal": "Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Depan kobam",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Mirza Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "BSD",
                "alamat": "Teluk",
                "hobi": "Buka liat linked in, puasa senin kamis, ngerjain tugas di draw.io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal": "Malang",
                "alamat": "Jatiagung",
                "hobi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!"
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e1cQfiQrwWICHfv2kqw5iqefkla0BexY", 
            "https://drive.google.com/uc?export=view&id=19WN-RUENVRbBwJd_luWJNJKekNKQUb3I", 
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450098",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu Indomaret",
                "hobi": "Nyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "",  
                "pesan":""
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
