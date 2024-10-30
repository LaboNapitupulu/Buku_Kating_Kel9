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
            "https://drive.google.com/uc?export=view&id=1iOQLQe7biXtCxRuYXmyMa1vRTHE8ojM_",
            "https://drive.google.com/uc?export=view&id=1dLzo4Am4yobPY-jAMXT5KukNpNol5uP6",
            "https://drive.google.com/uc?export=view&id=1hJIz9KdSIt4xhkQsdy3yBRhGXOkLdcT9",
            "https://drive.google.com/uc?export=view&id=14kQFzU_QcbOJgwhGg7RWAipDfWR-tQNS",
            "https://drive.google.com/uc?export=view&id=1iY5fptVh8QtVo1OWxmJLimp8yq6HbWa0",
            "https://drive.google.com/uc?export=view&id=1vETWfqKdLBQo4kDiCoQ_5jOWIo3ecizR",

        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar ",
                "hobi": "Main Bola, Belajar",
                "sosmed": "@gumilsngkharisma",
                "kesan": "Abang ini tegas banget",  
                "pesan":"Semangat ya bang"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jalan Bawean 2, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Wah tetangga saya",  
                "pesan":"Semangat ya bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Cantik euy",  
                "pesan":"Semangat nyekre nya"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Jalan Nangka IV",
                "hobi": "Dengarin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "cantik kakaknya",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "1121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "baik banget kakaknya",  
                "pesan":"semangat terus kak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Membaca",
                "sosmed": "nadillaandr26",
                "kesan": "baik kakaknya",  
                "pesan":"semangat terus kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1VGLljCBu1W4FlHJmaZUAwSMoCKf-xrZ3",
            "https://drive.google.com/uc?export=view&id=1p1HvT0_NwCFiEwYEeall1AMv3QV_Wf5E",
            "https://drive.google.com/uc?export=view&id=1cTPnjWmbijw2No1nYk_OC-vE2GluRpDW",
            "https://drive.google.com/uc?export=view&id=11hi02LB-SdI9ej9BXbCZmsec2UMvAGcF",
            "https://drive.google.com/uc?export=view&id=1tfcp_NHfqJrgUgD8_nexVtv0XDQUyC2J",
            "https://drive.google.com/uc?export=view&id=14N-C2x-y8puLO9Rh0Xb4g6w6kKhJke1O",
            "https://drive.google.com/uc?export=view&id=142SZI0IjVt7lKhK5AYzWL3Py2Nz-fIbI",
            "https://drive.google.com/uc?export=view&id=1k2ZwZlnlsUdQHRhGukrz75bKHMsNRps4",
            "https://drive.google.com/uc?export=view&id=1pufL9stOQVwQgl0_UAA7GtbD0nqqPtUW",
            "https://drive.google.com/uc?export=view&id=1P0_R6vL0hWmA4Bf3n8jLcQkC27Mz0P16",
            "https://drive.google.com/uc?export=view&id=1Oi39BhNnLrQ4U1ki3l2R5wUrGILi9o--",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal": "Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Depan kobam",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Mirza Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "BSD",
                "alamat": "Teluk",
                "hobi": "Buka liat linked in, puasa senin kamis, ngerjain tugas di draw.io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal": "Malang",
                "alamat": "Jatiagung",
                "hobi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!"
            },
           
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e1cQfiQrwWICHfv2kqw5iqefkla0BexY", 
            "https://drive.google.com/uc?export=view&id=19WN-RUENVRbBwJd_luWJNJKekNKQUb3I", 
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
                "kesan": "public speakingnya bagus bangett, ramah dan baik juga",  
                "pesan":"semangat yaa kak TA nya "
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "baik banget, ramah juga",  
                "pesan":"gas jadi ketuplak lagi bang"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17pfBiDicLs2Wx1wYDyy3g-YUrxXGXIRW", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1xq1rpVifkUQu5Ar47pg2K6LNRGc379qU", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1nRiSRXoAWWN9IwqR_dvGH0iAhsqsYdew", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1nKKS0NtHMj1ZZ9Vn1i3rxgQ3BRGsZSvV", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1mw7qqIKTLo3_gwMCoQcyNavCW6bqdr8F", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1n4_J7iIxhAIU5Hbe3fd90_9n6jN6F0ot", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1n24fYcKxmsdh_YMZTE_aEm9EIFcR0r3y", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1Ll1578N_0TkhLPRMfhsuI1lU7JgPFUeu", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1nAndX3aZTE9X90-6pgK9ycOkbJDH4so9", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1lmohXujT_6f3NaJ-l6dWt54FMNtVmavb", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1lcAL_pOpnHyBWyNLhneJT3ab5ZbWYr9t", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1lsGcSZQEX3VeJ4bCuM7uNwJLRvkmH5Wj", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1mGjI0q4_fn12RBEHsn4KTIA0RuyMqir8", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1m-mu6bVkY2sM2iNuSr_0C7cNiaXtUCvF", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1tpbiWfIk9WjkBIsdYldqwtONgaAOuMZ3", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1mZoS9L1kVZEx4BPEWz_-1xVLLYhJaLk6", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1mQVEVgbynH7IJlSF2q4tvbI656AA4kPy", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1mcREh3t1IbvrEH_c10r7gjUVaVIRk-ui", #Kak Dini
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
                "kesan": "lumayan cool",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kost, Sukarame",
                "hobi": "",
                "sosmed": "@elisabethh_",
                "kesan": "sering ketemu nih sama kak abeth",  
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "cantik kakaknya",  
                "pesan":"semangat kuliahnya ya kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "sebenernya asik kok kakak ini",  
                "pesan":"semangat terus kak kuliahnya"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "ambis banget kakak ini",  
                "pesan":"semangat ngambisnya kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "cantik kakaknya",  
                "pesan":"semangat kak kuliahnhya"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "baik abangnya",  
                "pesan":"semangat terus bang kuliahnya"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "baik abangnya",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "baik kakaknya",  
                "pesan":"semangat kak kuliahnya"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "humoris banget abangnya",  
                "pesan":"semangat bang kuliahnya"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abang ini juga humoris",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "abang ini pinter",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "baik banget kakaknya",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "abang ini ramah banget",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kotabaru",
                "hobi": "menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "berwawasan sekali abang ini",  
                "pesan":"semangat kuliahnya bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "baik banget kakaknya",  
                "pesan":"semangat kuliahnya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "main game",
                "sosmed": "@raflyy_pd",
                "kesan": "baik banget abangnya",  
                "pesan":"semangat terus kuliahnya bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "kalem baik nih kakaknya",  
                "pesan":"semangat kuliahnya kak"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GAKmUTgePAiGksWyYGOeeQGEamb5C9ft", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1kN8_7gfwwcG7Szv_WhnimgbB7u-zFDd1", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1JWhOAPD5niaKok7HQEbqusqPixVW6Sxz", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=1SalqFm0LlggWPAKCq7LS8gsjpLR8f3rK", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1_fgsTlgGmaq5YM2pLPY0BSl53N94KW-n", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1NN6ZbQ0VF1REDEyZP44x7QnK5voS4ev8", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1khFsXDd7cnN2Hi8JGWHBYyET3dwjER2R", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1eZNZWShe4MWKsx_CklK64OPxTWqrNoyL", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1IdFmSt1bzXil2OuJybpKLzoHafDieWUS", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1NuCtukoVOUb2F3rk3QH6ZnWq618c8m5H", #Bg Eggi ok
            "https://drive.google.com/uc?export=view&id=1EoedkNF8g1j1MM1_N5p-E-XnfS5xq8sy", #Kak Febiya ok
            "https://drive.google.com/uc?export=view&id=1gBiMUlaZRCItjqdVdseN_B1wjozkdLbC", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1gwMnCUrIguIUIHTtDdFpp3cQy2_P14_N", #Bang Randa ok
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
                "kesan": "wuih kadep mikfes",  
                "pesan":"semoga sukses bang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "bagus banget namanya",  
                "pesan":"sukses terus ya kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "baik banget abangnya",  
                "pesan":"sukses terus bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abang medis kader nih",  
                "pesan":"semoha sukses terus bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "baik banget kakaknya",  
                "pesan":"sukses terus kak"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "baik banget kakaknya",  
                "pesan":"sukses terus kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakak asprak strukdat nih",  
                "pesan":"sukses terus ya kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "baik banget kakaknya",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "baik banget kakaknya",  
                "pesan":"sukses terus bang"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "baik abangnya",  
                "pesan":"sukses terus bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "imut kakaknya",  
                "pesan":"sukses terus ya kak"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "baik banget abangnya",  
                "pesan":"sukses terus bang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "abang medis kader juga nih",  
                "pesan":"sukses terus ya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1PV1uCPa-CuUq6oD0Jyru0jZmcNV5b5OT", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=1zNJ8dbSZA6Ehq8KgcBeuvBxsJmfAv4wZ", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=1vTTFmPaNMofwVMUFk3-qjbsijmDstwng", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=18Xne8jDXVemqszttaiRz5-L-DtmjqYjy", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=1oI8p8oj2BbCvCxu93yGfS1orvLtTSVDK", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=1Q2ScuuR18f8pECmFmbfabLy7ZpPYbcqp", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=1P4OV3O9-1f1syk-4sJXmY1pjc6CntPDh", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=1ZLTMMWDmOr1ZxjxobehSC5eSwHH2jkg9", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1c-Nl-KBHevzpdM2yLwhmxFthWyowtcFo", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1bYXT4KZDX_8OnwMlNZTjY8sXkfD9Z9x8", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=18OPXu4zWpaRFmV4bfO5ClZBf4CYlKTej", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=1duxsrQLgKrumBr1lsk6qltoznEXKghJE", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id=1gwHCCcUZofEwg2ULxq1xQsK5Z23-Q1PE", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1OTHFD1GzOiYB1gXkYsJkqCNpALR0nsQ1", #Kak Asa ok 
        "https://drive.google.com/uc?export=view&id=1PldXkJ3orfnoaFwx7xhESvNjpE4CTP4W", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=1eoTnei87n9ajlzyLKs3HhWTPZWLc0vgZ", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1xkaj57cCyKNoBhvkgu55wZJdLTMQ1Li_", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1_xZXV0wYpUACanTBI3t-A3xzXVS7-dg9", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1r5UjQvhpnuxvn6tOjri5zE62SS2NhPmK", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=17KPq7y1xQbI0DJuhxKOFtEzVOb8btQzi", #Kak Tria ok
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
                "kesan": "humoris banget",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Travelling",
                "sosmed": "@ramadhitatifa",
                "kesan": "kakaknya baik",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "baik, cantik",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "baik abangnya",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "cheerful kakaknya",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "imutt kakaknya",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "baikk kakaknya",  
                "pesan":"semangat terus kakk"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "baik bangett kakaknya",  
                "pesan":"semangatt teruss kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "nama kita sama nih kak",  
                "pesan":"semangat terus kak jasmine role model kuu"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "abang asprak ads nih",  
                "pesan":"semangat terus bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "cantik kakaknya",  
                "pesan":"semangat terus kak"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "banyak experiences nih abangnya",  
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "baik banget abangnya",  
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "solehah banget kak",  
                "pesan": "semangat terus kakk"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "imut kakaknya",  
                "pesan": "semangat terus kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "imut nih abangnya",  
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "keren banget kakak ini pengalamannya",  
                "pesan": "semangat terus kak"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "baik banget kakaknya",  
                "pesan": "semangat terus kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "baik banget abangnya",  
                "pesan": "semangat terus bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "imut kakaknya",  
                "pesan": "semangat terus kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=", #BgDimas ok
        "https://drive.google.com/uc?export=view&id=1C3lQykCkGAtEqS9OPdNAhfZPK25wiEns", #Kak Catherine ok
        "https://drive.google.com/uc?export=view&id=1XFyUYJ3LEBDvwpc0Ozlw-dPn5YvA0r-L", #Bg Akbar ok
        "https://drive.google.com/uc?export=view&id=1BIUdENdpMI7HG9uw7oc2MVQiByz5EeNB", #Kak Rani ok
        "https://drive.google.com/uc?export=view&id=1rM454hxGC8nqs2belqPbkVcHmwQ39MVO", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=1tMwUVrmEnSuzBxc2JsLCoZMHx2AUbDGw", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1QH9QPoU12EXqc7Suw7vuU026pu6Vdjnx", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=15p-0B08xUuXoEsYn9BO5KWnqaEte9TNi", #Kak Azizah ok
        "https://drive.google.com/uc?export=view&id=1vZEN_7XP3zo5r5btXM0c0Oss95LoLbLa", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1UTElFv671Lz29ETU4KwSE08wCEG_wlx-", #Kak Meira ok
        "https://drive.google.com/uc?export=view&id=1Bc6Mlq5-DYkS-ypDPKV3kNmmHqmDlh1j", #Bg Rendi ok
        "https://drive.google.com/uc?export=view&id=1rlufzIRvIjjPjHQG0uvdFtbM5LQ3Ep3i", #kak Renta ok

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
            "kesan": "asik banget abangnya",
            "pesan": "semangat kuliahnya bang"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "imut banget kakaknya",
            "pesan": "semangat ya kuliahnya kak"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "baik abangnya",
            "pesan": "semangat kuliahnya bang"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "",
            "hobi": "",
            "sosmed": "@",
            "kesan": "baik banget kakaknya",
            "pesan": "semangat kak kuliahnya"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "asprak strukdat yang sering saya mintain tolong nih",
            "pesan": "semangat terus bang kuliahnya"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@",
            "kesan": "baik banget kakaknya",
            "pesan": "semangat kuliahnya kak"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "baik banget abangnya",
            "pesan": "semangat kuliahnya bang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "baik banget kakaknya",
            "pesan": "semangat terus kuliahnya kak"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "religius banget",
            "pesan": "semangat terus kuliahnya bang"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "kakaknya baik sekali",
            "pesan": "sukses terus kuliahnya kak"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "baik banget abangnya",
            "pesan": "semangat terus bang"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "baik sekalii",
            "pesan": "semangat kuliahnya kak"
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


# Tambahkan menu lainnya sesuai kebutuhan
