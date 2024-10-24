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
            st.write(f"Hobi: {data_list[i]['hobbi']}")
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
                "hobbi": "Denger musik",
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
                "hobbi": "Main gitar",
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
                "hobbi": "Drakoran",
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
                "hobbi": "Dengarin Bang Pandra gitaran",
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
                "hobbi": "Nyanyi",
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
                "hobbi": "Membaca",
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
                "hobbi": "Searching di perplexity",
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
                "hobbi": "Baca dan nonton",
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
                "hobbi": "Nonton drakor",
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
                "hobbi": "Nonton drakor",
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
                "hobbi": "Baca jurnal",
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
                "hobbi": "Bercocok tanam",
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
                "hobbi": "Ngopi",
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
                "hobbi": "Baca buku",
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
                "hobbi": "Membaca",
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
                "hobbi": "Gangguin orang",
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
                "hobbi": "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "kakak ini cukup pendiem sewaktu wawancara",  
                "pesan":"semangat kuliahnya kak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
