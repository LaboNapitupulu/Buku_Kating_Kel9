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
                "kesan": "oo ini abang kahim",  
                "pesan":"semoga bisa jadi ketua terus di organisasi lainnya, hehe"# 1
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
                "pesan":"akur akur sama bang gumi yaa bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kotabaru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "cantik euy",  
                "pesan":"terima kasih tips untuk bikin notulensinya kak"# 1
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
                "pesan":"semangat kak nyekre nya"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "1121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "akrab sama bang pandra nih",  
                "pesan":"semoga pada rajin bayar kas yaa kak"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kotabaru",
                "hobi": "Membaca",
                "sosmed": "nadillaandr26",
                "kesan": "nama kita mirip kak",  
                "pesan":"semangat nagih kasnya kak"# 1
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
                "kesan": "cheerful banget kakaknya",  
                "pesan":"terima kasih sudah sharing ilmunya kak"
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal": "Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "kacamatanya bagus kakk",  
                "pesan":"spill beli kacamatanya kak hehe"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal": "Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya lumayan humoris",  
                "pesan":"tetap menjadi humoris yaa kak"# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "rajin nugas nih kayanya",  
                "pesan":"tips nugasnya dong bang"
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Depan kobam",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "sering ketemu nih di panitiaan duta",  
                "pesan":"rekrut jadi staff pusdat dong bang hehehe"
            },
             {
                "nama": "Mirza Yusuf Rabbani",
                "nim": "122450118",
                "umur": "21",
                "asal": "Jakarta",
                "alamat": "Korpri",
                "hobi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "emang keliatan kalo abangnya anak jakarta",  
                "pesan":"keep your vibes yaa bang"
            },
             {
                "nama": "Muhammad Farul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal": "Surakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "abangnya humble banget",  
                "pesan":"jangan dicukur kumisnya yaa bang hehe"
            },
             {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "22",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "vibesnya kakak kakak baik gitu",  
                "pesan":"spill outfitnyaa dong kak"
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal": "BSD",
                "alamat": "Teluk",
                "hobi": "Buka liat linked in, puasa senin kamis, ngerjain tugas di draw.io",
                "sosmed": "@berlyyanda",
                "kesan": "namanya bagus bangett",  
                "pesan":"tetaplah menjadi berlian seperti nama kakak yaaa"
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal": "Malang",
                "alamat": "Jatiagung",
                "hobi": "Baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "kakak mirip shakira coc",  
                "pesan":"semoga pintarnya setara bahkan lebih dari shakira coc yaa kak"
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "keren bangett keterima msib",  
                "pesan":"tips beauty with brain nya dong kak"
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
                "kesan": "udah familiar nih sama abang ini",  
                "pesan":"gas jadi ketuplak lagi yaa bang"
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
                "pesan":"tetap semangat mengurusi kami semua yaa bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kost, Sukarame",
                "hobi": "memancing keributan",
                "sosmed": "@elisabethh_",
                "kesan": "sering ketemu nih sama kak abeth",  
                "pesan":"humble terus yaa kakk"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "cantik banget kakak ketuplak",  
                "pesan":"tips glowingnya dong kak"
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
                "pesan":"jaga kesehatan yaa kak"
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
                "kesan": "cantik babyface gitu kakaknya",  
                "pesan":"ajarin bahasa padang dong kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "pernah ketemu pas riuh pertama nih",  
                "pesan":"semoga nugasnya lancar yaa bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "mirip sama bang devyan",  
                "pesan":"semoga semangat terus sampai semester akhir bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kalem dan baik kakaknya",  
                "pesan":"semangat pp dari way hui - itera nya ya kak, hehe"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "humoris dan mirip sama bang deriii",  
                "pesan":"keep your humour yaa bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "humoris tapi masih bisa tegas juga",  
                "pesan":"tetep jadi humoris aja yaa bang"
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
                "pesan":"semoga ipk nya 4.00 yaa bang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kakaknya manis sekalii",  
                "pesan":"spill bahasa melayu nya dong kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "murah senyum bangett",  
                "pesan":"terima kasih sudah humble yaa bang"
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
                "pesan":"semangat nemenin kami lomba bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "mirip sama kak tria yunanni eksternal",  
                "pesan":"jangan lupa makan yaa kakk"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "main game",
                "sosmed": "@raflyy_pd",
                "kesan": "kayanya orang lampung deh",  
                "pesan":"jangan suka begadang yaa bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "sering ketemu sama kakak inii",  
                "pesan":"makasii yaa sudah ramah kak"
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
                "pesan":"tips jadi kadep mikfes dong bang"
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
                "pesan":"ajak ajak yaa kak kalo ke kobum"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "baikk dan ramah abanngnya",  
                "pesan":"terima kasih sudah berbagi ilmu yaa bang"
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
                "pesan":"semoga kebaikan abang pas nolong saya di medis terbalaskan yaa"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "keren kakaknya",  
                "pesan":"spill beli topinya kak"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "vibesnya kakak baik baik",  
                "pesan":"keep your vibes yaa kak"
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
                "pesan":"semoga ga cape ngajarin aku yaa kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "aku suka bajunyaaa",  
                "pesan":"spill bajunya beli di mana kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kalem banget kakaknya",  
                "pesan":"semangat kak di mikfesnya"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "kayanya sering liat juga deh",  
                "pesan":"semoga sehat selalu yaa bang"
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
                "pesan":"terima kasihh sudah ramah kak"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "bagus namanyaa",  
                "pesan":"semoga takdir abang sama seperti nama depan abang yaa"
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
                "pesan":"terima kasih sudah nanyain kondisi saya pas tumbang kemarin sebelum poto, hehe"
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
                "kesan": "easy going banget",  
                "pesan":"tetep menjadi seperti ini yaa bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Travelling",
                "sosmed": "@ramadhitatifa",
                "kesan": "parfumnya wangi bangett",  
                "pesan":"spill parfumnyaa kak hehe"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "style hijabnya cantikk",  
                "pesan":"tutor hijabnya dong kakk"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "kaya familiar gitu abangnya",  
                "pesan":"jangan telat ngampus terus yaa bang"
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
                "pesan":"terimakasii sudah menjadi cheerful kak"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "mirip 2nd runner up duta 2023",  
                "pesan":"rekomen pilem yaa kakk"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "mirip kak natasua kania dept ssd",  
                "pesan":"mau denger kakak nyanyi dongg"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kacamatanya jugaa baguss",  
                "pesan":"tips cantiknya kak hehe"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "aku suda familiar nih dan yeay nama kita sama",  
                "pesan":"role modelku inii"
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
                "pesan":"semoga ga capek ngajarin saya ads yaa bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "rambutnya cantikk",  
                "pesan":"spill haircare gasii kak"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "banyak experiences nih abangnya",  
                "pesan": "tips banyak experience yaa bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "ramah sekali abangnya",  
                "pesan": "tetap ramah yaa bang"
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
                "pesan": "semoga kita bisa deket yaa kak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "mirip artis siapa gitu",  
                "pesan": "terima kasih sudah meluangkan waktu untuk wwc yaa kak"
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
                "pesan": "rekomendasi game dong bang hehe"
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
                "pesan": "mau juga dong kak main sama adek adek sd"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "jauh jugaa di rajabasa",  
                "pesan": "semangat pp rajabasa - itera nya kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "asprak ads saya juga nih",  
                "pesan": "ajarin bikin jurnal juga dong bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "mirip kak dini",  
                "pesan": "saran artikel yang bagus untuk dibaca sebelum tidur kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1N2e08BOjWb0NUsG5TKtFWSDA7qVKUjTQ", #BgDimas ok
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
            "kesan": "keren banget jadi ketua mulu",
            "pesan": "semoga ga homesick yaa bang"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "aku suka senyum kakakk",
            "pesan": "rekomen novell kakk"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "orang liwa nih abangnya",
            "pesan": "jangan lupa hangatkan badan kalo pulkam yaa bang"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "rajabasa",
            "hobi": "denger musik",
            "sosmed": "@ranniu",
            "kesan": "outernya baguss",
            "pesan": "dipake terus yaa kak outernya, baguss"
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
            "pesan": "jangan cape cape ngajarin saya ya bang"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "friendly nih kakaknya",
            "pesan": "belajar renang bareng yuk kak hehe"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "kayanya pernah ketemu deh kita",
            "pesan": "rekomen olahraga untuk pemalas kaya saya bang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "super semangat pp dari lampung selatan ke lampung selatan lagi kak",
            "pesan": "tips berkebun dong kak"
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
            "pesan": "rekomendasi film sedih dong bang"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "pesawaran nih",
            "pesan": "semangat merantaunya kak"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "abang ini juga humoris nih",
            "pesan": "sebulan lagi natal bang, mau kue yaa"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "aku suka angka NIM nya",
            "pesan": "boleh minta bacaan untuk survive sems 3 ga kak hehe"
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sXM3ySfIGovHwqm3F8E5buny-gMzUeud", #Bang Andrian ok
            "https://drive.google.com/uc?export=view&id=1ma4_PsIwQO_sRJrytURQjdR0rtRNUoXo", #Kak Adisty ok
            "https://drive.google.com/uc?export=view&id=1CRMifrYiQbcfHT6cFSB5O7Wzkprpv0se",# Kak Nabila ok
            "https://drive.google.com/uc?export=view&id=19cmuS4M283GPHo0VUVsQjFVVF-ldBy-q",# Kak Nabilah ok
            "https://drive.google.com/uc?export=view&id=1BIndXYAy0XCEnrAz9iBDBQA_tXWlWamh",# Bang Ahmad ok
            "https://drive.google.com/uc?export=view&id=1IHW4OLG2VK7WaMlvaUgUYg4D-we_3PoP",# Bang Danang ok
            "https://drive.google.com/uc?export=view&id=1eIsNDaz0EBEwbfNyg3wdZZOapH9nGzQ_",# Bang Farrel ok
            "https://drive.google.com/uc?export=view&id=1k8nWRIy4wu2XvFVV0ZrGLepfR7zlT7HA",# Kak Tessa ok
            "https://drive.google.com/uc?export=view&id=1OVUVT2q5mMAelTeeTQu2igoqDW_9ZpuN",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=15yknxUA8TWvR_cwseLV9I8747-JGsJHF",# Kak Dhafin ok
            "https://drive.google.com/uc?export=view&id=1Ha8y4fp0AdNF-LeGXrP5YYUAkGxwHmJV",# Kak Elia ok

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
                "kesan": "kaya orang lampung",  
                "pesan": "semoga hobinya segera ketemu bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakak ini baik",  
                "pesan": "jaga kesehatan yaa kak di tahun ketiga ini"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "senyumnya manis sekalii",
                "pesan": "itungin uangku dong kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "kacamatanya bagus kak",
                "pesan": "spill tempat belinya dong kak, aku lagii butuhh"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "namanya mirip seperti temen seangkatan saya",
                "pesan": "spill pernah jalan jalan kemana aja bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "jago banget marketingnya",
                "pesan": "semangat terus panitiaan dutanya bangg"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "sering ketemu sama abang ini di bkl",
                "pesan": "langgeng yaa bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "namanya mirip teman sekelompok saya",
                "pesan": "sabar ya kak melewati jalanan pemda nya"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "hobi kita sama kak hehehe",
                "pesan": "ayo tonton vid windah yang plant vs zombie cina kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "pernah beberapa kali ketemu abang ini",
                "pesan": "tetap semangat berolahraga banggg"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "kakak ini mirip artis siapa gitu",
                "pesan": "ayo kapan kapan nyanyi bareng kakk"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18eBsHTMi1qq2Zi3xULLf7utA7F4MlF6c", # bang tao
            "https://drive.google.com/uc?export=view&id=1Kuf-aTAP50VuuZH75mxU-lyEQ4raQ9ey", # kak arsyi
            "https://drive.google.com/uc?export=view&id=1VLeP3Wjp1YTnJ9RNHDRfOVwBkqPB4B-h", # bang kai
            "https://drive.google.com/uc?export=view&id=1rwL8_P3HjQ4fHXBGoW2YLsYVoCknnPe2", # bang arsal
            "https://drive.google.com/uc?export=view&id=1ZC2t3X8cXinn91O1q0H7WMHbd7KrhzI7", # kak elok
            "https://drive.google.com/uc?export=view&id=10S5vLAbWHFd2cOyKhQojs7k0yrHi2-sC", # kak juju
            "https://drive.google.com/uc?export=view&id=1jfyvF-c6DTee33QpfbQOcGfyuUUzPA_8", # kak nel
            "https://drive.google.com/uc?export=view&id=1sasA0bKDJUFv4xkAPH1EhTw8hGqb2rK8", # kak try yani
            "https://drive.google.com/uc?export=view&id=1oGTXYHRVpHMYm9oNIiQqIAoVINFYbzAC", # kak dwi
            "https://drive.google.com/uc?export=view&id=1LbO21FN5937IZsxUM4n_Jg8OjdoUZpjy", # bang gym
            "https://drive.google.com/uc?export=view&id=1v1OUeQwrw0kLN20uuQSCvmp0fkyiJdqm", # kak nasywa
            "https://drive.google.com/uc?export=view&id=1AilftMdDlRauO5IWMhG3GPXT2joRP7fV", # kak priska
            "https://drive.google.com/uc?export=view&id=1Pb5JetfmlnoO6u1L0Q-Fxn73YYA7kgP-", # bang abit
            "https://drive.google.com/uc?export=view&id=1y9KGPdf39LX_pGgfm5K0v67T7VlY6OmG", # bang hermawan
            "https://drive.google.com/uc?export=view&id=1xwgpVHa_jy384m5uLUkjg9KiblGO4aTW", # kak khusnun nisa
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "21",
                "asal": "Makassar",
                "alamat": "Sukarame",
                "hobi": "Nonton",
                "sosmed": "@wahyudnt_0202",
                "kesan": "jauh banget rumah abang ini",
                "pesan": "semoga jarang homesick yaa bangg"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "akamsi nih",
                "pesan": "ayo kak ngonten bareng"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "chill banget abang ini",
                "pesan": "semoga udah ketemu hobinya ya bang"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "mirip seleb siapa gitu ya",
                "pesan": "boleh minta parfumnya ga bang hehehe"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "asprak ads akuu nii",
                "pesan": "tips ngedit dongg kak"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "kakak daplokku tersayangg",
                "pesan": "ayo fangirlingan bareng kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "humoris, imut, dan lucu bangett",
                "pesan": "kayanya seru deh kak kalo kita hangout bareng"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "orang liwa bukan yaa kakak ini",
                "pesan": "hati hati kalo lewat korpri yaa kak"
            },
            {  
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "Scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "wuihh orang jambi",
                "pesan": "hati hati kalo pulang malem ke pemda yaa kak"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "daplok kebanggaan saya nih",
                "pesan": "ajarin ngotak ngatik kamera juga dong bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "sering ketemu nih yaa kita kak",
                "pesan": "tips bersih bersih untuk pemalas kaya akuu kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "wah orang palembang",
                "pesan": "boleh jastip pempek candy ga kak hehehe"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "humoris, asik, dan mirip seleb siapa gitu yaa abang ini",
                "pesan": "semangat terus bang jualan dan desain stikernya"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat toll",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "abang asprak alpro nih",
                "pesan": "hati hati yaa bang tiap hari ngampus lewat jalan deket toll"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "diy pake printer maksudnya gimana tuh kak",
                "pesan": "tips jadi pemateri dong kakk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()


# Tambahkan menu lainnya sesuai kebutuhan
