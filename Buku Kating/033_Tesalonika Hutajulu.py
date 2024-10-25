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
            "https://drive.google.com/uc?export=view&id=1zRYxOFHbNRRGTk3UUP138ydkXiWaFWkB",#2
            "https://drive.google.com/uc?export=view&id=169FBdqWC1kpaf4mKY63fT2WuB3CfCLk8",#3
            "https://drive.google.com/uc?export=view&id=1nkPlilRFlKPq0pGaEbNlABW-3STBqNea",#4
            "https://drive.google.com/uc?export=view&id=1OZoBju5VysT0pUE0VXiL8RcwZnS6-Knf",#5
            "https://drive.google.com/uc?export=view&id=1cWc8pDHQ1H-9UVWzgQlP4NV-8m6XNOGw",#6
            "https://drive.google.com/uc?export=view&id=1egr6bZbEdM9G6NdKrch87m9b8V5iP9RR",#7
            "https://drive.google.com/uc?export=view&id=1wssXe2jtdP8HfgQ7aX4LNtTRGYG6NdzK",#8
            "https://drive.google.com/uc?export=view&id=1P6RDs78aJicjEiBFgCcOdJee2uFQ7A3A",#9
            "https://drive.google.com/uc?export=view&id=1Go2oAgpWEqx8VXkzYKBjYX8Asn95B_x7",#10
            "https://drive.google.com/uc?export=view&id=1H2XuyH2O4n_llfKH8Ql1b9XSyOSBEy7k",#11
            "https://drive.google.com/uc?export=view&id=1ygPgLGGlG66hjogkBAbBDvPYfeVPRrFE",#12
            "https://drive.google.com/uc?export=view&id=1xsrq4XEL3PQrbg2a5atR5cYUDwWOZEoT",#13
            "https://drive.google.com/uc?export=view&id=1Jg_qC20ckNd8bl1SDCMBYD1zNrVQkssZ",#14
            "https://drive.google.com/uc?export=view&id=14jjcpgzu2lMPJNyaZ1aR6Sj9dwnozNKe",#15
            "https://drive.google.com/uc?export=view&id=1yoqFufS0P1xJgahg7kY3wcHtIqKMZ1lw",#16
            "https://drive.google.com/uc?export=view&id=1iDv6b644btJ-QgAEmoFjr9CDFcuRjOcj",#17
            "https://drive.google.com/uc?export=view&id=1b41OUsirJEBvvcyw5ZxrDR6EVXLPQnET",#18
            
            
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
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@elisabethh_",
                "kesan": "Kakaknya ngejelasin materi bagus banget",  
                "pesan":"semogaa kakaknyaa bisa cepatt lulus yaa !!!"#2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknyaa cantikk dann menawan",  
                "pesan":"selalu bahagia ya kakk !!!"#3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatra Barat",
                "alamat": "Kemiling",
                "hobbi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "kak Allyaa kerennn",  
                "pesan":"Semoga lancar dann aman terus yaa kakk kuliahnyaa !!!"#4
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobbi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kak inii pintarr dann baik juga",  
                "pesan":"Semoga dipermudahh di semua pekerjaannya ya kak!!!"#5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakakk cantikk dann caree",  
                "pesan":"Semoga selaluuu cantiiii !!!"#6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya perhatiann dan baguss banget menyampaikan materi",  
                "pesan":"Semoga bang ferdiii sehattt dann diberkati teruss yaa !!!"#7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Abangnya kerenn dann berwibawa",  
                "pesan":"Semoga kerjaannya lancar dan bagus terus ya bang !!!"#8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobbi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "senyum kakaknyaa maniss",  
                "pesan":"sehatt dann gembiraa teruss kakk !!!"#9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya kerenn, lucu, imutt dan juga menyenangkan",  
                "pesan":"Semoga tugas tugass nya di kampuss selalu dipermudah bangg !!!"#10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya kerenn, baik dan aktiv di semua bidang",  
                "pesan":"semogaa baikk teruss ya bang !!!"#11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (kojo)",
                "hobbi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya jago ngoding banget",  
                "pesan":"Semoga styling skena nya tercapai !!!"#12
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekan Baru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya baikkk",  
                "pesan":"Semoga doa doanya terkabul!!!"#13
            },           
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya kerennn bisa main gitar",  
                "pesan":"Semoga tugas tugass nya di kampuss selalu dipermudah dann aman selalu !!!"#14
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Muliaa sekalii suka menolong ",  
                "pesan":"semogaa hobbi menolong nyaa keterusan ya bangg !!!"#15
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakak inii kecee sekalii",  
                "pesan":"Semoga bisa berenang bareng nanti!!!"#16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya ramahh",  
                "pesan":"Semoga setiapp perjalanan nya selalu Happy!!!"#17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kakaknya keceee",  
                "pesan":"Semoga minat bacanya nular ke aku ya kak!!!"#18
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
            "https://drive.google.com/uc?export=view&id=1l3Z4HNZTUiYrZhdyUg-rNwj1DK-yVkV-",#9
            "https://drive.google.com/uc?export=view&id=1aAZYKWJ24PkUjX0HHc9foIrNap2YLZl9",#10
            "https://drive.google.com/uc?export=view&id=1aE7G4CVwsa75WiMnN9OjcmDa0xnzbBOn",#11
            "https://drive.google.com/uc?export=view&id=1bQ1GaDvIjpB0aFMAkcv04K85-xiWy1dC",#12
            "https://drive.google.com/uc?export=view&id=1putwiQaFre2kW9CzzdP2RsPy_eNUhgq7",#13
                     
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
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya sangatt tinggi",  
                "pesan":"Semoga jadi gamers keren !!!"#4
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "kakak ini aktiv di banyak hal",  
                "pesan":"Semoga nilai nilainya bagus terus ya kakk !!!"#5
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "keren sekali kakaknya hobbi belajar",  
                "pesan":"moga aja hobbi nya nular ke aku ya kakk !!!"#6
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kak etaa jago musikk keren",  
                "pesan":"semogaa sehatt dan jaya terus kak !!!"#7
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "seny",  
                "pesan":"Semoga kerjaannya lancar terus ya bang !!!"#8
            },
                        {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknyaa terlihat telatenn dan baik",  
                "pesan":"Semogaa semester ini bisa berjalan lancar buat kakak ya !!!"#9
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobbi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Abangnya berwibawaa",  
                "pesan":"lancarr terus ngodingnya bang !!!"#10
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobbi": "Riview Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakanyaa ramahh dan pintar public speaking",  
                "pesan":"Semoga kepintarannya bisa ke aku jugaa ya kakk !!!"#11
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya baikk dann pintarr bangett",  
                "pesan":"Mau juga cerdas kaya abangnya !!!"#12
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "121450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya rajinnn bett",  
                "pesan":"semoga dapat tutor rajin dari abangnya !!!"#13
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17nVnjVFcHwgClFValnwvBXv0R-N2VmUz",#1
            "https://drive.google.com/uc?export=view&id=1caiU_wRF07cozdohUmcMEt9SsieSvjJx",#2
            "https://drive.google.com/uc?export=view&id=1ouJfiz9IgNr78oLo1pWdI4jfbPUTGOIj",#3
            "https://drive.google.com/uc?export=view&id=1TAPT9Cnh3VerHCjJhR1RYAyDh4EIoqLU",#4
            "https://drive.google.com/uc?export=view&id=1Iu_NE8OwmfYwoj2U3W8iwC_6qqryEPrU",#5
            "https://drive.google.com/uc?export=view&id=1kkGmbnxsYW-nDJPmDQVU5YY-CSjIJisD",#6
            "https://drive.google.com/uc?export=view&id=1Bg3dSz69elF8do0IDzePfKp6LhGJ4uzM",#7
            "https://drive.google.com/uc?export=view&id=1kJcRQH1OZmtwAG5bTBnbtJyUfrJKc1Jx",#8
            "https://drive.google.com/uc?export=view&id=19YWpyXrDLAkj_MX5GMdFHCUyi1HFG8so",#9
            "https://drive.google.com/uc?export=view&id=1PHgIbDIS68u6lG5aaUwUxuPLclFEZLis",#10
            "https://drive.google.com/uc?export=view&id=1AtIDVYh-KHd2BEf2ncCq97nGfcEr7rIQ",#11
            "https://drive.google.com/uc?export=view&id=1Bn07d2y7_hyRrd713nW9eLscj07OVLTz",#12
            "https://drive.google.com/uc?export=view&id=1xzhHBtAQmaG_AxMML4KV8OPmcbQ7yrrw",#13
            "https://drive.google.com/uc?export=view&id=1n5jUrvFUhufhXxWan0-6Kw4mDeJpqeOM",#14
            "https://drive.google.com/uc?export=view&id=1F4M8cwz6lOraaRSRe4EZ7_A5si-VdMeH",#15
            "https://drive.google.com/uc?export=view&id=1u0ck2ElKC8c6aPC5QBV81JFuSJ0ZbQZe",#16
            "https://drive.google.com/uc?export=view&id=1xXraWYGAW-qQR5xxko2A-myCzlXmDP4O",#17
            "https://drive.google.com/uc?export=view&id=1hwDK3gR9CCw5JwJdsSvrVzQbB7JouHnM",#18
            "https://drive.google.com/uc?export=view&id=1CppmGUwpKbpgOLP-onLxSyAEnZLuhiWk",#19
            "https://drive.google.com/uc?export=view&id=1xaUzqDJ-JRiqe3sHpDbonzUx3NQHYeo7",#20

        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@yogyyyyyyy",
                "kesan": "Abangnya humoriss tapi berwibawa",  
                "pesan":"lancar terus ya bang jadi kadepp !!!"#1
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya terlihat tegass tapi baik kok",  
                "pesan":"lsemogaa lancar ya kak jadi sekertaris eksternal !!!"#2
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Suara kakaknya lembuttt sekalii",  
                "pesan":"semoga lancar teruss kuliahnya ya kak !!!"#3
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobbi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang inii tinggi bett",  
                "pesan":"semogaa semangat terus di hublu !!!"#4
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya terlihat tegass tapi baik kok",  
                "pesan":"lsemogaa lancar ya kak jadi sekertaris eksternal !!!"#5
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Suara kakaknya lembuttt sekalii",  
                "pesan":"semoga lancar teruss kuliahnya ya kak !!!"#6
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobbi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Abangnya humoriss tapi berwibawa",  
                "pesan":"lancar terus ya bang jadi kadepp !!!"#7
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=138xazlvnfHz5RkUhbg8SSnYMA-SOAwky",#1
        "https://drive.google.com/uc?export=view&id=17BIwu96P7aSE3MtFRMmHJ-iUHxlyVkIA",#2
        "https://drive.google.com/uc?export=view&id=1s62MuQL6HSTLYCe-qJUQBx_e5Mhl5B99",#3
        "https://drive.google.com/uc?export=view&id=12WTXpxYpn8jwfixA9XbtgPgQQ-1daTy-",#4
        "https://drive.google.com/uc?export=view&id=1_8_sRnfDGDhkKCnprzAzZyT72i1rN2G6",#5
        "https://drive.google.com/uc?export=view&id=1_8_sRnfDGDhkKCnprzAzZyT72i1rN2G6",#6

        ]
        data_list = [
            {
            "nama": "Dimas Rizky Ramadhani",
            "nim": "121450027",
            "umur": "20",
            "asal": "Pamulang, Tangsel",
            "alamat": "Way Kandis (Kobam)",
            "hobi": "Manjat Tower Sutet",
            "sosmed": "@dimzrky_",
            "kesan": "Keren banget dan asik",
            "pesan": "Sehat dan semangat kuliahnya bang"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "Lucu dan cantik",
            "pesan": "Semangat kuliahnya kak"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "Keren dan asik orangnya",
            "pesan": "Semangat kuliah abang"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Rajabasa",
            "hobi": "Denger musik",
            "sosmed": "@ranniu",
            "kesan": "Keren dan seru banget",
            "pesan": "Semangat dan sehat selalu kak"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "Lucu dan keren",
            "pesan": "Semangat kuliah dan ngaspraknya bang"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "Asik kakaknya",
            "pesan": "Semangat dan semoga keren selalu"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "Asik abangnya",
            "pesan": "Semoga cepat lulus dan semangat abang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "Lucu dan asik",
            "pesan": "Semangat kakak buat kuliahnya"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "Asik dan informatif",
            "pesan": "Semangat bang buat kuliahnya"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "Keren dan asik",
            "pesan": "Semangat kuliah"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "Asik dan keren",
            "pesan": "Semangat ya bang kuliahnya"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "Keren kakaknya",
            "pesan": "Semangat kakak kuliahnya"
        },
    ]
        display_images_with_data(gambar_urls, data_list)
    internal()

# Tambahkan menu lainnya sesuai kebutuhan

