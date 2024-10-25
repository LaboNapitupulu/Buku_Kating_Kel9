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

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n1emj1viQMnMniWHIqy3jbsooGV6bq7V", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1zYcrLq_fR2ai4T9Pa1j4tTsKGZsnelRy", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1Z09RRM9mTYXfDzZJjCQtTbNInuO8lsp_", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=1UzMRc8kjN3C7HvSZyGl3jdzmXDhDKTn2", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1hZYsSSSpdD3BGdf31Yg9P8s3qAfPs7bG", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1xIGJQN0qh9VBcMGmpwkRKSj3s1At3nfW", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1s1VKLzYXWbQ0URu8B1supVUpFcPKJUid", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1rla2qFecdHSC7t4_wNx1WUyoAl1HFII1", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1hmGI2ZMuk0hxrvN8l8oMH-v16ML_Fi2K", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=17qBzw_iWggGa8mbtmNBPoIOMWw-zH0fJ", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1RDz8XeRj9VJ8EBDqWMOFmzcwUmcUl-TL", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1nIxw8gZGKo8Ui15y94MankFON8KtUTbk", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1IIgzkhK0ZrPHIcvYxPK1ymb6KiwELoYi", #Bang Randa ok
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
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobbi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya cantik",  
                "pesan":"Semangat terus kakaknya kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya baik",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobbi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semangat terus kuliahnya bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobbi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat terus kuliahnya kak"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobbi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya pinter banget",  
                "pesan":"Tips pinter kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobbi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobbi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat kuliah nya kakak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobbi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Abangnya pinter sekali",  
                "pesan":"Tips pinter bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobbi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya keren banget",  
                "pesan":"Semangat terus kakak kuliahnya "
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat terus bang kuliahnya"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"",
                "alamat": "Sukarame",
                "hobbi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semangat terus kuliahnya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1DNKn1GGM9AI_S4o1q2d4Kpc7WbWwMxKy", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=16bzSblzflAmc6Swp4rRxQwTIqcI29YvW", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=14kbf5ymDMVECPd-Sbr8bANY40geWkB7o", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=1Mxk9V3n_tbzoZsZRyvEagSNq9cAxqeoY", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=1vKjG465Xghy0vJFmbIaohnS67GqCeP0p", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=1dsaD4rKktfN9AlPzm96An80OP2hrmiqY", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=1ejIV9DvtFplWlp0RawGDJMGtTM8d8dY9", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=1kjDq3naKh93UABoT15xTBZ46lF1VQB-I", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1LB3vQ9RXmdKcHLCgwbdHbulyJAsBxhAn", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1gziWxzYnDRk8dj3g-vIalJTlW8yQKvBX", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=1eE8STZxkRNXyI90TtTU2BzkzSUysL9LT", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=1vD7rC3oKkgR0gWk3M4nKRMycHPw-6ZK5", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id=1gwHCCcUZofEwg2ULxq1xQsK5Z23-Q1PE", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1_8NM4SNai5Igeia3vepWpqMTaQ0kIogr", #Bg Asa ok 
        "https://drive.google.com/uc?export=view&id=1FlHevrsR7xgt6DrAdaLPuxqZSKR1Wz1N", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=19CohBwfnk5x1A1rZQXUhuGjEhc0xtR7m", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1Y-mLbLhHfmFa9J3uUcx2uMIj4wYPchmr", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1kYN3NV1Zx40GGzA4PVlgLCy1brS0zI8T", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1CaQZs-FQYF50fZtSJSq59suTvnkFGjHB", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=1mlxetTaA32rpgxzsNRi9wZUnVP8PzVS_", #Kak Tria ok
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
                "kesan": "Abangnya kece",  
                "pesan":"Tips menjadi kadept bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobbi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya asik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya baik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobbi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abangnya baik banget",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobbi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya keren",  
                "pesan":"Semangat terus kuliahnya kak"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobbi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Kakaknya keren",  
                "pesan":"Tips menjadi keren"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat terus kuliahnya kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobbi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya cantik banget",  
                "pesan":"Semangat kuliahnya kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobbi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Abangnya kece",  
                "pesan":"Tips menjadi kece bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobbi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Abangnya keren",  
                "pesan":"Semangat kuliahnya bang"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya baik banget",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobbi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya kece",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobbi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya baik banget",  
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobbi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya cantik banget",  
                "pesan": "Semangat kuliahnya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobbi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya kece kali",  
                "pesan": "Tips menjadi kece"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakak nya asik banget",  
                "pesan": "Tips agar asik kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "kakaknya cantik banget",  
                "pesan": "Semangat terus kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Abangnya baik",  
                "pesan": "Semangat terus bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobbi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya cantik banget",  
                "pesan": "Semangat terus kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=17iwcHYvx8CzctOqq-m1yEQh387PSjecU", #BgDimas ok
        "https://drive.google.com/uc?export=view&id=1tfBGDEbcGOl-F-KK5cotAE1Wo5H0WXCm", #Kak Catherine ok
        "https://drive.google.com/uc?export=view&id=14SWMPFVAbfmqQswMzPxaTeu4TiQ_96St", #Bg Akbar ok
        "https://drive.google.com/uc?export=view&id=1uU7q8kppXJ-RbCg8xoTq3rReXTkNWLUG", #Kak Rani _
        "https://drive.google.com/uc?export=view&id=1mZTPYwBX_ElNOUGeY8r7eWVzYZ74BH3s", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=1lcNsb4LbYwNHzf6qErT1gkCcB4Blx6M4", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1v0awN0w3lmpd7MSGIxMMTprzqAf0wUyc", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=1t7iufaJVXSiAeVcaMGhR026jLhFDHp0L", #Kak Azizah _
        "https://drive.google.com/uc?export=view&id=1ZbCDo6B5NIt3zpe65TAKEeUkK8HYWsUc", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1DTQ6cRwotr7PsgtQsOxUyxGG1K9hO8dS", #Kak Meira _
        "https://drive.google.com/uc?export=view&id=1vSYwFTibcsEfdyWa35b-n5OoCptFQJB8", #Bg Rendi ok
        "https://drive.google.com/uc?export=view&id=1ziJMEXqo4v-0W9zBtyySWI3t12u44VH8", #kak Renta ok

        ]
        data_list = [
            {
            "nama": "Dimas Rizky Ramadhani",
            "nim": "121450027",
            "umur": "20",
            "asal": "Pamulang, Tangsel",
            "alamat": "Way Kandis (Kobam)",
            "hobbi": "Manjat Tower Sutet",
            "sosmed": "@dimzrky_",
            "kesan": "Public Speaking abangnya bagus banget",
            "pesan": "Tips agar kece bang"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobbi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "Kakaknya cantik banget",
            "pesan": "Semangat terus kak"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobbi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "Abangnya kece",
            "pesan": "Semangat kuliahnya bang"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "",
            "hobbi": "",
            "sosmed": "@",
            "kesan": "Kakaknya cantik banget",
            "pesan": "Semangat terus kuliahnya kak "
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobbi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "Abangnya kece",
            "pesan": "Semangat terus abang"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobbi": "Renang Tapi Gabisa Renang",
            "sosmed": "@",
            "kesan": "Kakaknya cantik",
            "pesan": "Semangat terus kuliahnya kak"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobbi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "Abangnya baik banget",
            "pesan": "Semangat terus kuliahnya bang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobbi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "Kakaknya baik banget",
            "pesan": "Semangat terus kuliahnya kak"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobbi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "Abangnya kece",
            "pesan": "Semangat terus bang"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobbi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "Kakaknya cantik banget",
            "pesan": "Semangat kuliahnya kak"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobbi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "Abangnya keren banget",
            "pesan": "SEmangat kuliahnya bang"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobbi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "Kakaknya baik banget",
            "pesan": "Semangat kuliahnya kak"
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()