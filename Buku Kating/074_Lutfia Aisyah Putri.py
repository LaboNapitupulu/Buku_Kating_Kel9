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
                "pesan":"semangat bang"
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
            "https://drive.google.com/uc?export=view&id=1ZaZkJtoUKBZv9EKChp8DbdAi6UMDQIaJ", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1RUaqKpDXZoQ8pyxJXnZkSa7QsR4HTUpj", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1H_WDjiYFDKCsiQuIcTCwjoBAGVdlje1j", #Bang Deri
            "https://drive.google.com/uc?export=view&id=18oCFPkTFlErClE6exnu-7d5sfn9OUcst", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1wsyqOCOltm5jjzcfBZU5_i11m7o2KwfC", #Bang Deyvan
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
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobi": "Memancing Keributan",
                "sosmed": "@elisabethh_",
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
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "",  
                "pesan": "" #15
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "",  
                "pesan": "" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "",  
                "pesan": "" #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "",  
                "pesan": "" #18
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nOeERLpfGRtBZf3CMBA_x9gN1GqHJ23S", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1obxtWGZnduLKopfygCh9tLOplfRR5SDb", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=13-ZWyfcgIJ9ylSIom4biRzVv6T5ajZx8", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=1nTNQylLe4VLtRZtWpv4-J3WghblF1BFO", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1nnWZPzVG_X_ejtQsNHZDSSt-LsPX_S0M", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1o9TyqhoWBJmIrSMUKGjbx8Q61hCC-iGy", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1oyLir7k_3NmHZcISv42mo5F0x4qlzkIm", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1oVMWzKxZ7EFSajcvdozfw5n53cHaD-QE", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1oIdQ2mkUTMVzhVqjxmexZN4tWWEzL_G6", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1n8LpPGIYM1tyb_G_DatOOd9hU2MOGwgs", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1oEa2ReH9xPXEWYh-ngPBDYYU8A9p6XXz", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1nQYyV0J_5f2NNZIHx_Vucis_gQ69DSgt", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1orQtMT744H7iNxkeRiXFhnnv0a6YQQQy", #Bang Randa ok
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

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1goljqkhAgCwWIB9vLkbZ6kHfhzhbYoJi", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=1-5gqsvWUXikpJHSQ9iGVR8o3RsKQ8jfF", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=1Z9SftBE4eNyvLkbImKohCc7K9HFm2XfU", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=1z8Hqkx7dN9b9az1mKlsWKlMrOSvQ5CAy", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=1FZLnWIJAZqP-48Orf-5ZX58Ci2JtTI6U", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=1PTz9fbeIyvUo015QiVfpcvVo0OjbVlYm", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=132m9wfOAyGZdDKfIvy5NOOggnMtqB48L", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=1sbYlzaoC8JCNN2kXBQB8lvB821wbTC6U", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1aaxXV_zBA1jZTyfFGtqxKMaURXmPsyTF", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1jxXCO0MbP7XD0EyzdDse-QO9IBohR057", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=1Z9SftBE4eNyvLkbImKohCc7K9HFm2XfU", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=1zWLp-Q2swAMkSXEA8OOXb7Eznu7p23pl", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id=1pH4ZNa8m1Q0F8xfTbSjuU00O98PFCHXx", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1n9kA7SpNliH9h9rUzDMyUBEeoBX3-T3i", #Kak Asa ok 
        "https://drive.google.com/uc?export=view&id=1oPxAfK9m0PU50qszwDq_tbs3mAPoh5ye", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=1NKpmZS9JWvfzG_tEC07EAcNbsLSExQQq", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1iCK9aICSzGIkbnQHdAC65jnmlPgkrCVa", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1mLRYsTiOn6w8cdZjHP_QaJ87r14aODcS", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1FQ-fxvLPkQu376U8ZelrruA-X4HOCuy9", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=1iIDp7EqqGWmVLh-4PT47w3CcEOH6uw_4", #Kak Tria ok
        ]
        data_list = [
            {
                "nama": "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@yogyyyyyyy",
                "kesan": "Keren dan asik",  
                "pesan":"Semangat kuliah dan semoga cepat lulus"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Asik dan keren",  
                "pesan":"Semoga sehat dan cepat lulus"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Keren dan informatif",  
                "pesan":"Semoga cepat lulus dan semangat terus buat kakaknya"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kuliahnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Asik, Keren, dan informatif",  
                "pesan":"Semangat kuliahnya abang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Keren, informatif dan kelihatan pendiam",  
                "pesan":"Semoga sehat selalu dan semangat buat kak Yohana"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "Asik, keren dan informatif",  
                "pesan": "Semangat abang kuliahnya, semoga cepat lulus"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat abang kuliahnya"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Lucu, asik, Keren dan informatif",  
                "pesan": "Semangat kak UYI kuliahnya"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Keren dan informatif",  
                "pesan": "semangat kakak kuliahnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat ABANG kuliahnya"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Asik, keren, aktif banget, dan informatif sekali kak izza",  
                "pesan": "Semangat kak IZZA kuliahnya, ngaspraknya juga, sehat selalu kak izza"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat kakak kuliahnya"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Pendiam dan informatif penyampaiaannya",  
                "pesan": "Semangat ABANG kuliahnya"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat kakak kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()


elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1-cfSlhG74jd8U8ZPCoRT3cpWTeBOP85n", #BgDimas ok
        "https://drive.google.com/uc?export=view&id=1TR5sLk7VvElN9kY3DcWoCjKwhXrfN3rr", #Kak Catherine ok
        "https://drive.google.com/uc?export=view&id=1A9M4CA7khTW6kNkGVc0goh34qX6qfxEs", #Bg Akbar ok
        "https://drive.google.com/uc?export=view&id=1bGzZ67-Q37j1QSHu5WD7y_ik1BtdYkri", #Kak Rani ok
        "https://drive.google.com/uc?export=view&id=", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=1Cz9BVD-1miCyabKj7cohgN35JsxvEwLN", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1GHP-VYCTnqN5lytO00tU0yiPAbMoOWfp", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=1A5GkUZyIQUeEJWNGd8zqlUIq6Aim_AAF", #Kak Azizah ok
        "https://drive.google.com/uc?export=view&id=1gbolnFEUdtJBDR_vZT1ZRGc_8b5JsW9v", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1blXIwtQ0ofxhJx2-RdYW_hrYkToPLKx-", #Kak Meira ok
        "https://drive.google.com/uc?export=view&id=10wQpR-X4XcieSlxYjrU0kTzygJ1DGPU_", #Bg Rendi ok
        "https://drive.google.com/uc?export=view&id=1HsH10NGsZW-jIoVIv4a1mN9xIgPhDa4l", #kak Renta ok

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
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "",
            "hobi": "",
            "sosmed": "@",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "",
            "pesan": ""
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "",
            "pesan": ""
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()
    
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lhK5_2GOiVO9VQ8YmWUp-tzT4PpjlQPi", #Bang Andrian ok
            "https://drive.google.com/uc?export=view&id=19OJDEWY7tkq1A3yFe05rqZ8q82k7z5Na", #Kak Adisty ok
            "https://drive.google.com/uc?export=view&id=1L04MBn0jRYm_JmTFgE2UlU2HfdCCCMVu",# Kak Nabila ok
            "https://drive.google.com/uc?export=view&id=1Tj61nZIwbNbVRYsAN_qF6dxQiXL8P-gO",# Kak Nabilah ok
            "https://drive.google.com/uc?export=view&id=1cKXK0MzOcyCw_17x8SJ6Vog910aLsVCk",# Bang Ahmad ok
            "https://drive.google.com/uc?export=view&id=1TfVXFKU5PNYcEHLtqKzglpUuffi0OHJV",# Bang Danang ok
            "https://drive.google.com/uc?export=view&id=1_rY7_kuxdrZ0qpDhwUzoctZzemkOjIjw",# Bang Farrel ok
            "https://drive.google.com/uc?export=view&id=185LxfpL7bAAUZYB9_bz3oh9PBa0vOu-b",# Kak Tessa ok
            "https://drive.google.com/uc?export=view&id=1Xlhj8aldO9kFSCx44cnAwitVceiZvAKj",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=18ea20rjYT9w3n1ln_Eslu39j0ovaORB5",# Kak Dhafin ok
            "https://drive.google.com/uc?export=view&id=1uXRcGvzNZ0saDX67DiEbnXI_iFIKuxbJ",# Kak Elia 

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "22",
                "asal":"Sidikalang",
                "alamat": "Dekat Lapas",
                "hobi": "Nyari hobi",
                "sosmed": "@andrianlgaol",
                "kesan": "Abang ini saya kira PDD soalnya keliatan bawa kamera terus",  
                "pesan": "Semoga cepat lulus bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini senyum terus",  
                "pesan": "Semoga cepat lulus kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "",
                "pesan": "K"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16Zzi63VoIIiM7JOM0VMVZNK2mjmJV7pK", # bang tao ok 
            "https://drive.google.com/uc?export=view&id=10IOZam_B8zrZTv-EH0SAb9UrqY2pJCSO", # kak arsyi ok
            "https://drive.google.com/uc?export=view&id=10JbY_dYbErs1rDf6LOpkSt705CcjocT8", # bang kai ok 
            "https://drive.google.com/uc?export=view&id=1a2sQgKTKc3q59rm_rzUqeAnj2Sd8MeyA", # bang arsal ok 
            "https://drive.google.com/uc?export=view&id=1NgV2ufZdMGXyXECxYFDvVuqsvassHNv5", # kak elok ok
            "https://drive.google.com/uc?export=view&id=18vgM_K82ao9CTSIRyCM9oURIENsnFhsK", # kak juju ok
            "https://drive.google.com/uc?export=view&id=1rt6rsOTUUQoGt5tAsjqlpMJFSNTuc534", # kak nel ok
            "https://drive.google.com/uc?export=view&id=1GNThrsqAcdi2Ig7KsFNm8TezeOex919F", # kak try yani ok 
            "https://drive.google.com/uc?export=view&id=1V3XK9B_U5qiJhdRYJLJ0nZQcofj8nGgf", # kak dwi ok
            "https://drive.google.com/uc?export=view&id=1bKhXglpjBZT-LxgQ8ol6XquM90BjcRDj", # bang gym ok
            "https://drive.google.com/uc?export=view&id=1lAxDfbxoOpxbw4Sgfsetg4TbTZYv7WkU", # kak nasywa  ok
            "https://drive.google.com/uc?export=view&id=1WFddmri3wuG6gk3huEnySJ5i3OjzdQNz", # kak priska ok
            "https://drive.google.com/uc?export=view&id=1HO9nPDMZ5GoeEzE_Dbt0XbyPnPp8w4RZ", # bang abit ok
            "https://drive.google.com/uc?export=view&id=1wf-KzZ0mTv-O4ln5D3Ug38C5_pbex-is", # bang hermawan ok ok
            "https://drive.google.com/uc?export=view&id=14oiGr2OXOHKYWlGmCyOvHAMrVnPCOZLN", # kak khusnun nisa ok
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "21",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobi": "Nonton",
                "sosmed": "@",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
                "pesan": ""
            },
            {  
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "Scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "",
                "pesan": ""
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "",
                "pesan": ""
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
