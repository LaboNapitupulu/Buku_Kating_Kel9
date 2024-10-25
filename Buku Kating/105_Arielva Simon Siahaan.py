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
            "https://drive.google.com/uc?export=view&id=1OT8kifKMI_eAoHdNRsWJCctWZT2gO67Z",
            "https://drive.google.com/uc?export=view&id=15tpruKqGj8dTF4CF81rN98vsVeu1m0-B",
            "https://drive.google.com/uc?export=view&id=1qec4S_zjGE-Sg9Bmk5HzNs7jzDewUqPx",
            "https://drive.google.com/uc?export=view&id=1k6ax9DVVMVMsaS6eeRVqG5SSjK0cdEu7",
            "https://drive.google.com/uc?export=view&id=14pdn8bWUYVR6iZfnzdgZJvL_2JAJibZP",
            "https://drive.google.com/uc?export=view&id=1wbbAmCVk4WH7-tk8VB4MiT83XjSHUtFU"
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang ini keren",  
                "pesan":"sukses dalam studi dan karir mendatang bang!" # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Saya kira abang ini angkatan 22",  
                "pesan":"semangat TA dan ngaspraknya bang"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Public speaking kakak ini keren", 
                "pesan":"semangat kuliahnya kak"# 3
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "JL. Nangka IV",
                "hobi": "Dengarin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak ini asik",  
                "pesan":"semangat kuliahnya kak"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "kakak ini agak pendiem di wawancara",  
                "pesan":"semangat kuliahnya kak"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "kakak ini cukup tegas, namun menyesuaikan situasi",  
                "pesan":"semangat kuliah dan ngaspraknya kak"# 6
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HU9WM-8HyIrD--lG49zjXz5UOg9rdBVp",
            "https://drive.google.com/uc?export=view&id=1ti0XNBtosDbEZlJ9wp5WciZ-iMiccGiI",
            "https://drive.google.com/uc?export=view&id=136VRWd5vj50ftaN1Z9fnD4AQhVkTglML",
            "https://drive.google.com/uc?export=view&id=1oiqbRSbVX2mn_R1Ec2qdzsySHxSoM1CD",
            "https://drive.google.com/uc?export=view&id=1_0giXo-avcfcoNk_Loth38VhIuRBhPmy",
            "https://drive.google.com/uc?export=view&id=1opTZdOKnFmNrHO8UZ0qy9kX5vmzduy4Y",
            "https://drive.google.com/uc?export=view&id=1ly2cTlDDHQvWTgHxtpHVouIpQSfUD-FG",
            "https://drive.google.com/uc?export=view&id=1ucMU-YrgoN0U28CdwFBqck24_91J881l",
            "https://drive.google.com/uc?export=view&id=18qDViapEGwRT0lmkn_qBjdHhWLpIFL00",
            "https://drive.google.com/uc?export=view&id=1ElnzWKvEU7xsUpRli1wCLby_98FfkyyD",
            "https://drive.google.com/uc?export=view&id=16jKm038KCPfMaRvDAeQ_e9tIurjNI8QJ",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "kakak ini keren dan tegas sebagai asprak, cukup asik di wawancara",  
                "pesan":"semangat kuliah dan ngaspraknya kak" #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakak ini cukup pendiam di wawancara",  
                "pesan":"semangat kuliahnya kak"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "kakak ini keren dengan pengalaman dan skill komunikasinya",  
                "pesan":"semangat kuliah dan karir mendatang kak"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@anisadini10",
                "kesan": "sama seperti kesan teman lain, kakak ini mirip peserta CoC",  
                "pesan":"semangat kuliahnya kak"# 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": " Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "asal kakak ini cukup jauh juga dari salatiga",  
                "pesan":"semangat kuliahnya kak" #5
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakak ini cukup pendiam di wawancara",  
                "pesan":"semangat kuliahnya kak"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "kayak pernah ketemu abang ini, tapi gatau dimana",  
                "pesan":"semangat kuliahnya bang"# 7
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "abang ini cukup ramah sewaktu wawancara",  
                "pesan":"semangat kuliahnya bang"# 8
            },
            {
                "nama": "Mirza Yusuf Mirzani",
                "nim": "1224500118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": "abang ini cukup cool",  
                "pesan":"semangat kuliahnya bang"# 9
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "di tpb sering liat abang ini karena cukup aktif",  
                "pesan":"semangat kuliah dan ngaspraknya bang"# 10
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD, Tangerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "kakak ini cukup pendiem sewaktu wawancara",  
                "pesan":"semangat kuliahnya kak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B2v1o1X1DNwUYdR-b6OpBsSaNhdcXg92", 
            "https://drive.google.com/uc?export=view&id=142cMG-2weH0hBC-ZyA0pFvXSfnmOYaDq"
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
                "kesan": "Gaya komunikasi kakak ini keren",  
                "pesan": "Semakin keren kak!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini sangat tegas sewaktu wawancara dan rangkaian kaderisasi",  
                "pesan": "Semakin bersinar bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-hsmE0Mfm74-YlFzG3Nbygi3fNhdz5w_", #1
            "https://drive.google.com/uc?export=view&id=1TjVfWjv1gF_7rSa4g_0e8yOEaP7Rb51Q", #2
            "https://drive.google.com/uc?export=view&id=1pJGyRdgr5SLU3s2uVf-mwZF_dN_siFJS", #3
            "https://drive.google.com/uc?export=view&id=1EOyibI8wPGoSSz47Xj6AjLbyo_D8GgJ-", #4
            "https://drive.google.com/uc?export=view&id=", #5
            "https://drive.google.com/uc?export=view&id=1VtwkbMM6JJ24x31hnVcPgxCza1CSn4Zy", #6
            "https://drive.google.com/uc?export=view&id=1lHLASEPIiMoKvMEVmnW_DwHmxxnG6Qgs", #7
            "https://drive.google.com/uc?export=view&id=1to0KxMO7jYMLa7A7C1Ck93lWcn6QXoj3", #8
            "https://drive.google.com/uc?export=view&id=1nrCDX4tVdMAlNDNwEwrEL9lWfkYLiwpI", #9
            "https://drive.google.com/uc?export=view&id=1ERSZ65YIRoEozAV_naqO1bIb33IbPX_h", #10
            "https://drive.google.com/uc?export=view&id=16h2LeYvmU-I4PbafWzMTeYz4-lLkdni0", #11
            "https://drive.google.com/uc?export=view&id=1YfMKSsPHW8DeJ-s2VSHl2PZstvqn1Xvg", #12
            "https://drive.google.com/uc?export=view&id=1fM_dXme-vtgVCatRfXMx5jSjU07H2SOI", #13
            "https://drive.google.com/uc?export=view&id=154UeRbIQo7H6MnYt8WaoQv0c2Ti-uUry", #14
            "https://drive.google.com/uc?export=view&id=1HgcpzC2ZSOgfQCgvCB-qZwUYXeq95TNE", #15
            "https://drive.google.com/uc?export=view&id=1WmDmyoNC3v5toufIq3Ijcpx7TrtH965F", #16
            "https://drive.google.com/uc?export=view&id=1fZN-ZPh41BetMWWKdMarXUIBqi6DJwyx", #17
            "https://drive.google.com/uc?export=view&id=17V8sN7qn4gAr_P30lGZwvdo9_B7xOA-n", #18
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobi": "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Abang ini tegas dan berwibawa",  
                "pesan": "Semangat kuliah dan membimbing angkatan 23 bang" #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kos, Sukarame",
                "hobi": "",
                "sosmed": "@elisabethh_",
                "kesan": "Kakak ini tegas namun bisa juga santai menyesuaikan situasi",  
                "pesan": "Semangat kuliahnya kak" #2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini berwibawa",  
                "pesan": "Semangat kuliah dan membimbing angkatan 23 kak" #3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini berwibawa dan tegas",  
                "pesan": "Semangat kuliah dan membimbing angkatan 23 kak" #4
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini juga berwibawa dan tegas",  
                "pesan": "Sukses kuliahnya kak" #5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini berwibawa juga",  
                "pesan": "Semangat kuliahnya kak" #6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini cool dan berwibawa",  
                "pesan": "Semangat kuliah dan mengkader angkatan 23 bang" #7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini tegas namun santai menyesuaikan situasi",  
                "pesan": "Semangat kuliah dan mengkader angkatan 23 bang" #8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Cukup jarang lihat kakak ini",  
                "pesan": "Semangat kuliahnya kak" #9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abang ini asik dan seru",  
                "pesan": "Bahagia selalu bang dan sukses buat kuliahnya" #10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang ini tegas dan berwibawa",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan bang" #11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini keren dan pengetahuan codingnya luas",  
                "pesan": "Semangat belajar dan menghadapi tiap errornya bang" #12
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini cukup pendiam",  
                "pesan": "Semangat kuliahnya kak" #13
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini cukup santai dan menyenangkan",  
                "pesan": "Semangat kuliahnya bang" #14
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini cukup santai dan menyenangkan",  
                "pesan": "Semangat TA-nya bang" #15
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakak ini cukup pendiam",  
                "pesan": "Semangat kuliahnya kak" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya cukup pendiam",  
                "pesan": "Semangat kuliahnya bang" #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak ini cukup pendiam",  
                "pesan": "Semangat kuliahnya kak" #18
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

# Tambahkan menu lainnya sesuai kebutuhan
