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
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
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
            "https://drive.google.com/uc?export=view&id=1cFmuGqperuTRHJ7cMD6ooo9x2I83Pp0L",#1
            "https://drive.google.com/uc?export=view&id=14QBFjd1tiMuNYys5FqIQppx4VPdnXWaJ",#2
            "https://drive.google.com/uc?export=view&id=18yEvp-IlXURqIrqbMFCir2wZxI_cWnRp",#3
            "https://drive.google.com/uc?export=view&id=1QTqYfHsNDSx6s-HrwvhoYi9Ce7oFoEcE",#4
            "https://drive.google.com/uc?export=view&id=1UtEQpAc9SydjSSndhxjBCaxF6rH9-of8",#5
            "https://drive.google.com/uc?export=view&id=1jbfoGRMKjPqMtSyRZe6JWX988QoNo11N",#6
        ]
        data_list = [
            {
                "nama"    : "Kharisma Gumilang",
                "nim"     : "121450142",
                "umur"    : "21",
                "asal"    :"Palembang",
                "alamat"  : "Pulau Damar",
                "hobbi"   : "Dengar Musik",
                "sosmed"  : "@gumilangkhasirma",
                "kesan"   : "Bang gumilang begitu berwibawa",  
                "pesan"   :"semangat selalu ya bang !!!"#1
            },
            {
                "nama"    : "Pandra Insani Putra Azwar",
                "nim"     : "121450137",
                "umur"    : "21",
                "asal"    :"Lampung Utara",
                "alamat"  : "GJl. Bawean 2, Sukarame",
                "hobbi"   : "Main Gitar",
                "sosmed"  : "@pndrinsni27",
                "kesan"   : "abangnya sangat asik",  
                "pesan"   :"semoga dapat A terus !!!"#2
            },
            {
                "nama"    : "Meliza Wulandari",
                "nim"     : "121450065",
                "umur"    : "20",
                "asal"    :"Pagar Alam",
                "alamat"  : "Kota baru",
                "hobbi"   : "Drakoran",
                "sosmed"  : "@wulandarimeliza",
                "kesan"   : "kakaknya cantikk dan baik",  
                "pesan"   :"semoga kuliahnya berjalan lancar !!!"#3
            },
            {
                "nama"    : "Hartiti Fadilah",
                "nim"     : "121450031",
                "umur"    : "21",
                "asal"    :"Palembang",
                "alamat"  : "Pemda",
                "hobbi"   : "Nyanyi",
                "sosmed"  : "@hrtfdlh",
                "kesan"   : "Kakak nya imut",  
                "pesan"   :"semangat kakk !!!"#4
            },
            {
                "nama"    : "Putri Maulida Chairani",
                "nim"     : "121450050",
                "umur"    : "21",
                "asal"    :"Payakumbuh",
                "alamat"  : "JL. Nangka IV",
                "hobbi"   : "Dengarin Bang Pandra gitaran",
                "sosmed"  : "@ptrimaulidaaa_",
                "kesan"   : "Kakak ini asik saya suka belajar dengan dia",  
                "pesan"   :"Lancar terus kerjaanya ya kak !!!"#5
            },
            {
                "nama"    : "Nadilla Andhara Putri",
                "nim"     : "121450003",
                "umur"    : "21",
                "asal"    :"Metro",
                "alamat"  : "Kota baru",
                "hobbi"   : "Membaca",
                "sosmed"  : "@nadillaandr26",
                "kesan"   : "Kakak nya manis",  
                "pesan"   :"semoga nailainya baguss terus jugaa !!!"#6
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fti-1_bOFAahEPNRcUteFut9ady_oGS5",#1
            "https://drive.google.com/uc?export=view&id=1fkmYmpuVnwN7EeRUqHdTchfGyXS1fmQG",#2
            "https://drive.google.com/uc?export=view&id=1fH5dxUi8eBhIYJFM8Y577vHRRH9lC6jj",#3
            "https://drive.google.com/uc?export=view&id=1fmfjpD30ac4YisaP3f7lVnUCwMTXMf0c",#4
            "https://drive.google.com/uc?export=view&id=1fnP8iw6POjmCnCc1UQNR1tpU0UKlb9_x",#5
            "https://drive.google.com/uc?export=view&id=1ftxUlVtUGDH1XsiYVhWapZ3o-bQeemMK",#6
            "https://drive.google.com/uc?export=view&id=1faaP_9HiI87BQ3ZlB8QIiF5zV7k-Sgw9",#7
            "https://drive.google.com/uc?export=view&id=1fruR889t4X1PcSp3hUYbKlvySQsZJ5nN",#8
            "https://drive.google.com/uc?export=view&id=1flUxAQuW0X0D1gifhIrzqMF_qM1tQKAh",#9
            "https://drive.google.com/uc?export=view&id=1fpev7CULyljGO1odDn2w05Bg1NE1XjzN",#10
            "https://drive.google.com/uc?export=view&id=1fcKxt1QOwRxvYRmaKYbLIxa9dbqMK-Vo",#11
            
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak nya imut dan baik",  
                "pesan":"semangat yaww kak !!!"#1
            },
            {
                "nama": "Annisa cahyani surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"tangerang",
                "alamat": "jatimulyo",
                "hobbi": "baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakaknya ramah dan cerdas",  
                "pesan":"semoga cepat tercapai impiannya !!!"#2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "kakaknya pintarr banget",  
                "pesan":"sukses selalu kak !!!"#3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"malang",
                "alamat": "jati agung",
                "hobbi": "baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak nya sangat baik dan pintar",  
                "pesan":"sukses dan jaya terus kak !!!"#4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakaknya ramah",  
                "pesan":"ramah dan manis terus ya kak!!!"#5
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya baikkk bangett",  
                "pesan":"baikk teruss ya kakk !!!"#6
            },
            {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"surakarta jatim",
                "alamat": "pahoman",
                "hobbi": "ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya baik dan ganteng",  
                "pesan":"jaya terus bang !!!"#7
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"sumsel",
                "alamat": "depan koban",
                "hobbi": "baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abangnya sangat supportif",  
                "pesan":"semoga dapat nilai sempurna semester ini !!!"#8
            },
            {
                "nama": "Mirza yusuf mirzani",
                "nim": "122450118",
                "umur": "20",
                "asal":"jakarta",
                "alamat": "korpri ",
                "hobbi": "main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya baik dan ganteng juga",  
                "pesan":"semoga cepat lulus nantinya !!!"#9
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya sangat rajin",  
                "pesan":"semoga rajinnya nular ya bang !!!"#10
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD",
                "alamat": "teluk",
                "hobbi": "suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak nya cantikk ",  
                "pesan":"semoga cepatt sukses ya kak !!!"#11
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#1
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#2
            
        ]
        data_list = [
            {
                "nama": "Anissa Luthfi Alifia",
                "nim": "121450098",
                "umur": "22",
                "asal":"Lampung Tengah",
                "alamat": "Kost Putri Rahayu Indomaret",
                "hobbi": "Nyanyi",
                "sosmed": "@anissaluthfi_",
                "kesan": "Kakaknya sangat inspiratif",  
                "pesan":"semoga tugas akhirnya lancar terus ya kak !!!"#1
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#2
            },        
            
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YuljW_UEySLJ-mYxR7whZPPJn3eGOOSz",#1
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#2
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#3
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#4
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#5
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#6
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#7
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#8
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#9
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#10
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#11
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#12
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#13
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#14
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#15
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#16
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#17
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#18
            
            
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#2
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#3
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#4
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#5
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#6
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#7
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#8
            },
                        {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#9
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#10
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#11
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#12
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#13
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#14
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#15
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#16
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#17
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pp6v77Yo8C5l-ff4AJVVnW73jJIe69UZ",#1
            "https://drive.google.com/uc?export=view&id=1or-78AsXmgDh6pQq1BX_KLa7rMCjyto0",#2
            "https://drive.google.com/uc?export=view&id=1gbeAbVa0RQDdzeLH6mOTwwYPvBadK94W",#3
            "https://drive.google.com/uc?export=view&id=1yKVyAMiY19pW-_8YnPez16SvrLPWScuT",#4
            "https://drive.google.com/uc?export=view&id=1kdwQPQ3KNrnIgPWFBUzb619fTz6xV4KW",#5
            "https://drive.google.com/uc?export=view&id=16bdwFNwKW2v5fXS2N0QHvV2ztptGvvUT",#6
            "https://drive.google.com/uc?export=view&id=1LYoG9jPLT2odXgp9lKTTarRiJ0ouGTc0",#7
            "https://drive.google.com/uc?export=view&id=1L7ay3gqw3jMtcwg_ob-cigxSx6irYQ1o",#8
            "https://drive.google.com/uc?export=view&id=1l3Z4HNZTUiYrZhdyUg-rNwj1DK-yVkV-",#9baru done disini
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#10
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#11
            "https://drive.google.com/uc?export=view&id=17EQI3v7U1_jatAhjcvUQ01-SfC1IiDdh",#12
            "https://drive.google.com/uc?export=view&id=1YfH3GzFhIUqXhOXb-S6KIDSMy7Pym40M",#13
                     
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobbi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "Abangnyaa care dan baikk banget",  
                "pesan":"semogaa lancar terus urusannya ya bang !!!"#1
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakakknyaa pintarrr bett",  
                "pesan":"Semogaa hobbi nyaa berjalan terus !!!"#2
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya baik sekali mengajari",  
                "pesan":"baik teruss ya bangg !!!"#3
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#4
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#5
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#6
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#7
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#8
            },
                        {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#9
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#10
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#11
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "22",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abangnya kerenn",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#12
            },
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abangnya tegas dan baik",  
                "pesan":"Semoga setiap step yang diambil berjalan lancaar !!!"#13
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

# Tambahkan menu lainnya sesuai kebutuhan

