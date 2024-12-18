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
                "pesan"	:"Semoga jadi aktris drakor"# 3
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
                "pesan"	:"Semoga jadi penyanyi handal"# 5
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
                "pesan"	:"Semoga gayanya tetap kece"# 6
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
                "kesan": "Kakak ini asik banget, lengah dikit ganti topik",  
                "pesan": "Semoga selalu aktif kak"
            },
            {
                "nama"	    : "Annisa Cahyani Surya",
                "nim"		: "121450114",
                "umur"	    : "21",
                "asal"		: "Tangerang",
                "alamat"	: "Jatimulyo",
                "hobi"		: "Baca dan nonton",
                "sosmed"	: "@annisacahyanisurya",
                "kesan": "Kakak ini definisi cewe kue",  
                "pesan":"Semoga jadi penulis webtoon"
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak ini gayanya kayak tomboy",  
                "pesan":"Semoga kakak ini stay tomboy soalnya cocok"
            },
            {
               "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati agung",
                "hobi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan"	    : "Kakak ini dari cara ngomongnya pinter",  
                "pesan"	    : "Semoga lulus tepat waktu kak"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini lucu dan ramah",  
                "pesan": "Semoga punya banyak paper dan project sama dosen kak"#
            },
            {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Srakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini kayak abang-abangan tongkrongan (asik banget)",  
                "pesan": "Semoga saya diajakin ngopi sama abangnya"
            },
            {
                "nama"	    : "Feriyadi Yulius",
                "nim"		: "122450087",
                "umur"	    : "20",
                "asal"		: "Sumatera Selatan",
                "alamat"	: "Depan Koban",
                "hobi"		: "Baca buku",
                "sosmed"	: "@fer_yulius",
                "kesan"	    : "Abang ini cool abis",  
                "pesan"	    : "Stay chill and cool bang"
            },
            {
                "nama"	    : "Mirza Yusuf Rabbani",
                "nim"		: "1224500118",
                "umur"	    : "20",
                "asal"		: "Jakarta",
                "alamat"	: "Korpri",
                "hobi"		: "Membaca",
                "sosmed"	: "@myrrinn",
                "kesan"	    : "Abang ini dari jauh kayak blasteran",  
                "pesan"	    : "Bagi tips outfit kecenya bang"
            },
            {
                "nama"	    : "Dhea Amelia Putri",
                "nim"		: "122450004",
                "umur"	    : "19",
                "asal"		: "Buleleng",
                "alamat"	: "Natar",
                "hobi"		: "Bercocok tanam",
                "sosmed"	: "@_.dheamelia",
                "kesan"	    : "Kakak ini suaranya lucu",
                "pesan"	    : "Semoga jadi punya kebun seluas ITERA kak" 
            },
            {
                "nama"	    : "Berliana Enda Putri",
                "nim"		: "122450065",
                "umur"	    : "20",
                "asal"		: "BSD, Tangerang Selatan",
                "alamat"	: "Teluk",
                "hobi"		: "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed"	: "@berlyyanda",
                "kesan": "Kakak ini ambis dan taat beragama",  
                "pesan":"Semoga bisa jadi contoh yang baik bagi kami"#
            },
            {
                "nama"	    : "Jeremia Susanto",
                "nim"		: "122450022",
                "umur"	    : "20",
                "asal"		: "Balam",
                "alamat"	: "Balam",
                "hobi"		: "Gangguin orang",
                "sosmed"	: "@jeremia_s_",
                "kesan": "Abang ini beneran suka jail",  
                "pesan":"Dikurangin dikit hobinya bang"#
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
                "kesan": "Kakak ini super tegas tapi enak ngobrolnya",  
                "pesan":"Semoga selalu tegas dan teguh dengan badai yang huru-hara ini kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini ngerangkul banget dari dulu",  
                "pesan":"Semangat terus bang deengan segala kegiatannya"
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
                "kesan": "Abang ini sangat berwibawa dan punya auranya sendiri",  
                "pesan":"Terimaksih ilmu-ilmunya bang, semoga cepat lulus"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobi": "Memancing Keributan",
                "sosmed": "@elisabethh_",
                "kesan": "Kakak ini asik banget terus kalo ngomong ramah banget",  
                "pesan": "Sehat-sehat iban"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kakak ini manis dan murah senyum",  
                "pesan":"Jangan sering-sering nyubit orang kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Kakak ini super tegas dan punya karismanya sendiri",  
                "pesan":" Jangan kebanyakan minum kopi kak, nanti asam lambung"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Kakak ini kalo ketawa kuat terus mukulnya juga kuat",  
                "pesan": "Jokesnya jangan darurat terus ya kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini kalem banget bawaannya",  
                "pesan":"Suka mukulnya dikurangin ya kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini kalo diluar pendiem, cuma kalo udah kenal asik",  
                "pesan": "Jangan suka muncul tiba-tiba terus ngajak ngobrol bang, kadang bikin kaget"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini kalo ngomong suka asal tapi kocak",  
                "pesan": "Semoga bisa jadi imam yang baik"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakak ini agak pendiem tapi kayaknya selalu sepaket sama kak Hanum",  
                "pesan":"Semoga selalu akrab sama kak Hanum ya kak"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "AAbang ini selalu ada tingkahnya",  
                "pesan":"Ditunggu emote barunya bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang ini gayanya keren",  
                "pesan": "Bagi ide outfit bang"
            },
                        {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini awalnya cool banget, pas udah keenal ytta",  
                "pesan":"Katanya skena padahl outfitnya old-money"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini kalem + anggun",  
                "pesan":"Semoga bisa jadi dancer"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini kalo ngomong tegas",  
                "pesan":"Semoga punya band sendiri bang"
            },
        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini kalem kalo serius, kocak kalo udah ga serius",  
                "pesan": "Semoga selalu jadi orang baik yang rajin menolong" #15
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakak ini kalem tapi lucu",  
                "pesan": "Semoga jadi atlit renang" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abang ini ga banyak ngomong",  
                "pesan": "Ajakin saya mabar bang" #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Susah bedain kak Dini sama kak Dina",  
                "pesan": "Akur terus sama kak Dina" #18
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
            "https://drive.google.com/uc?export=view&id=1SWEVK9Pj-cruEQW0am2nATSqTXDqaznR", #Bg Eggi ok
            "https://drive.google.com/uc?export=view&id=1zzDdXFn4qtPo-dMVolOo8mH4i4xXJrAO", #Kak Febiya ok
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
                "kesan": "Abang ini kedengeran logat wong kito",  
                "pesan":"Sehat-sehat orang perbatasan"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakak ini keren nama panggilannya",  
                "pesan":"Mau coba masakan kakak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini mukanya familiar banget",  
                "pesan":"Ajak saya explore Lampung bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abang ini kayak orang korea",  
                "pesan":"Terimakasih udah jadi medis selama kader"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Susah bedainnya sama kak Dini",  
                "pesan":"Semoga akur terus sama kak Dini"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak ini kalem tapi keliatannya ambis ",  
                "pesan":"Bagi tips belajar yang efektif kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini waktu jadi penutor matdas jago banget ngajarinnya",  
                "pesan":"Tutor jadi penutor yang baik kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini murah senyum, tapi logatnya mirip mama Saya",  
                "pesan":"Semoga logatnya tetap kental kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Saya awalnya susah nulis nama depan kakak, ternyata nama panggilannya nama tengah",  
                "pesan":"Bagi cara efektif buat ngeresume kak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Abang ini  pinter banget dari cara ngomongnya",  
                "pesan": "Bagi ilmunya jadi fullstack developer bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini kaleem cuma ternyata asik juga pas udah ngobrol",  
                "pesan":"Semangat jadi jurnal analist"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang ini asik banget cara ngomongnya",  
                "pesan":"Jangan kebanyakan main game ya bag"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abang ini super kalem dan sabar keliatannya",  
                "pesan":"Semoga bisa nuangin ilmunya ke banyak orang"
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
        "https://drive.google.com/uc?export=view&id=1qryXfNHklg2X7jYl3TBtPbSL3P_uu8AP", #Bg Arafi ok
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
                "umur": "79",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@yogyyyyyyy",
                "kesan": "Abang ini asik banget terus bisa ngobrol sama siapa aja",  
                "pesan":"Dikurangin gerakan tambahan ya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakak ini kayaknya nempel terus sama bang Yogy",  
                "pesan":"Langgeng terus sama bg Yogy ya kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini kalo ngomong berwibawa",  
                "pesan":"Jangan kebanyakan belajar kak"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang ini asik tapi ngomong seadanya",  
                "pesan":"Stop telat bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakak ini baik banget terus kalo ngomong lembut",  
                "pesan":"Dijaga sifat keibuannya"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini murah ramah banget tapi ngomongnya irit",  
                "pesan":"Semoga bisa menamatkan netflix"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Kakak ini kalau ngomong cepet tapi tegas",  
                "pesan":"Semangat humas abadi "
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak ini dari luar kayak pendiem gitu padahal asik",  
                "pesan":"Jangan sering-sering tidur kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini super anggun",  
                "pesan":"Jangan banyak-banyak minum es teh kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini kalau lagi formal sopan banget ",  
                "pesan":"Semangat ketuplak natal sains data"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini ga banyak ngomong tapi suka ketawa ",  
                "pesan":"Semangat belajar dan jadi panitia natal kak"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin Portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abang ini ganteng bener",  
                "pesan": "Semoga bisa jadi lead vocal grup band metal"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang ini lumayan kalem",  
                "pesan": "Semoga bisa jadi chef terus berbakti buat masyarakat (pengmas abis)"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini kalo misal belum kenal kayaknya ga banyak ngomong, tapi kalo sama temennya asik ngobrolnya",  
                "pesan": "Ayo kita banyak bercengkrama kak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Kakak ini super baik",  
                "pesan": "Semoga bisa punya jurnal sinta 1 "
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abang ini leadershipnya bagus terus kayaknya ngerangkul banget ke semua orang",  
                "pesan": "Saya tergoda masuk pengmas karena abang"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakak ini baik, ambis, suka ketawa, multitasking parah, jago ngomong, dan masih banyak hal baik lainnya",  
                "pesan": "Sehat selalu orang paling sibuk se-Teluk"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakak ini sangat-sangat extrovert",  
                "pesan": "Jangan pernah berhenti talk-active ya kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Abang ini pendiem tapi selalu keliatan sibuk",  
                "pesan": "Semangat terus sama kesibukannya bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini sabar banget cara ngomongnya",  
                "pesan": "Ditunggu artikel pribadinya kak"
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
        "https://drive.google.com/uc?export=view&id=14sl6577uNK8MpvHKMzGwuEcLEOI6_1qB", #Kak Rani ok
        "https://drive.google.com/uc?export=view&id=1SD8xwVSJWx2y3hXmwcW2k4AbJmnMukSi", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=13WXdXx2vOxM7VpaGpoA0awtJ5vMxDzIO", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1kJycwwidXEaqBRGBU6r5HuToupQ4Krl2", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=1-4mfib8QGiiLHWcuQAP2N-6AWkgMD7Dl", #Kak Azizah ok
        "https://drive.google.com/uc?export=view&id=1CkJV-CqxUTdeYI9Kjm3UN9HxgNZtvTZo", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1XtgBbEHieOkhhe5rFatgSgNRgP0KK_sc", #Kak Meira ok
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
            "kesan": "Abang ini ga pernah cape ngobrol sama orang",
            "pesan": "Sehat selalu orang ambivert(kayaknya)"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "Kakak ini ramah dan baik banget, tapi lengah dikit main game (gatau main game apa)",
            "pesan": "Semangat duta Kristiani SD"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "121450066",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "Abang ini kalem tapi ngomongnya tegas",
            "pesan": "Open tutor ngoding ga bang?"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": " Rajabasa",
            "hobi": "Denger musik",
            "sosmed": "@rannipu",
            "kesan": "Kakak ini gayanya tomboy tapi kadang ga tomboy",
            "pesan": "Gaya kakak keren banget, kayak anak FSRD ITB"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "Abang ini baik, lucu, penyanyi, king of PES",
            "pesan": "Semangat terus kuliahnya bang (semoga nilai prak strukdat saya aman)"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "Kakak ini rada pendiem",
            "pesan": "Jangan renang tapi gabisa renang ya kak, saya yang takut"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "Abang ini kalem tapi kalo ngomong to the point",
            "pesan": "Semangat terus olahraganya bang (semoga badannya makin jadi)"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "Kakak ini kalem dan irit kata",
            "pesan": "Kakak pasti nature lover"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "121450061",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "Abang ini kalem tapi asik kalo diajak ngobrol",
            "pesan": "Ayo kita makan mie pangsit gajah Siantar bang"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "Kakak ini ramah banget",
            "pesan": "Sselalu ramah sama orang ya kak"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "Abang ini gampang ketawa terus asik",
            "pesan": "Semangat selalu murah senyum ya bang"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "Kakak ini baik banget",
            "pesan": "Keep it up ya kak"
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Uw1-JI1qxLQUvA7Xf8pekGQ3txrKnnL", #Bang Andrian ok
            "https://drive.google.com/uc?export=view&id=1uqYm63Bs1Fj6Y_EPEG9ze0bhGrkUqcgs", #Kak Adisty ok
            "https://drive.google.com/uc?export=view&id=19IfLlXQ5Gow5JdWHAh8ohbGSfcRkAwrS",# Kak Nabila ok
            "https://drive.google.com/uc?export=view&id=1knhzTqGI8d6d2yhW8yqpqfh22pXZI-8n",# Kak Nabilah ok
            "https://drive.google.com/uc?export=view&id=1RxYxTvmnUAnPx8RCEbC9Ing39CMTZ7z5",# Bang Ahmad ok
            "https://drive.google.com/uc?export=view&id=1PgdpKVgEiH3ER3UTBFAuZ9vqle5WEJ7z",# Bang Danang ok
            "https://drive.google.com/uc?export=view&id=1CytN_hx6Ey2g2rP5AmpCbGAY-POy6Fu9",# Bang Farrel ok
            "https://drive.google.com/uc?export=view&id=1zGAQZcw27dBH45Q7qIoL3kEc7nMknKx6",# Kak Tessa ok
            "https://drive.google.com/uc?export=view&id=1YczO_c0rDqAa_dqtGs0WbT-pO1CqjPPC",# Kak Alvia ok
            "https://drive.google.com/uc?export=view&id=1DUFlMAhodm34DOAz5CNVcda2bl4GIS2g",# Kak Dhafin ok
            "https://drive.google.com/uc?export=view&id=1nIzybshnCGvCCCxaOO-NtQJ1nawfBY4x",# Kak Elia ok

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
                "pesan": "Semoga bisa jadi fotografer profesional ya bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakak ini senyum terus orangnya lembut terus",  
                "pesan": "Jangan pernah berubah kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakak ini saya kira orang Riau dari logatnya",
                "pesan": "Semoga rejekinya lancar terus kak biar ga berhenti ngitung uang"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "Awalnya saya bingung sama nama kakak, ternyata kak Nabilha ada yang make H dan ada yang ga pake ",
                "pesan": "Semoga selalu bisa jadi contoh yang baik kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Abang ini lebih banyak diem dan kalem gitu",
                "pesan": "Ajak saya jalan-jalan bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "Abaang ini public speakingnya bagus banget kacau",
                "pesan": "Ajarin punya confidence segede abang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "Abang ini aurnya selalu cerah (pasti sering ngerawat badannya)",
                "pesan": "Semoga selalu konsisten ngegym dan olahraganya bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kakak sangat postive vibes",
                "pesan": "Seemoga bisa jadi penulis terkenal kak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kakak ini kalem dan pendiam, tapi waktu ngomong logatnya keluar",
                "pesan": "Semangat terus di dunia perkuliahan kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abang ini santai dan asik diajak ngobrol",
                "pesan": "Fokus terus sama olahraganya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakak ini semangat banget kalo ngobrol",
                "pesan": "Sehat-sehat iban"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VBAar8G7oqJwhOLGZfm96xQNVypoq38M", # bang tao ok 
            "https://drive.google.com/uc?export=view&id=1syX6XrXzAeTWNeJ8ZwfhtecM6cRbe3zT", # kak elok ok 
            "https://drive.google.com/uc?export=view&id=1Fov5SpqCK8jV3zEDbtBfZAxy2LTrsbBO", # bang kai ok 
            "https://drive.google.com/uc?export=view&id=1OzNnfoYrkiIN6AdbYP-rCU95zeGHqxbQ", # bang arsal ok 
            "https://drive.google.com/uc?export=view&id=1clzHh3lkenTxF7V3FX_sOwfjMzz5XK-x", # kak arsyi ok
            "https://drive.google.com/uc?export=view&id=179hjuj9lnTVLwEAId3C5nbI6u7MvKfUw", # kak juju ok
            "https://drive.google.com/uc?export=view&id=1FjUv3Aetnhgd65ycWmwAuLuQReyg-BBb", # kak nel ok
            "https://drive.google.com/uc?export=view&id=1ooajHVfqdXIjTAz1kMgQrZXxQBoOrX_J", # kak try yani ok 
            "https://drive.google.com/uc?export=view&id=1plBJrVTD0OMMxRsWQXk0GPADdi18D0Y0", # kak dwi ok
            "https://drive.google.com/uc?export=view&id=1buUiBFPLuqEKYfIVb_OMnKfCRu0mFOFX", # bang gym ok
            "https://drive.google.com/uc?export=view&id=1Z_N6wvEfPUNRRHFj2wTs4Rrr19oCIagG", # kak nasywa  ok
            "https://drive.google.com/uc?export=view&id=1t6k96LxddFfuvESz5VuKnW4kNLQvEDUA", # kak priska ok
            "https://drive.google.com/uc?export=view&id=1oIjV5fIXd9ZyEgPi1pD8tgyijuuobkNz", # bang abit ok
            "https://drive.google.com/uc?export=view&id=1xVVVueag0HaA8SsiwmL4C7dvbIssCpx1", # bang hermawan ok ok
            "https://drive.google.com/uc?export=view&id=1Sx5QdsCilcNSzMgK_2t0j4fhe5lcgr2y", # kak khusnun nisa ok
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
                "kesan": "Abang ini kalem dan hemat kata banget, cuma disegani banyak orang sepertinya",
                "pesan": "Semangat sama tugas-tugas akhirnya bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Jujur salfok karena kakak ini cakep banget",
                "pesan": "Semangat terus jadi editor handal kak"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Abang ini kalo misal belum kenal kayak serem, tapi setelah banyak ngobrol seru pol",
                "pesan": "Semoga ketemu hobinya ya bang (Saya yakin hobinya bercandain orang)"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "Abang ini asik sama kece banget",
                "pesan": "Bagi parfum bang, soalnya abang wangi banget"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Kakak ini orangnya ga banyak ngomong tapi lumayan tegas dari cara ngomongnya",
                "pesan": "Seemoga selalu bisa jadi panutan ya kak"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Kakak ini sangat baik, keibuan, soft-spoken, merangkul dan masih banyak lagi",
                "pesan": "Sehat selalu dan semangat sama kesibukannya kak, jangan pernah cape jadi orang baik"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakak ini super extrovert, kalo ngobrol juga ekspresif",
                "pesan": "Jangan cape jadi orang ekstrovert ya kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Kakak ini gayanya gaul banget",
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
                "kesan": "Kakak ini kalo ketawa bisa ga berhenti",
                "pesan": "Tetap receh ya kak"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang ini super keren, tegas bisa, soft-spoken bisa,dan masih banyak hal baik lainnya",
                "pesan": "Semoga bisa selalu share ilmu PDDnya bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "Kakak ini kalem tapi lucu kalo ngomong",
                "pesan": "Jangan keliatan banget jametnya kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "Kakak ini kalem dan ga banyak ngomong, tapi kalo dapet topik bisa yang paling banyak ngomong",
                "pesan": "Semoga selalu bisa jadi orang paling asik kak"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "Abang ini duta discord, duta stiker, duta pdd dan duta lainnya",
                "pesan": "Jangan berhenti ramah sama orang ya bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Abang ini aktif dimana-mana, ngoborol sama orang juga asik dan baik banget",
                "pesan": "Semoga selalu bisa jadi orang sebaik ini bang, society need people like you bang"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakak ini kalo dari luar kalem, tapi sebenanrnya asik-asik aja kalo diajak ngoborol",
                "pesan": "Semangat terus kak dengan kesibukan DIYnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
