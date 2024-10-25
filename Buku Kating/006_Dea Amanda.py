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
            "https://drive.google.com/uc?export=view&id=1e_bWpaa4B6DI15UgmNa8IQHmOyYFl_NB",
            "https://drive.google.com/uc?export=view&id=1b0FF6uAJ24IJGf5ehEEPZU0UApUGAGp7",
            "https://drive.google.com/uc?export=view&id=1ovUtuohdnq2vudTjmk3xYxxehMuUPUw9",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mOKw2gQ7qg5TW3a28KvCPjPBLqN9Z41W",
            "https://drive.google.com/uc?export=view&id=1yxDgumdy11aBB1K91uZCzedDqWcTujNu",
        ]
        data_list = [
            {
                "nama"	: "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkhasirma",
                "kesan"	: "berkarisma sesuai namanya",  
                "pesan"	:"jadilah pemimpin yang amanah dan sukses selalu "# 1
            },
            {
                "nama"	: "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	: "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	: "berwibawa",  
                "pesan"	:"jadilah pemimpin ya amanah"# 2
            },
            {
                "nama"	: "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	: "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	: "baik, dan humble",  
                "pesan"	:"sukses selalu dan kuliahnya dilancarkan"# 3
            },
            {
                "nama"	: "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	: "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	: "ramah",  
                "pesan"	:"sukses dan semoga cepat lulus"# 4
            },
            {
                "nama"	: "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	: "kalem",  
                "pesan"	:"seomoga amanah"# 5
            },
            {
                "nama"	: "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	: "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	: "profesional",  
                "pesan"	:"semoga amanah dan dapat dipercaya"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qgZivvT27lAv2rAvtqdUCjDHur_2ppE4", #1
            "https://drive.google.com/uc?export=view&id=1qX9gJr-90sSXE7GUewgSCjZBeBhpXGZ-", #2
            "https://drive.google.com/uc?export=view&id=1qUpnn8V6zpAd2FbipnE2-Ha0KWBcNeVY", #3
             "https://drive.google.com/uc?export=view&id=1qlgSYbx3SUI2cTaBoO9GbZtsviIcQI10", #4
            "https://drive.google.com/uc?export=view&id=1qY4my859dtfcXkJRKWAaQGJrxxR0tnU6", #5
             "https://drive.google.com/uc?export=view&id=1qimrCx4Av1CCAyNr0Mjr8Vkpz15YTd9j", #6
            "https://drive.google.com/uc?export=view&id=1rNjJmeZ5fUvSvlrPyOO_JgE7Vp3cJVTy", #7
             "https://drive.google.com/uc?export=view&id=1rQIhwwC6kmliFbvYUCcoHFOi9N7c_3ZJ", #8
            "https://drive.google.com/uc?export=view&id=1rAF8dt5aYjNbuYIetTxN7ssiw4siHpL9", #9
             "https://drive.google.com/uc?export=view&id=15MMrZP6G-iY2uR5kPBb41yWpNIUe9ZzV", #10
            "https://drive.google.com/uc?export=view&id=1qakcRtH8HLeL36-RsPQuXx9B2DARdnR3", #11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity ",
                "sosmed": "@trimurniaa_",
                "kesan": "Kk nia sangat aktif berbicara",  
                "pesan":"semangat terus kuliahnya kakak !!!" #1
            },
            {
                "nama": "Claudhea Angeliani ",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "lampung timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 2
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang ",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jerr asikk",  
                "pesan":"semangat terus kuliahnya kakak !!!" # 4
            },
            {
                "nama": "Feriyadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 5
            },
            {
                "nama": "Mirza yusuf mirzani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 6
            },
            {
                "nama": "Muhammad Farul Aditya  ",
                "nim": "121450156",
                "umur": "22",
                "asal":"surakarta jatim",
                "alamat": "Pahonam",
                "hobi": "ngopi ",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakaknya asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!" # 7
            },
            {
                "nama": "Annisa cahyani surya ",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Jatimulyo",
                "hobi": "baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 8
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobi": "suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 9
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor ",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakaknya asik dibawa ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!" #10
            },
            {
                "nama": "Anisa Dini Amalia ",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobi": "baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12CS_ixDPLoLBOmM3kMKUr7D6u11gWAB9", 
            "https://drive.google.com/uc?export=view&id=14GYINcskw8zBLnKMs4iUJD1f02uo6k_t"
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
                "kesan": "Tegass dan berwibawa",  
                "pesan": "Sukses selalu buat kakak dan makin keren "
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "romance",  
                "pesan": "Semoga makin bersinar seperti namanya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


# Tambahkan menu lainnya sesuai kebutuhan
