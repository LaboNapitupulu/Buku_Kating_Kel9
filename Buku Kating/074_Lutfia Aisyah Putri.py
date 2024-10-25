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

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10aJ6XJ53etZlmOTIj3N_PtbtnHhllX2x", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1ZAH6_tgZUpy679hUBmgsPdc1LZw-90zW", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1wWXm_8edhA-lncVM6TOxeT02CxtipTYC", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1ci4JpuQmu_XTpKObwJipvs8c0EqyRdtp", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1ffvp-xkP44fcg5rEkSqrEPW8DQPIMGr2", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1tppR50lKy1NhS_LnMcUGO-VfPrf_GBj2", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1RUaqKpDXZoQ8pyxJXnZkSa7QsR4HTUpj", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1H_WDjiYFDKCsiQuIcTCwjoBAGVdlje1j", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1nxUwX8N-x6nHIGduHzaxZdX0XHj7Pcnt", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1hm_8shp4zf_QQgFJ4qx9ZwwHsQkTACvQ", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1MAV2-WYqZZvYkXSU_vyEeEajINYJiI1v", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1eqO0e3sD9aGe6N1z1-ZVGL8Ixep2yaWX", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1_TPyjznN5ezmoqNdFX0erhMublD439l3", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1dyKQvH_TvaEozJ-i2dZUZOFPit1XJAlh", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1Aas_m1rNvP1Nozx8Gc2tVHzm-dk3gBvh", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1Y5RNrjE-9WT1Vc4EHspGr63VAY05nben", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=17bXjoBsx3XTKbP_DIL4wCh8biBpJtZmX", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1pCWEN8OY5L8ZR9jLWfuF_LlJJwe4yEug", #Kak Dini
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobi": "Travlling",
                "sosmed": "@ericsonchandra99",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "",
                "sosmed": "@allyaislami_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "",  
                "pesan":""
            },
                        {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RyClBWDlhq3IuJqC7pEz6qtEpChyr3lX", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1VHxnMk3xhFiOGhbcM5i_RExqNXp-P_iX", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1DIdpoOokhnDwt820eEoMCekB8PymRil8", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=1qijYN3DnNr-QYQc2zfcun0j6BR-zaiun", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1bAcfVXfRvA0OT-O7jWDzuTd3-EFVprNc", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1pymHQ8pB2_5-Q2L8xGgCP73qD_aTKLc3", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1Ic_fHbRtHuscLJ-WFPMxLuhiqnJcp-Dv", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=15cFweZi2EaOksvZlK0z1eCi-TEQQul1O", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1TF30hRACOm_nrr5_0Mkg6xTHZF1c_hnK", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1AhWof85tQHvHaTZyZkpJjLsrtU-Mu08K", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1bQQO3dqG1b0EfuKsvcxKlW4sgAuFAXgf", #Bang Randa ok
        ]
        data_list = [
            {
                "nama": "Rafi Fadhlillah",
                "nim": "121450143",
                "umur": "21",
                "asal":"Lubuk Linggau",
                "alamat": "Jl. Nangka 4",
                "hobi": "Olahraga",
                "sosmed": "@rafadhlillahh13",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "",  
                "pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

# Tambahkan menu lainnya sesuai kebutuhan
