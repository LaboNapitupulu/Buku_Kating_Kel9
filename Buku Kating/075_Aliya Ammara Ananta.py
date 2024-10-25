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
            "https://drive.google.com/uc?export=view&id=193qwISxqk8bxaBwKz_9gfyfaXN3VFeO1",
            "https://drive.google.com/uc?export=view&id=1l2f2UhJ-L7lGm3Bc1slhJBhpr9h6zuGp",
            "https://drive.google.com/uc?export=view&id=1p9bqnoPZAB0sIcKZNbkdZfPuDqFAFMzo",
            "https://drive.google.com/uc?export=view&id=174nbVwlPFLrmplDVuN1m0lBtE51IINyO",
            "https://drive.google.com/uc?export=view&id=1p08cx8e2txF94QYSdvRuHhgkXn5wFaqe",
            "https://drive.google.com/uc?export=view&id=1B2Eacl7t6YIGkbqDHljKwdBBzPi6h8In",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobbi": "Dengar musik",
                "sosmed": "@gumilangkhasirma",
                "kesan": "Abang ini sangat menginspirasi",  
                "pesan":"Semangat jadi kahimnya bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobbi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Abang ini sangat ketje",  
                "pesan":"Semangat semester akhirnya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota baru",
                "hobbi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakaknya cakep deh",  
                "pesan":"Semangat terus kuliahnya kak"# 1
            },
             {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "JL. Nangka IV",
                "hobbi": "Dengarin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Tetap semangat kakak"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Keren banget kakak",  
                "pesan":"Semangat dan pantanag menyerah kak"# 1
            },
             {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota baru",
                "hobbi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakaknya keren",  
                "pesan":"Tetap semangat kakak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13ovlGzJPmi9bvBaj6BcCnhW6Wpg9cRQq",
            "https://drive.google.com/uc?export=view&id=1YzF3JZt-S0qn0Rrv4Dq_VeOkNJiPK1gI",
            "https://drive.google.com/uc?export=view&id=19maXZ10_EaUndwbn7ujYWkYCRmhCriRK",
            "https://drive.google.com/uc?export=view&id=1El2pUbsZQrgU3hwiGZNFeVe3Rgmcfaoe",
            "https://drive.google.com/uc?export=view&id=1jhYEpoZI-8hkTahVGZNVc5Xj7iwxTFG8",
            "https://drive.google.com/uc?export=view&id=1Unt7j4PEtTAhhJndMShHqFGGQSWrpMgp",
            "https://drive.google.com/uc?export=view&id=17lxAVHTnbAsVefxatOGfqke1E5I-GRV7",
            "https://drive.google.com/uc?export=view&id=1NJxOiGekvPK6eCKwlEEoMqr9ev8oqeza",
            "https://drive.google.com/uc?export=view&id=1TorP-oZ_8BEFwNtK9eCVbGu7sXoqoMvI",
            "https://drive.google.com/uc?export=view&id=1-AFPDiy1gn68c99u-yU-hUNoFzi0T1K8",
            "https://drive.google.com/uc?export=view&id=1owENVS5cdiofDK0Nrnc4bLN3qSEuyOeX",

        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Searching di perplexcity",
                "sosmed": "@@trimurniaa_",
                "kesan": "Public Speaking kakaknya bagus banget",  
                "pesan":"Semangat semester akhirnya kak"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobbi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak nya cantik banget",  
                "pesan":"Semangat terus kakak cantik"
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobbi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak nya asik banget",  
                "pesan":"Semangat kakak kuliahnya"
            },
              {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Balam",
                "hobbi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abangnya kece",  
                "pesan":"Semangat terus jangan putus asa"
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"sumsel",
                "alamat": "depan kobam",
                "hobbi": "baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat terus abang!"
            },
            {
                "nama": "Mirza yusuf mirzani",
                "nim": "122450118",
                "umur": "21",
                "asal":"jakarta",
                "alamat": "korpri",
                "hobbi": "main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat abang kuliahnya"
            },
             {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"surakarta jatim",
                "alamat": "pahoman",
                "hobbi": "ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abangnya enjoy",  
                "pesan":"Semangat bang kuliahnya"
            },
            {
                "nama": "Annisa cahyani surya",
                "nim": "121450114",
                "umur": "22",
                "asal":"tangerang",
                "alamat": "jatimulio",
                "hobbi": "baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak nya skena abis",  
                "pesan":"Semangat kakak kuliahnya"
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "teluk",
                "hobbi": "suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
              {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"malang",
                "alamat": "jati agung",
                "hobbi": "baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semangat terus jangan putus asa kak"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakaknya baik",  
                "pesan":"Semangat terus kakak kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Uw4zTtGqIpd3JP1gqi2IFzjBOO4MkDX1", 
            "https://drive.google.com/uc?export=view&id=13CD8FHbJ1iiXb-4sXpjeO8noJXu-Peua", 
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
                "kesan": "Public Speaking kakaknya bagus banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobbi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Keren bang",  
                "pesan":"Semangat kuliahnya bang"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UjvaFS_1EGGcQD1SiyUJHZCQAQAgb2g3", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1VCPmYuE2J_LfQ7uchZs0fxjNDYcKKAIX", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1S794LMl2cer48Cks9uhpmhB2CKtIj-QW", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1S9TonWPcV2D-LqoCuuihRuGpzsrSTuPA", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1TThZsqpJwflNvTw4-mjZoxfjShCG6mmZ", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1SB4MxRzRAHHr7xfmpnXxyO8YQb75tKhT", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1WcNdUkTzWYcvosPdeoNq2UTlL79qTv7f", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1Ts9PkzZ_mRIeoAkXlytFEKQbxOUCLFm5", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1TLaaA6Slf8oW4sNW3zIwo4WdGSUR1HMW", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1Ru58-vzimYG16UlOxi21h1KcEfFiHwr7", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1RyXECHNWnn4yigbwrYQ6zxU6AEe_9R-o", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1RWP9JQ6u5ZnTJ9sTinZm-zkuPJRVKZDO", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1RiKINinkos7qS9nSIAFiZlKu-h59izgF", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1F1Uvm7AEBxXZu_ATB2_iOcYNVlY6cJy6", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1UcNaiAiUN7gB5tkXHTEogtNy4C3dnJr5", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1U0QzfmJq3m6_vBgrpkUfOdr2xMYoQqmj", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1US5kTbQK6nG6UVOeI5szAcP7S5U_eBuh", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1UIvGYQ1CEH2CFCGphaJqIvK1n27a81QW", #Kak Dini
        ]
        data_list = [
            {
                "nama": "Ericson Chandra Sihombing",
                "nim": "121450026",
                "umur": "21",
                "asal":"Bekasi",
                "alamat": "Kobam",
                "hobbi": "Travlling",
                "sosmed": "@ericsonchandra99",
                "kesan": "Banyak ilmu yang bisa diambil dari abang ini",  
                "pesan":"Semangat kuliah nya bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobbi": "",
                "sosmed": "@elisabethh_",
                "kesan": "Kakaknya cantikk",  
                "pesan":"Semangat jadi sekre nya kak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobbi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobbi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Ternyata kakaknya baik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobbi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobbi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat terus kakak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobbi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobbi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat terus bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobbi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobbi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobbi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abangnya asik",  
                "pesan":"Semangat bang kuliahnnya"
            },
                        {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobbi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Abangnya asik banget",  
                "pesan":"Tips agar pintar bang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobbi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobbi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya keren",  
                "pesan":"Tips jago gitarnya bang"
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobbi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatra Selatan",
                "alamat": "Korpri",
                "hobbi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Keren dan baik banget",  
                "pesan":"Semangat terus kuliahnyaa"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobbi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Keren banget kak",  
                "pesan":"Semangat terus kuliahnya kak"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()



