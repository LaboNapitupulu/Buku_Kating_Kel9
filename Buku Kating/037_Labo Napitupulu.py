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
            "Depertemen MEDKRAF",
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
            st.write(f"Nama\t: {data_list[i]['nama']}")
            st.write(f"NIM\t: {data_list[i]['nim']}")
            st.write(f"Umur\t: {data_list[i]['umur']}")
            st.write(f"Asal\t: {data_list[i]['asal']}")
            st.write(f"Alamat\t: {data_list[i]['alamat']}")
            st.write(f"Hobi\t: {data_list[i]['hobi']}")
            st.write(f"Sosial Media\t: {data_list[i]['sosmed']}")
            st.write(f"Kesan\t: {data_list[i]['kesan']}")
            st.write(f"Pesan\t: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yTQ3IwaEddPzuRQQrWvlhkZISQb_75vc", #1
            "https://drive.google.com/uc?export=view&id=1y8nGSOHoCsbn82pq3Ksd5kpXwBILfl4y", #2
            "https://drive.google.com/uc?export=view&id=1k5TxZnVZxS_tY-BrUO5MmF2FfGCOufvi", #3
            "https://drive.google.com/uc?export=view&id=1yCBcCRjAzL3tK9A56GZ7ipv46UxPetdO", #4
            "https://drive.google.com/uc?export=view&id=1y9ca2O072noal3KhxDbPr1JhkuhuD8I6", #5
            "https://drive.google.com/uc?export=view&id=1y9XJgvfzHk9O1qdc9kEuj5ynfHqBTdmv", #6
        ]
        data_list = [
            {
                "nama"	    : "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Jl. Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkhasirma",
                "kesan"	: "Abang ini tegas dan berwibawa",  
                "pesan"	:" Semoga memiliki karir yang sukses setelah berhasil magang di Telkom"# 1

            },
            {
                "nama"	: "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	: "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	: "Ada aja gebrakannya kalau ngomong",  
                "pesan"	: "Semoga jadi konco abadinya Bang Gumi"# 2
            },
            {
                "nama"	: "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	: "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	: "Kalau ngomong tuh kalem tapi singkat dan padat",  
                "pesan"	:"Semoga kuat sampai tamat"# 3
            },
            {
                "nama"	: "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	: "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	: "Jago ngjelasin dan keliatannya jago multi-tasking ",  
                "pesan"	:"Semoga jangan jadi sekre abadi(gapapa kalau mau)"# 4
            },
            {
                "nama"	: "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	: "Kalo ngomong berasa melayunya",  
                "pesan"	:"Semoga jadi penyanyi"# 5
            },
            {
                "nama"	: "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	: "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "Membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	: "Gayanya keren karena make kacamata gelap",  
                "pesan"	:"Semoga selalu murah senyum"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kh-lyef9moCoZRR87FTar60F8fNE7T0B", #Kak Tri
            "https://drive.google.com/uc?export=view&id=1lQlSq-UhKE3v_HuJZ4PgAOIE8F--F3hz", #Kak Anisa
            "https://drive.google.com/uc?export=view&id=143ozXy1GiNC6ip1TDKU2p08PFGMU5GI7",
            "https://drive.google.com/uc?export=view&id=1nSPvZ_r5o5SKRICbwWklHIjdPGG2g9yR", #Kak Anisa           
            "https://drive.google.com/uc?export=view&id=1rErl9RtAvNjF-oeoSVisoSD6EWLXn2iE", #Kak Claudhea
            "https://drive.google.com/uc?export=view&id=1m_zeYj-Qyvp6feU5VKcROoHHE_1SkW5N", #Bang Farul
            "https://drive.google.com/uc?export=view&id=1GNt4cgjiHtezIQfEtLGSka9uaRSLiMgg", #Bang Feriyadi
            "https://drive.google.com/uc?export=view&id=1PJ1RsYo7JjQbd4b_4Czvq6tFn8QwT78y", #Bang Mirzan
            "https://drive.google.com/uc?export=view&id=1HNjCd57SZsypXeb5ZdJrwygaZKFVteEV", #Kak Dhea
            "https://drive.google.com/uc?export=view&id=12T0NsqZ9UXSZ8CSUf_nvf5ZfGiteQ6ZF", #Kak Berliana
            "https://drive.google.com/uc?export=view&id=1NjdmGUuJVPHFzhXiG5DntkDMPWTSwJ8B", #Bang Jer
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Jl. Raden Saleh",
                "hobi": "Searching di perpexcity",
                "sosmed": "@trimurniaa_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati agung",
                "hobi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama"	    : "Annisa Cahyani Surya",
                "nim"		: "121450081",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@anisadini10",
                "kesan"	    : "",  
                "pesan"	    : ""#
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "",  
                "pesan":""#
            },
            {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Srakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama"	    : "Feriyadi Yulius",
                "nim"		: "122450087",
                "umur"	    : "20",
                "asal"		: "Sumatera Selatan",
                "alamat"	: "Depan Koban",
                "hobi"		: "Baca buku",
                "sosmed"	: "@fer_yulius",
                "kesan"	    : "",  
                "pesan"	    : ""
            },
            {
                "nama"	    : "Mirza Yusuf Rabbani",
                "nim"		: "1224500118",
                "umur"	    : "20",
                "asal"		: "Jakarta",
                "alamat"	: "Korpri",
                "hobi"		: "Membaca",
                "sosmed"	: "@myrrinn",
                "kesan"	    : "",  
                "pesan"	    : ""
            },
            {
                "nama"	    : "Dhea Amelia Putri",
                "nim"		: "122450004",
                "umur"	    : "19",
                "asal"		: "Buleleng",
                "alamat"	: "Natar",
                "hobi"		: "Bercocok tanam",
                "sosmed"	: "@_.dheamelia",
                "kesan"	    : "",
                "pesan"	    : "" 
            },
            {
                "nama"	    : "Berliana Enda Putri",
                "nim"		: "122450065",
                "umur"	    : "20",
                "asal"		: "BSD, Tangerang Selatan",
                "alamat"	: "Teluk",
                "hobi"		: "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed"	: "@berlyyanda",
                "kesan": "",  
                "pesan":""#
            },
            {
                "nama"	    : "Jeremia Susanto",
                "nim"		: "122450022",
                "umur"	    : "20",
                "asal"		: "Balam",
                "alamat"	: "Balam",
                "hobi"		: "Gangguin orang",
                "sosmed"	: "@jeremia_s_",
                "kesan": "",  
                "pesan":""#
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1L3hGnPMAEELYata4I876szTYQUFigZXg", 
            "https://drive.google.com/uc?export=view&id=1zrGtT5bJ9W9KZy14_FxRhZbVK4vaUdMR", 
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
            "https://drive.google.com/uc?export=view&id=1UyCryMD5T7uSHZAnWWSW9PsECZ881ys6", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1VFR2MR-cdzWkkieqiKq8hX8nC5Dh2yRk", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1S8hAFnCa5O7t-7WgyRRaUJ-IxyZGj7cw", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1S9rr5O8qs_IApZL8Eqcg--j7wVywvwa1", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1Tfl4po74UAb9MXlYLI3SGXIlKzpIoHu3", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1TJ1LH8icOBceQrvUl_U0ctPxkiQdmUZJ", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1TSPCFg8wWAsbxcS2KN8P1Mm98K_p4W8r", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1Ty9ZjS_KUfN4yZBRuNMVRo0aktVmjBcI", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1TMZx1mvADm-g2Ca5jipYGKv1BOmCM8AG", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1RunBGRpzlwnMWExGrA9Xek-X74pwNutx", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1S2yV67MQZQouADcYQ0eVET2CxHwu41_v", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1RZLYWIPd1NheCnzEknDp0R0fJe6c-yDf", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1RqXQB5ARAnuI4vqEfwMhGUcNH-ZEANaD", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1RVfQ7ajZ45Hbis2RBMY7ZQbMO3Hkcw7k", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1Uh79V4Akmj5j3IM3jDPPTU7fBqScAGbK", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1UEx1UKhkt8w4BGVgt2zKiqCYCr_xdbgB", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1Ualo9wgjkUO-z2XQayuxpOKXJ_mF7wox", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1UOZQgE8AD9EQTswiFkhDyHFZ2Ah3hbSh", #Kak Dini
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

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1ruaNPDoOjdMwXETaFKK5wdP9OjPz-OLP", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=1rS3qoPt8yWsxVWxnmgf_sRxMYHVYo57T", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=1rWQ_nohAw_y1v_Ue3Q-QcpkmDIFGXfBj", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=1qxVmT9Qv9onJDUTqhWfHtUiZnK_AFMOq", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=1qfl63GBbHtkDYot4lyZl_QfSlIOHIlIO", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=1rQKpwrd02lTQ6Dtdkqouav7HCHtI3M8g", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=1qwGPuqACnI8RNAECH4zeYQ1BGnlHD7cr", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=1qm73uBczPL5ZmDl8D_74mNCbfBIVsVDd", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1r3h7UvdmZIG-_lFExwjRhtxAZPBPKJmm", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1rGAkQfs-IL9812e38jWYRYOjnXehATji", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=1qeoZVwY_IvnakkBCs3Wdl3wpU4MTzzhx", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=1rWmPwTx5AUIp02rid27z8qM4m59uKWy_", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id1qryXfNHklg2X7jYl3TBtPbSL3P_uu8AP=", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1rVHm5ihmkIcUWfri-3VbLLnBwd3Zw7i7", #Kak Asa ok 
        "https://drive.google.com/uc?export=view&id=1rlmW4FgckVRGuCIkkXU_oBd4Mmq242FB", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=1r-GSq7sarO6WXN6s0PfVOmmRaP5U0STZ", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1qZBON19sl80elIG0Rp5VWhwkBvdyRjja", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1qdNxik2-7nhcTNqBHUO8Q5evXY8jD6eT", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1qphs1piiqjosN0nx7OSDHxHYwDNQCA_q", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=1qskmw0YshRfoEGdlDhLSawEH4fKJh92l", #Kak Tria ok
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
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "",  
                "pesan": ""
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "",  
                "pesan": ""
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=17iwcHYvx8CzctOqq-m1yEQh387PSjecU", #BgDimas ok
        "https://drive.google.com/uc?export=view&id=19GbVJXP5jnMHJbPKAW27_PGSNnb2bhEQ", #Kak Catherine ok
        "https://drive.google.com/uc?export=view&id=1RH8vudXdX_-6gy2AUEfO81f95dW66y36", #Bg Akbar ok
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Rani _
        "https://drive.google.com/uc?export=view&id=1SD8xwVSJWx2y3hXmwcW2k4AbJmnMukSi", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=13WXdXx2vOxM7VpaGpoA0awtJ5vMxDzIO", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1kJycwwidXEaqBRGBU6r5HuToupQ4Krl2", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Azizah _
        "https://drive.google.com/uc?export=view&id=1CkJV-CqxUTdeYI9Kjm3UN9HxgNZtvTZo", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #Kak Meira _
        "https://drive.google.com/uc?export=view&id=1Gh0vHoHICRqPL623BCjGYV9Yx0rk68Li", #Bg Rendi ok
        "https://drive.google.com/uc?export=view&id=1oJwfUP05xqCDVTmz4fqIMm8yrszZUWGa", #kak Renta ok

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


# Tambahkan menu lainnya sesuai kebutuhan
