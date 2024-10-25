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
            st.write(f"Nama          : {data_list[i]['nama']}")
            st.write(f"NIM           : {data_list[i]['nim']}")
            st.write(f"Umur          : {data_list[i]['umur']}")
            st.write(f"Asal          : {data_list[i]['asal']}")
            st.write(f"Alamat        : {data_list[i]['alamat']}")
            st.write(f"Hobi          : {data_list[i]['hobi']}")
            st.write(f"Sosial Media  : {data_list[i]['sosmed']}")
            st.write(f"Kesan         : {data_list[i]['kesan']}")
            st.write(f"Pesan         : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rFxFPswgUWXkSRpvAVDziRwI3zi96-Rd",
            "https://drive.google.com/uc?export=view&id=160KRFxbOTlh65yuFGVv1zviaz-XmENrG",
            "https://drive.google.com/uc?export=view&id=1QHuI70jB8yxoZIyOueCXmpdxCHKkjb5n",
            "https://drive.google.com/uc?export=view&id=16EOs6rIPUaBMGyEOiw3izEtM3r_HEFoU",
            "https://drive.google.com/uc?export=view&id=1hmlE4HgO2McumkOmZ_og6RUR0ilGM1pW",
            "https://drive.google.com/uc?export=view&id=1WENphSXp1NA7h1ABaufl7jFVJYHLY8rz",
        ]
        data_list = [
            {
                "nama"	    : "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkharisma",
                "kesan"	    : "Bang Gumi sangatlah berkharisma",  
                "pesan"	    : "Semangat TA bang"# 1

            },
            {
                "nama"	    : "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	    : "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	    : "Nggak nyangka pernah sekelompok MSS sama Bang Pandra",  
                "pesan"	    : "Semangat MSS bang"# 2
            },
            {
                "nama"	    : "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	    : "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	    : "Aku inget banget Kak Meliza yang nyapa aku pas maulidan^^",  
                "pesan"	    : "Kakak kerennn, semangat kak!"# 3
            },
             {
                "nama"	    : "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	    : "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	    : "Nggak nyangka urang awak hehe",  
                "pesan"	    : "Semangat nyekre kak^^"# 4
            },
            {
                "nama"	    : "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	    : "Kakaknya pendiem",  
                "pesan"	    : "Kutunggu debutnya kak"# 5
            },
            {
                "nama"	    : "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	    : "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "Membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	    : "Kakak asprak strukdat RA",  
                "pesan"	    : "Jangan kapok asprakin kita yaa kak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12X592X0iyyY5tUFgtpuAR_Qal0aZb0pu",
            "https://drive.google.com/uc?export=view&id=1VTuAEnH9u1IZeHdTwwGjufHW8I-KD46t",
            "https://drive.google.com/uc?export=view&id=1HZDc5mPndEWZd-C-oP4ETp2WQO0kLcet",
            "https://drive.google.com/uc?export=view&id=1853QyVYGjQsZmXuG7XLeKSrmvq4tGuLP",
            "https://drive.google.com/uc?export=view&id=1hezfODhirAMNZTGZls72f7LnAEptt9z8",
            "https://drive.google.com/uc?export=view&id=1YydouQ6hNqFaifn2x_VXNWVzBu3I521P", 
            "https://drive.google.com/uc?export=view&id=1HnTYHGxHErVMltYfSm3ma-X0AHW4yWLu",
            "https://drive.google.com/uc?export=view&id=1dviUKg6LYiWdRZBrsYxxNQc2vCHKtuwX",
            "https://drive.google.com/uc?export=view&id=178FvUg8q57WEmkZr0a1a3YeE_G0IUXJK", 
            "https://drive.google.com/uc?export=view&id=1jTRBttbxVyTobK09JEYt6EpSy8NI6JVs",
            "https://drive.google.com/uc?export=view&id=11bOHc0wOybjtxEh9GwFptxZ8weZAjrAE"
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
                "kesan"	    : "Kak Niya good-vibes bangett",  
                "pesan"	    : "Semangat ngasprak RA kak"# 1

            },
            {
                "nama"	    : "Annisa Cahyani Surya",
                "nim"		: "121450114",
                "umur"	    : "21",
                "asal"		: "Tangerang",
                "alamat"	: "Jatimulyo",
                "hobi"		: "Baca dan nonton",
                "sosmed"	: "@annisacahyanisurya",
                "kesan"	    : "Kak Annisa kece hehe",  
                "pesan"	    : "Semangat nyekre kak"# 6
            },
            {
                "nama"	    : "Wulan Sabina",
                "nim"		: "121450150",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@wlsbn0_",
                "kesan"	    : "Pengen ketularan possitive vibesnya Kak Wulan^^",  
                "pesan"	    : "Keep your vibes kak!",
            },
            {
                "nama"	    : "Anisa Dini Amalia",
                "nim"		: "121450081",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@anisadini10",
                "kesan"	    : "Kak Anisa mirip Shakira CoC",  
                "pesan"	    : "Semangat nge-stan Svt kak!"# 6
            },
            {
                "nama"	    : "Claudhea Angeliani",
                "nim"		: "121450124",
                "umur"	    : "21",
                "asal"		: "Salatiga",
                "alamat"	: "Lampung Timur",
                "hobi"		: "Baca jurnal",
                "sosmed"	: "@dylebee",
                "kesan"	    : "Vibes kak Claudhea girly bangett",
                "pesan"	    : "Semoga kubisa girly kayak kakak^^"# 2
            },
            {
                "nama"	    : "Dhea Amelia Putri",
                "nim"		: "122450004",
                "umur"	    : "19",
                "asal"		: "Buleleng",
                "alamat"	: "Natar",
                "hobi"		: "Bercocok tanam",
                "sosmed"	: "@_.dheamelia",
                "kesan"	    : "Kak Dhea lucu",
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
                "kesan"	    : "Kayak sering ngeliat abang tapi dimana yak",  
                "pesan"	    : "Semangat bangggg"# 6
            },
            {
                "nama"	    : "Feriyadi Yulius",
                "nim"		: "122450087",
                "umur"	    : "20",
                "asal"		: "Sumatera Selatan",
                "alamat"	: "Depan Koban",
                "hobi"		: "Baca buku",
                "sosmed"	: "@fer_yulius",
                "kesan"	    : "Ternyata kita mutualan di LinkedIn bang",  
                "pesan"	    : "Semangat bang"# 5
            },
            {
                "nama"	    : "Mirzan Yusuf Rabbani",
                "nim"		: "1224500118",
                "umur"	    : "20",
                "asal"		: "Jakarta",
                "alamat"	: "Korpri",
                "hobi"		: "Membaca",
                "sosmed"	: "@myrrinn",
                "kesan"	    : "Abang ini lucu",  
                "pesan"	    : "Semangat otw semester akhir bang"# 6
            },
            {
                "nama"	    : "Jeremia Susanto",
                "nim"		: "122450022",
                "umur"	    : "20",
                "asal"		: "Balam",
                "alamat"	: "Balam",
                "hobi"		: "Gangguin orang",
                "sosmed"	: "@jeremia_s_",
                "kesan"	    : "Bang Jere suka random datengin kelas anak 23",
                "pesan"	    : "Semangat panitnya bang"# 4
            },
            {
                "nama"	    : "Berliana Enda Putri",
                "nim"		: "122450065",
                "umur"	    : "20",
                "asal"		: "BSD, Tangerang Selatan",
                "alamat"	: "Teluk",
                "hobi"		: "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed"	: "@berlyyanda",
                "kesan"	    : "Kak Berlin pendiem",  
                "pesan"	    : "Semangat kakk"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YlEIT7a0PjbiOgAzF-LO_tlfsByRBS-C", 
            "https://drive.google.com/uc?export=view&id=1LlDsHIqBxd0qMhwkU5sThke77MPzHmOA", 
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
                "kesan": "Kak Upi I like the way you speak",  
                "pesan": "Semoga makin keren kak!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang sepertinya softboy",  
                "pesan": "Semoga next jabatannya adalah senator"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

# Tambahkan menu lainnya sesuai kebutuhan
