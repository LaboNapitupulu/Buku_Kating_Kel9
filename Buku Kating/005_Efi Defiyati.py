import streamlit as st
from streamlit_option_menu import option_menu # type: ignore
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
            "https://drive.google.com/uc?export=view&id=1fvT0zX5JSIJarhL1w20v2Vxydnr4t6f6",
            "https://drive.google.com/uc?export=view&id=1gpzXhQqTal4QMz8n_7-qPp_HX8Kkn5Y8",
            "https://drive.google.com/uc?export=view&id=1gxgLxHUhP_UoJW5X8JNBa6EtWF6zKlw1",
            "https://drive.google.com/uc?export=view&id=1gqBmC_OIUcSZfynv6zMMznH_WCyR3HkI",
            "https://drive.google.com/uc?export=view&id=1glQaLaHMIm4Wvt9laybHa4d0xhjuY4Ho",
            "https://drive.google.com/uc?export=view&id=1gnrcPtts5xTlmE-2ni254VqLN22YxNQ6",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Denger Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Bang Gumilang orangnya tegas dan asik, serta berwibawa",  
                "pesan":"Semoga sukses dan dimudahkan untuk cepat lulus"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Keren banget pas pertama kali tau kalo abang jadi SEKJEN",  
                "pesan":"Semangat buat kuliah, semoga cepet lulus"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota Baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak keliatanyan orang yang bener-bener sibuk gitu",  
                "pesan":"Semangat buat kakaknya, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Jl. Nangka IV",
                "hobi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa",
                "kesan": "Sama kaya kak Meliza, kakak kelihatan kaya sibuk banget ",  
                "pesan":"Semangat terus ya kak, semoga kuliahnya lancar"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Pertama kali ngira kakak orangnya pendiem",  
                "pesan":"Semangat terus kak, semoga kuliahnya cepet selesai dan lancar"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ceria dan asik banget",  
                "pesan":"Semangat buat kak Nadilla, semoga sukses !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gZUhWgalH7N9O5QfIt76SuTJz-vA-abJ",
            "https://drive.google.com/uc?export=view&id=1gMJVGwL0dE99oIpvTdix44klkOmJJN2m",
            "https://drive.google.com/uc?export=view&id=1g3sUuy6GdHKA5QqfVLhclTdxkWskoCUF",
            "https://drive.google.com/uc?export=view&id=1geika8xMp7BPDrLbenLHUg1J3UqS2HOl",
            "https://drive.google.com/uc?export=view&id=1fwMSdL_xd0ofPtzUGK3aYtl_CHXDB7DO",
            "https://drive.google.com/uc?export=view&id=1g7BYSADN56inEIe3SzYqhECspOwUI5Wa",
            "https://drive.google.com/uc?export=view&id=1gHOgTnBtHDcJ6_2q7lNrmsexuw2nfF24",
            "https://drive.google.com/uc?export=view&id=1gGEzSdQr-el2yBHKfeUfV9z67epcFoDG",
            "https://drive.google.com/uc?export=view&id=1gkTql5E06xpdXJSEKu3AKX8XhooJuDcG",
            "https://drive.google.com/uc?export=view&id=1g6G2Nkwv01CLHcMyVVLjm_ByO4P9DcQ7",
            "https://drive.google.com/uc?export=view&id=1gVJiNXzcNm_4t3epbgbW77kWlgCSPjkG",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perpexicity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak lucu dan membawa energi positif",  
                "pesan":"Semangat terus, semoga lancar kuliahnya, dan sukses buat kakaknya"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Lucu banget, suka sama outfit kakak",  
                "pesan":"Semangat buat kakaknya, spill outfit lucu lucu kakak"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak positive vibes banget dan keliatan orang pinter hehheh",  
                "pesan":"Semangat kak kuliahnya, semoga tahun ini langsung lulus"# 1
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@anisadini10",
                "kesan": "Pertama kali ngeliat kaya engga asing, ternyata mirip Shakira di COC",  
                "pesan":"Semangat kuliah kak, sukses selalu"# 1
            },
             {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Ternyata kita se Kabupaten hehhehe, kakak lucu, outfitnya juga lucu",  
                "pesan":"Semangat ngampus kak, semoga lancar kuliahnya"# 1
            },
             {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok Tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak lucu banget, dan asik",  
                "pesan":"Semangat kuliah kak, semoga lancar kuliahnya"# 1
            },
             {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang asik banget orangnya",  
                "pesan":"Semangat kuliah bang, sukses selalu"# 1
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya aga sedikit kalem, tapi asik",  
                "pesan":"Semangat kuliah bang"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya lucu dan pendiam orangnya",  
                "pesan":"Semangat kuliah bang, sukses selalu"# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Seperti biasa tidak bisa diam orangnya",  
                "pesan":"Sehat selalu bang, abang satu ini sibuk banget, semangat kuliah dan sukses buat bang jere"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD Tangerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linkedln, puasa senin kamis, dan ngerjain tugas draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya keliatan pendiem",  
                "pesan":"Semangat ngampus dan sukses buat kakaknya"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
