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
                "pesan"	:"sukses dan semoga cepat lulus dan bisa pulang ke payakumbuh dengan membanggakan ortu "# 4
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
                "pesan"	:"seomoga amanah dan bendahara yang jujur"# 5
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
                "pesan":"semangat terus kuliahnya kakak yang sangat menginspirasi!!!" #1
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
                "pesan":"semangat terus kakk dan semakin percaya diri"# 3
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang ",
                "sosmed": "@jeremia_s_",
                "kesan": "Bang jerr asikk, baik dan ramah",  
                "pesan":"semangat terus kuliahnya bangg, bahagia selalu orang baik" # 4
            },
            {
                "nama": "Feriyadi Yulius ",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "kalem or pendiam?",  
                "pesan":"sukses selalu bang dan makin berjaya"# 5
            },
            {
                "nama": "Mirza yusuf mirzani",
                "nim": "122450118",
                "umur": "21",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "main kucing",
                "sosmed": "@myrrinn",
                "kesan": "oppa sd22",  
                "pesan":"makin cool bang dan jangan sombong"# 6
            },
            {
                "nama": "Muhammad Farul Aditya  ",
                "nim": "121450156",
                "umur": "22",
                "asal":"surakarta jatim",
                "alamat": "Pahonam",
                "hobi": "ngopi ",
                "sosmed": "@fhrul.pdf",
                "kesan": "pernah ketemu sebelumya tapi lupa",  
                "pesan":"makin sukses bangg, apakah kita pernah ketemu sebelumnya bang?" # 7
            },
            {
                "nama": "Annisa cahyani surya ",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tanggerang",
                "alamat": "Jatimulyo",
                "hobi": "baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "pintarr, sepertinya anak kesayangan pak ardika",  
                "pesan":"ketemu kakaknya di program pak ardika , sukses terus ya kak"# 8
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
                "kesan": "face nya agak mirip kakak nim kuh",  
                "pesan":"kurangi banyak diamnya kak" #10
            },
            {
                "nama": "Anisa Dini Amalia ",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "Jati Agung",
                "hobi": "baca webtoon",
                "sosmed": "@anisadini10",
                "kesan": "indenpendent women",  
                "pesan":"sukses dunia akhirat kakakku yang sangat menginspirasi"# 11
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
                "hobi": "memancing keributan",
                "sosmed": "@elisabethh_",
                "kesan": "rambut kakak lucu dan cantik",  
                "pesan": "semangat terus kakak cantik,& maapkan saya jika ada salah, jujur diluar alam kesadaran saya kak" #2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "canti & berwibawa",  
                "pesan": "makin berwibawa dan sehat selalu kak" #3
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
                "kesan": "cantik ",  
                "pesan": "Semangat kakak cantik, i am looking kak hanum mirip kak afifah" #6
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
                "kesan": "abang nya kocak, dan asik",  
                "pesan": "Bahagia dan sehat selalu abangkuh" #10
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
                "pesan": "Semangat kuliahnya kak dan jangan banyakin diamnya kak heheh" #13
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
                "pesan": "Semangat gapai cita citanya bang " #14
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
            "https://drive.google.com/uc?export=view&id=1eKLMbY4SkPTq7Oz8UCR5fFyos8zd0jN4", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1O0CUwuxZdmPuoEgdQSHM1ururqHj_T87", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1rDEtanzd4DLcYJz8zhRbMGOh-zasBTNG", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=12h25fX0R5s0uRxNHyn0nR5bGEZS3NZ0B", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1mggnCSnwrv7x244RaCab81pA_g6IUssr", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1drp7xkJ8QdP0KwVXxKS4r2BqWzOrBOX3", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1GR_izPUGEeyGVoey8QpilLezSKZyBaEB", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1pTjUAqytKR2sQcJi46r23nbUZVu9zRNu", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=12ATJFg85z7Lp_Up9MoxyilODkfCcbTZH", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1aVSLI7Bc8-s_PxjevvMQvuW3CgQdeWnm", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1zsNCEfi8AyO3dOlYAfTlfyKB9Rt8gGCc", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1FNWESruBRjhMV__oogOTpsluOBwdFlh1", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1eKLMbY4SkPTq7Oz8UCR5fFyos8zd0jN4", #Bang Randa ok
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
                "kesan": "abggnya cool",  
                "pesan":"semangat kuliahnyaa bang dan sukses selalu"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "kakak kalemm",  
                "pesan":"semooga lulus tepat waktu kakakk"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "abg nya mirip pahlawan indonesia",  
                "pesan":"semangat kuliah dan lulus nilai terbaikk"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abg nya mirip orang korea",  
                "pesan":"semangat teruss bangg dan semoga benaran bisa ke korea"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "kakaknya lucuu apalagi kalau sama kembarannya",  
                "pesan":"semangat kuliahnya kakak dan akur terus sama saudaranya kakkk"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "kakak kalemm dan pendiam",  
                "pesan":"semangat kuliahh nya kakak semoga dilancarkan"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "kakak pintarr dan pertama kenal di sdm",  
                "pesan":"semnagt kuliahnya kakak dann semoga dapat cumlaude"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "kakak nya baikkkk dan ramahh",  
                "pesan":"semangat kakak, semoga dapat ipk terbaikkk"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "kakaknya agak mirip kakak nova",  
                "pesan":"semogaa cepat lulus kakak dan semogra prediksi ku tidak salah"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "sangatt baiikkk dan pintarrr",  
                "pesan":"semangat teruss bangg, cepat lulus, dan ipk tinggi"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "kakak pendiam dan kalemm",  
                "pesan":"semoga dapat ipk tinggi kakak dan jangan sering diam diam kak"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "abgnya pendiam dan pemalu",  
                "pesan":"semoga cepat lulus bang dan dapat cumlaude bang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "bang randa sangat baik hati tidak sombong dan suka menabung",  
                "pesan":"sukses teruss banggg, dan ipk 4.0 "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1W0iwXibaCqC9xzcVHDMvKn_UXZHRfL6A", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=16sH8yQrAGsJsDvBNVdAGRLGx1YIqXqJ6", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=1wKUYVuRw8LiR4tlQK1eS4c3jazDw_fFE", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=1CsnzGqElI1kaYef4mFuZ-YX9qA_6TZiL", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=17yW7ZFy9NtsvwWF82OPHfIFCG825nOwW", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=18pXrmPijFAIVYF3jC2y8ZHSETyTOvOEf", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=1yqyzIFSRI21j2xw-BP3hzvMjTxQwJEn1", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=1-FE9yQudqWHJ_rPHmBVIVnRqKAPw_t5L", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1w3VW6g1DVkt5JZwEd2t9UnvjNmo_co2L", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1e-FaRHTKyijTE35Tm4FNMcO98wKBVzCz", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=1KJ9kB-nes3sIe2oryY4lSnDmrMISkofK", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=15wyqwwAiYs_l72zi7eyIIvGKK9-RpQxN", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id=1KLidLL8NQ_qGBdjlK5FJdK5X07JHyndy", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1EMY1sYg2Be9m9d1iYpVe9AXNiMI3j_xV", #Kak Asa ok 
        "https://drive.google.com/uc?export=view&id=13Ao2uizdil2exZKe5YwjY-lpaDn-eyEf", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=1vtaFgY35UjfWZJqMiZatPp7usShu9ctj", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1XLiIOEjXM6hkSfY9tk9MBOIw80nvnRa_", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1aL90w1XGFP1G8AlYJ98Vh0CITJ5-qAyX", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1ClwTEohhnDXWNdQfDBggM73rzBPP4uqj", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=1ClwTEohhnDXWNdQfDBggM73rzBPP4uqj", #Kak Tria ok
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
                "kesan": "abg yogiii baekkk",  
                "pesan":"semoga selalu bersama kak diita wkwkkwk"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "ibuable",  
                "pesan":"selalu bahagiaa selalu sama bang yogi kak hehheh"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "kak wawa cantikkk se eksternal",  
                "pesan":"bahagia selalau sama abg psda nya kakkk"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "cool dan wibawa",  
                "pesan":"makin kritis banggg"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "wibawa dan aktif beyull",  
                "pesan":"makin sukses dan sehat selalu kak"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "cantik, imut pendiam",  
                "pesan":"makin sukses dan semoga exploring kita lancar kak"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "sibukkk but i am fun with you",  
                "pesan":"sehat selalu dengan kesibukannya kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "pendiam dan kalem",  
                "pesan":"semngat kuliahnya kakak dan banyakin interaksinya kak biar makin kenal kita"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "wibawa dan orang penting itera",  
                "pesan":"sukses selalu kakk dan bahagia selalu bersama bang sofyan kak heheh"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "wibawa and i like yourhair (gondrong)",  
                "pesan":"kata teman saya abg lebih tampan kalau rambutnya pendek"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "kalemm pendiam dan pemalu",  
                "pesan":"ternyata first impression saya salah kak"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "manisss",  
                "pesan": "sukses terus dan semangat semester akhirnya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "keren, kece",  
                "pesan": "suksess dan sehat sehat sehat selalu bang, btw teman saya ada yg naksir bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "ceriaaa",  
                "pesan": "makin ceriaa kak dan sukses terus kakkk"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "adem ayem",  
                "pesan": "somoga selalu istiqimah un"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "wibawa",  
                "pesan": "kerennn , semakin kerenyo uda"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "sibukk dan aktif",  
                "pesan": "sehat selalu dan semangat kakak sibukk"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "kak alya cantik, awalnya ku pikir galak",  
                "pesan": "kak alyaa sehat selalu kak"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "pendiam",  
                "pesan": "semngat banggg , mampir terus ke meja saya pas ads ya bang heheh"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "ceru abizz",  
                "pesan": "sehat sehat kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1qmjv3CRxvqDPBLyaeGWxIPtS1uWyuot3", #BgDimas ok
        "https://drive.google.com/uc?export=view&id=1IxAh5x64e-NEuArqjewvw2gKbTjyUmVU", #Kak Catherine ok
        "https://drive.google.com/uc?export=view&id=1nfgn0_CSGxPhjVACBQaYtC9KkSgdrwRu", #Bg Akbar ok
        "https://drive.google.com/uc?export=view&id=1XzJGc384I_WqMSFk1pIpYFCEEGSiRI4t", #Kak Rani ok
        "https://drive.google.com/uc?export=view&id=1D1Pvl_7XRv0Paz0x9xudiczuo_ziEt0P", #Bg Rendra ok
        "https://drive.google.com/uc?export=view&id=1jM4-0OFEhpCQeEa80Y1Z3g5O7YWLNdQq", #Kak Salwa ok
        "https://drive.google.com/uc?export=view&id=1uBfJMZDDk_0-71pI0WFD6i7pPR-ZLwb0", #Bg Ari ok 
        "https://drive.google.com/uc?export=view&id=1SSWH3xWeo_xRR5VFYMweXsNtf0pSRy1j", #Kak Azizah ok
        "https://drive.google.com/uc?export=view&id=1B3Cdtzl2asN7G0lKufK8f5iF9zQZfYbQ", #Bg Josua ok
        "https://drive.google.com/uc?export=view&id=1QD1EtdGHFMpRzxQuVu5Xi9xY46I3j0-S", #Kak Meira ok
        "https://drive.google.com/uc?export=view&id=1vZ4YTnN8uIv3o8hVVqBLY3LW1SeOXjzY", #Bg Rendi ok
        "https://drive.google.com/uc?export=view&id=1f8iqcHvU5QGjrzmf_buevXpBNe8QPHrN", #kak Renta ok

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
            "kesan": "keren begete abg ketang",
            "pesan": "makin berjaya bang dimm"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "pendiamm",
            "pesan": "banyakin interaksi kak biar kita makin kenall"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "baik tampan rupawan",
            "pesan": "semngat ngodingnya bangg sampai jadi hacker keren"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Raja Basa",
            "hobi": "dengar musik",
            "sosmed": "@ranniu",
            "kesan": "dari wajah terlihat pemarah",
            "pesan": "asli nya tidak sama sekali"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "masyaallah hobi mengaji",
            "pesan": "semoga selalu diberkati allah"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "luarbiasaa tutor renang kakk",
            "pesan": "mau renang bareng dong kak"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "kalemm, diammnya masyaallah",
            "pesan": "sehat selalu bang, info olahraga bareng bang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "nyunikkk hobi berkebut di era sibuknya kuliah",
            "pesan": "boleh minta sayur dikebunnya ga kak, mau masak soup"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "ku kira bang islam",
            "pesan": "semoga ingat tuhan selalu bang"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "cantikk masyaallah tabarakallah",
            "pesan": "info buku bacaan islami kak"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "aku kira abgnya harmon",
            "pesan": "bernyanyi sambil beribadah"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "kakaknya imuttt",
            "pesan": "sehat selalu kak"
        },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12rnbBAhjruelhPNj_JlniXWOuAXOZE6W", #Bang Andrian ok
            "https://drive.google.com/uc?export=view&id=1mI9AppvUxL6jIPNyWD7LlWoHxhKznWO8", #Kak Adisty ok
            "https://drive.google.com/uc?export=view&id=1ws2cCz2IdrSYS-A2AfJ9LKawGPy7VJh6",# Kak Nabila ok
            "https://drive.google.com/uc?export=view&id=1uf_BGXJCcV9eVEPzow5xKZJDFmQ_m8a7",# Kak Nabilah ok
            "https://drive.google.com/uc?export=view&id=1oX51nYqqM71GrgkPhTECVDueQkGErsHT",# Bang Ahmad ok
            "https://drive.google.com/uc?export=view&id=1BASC6JTYR5DOcrIwUMcNmvXrKFfHj5UG",# Bang Danang ok
            "https://drive.google.com/uc?export=view&id=1VxqeozOXmNp7JW2Zhzlhr6Pzn-yEKxZn",# Bang Farrel ok
            "https://drive.google.com/uc?export=view&id=1twU5KfHygVJLx-DblpZpYTVFpWE0l8Pr",# Kak Tessa ok
            "https://drive.google.com/uc?export=view&id=1wW2R7bqZCA_YFEM2t9vjr3zWFzKGB3my",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=1GztF8D4NNJGBUIUdOt1q0c0AGfylQrhS",# Kak Dhafin ok
            "https://drive.google.com/uc?export=view&id=1DVb9IQIC76_fhlEr-cJRaZe03_FQNMZa",# Kak Elia ok

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
                "kesan": "kerenn dan gacorrr",  
                "pesan": "semakin menyala abgkuh"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "beakk dan murah senyumm",  
                "pesan": "infokan film untuk menghilangkan pening dong kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "mirip artis tapi lupa",
                "pesan": "semoga uangnya makin banyak pas di itung kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "ibuablee sekalih kakk",
                "pesan": "semoga mimpi indah ditidurnya kakkk"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "kaget dari padang",
                "pesan": "semoga bisa ketemu dipadang bang"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "marketingnya keren banget",
                "pesan": "semngat terus bang sampai jadi pengusaha besar"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "berdemagee dan wibawa begete",
                "pesan": "makinn sukse bangg dan jangan sombong, abgnya cocok sama pacarnya"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "wajah nya keliatan banget bataknya kak",
                "pesan": "semoga bisa jadi penulis sukses kakak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "kakaknya mirip pj tugas ku kakak deva anjani",
                "pesan": "seomoga sukses teruss kakakku"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "kalemm pendiam pemalu",
                "pesan": "info olahraga bareng bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "alis kakaknya bagus",
                "pesan": "mau dengar kakanya nyanyi dong kakkkk"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()
else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fPSkeMvigy9_FDCKYwxOGmm4o5WIJuyN", # bang tao ok 
            "https://drive.google.com/uc?export=view&id=1tNKUgyvrMEWoHcmZ9K-KnoX67gfmRjYY", # kak arsyi ok
            "https://drive.google.com/uc?export=view&id=18WnMMtcWKquu9mv9HtU6rLyJpowkuVMu", # bang kai ok 
            "https://drive.google.com/uc?export=view&id=19VajxHMmSUPZPRi-_x3Y0yyG-1jgt_6E", # bang arsal ok 
            "https://drive.google.com/uc?export=view&id=1JHZquqokaxv8jz5ghr0Pr-xjVphB2okl", # kak elok ok
            "https://drive.google.com/uc?export=view&id=1ZLHQyPlgNbyyn61KbVsUXkunqmTjOamu", # kak juju ok
            "https://drive.google.com/uc?export=view&id=1g-kRv7FualsnNSuT6bf8YGD0CMoxtHYd", # kak nel ok
            "https://drive.google.com/uc?export=view&id=1c2iKR0PlB9lYPu7GWwwKSFr-AzXWLH5X", # kak try yani ok 
            "https://drive.google.com/uc?export=view&id=1nH0HLgMrMYcBDOOGaMVFhmCMaXJXZnzy", # kak dwi ok
            "https://drive.google.com/uc?export=view&id=1hrKdnjqcUITMqUQUIkYlmMJ0l8urHRHQ", # bang gym ok
            "https://drive.google.com/uc?export=view&id=1owBK0QgpDHoRmDPjjZT6ID1rZSSBhHMf", # kak nasywa ---
            "https://drive.google.com/uc?export=view&id=1IF5_MYFdQS0TfjhHqWFwbU1QfyTqmjW6", # kak priska ok
            "https://drive.google.com/uc?export=view&id=1ip2UKpiMBWIuLxAKiEs49gKS2a8eNt5A", # bang abit ok
            "https://drive.google.com/uc?export=view&id=1w1wjnlqlb0WjKjpBxPrxvia7MPaPw61D", # bang hermawan ok ok
            "https://drive.google.com/uc?export=view&id=1v5FYY5A_g10fXe1RyAzo9K7z5mva3dqf", # kak khusnun nisa ok
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
                "kesan": "kaget abgnya dari makasar",
                "pesan": "semoga betah dilampung bang"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "aaaa kakakkuuu gemesss lucu lope lopee",
                "pesan": "sukses selalu kakak arsyy cihuyy kuuu"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "namanyaaa menarik",
                "pesan": "kalau hobinya masih belum ketemu biar aku bantu cari bang"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "abgnya maniss, sukak sama abg abg pake kacamataa",
                "pesan": "rekomendasi dong bang wangi parfume yang tak terlupakan"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kak elekk cantik dan gemess",
                "pesan": "ceritaain dong kak cara jadi sekre"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "awwww kakaku bangaiman ibu periii yang baik hati tidak sombong dan suka menabung yang ter segala galanya",
                "pesan": "kakak pokonya ga boleh ninggalin kita orang,"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "kak nela or kak neliz?",
                "pesan": "ceria selalu kak dimanapun berada"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "",
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
                "kesan": "sukakk kakaknya asikk",
                "pesan": "semnagt kakk di medraf yang katanya super sibuk"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "abgku pintar, jago ngoding, baik hati seperti ibu periku",
                "pesan": "bang gym yok bisa sama kak juju hehhehe"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "kakanya mirip teman sd kuhh",
                "pesan": "kakak tutor dongg biar kamar ku bersih selalu"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "kakaknya mirirp seseorang tapi lupa",
                "pesan": "mau dengar aku bernyanyi tidak kak?"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "kerenn, multitalent",
                "pesan": "tutor bangg jalanin hidup dg hobi sebanyak itu bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "pintar gagah dan pemberani",
                "pesan": "sukses selalu bang dan makin berjaya"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "alim tapi tegasss",
                "pesan": "semakin sukses kak dann tegass dan produktif selalu"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()







# Tambahkan menu lainnya sesuai kebutuhan
