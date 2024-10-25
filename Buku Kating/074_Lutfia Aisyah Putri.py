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
            st.write(f"Nama        : {data_list[i]['nama']}")
            st.write(f"NIM         : {data_list[i]['nim']}")
            st.write(f"Umur        : {data_list[i]['umur']}")
            st.write(f"Asal        : {data_list[i]['asal']}")
            st.write(f"Alamat      : {data_list[i]['alamat']}")
            st.write(f"Hobi        : {data_list[i]['hobi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan       : {data_list[i]['kesan']}")
            st.write(f"Pesan       : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bKC-ykh_l08R2NWuhtF2UE9Y7Y3VF1ue",
            "https://drive.google.com/uc?export=view&id=1gvfsEVBB6MgSR4If_HSj6r5P7Dj7pIvC",
            "https://drive.google.com/uc?export=view&id=1pp_pUIWJRFaU0QTpmnk7WCOsIvXuPZ7w",
            "https://drive.google.com/uc?export=view&id=18lcMyhh5Y3AlseTgO3vfev6A-nqjPS1z",
            "https://drive.google.com/uc?export=view&id=1BEAsLc-WGbtBO8PBbYCOVeN8cKAX-q4B",
            "https://drive.google.com/uc?export=view&id=1FHI4xEat25t5jOnVVbl74NQeuF5JDrjr",
            
            
            
        ]
        data_list = [
            {
                "nama"     : "Kharisma Gumilang",
                "nim"      : "121450142",
                "umur"     : "21",
                "asal"     :"Palembang",
                "alamat"   : "Pulau Damar",
                "hobi"     : "Dengar Musik",
                "sosmed"   : "@gumilangkharisma",
                "kesan"    : "Abangnya sangat berkharisma sebagai kahim, sama seperti namanya",  
                "pesan"    :"Semangat sukses terus kuliahnya bang semoga lulus tepat waktu!!!"# 1
            },
            {
                "nama"	    : "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	    : "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	    : "Saya kira bang Pandra angkatan 22",  
                "pesan"	    : "Semangat dan sukses selalu bang"# 2
            },
            {
                "nama"	    : "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	    : "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	    : "Ternyata kak Meliza asprak Strukdat RB kelas saya",  
                "pesan"	    : "Jangan kapok ngajarin error saya yaa kak, tolong dibantu nilai praktikum strukdat saya ya kak hehe :) "# 3
            },
             {
                "nama"	    : "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	    : "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	    : "Ternyatat kakanya urak awak juo",  
                "pesan"	    : "Semangat selalu kak"# 4
            },
            {
                "nama"	    : "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	    : "Kakaknya sedikit pendiem",  
                "pesan"	    : "Semoga selalu bahagia kak"# 5
            },
            {
                "nama"	    : "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	    : "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "Membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	    : "Kakaknyaa asik banget",  
                "pesan"	    : "Semangat selalu kak, semoga lulus tepat waktu kak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1J_uZRi1DHw8CDGgs4zO3HSiuBOoc2CLy",
            "https://drive.google.com/uc?export=view&id=1mMckJxJF_GrBanMoOBKJihKrHcPywJTy",
            "https://drive.google.com/uc?export=view&id=1VWr6kafUHYKqGvt4x7ShiZFXS9zZGMBM",
            "https://drive.google.com/uc?export=view&id=1ez55hjj5HG-xO7RpCI2RRKGMVq6hbwod",
            "https://drive.google.com/uc?export=view&id=11JefDCzF88qhAcBTspu4S9LYWPjFLhFv",
            "https://drive.google.com/uc?export=view&id=1c4MeWGulX6Yzo1rnZ_gDPT43RTNaraKn",
            "https://drive.google.com/uc?export=view&id=1v0-7p4N4Anu6nnrlrh9pzxrCpnhkWUVc",
            "https://drive.google.com/uc?export=view&id=1Kj_fSB5Iei36zWbEHkuL676O0_IhVeub",
            "https://drive.google.com/uc?export=view&id=16nkNwEHyS5k-Wop-IQ8ZEso1IH92b4pP",
            "https://drive.google.com/uc?export=view&id=1R3KM9FKXGTEC_8Tk_zC1lGWJlmiHsdnd",
            "https://drive.google.com/uc?export=view&id=1asy6c7dfYN0oTFUXGPOZHkyNpJlFVWVX",
    
        ]
        data_list = [
            {
               "nama"	    : "Tri Murniya Ningsih",
                "nim"		: "121450038",
                "umur"	    : "21",
                "asal"		: "Bogor",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Searching di perpexcity",
                "sosmed"	: "@trimurniaa_",
                "kesan"	    : "Kak Niya orangnya asiik bangett",  
                "pesan"	    : "Semangat menjelani semester tua kakk"# 1

            },
            {
                "nama"	    : "Annisa Cahyani Surya",
                "nim"		: "121450114",
                "umur"	    : "21",
                "asal"		: "Tangerang",
                "alamat"	: "Jatimulyo",
                "hobi"		: "Baca dan nonton",
                "sosmed"	: "@annisacahyanisurya",
                "kesan"	    : "Kak Annisa style nya kece abis",  
                "pesan"	    : "Minta rekom-rekom style dong kak hehe"# 6
            },
            {
                "nama"	    : "Wulan Sabina",
                "nim"		: "121450150",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@wlsbn0_",
                "kesan"	    : "Kak Wulan ternyata yang ngisi materi di acara Sains Data Mengabdi^^",  
                "pesan"	    : "Sukses selalu kak, semoga magang di telkomnya bisa nular ke saya!",
            },
            {
                "nama"	    : "Anisa Dini Amalia",
                "nim"		: "121450081",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@anisadini10",
                "kesan"	    : "Kakanya mirip Shakira CoC, apalagi kalo lagi nyengir",  
                "pesan"	    : "Semangat selalu kak menjalani tugas baleg dan semester 7"# 6
            },
            {
                "nama"	    : "Claudhea Angeliani",
                "nim"		: "121450124",
                "umur"	    : "21",
                "asal"		: "Salatiga",
                "alamat"	: "Lampung Timur",
                "hobi"		: "Baca jurnal",
                "sosmed"	: "@dylebee",
                "kesan"	    : "Kak Claudhea auranya feminim girl banget ",
                "pesan"	    : "Semangat selalu kak"# 2
            },
            {
                "nama"	    : "Dhea Amelia Putri",
                "nim"		: "122450004",
                "umur"	    : "19",
                "asal"		: "Buleleng",
                "alamat"	: "Natar",
                "hobi"		: "Bercocok tanam",
                "sosmed"	: "@_.dheamelia",
                "kesan"	    : "Ternysts kak Dhea orsngnya lucu",
                "pesan"	    : "Semangat nugasnya kak" # 3
            },
            {
                "nama"	    : "Muhammad Fahrul Aditya",
                "nim"		: "121450156",
                "umur"	    : "21",
                "asal"		: "Surakarta",
                "alamat"	: "Pahoman",
                "hobi"		: "Ngopi",
                "sosmed"	: "@fhrul.pdf",
                "kesan"	    : "Bang Fahrul asik orangnya",  
                "pesan"	    : "Semangat terus menjalani semester tuanya kk"# 6
            },
            {
                "nama"	    : "Feriyadi Yulius",
                "nim"		: "122450087",
                "umur"	    : "20",
                "asal"		: "Sumatera Selatan",
                "alamat"	: "Depan Koban",
                "hobi"		: "Baca buku",
                "sosmed"	: "@fer_yulius",
                "kesan"	    : "Asik banget diasprakin alpro sama bg Feri",  
                "pesan"	    : "Jangan kapok bantuin error alpro saya ya bg, tolong juga nilai praktikum alpro saya bang hehe "# 5
            },
            {
                "nama"	    : "Mirzan Yusuf Rabbani",
                "nim"		: "1224500118",
                "umur"	    : "20",
                "asal"		: "Jakarta",
                "alamat"	: "Korpri",
                "hobi"		: "Membaca",
                "sosmed"	: "@myrrinn",
                "kesan"	    : "Abangnya kalem",  
                "pesan"	    : "Semangat terus bang Mirzan"# 6
            },
            {
                "nama"	    : "Jeremia Susanto",
                "nim"		: "122450022",
                "umur"	    : "20",
                "asal"		: "Balam",
                "alamat"	: "Balam",
                "hobi"		: "Gangguin orang",
                "sosmed"	: "@jeremia_s_",
                "kesan"	    : "Bang Jere orangnya asik random banget apalagi kalo jadi asprak alpro di kelas RB",
                "pesan"	    : "Jangan panik-panikin kalo lagi ngerjain tugas alpro bg, tolong banget amanin nilai pratikum alpro saya ya bg hehe, semoga nilai bg jere juga jadi aman semua dapat A"# 4
            },
            {
                "nama"	    : "Berliana Enda Putri",
                "nim"		: "122450065",
                "umur"	    : "20",
                "asal"		: "BSD, Tangerang Selatan",
                "alamat"	: "Teluk",
                "hobi"		: "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed"	: "@berlyyanda",
                "kesan"	    : "Ternyata kak Berlin asik diajak ngobrol",  
                "pesan"	    : "Semangat selalu kakk"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T8PJm4wcogWFVEZl7TZaXcQkiEVtqZVS", 
            "https://drive.google.com/uc?export=view&id=1VSacP2YJwf6vynfOYpnhR3MCdMpA7ZEB", 
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
