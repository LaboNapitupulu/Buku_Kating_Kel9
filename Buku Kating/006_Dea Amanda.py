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
            "https://drive.google.com/uc?export=view&id=1e_bWpaa4B6DI15UgmNa8IQHmOyYFl_NB",
            "https://drive.google.com/uc?export=view&id=1b0FF6uAJ24IJGf5ehEEPZU0UApUGAGp7",
            "https://drive.google.com/uc?export=view&id=1ovUtuohdnq2vudTjmk3xYxxehMuUPUw9",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1mOKw2gQ7qg5TW3a28KvCPjPBLqN9Z41W",
            "https://drive.google.com/uc?export=view&id=1yxDgumdy11aBB1K91uZCzedDqWcTujNu",
        ]
        data_list = [
            {
                "nama"	: "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkhasirma",
                "kesan"	: "berkarisma sesuai namanya",  
                "pesan"	:"jadilah pemimpin yang amanah dan sukses selalu "# 1
            },
            {
                "nama"	: "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	: "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	: "berwibawa",  
                "pesan"	:"jadilah pemimpin ya amanah"# 2
            },
            {
                "nama"	: "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	: "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	: "baik, dan humble",  
                "pesan"	:"sukses selalu dan kuliahnya dilancarkan"# 3
            },
            {
                "nama"	: "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	: "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	: "ramah",  
                "pesan"	:"sukses dan semoga cepat lulus"# 4
            },
            {
                "nama"	: "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	: "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	: "kalem",  
                "pesan"	:"seomoga amanah"# 5
            },
            {
                "nama"	: "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	: "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	: "profesional",  
                "pesan"	:"semoga amanah dan dapat dipercaya"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qgZivvT27lAv2rAvtqdUCjDHur_2ppE4", #1
            "https://drive.google.com/uc?export=view&id=1qX9gJr-90sSXE7GUewgSCjZBeBhpXGZ-", #2
            "https://drive.google.com/uc?export=view&id=1qUpnn8V6zpAd2FbipnE2-Ha0KWBcNeVY", #3
             "https://drive.google.com/uc?export=view&id=1qlgSYbx3SUI2cTaBoO9GbZtsviIcQI10", #4
            "https://drive.google.com/uc?export=view&id=1qY4my859dtfcXkJRKWAaQGJrxxR0tnU6", #5
             "https://drive.google.com/uc?export=view&id=1qimrCx4Av1CCAyNr0Mjr8Vkpz15YTd9j", #6
            "https://drive.google.com/uc?export=view&id=1rNjJmeZ5fUvSvlrPyOO_JgE7Vp3cJVTy", #7
             "https://drive.google.com/uc?export=view&id=1rQIhwwC6kmliFbvYUCcoHFOi9N7c_3ZJ", #8
            "https://drive.google.com/uc?export=view&id=1rAF8dt5aYjNbuYIetTxN7ssiw4siHpL9", #9
             "https://drive.google.com/uc?export=view&id=15MMrZP6G-iY2uR5kPBb41yWpNIUe9ZzV", #10
            "https://drive.google.com/uc?export=view&id=1qakcRtH8HLeL36-RsPQuXx9B2DARdnR3", #11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity ",
                "sosmed": "@trimurniaa_",
                "kesan": "Kk nia sangat aktif berbicara",  
                "pesan":"semangat terus kuliahnya kakak !!!" #1
            },
            {
                "nama": "Claudhea Angeliani ",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "lampung timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 2
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 3
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang ",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jerr asikk",  
                "pesan":"semangat terus kuliahnya kakak !!!" # 4
            },
            {
                "nama": "Feriyadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 5
            },
            {
                "nama": "Mirza yusuf mirzani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 6
            },
            {
                "nama": "Muhammad Farul Aditya  ",
                "nim": "121450156",
                "umur": "22",
                "asal":"surakarta jatim",
                "alamat": "Pahonam",
                "hobi": "ngopi ",
                "sosmed": "@fhrul.pdf",
                "kesan": "Kakaknya asik diajak ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!" # 7
            },
            {
                "nama": "Annisa cahyani surya ",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Jatimulyo",
                "hobi": "baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 8
            },
            {
                "nama": "Berliana enda putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobi": "suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 9
            },
             {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor ",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakaknya asik dibawa ngobrol",  
                "pesan":"semangat terus kuliahnya kakak !!!" #10
            },
            {
                "nama": "Anisa Dini Amalia ",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobi": "baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "kakanya asyiik dan tenang liatnya",  
                "pesan":"semangat semester ganjil nya kakak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12CS_ixDPLoLBOmM3kMKUr7D6u11gWAB9", 
            "https://drive.google.com/uc?export=view&id=14GYINcskw8zBLnKMs4iUJD1f02uo6k_t"
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
                "kesan": "Tegass dan berwibawa",  
                "pesan": "Sukses selalu buat kakak dan makin keren "
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "romance",  
                "pesan": "Semoga makin bersinar seperti namanya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fTlLLsl1Wkwdy1e8UedBHLuXFuQWspYk", #1
            "https://drive.google.com/uc?export=view&id=1qV62qy2ofhqFVu-jE5PMHmXHUBjU4OfA", #2
            "https://drive.google.com/uc?export=view&id=1h_bsqHLFWCWoxjLB454TU0dklUq_Xlu1", #3
            "https://drive.google.com/uc?export=view&id=1GQi5ULwnCYju4FjwTSuG_ARbUvl6NedX", #4
            "https://drive.google.com/uc?export=view&id=1jgQLa-n0LfPvSiP7Q8z45iyEQrBGCNHI", #5
            "https://drive.google.com/uc?export=view&id=1hMgpmHHaK3sQgNf3rpqkR4UJMvQFfy7a", #6
            "https://drive.google.com/uc?export=view&id=13sUOGMZcQl0x0BAgzyjvtKHJ65f6W8W0", #7
            "https://drive.google.com/uc?export=view&id=11a5Fl-EEeTzlH7CamcBlQbXqZ_y4ERZ3", #8
            "https://drive.google.com/uc?export=view&id=1EsXHKqHuWucGYsFfvU_Xuk8tdIRPt3lj", #9
            "https://drive.google.com/uc?export=view&id=1VDCKnl9wNyAriIo21Tr59pTK-i7Apa0r", #10
            "https://drive.google.com/uc?export=view&id=1br8PSolrB9y7Vk4blxE3_12AvZJ7temZ", #11
            "https://drive.google.com/uc?export=view&id=1uCaTdGudbYt5qLi03YxYY2WpfBi42rXi", #12
            "https://drive.google.com/uc?export=view&id=1sWtrv0jippUrD7JtZzckD299_xpPE49Y", #13
            "https://drive.google.com/uc?export=view&id=1186Y8xvn7YzsYjd8o7DJGzQqD2J7HJ5i", #14
            "https://drive.google.com/uc?export=view&id=1bOfUW2k_2aO5we5xq4fai8Ozf0Dzfk6k", #15
            "https://drive.google.com/uc?export=view&id=1YpKKvf7Tht5UhM6DL8b7YT7uRtBs2lUp", #16
            "https://drive.google.com/uc?export=view&id=1FwSmUwyszyUiZH7dE93e35n4JCPSSKnG", #17
            "https://drive.google.com/uc?export=view&id=1saK1Jw3nsjgMS5RnNOoUreSkdgactztU", #18
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
                "kesan": "profesional",  
                "pesan": "Semangatt kuliah dan mendidik angkatan 23 bang" #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kos, Sukarame",
                "hobi": "",
                "sosmed": "@elisabethh_",
                "kesan": "rambut kakak lucu dan cantik",  
                "pesan": "semangat terus kakak cantik" #2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "berwibawa",  
                "pesan": "makin berwibawa" #3
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "cewek cool",  
                "pesan": "semangat membina angkatan 23 kak dan jangan lupa jaga kesehatan" #4
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "pintar, rajin, vibes kaya buk mika ",  
                "pesan": "Semoga bisa jadi dosen kaya buk mika" #5
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "cantik",  
                "pesan": "Semangat kakak cantik" #6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "cowok dingin",  
                "pesan": "jangan terlalau dingin bang" #7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "abg nya kocak",  
                "pesan": "Sering sering bercandanya bang" #8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "jarang lait kak oktavia, ternyata tim kader",  
                "pesan": "semangat mengkadernya kak" #9
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abang nya kocak dan asik",  
                "pesan": "Bahagia selalu abangkuh" #10
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "profesional",  
                "pesan": "Semangat dan sukses selalu bang" #11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "bagaikan ai berjalan, pintar ngoding",  
                "pesan": "semangat belajar dan mengajar kami bang" #12
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kak Rafa pendiam",  
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
                "kesan": "humble",  
                "pesan": "Semangat gapai cita citanya bang" #14
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "menaungi sekalihh",  
                "pesan": "Semangat olahraganya bang" #15
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakak sangat cantikk",  
                "pesan": "semangat mengemban tugas di orba kak" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "abangnya sangat pendiam",  
                "pesan": "banyakin ngobrolnya bang" #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya pendiam",  
                "pesan": "semoga kompak terus sama kembarannya kak" #18
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kP2vGf5rgq_LrTcQnKApW3T7kk3WvUaT", #Bg Rafi ok
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




# Tambahkan menu lainnya sesuai kebutuhan
