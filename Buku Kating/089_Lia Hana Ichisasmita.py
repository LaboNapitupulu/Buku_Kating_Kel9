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
            "https://drive.google.com/uc?export=view&id=138YG1WnVXAiNZSzrTrFdEXoYh1ryNSkN",
            "https://drive.google.com/uc?export=view&id=1L2CDQakXGiDLW1otx7P3QzqzXtfc2uwX",
            "https://drive.google.com/uc?export=view&id=1VtH6gtYMZmP4X1NckmZ7IS5hrrLd18dB",
            "https://drive.google.com/uc?export=view&id=1HXfkNlixI7zd7ei8LUr1TvQdz_R6WOpZ",
            "https://drive.google.com/uc?export=view&id=1htFol76dNLMmOXWlSyenJkSbdNs0MOiP",
            "https://drive.google.com/uc?export=view&id=1VTYjQi5uXt02NkTFl_gLFim77JObhWSc",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Dengar musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang ini berkarisma dan asik untuk ngobrol",  
                "pesan": "Semoga lulus tepat waktu"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Asik dan informatif",  
                "pesan": "Semangat kuliah dan ngaspraknya !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450056",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak baik banget, informatif jawab pertanyaan",  
                "pesan": "Semangat nerusin surat menyuratnya kak !!!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini agak pendiam",  
                "pesan": "Semangat kuliah dan ngurus bendaharanya kak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl. Nangka IV",
                "hobi": "Dengerin Bang Pandra gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya lucu, baik juga",  
                "pesan": "Semangat kuliah dan tugas sekretarisnya kak !!!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "122450000",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ini baik, seru juga",  
                "pesan": "Semangat ngurus keuangan himpunan kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dnsku-PsUCCMPsAQ1fbHjLQbh8hJpvR9",
            "https://drive.google.com/uc?export=view&id=1dlITh6jrEIjoFrKdJVe8dNNOWgP_BuKr",
            "https://drive.google.com/uc?export=view&id=1hcmisSbjn0QQOS6G79YhWVc6qjovX22x",
            "https://drive.google.com/uc?export=view&id=1sO0E7fAOroXtxBgWMxYREUJ1Jzik7Qfz",
            "https://drive.google.com/uc?export=view&id=1sW5fDqHqubPZvXUApPYnO9OR5hZ0wy9u",
            "https://drive.google.com/uc?export=view&id=1eduqIQ8qsLaZkRLPzfl86UUm5dvm_Svl",
            "https://drive.google.com/uc?export=view&id=10KxRK7yH0o36m12acpn0SgNWCbuaCxTB",
            "https://drive.google.com/uc?export=view&id=1NamXOptVY8VwE-rsbJlK5tAoQOQxOoVr",
            "https://drive.google.com/uc?export=view&id=1K6MLmUYS__FbrCC_Iv9CnGxYMsBcmq4k",
            "https://drive.google.com/uc?export=view&id=1lD5urM5arHyWSzTBJUTliLbnctx5m96q",
            "https://drive.google.com/uc?export=view&id=1R5sivbKS--ja_7kqutNqapEAicWhuJLL",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexcity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini lucu dan suka ngobrol",  
                "pesan":"Semangat ngasprak nya kakk !!!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "122450000",
                "umur": "22",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak mirip banget sama Shakira COC",  
                "pesan":"Semoga nilai di kuliah memuaskan ya kak !!!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak ini baik mau berbagi pengalaman magang di Telkom",  
                "pesan":"Semoga lulus kerja di Telkom ya kak, Spill portofolionya kak !!!"# 1
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "jati agung",
                "hobi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Style nya lucu banget kak",  
                "pesan":"Tetap on point ya kak stylenya !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Depan kobam",
                "hobi": "baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini seru di ajak ngobrol",  
                "pesan":"semangat kuliah dan organisasinya bang !!!"# 1
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak cantik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang stylenya bagus",  
                "pesan":"Semangat terus bang kuliahnya !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini lucu banget",  
                "pesan":"Semangat kuliah dan panitia kadernya kakk !!!"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini baik, salfok sama kumisnya ",  
                "pesan":"semangat kuliah dan ngaspraknya bang !!!"# 1
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobi": "Suka liat linked in, Puasa senin kamis, Ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini hobinya banyak banget pasti seru",  
                "pesan":"semangat kuliah dan puasa senin kamisnya kak !!!"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar lampung",
                "alamat": "Bandar lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini seru, asik di ajak bercanda",  
                "pesan":"Semangat nugasnya bang !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
