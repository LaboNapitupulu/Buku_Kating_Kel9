import streamlit as st
from streamlit_option_menu import option_menu # type: ignore
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
            "Dapartemen MEDKRAF",
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
            st.write(f"Nama            : {data_list[i]['nama']}")
            st.write(f"NIM             : {data_list[i]['nim']}")
            st.write(f"Umur            : {data_list[i]['umur']}")
            st.write(f"Asal            : {data_list[i]['asal']}")
            st.write(f"Alamat          : {data_list[i]['alamat']}")
            st.write(f"Hobi            : {data_list[i]['hobi']}")
            st.write(f"Sosial Media    : {data_list[i]['sosmed']}")
            st.write(f"Kesan           : {data_list[i]['kesan']}")
            st.write(f"Pesan           : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z_8hFGkASmVVtQheA5C_uYdHoq152yIM",# bang gumilang
            "https://drive.google.com/uc?export=view&id=16f3FM4fVkA5rXSlItLBFQq3qVN4_nIkH",# bang pandra
            "https://drive.google.com/uc?export=view&id=1JlUx1qvykOYKZtVBlgzGDXampO9-brw0",# kak meliza
            "https://drive.google.com/uc?export=view&id=1-0c7DbD84urcdTtS1c5_QitobMkbvF7V",# kak putri 
            "https://drive.google.com/uc?export=view&id=1LN8mGq1-Nr3dYJoVd4KWQycmETiTG7fy",# kak hartiti 
            "https://drive.google.com/uc?export=view&id=1d9PrTJPI1wzr6raN9EeJnbdfczzq4QFE",# kak nadila 
        ]
        data_list = [
            {
               "nama"	    : "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkhasirma",
                "kesan"	: "Abangnya sangat keren",  
                "pesan"	:" Semga sukses dikarirnya  "#1

            },
            {
                "nama"	    : "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	    : "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	    : "kadang suka lucu",  
                "pesan"    	: "Semoga jadi orang sukses"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota Baru",
                "hobi": "Drakoran ",
                "sosmed": "@wulandarimeliza",
                "kesan": "suaranya terlalu lembut",  
                "pesan":"Semoga bertahan sampe akhir"# 3
            },
            {
                "nama": "Putri Maulidia Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "JL. Nangka IV",
                "hobi": "Dengerin bang pandra gitaran ",
                "sosmed": "@ptrimaulidia_",
                "kesan": "jago berbicara ",  
                "pesan":"semoga menjadi orang yang sukses"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "suara yang merdu",  
                "pesan":"Semoga jadi artis "# 5
            },
            {
                "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadilaaandr26",
                "kesan": "orang yang seru asikk",  
                "pesan":"Semoga jadi orang yang selalu sukses dimasa depan"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NjXqIQvqBCfAlQob6-AjZgrxtI0V-HyE",#1 
            "https://drive.google.com/uc?export=view&id=1n9h8VScFm9GhzP0-0ZpwqBNDSIPj_NZn",#2 
            "https://drive.google.com/uc?export=view&id=1t9paUlTPguIJQ1jOxZdWWoAGduSyBQFl",#3  
            "https://drive.google.com/uc?export=view&id=1xLkgHVfSNgHUb2HBYa67YSOiZ6ZssVsy",#4 
            "https://drive.google.com/uc?export=view&id=1xE787bte8aXoRLTikxPljyArmNoakue8",#5 
            "https://drive.google.com/uc?export=view&id=1Ewq0Z8e9WqmsmMfADVwsBLivyGtWjYx7",#6 
            "https://drive.google.com/uc?export=view&id=1xZ6FhtT0KcTs5GmpUD5P8tr3Lbi7gqhw",#7 
            "https://drive.google.com/uc?export=view&id=1bT6HdnkqwMQlwMTVGby_rBnqMk85YL4G",#8 
            "https://drive.google.com/uc?export=view&id=1WrdA0fQi5ysEgp-NSTYxzWYdPDdcwzVs",#9 
            "https://drive.google.com/uc?export=view&id=1tAcVBArUBuCB5FsTZidN5JcfKEH0Mx6F",#10 
            "https://drive.google.com/uc?export=view&id=1ONb1dWYDLlXN5evfaC3Hfp1ccbv2sj9G",#11 
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexcity",
                "sosmed": "@trimuniaa_",
                "kesan": "kakaknya seruu , assikk suka bicara",  
                "pesan":"Tetap semangat sampai akhir "#1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "kakaknya baik terus keliatanya asikk",  
                "pesan":"semangat terus kuliahnya kakak "#2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "1221450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "kakaknya dapat dilihat pinter dalam semua matkul",  
                "pesan":"cepat lulus dan sukses kakak"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@anisadini",
                "kesan": "kakaknya yang seru asikk",  
                "pesan":"Cepat suksess kak"# 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "1221450124",
                "umur": "21",
                "asal":"Saltiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "kakaknya terlihat kece",  
                "pesan":"kakaknya lucu seruu"# 5
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok Tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "kakaknya lucuu terus kek random",  
                "pesan":"semangatt kuliah kak "# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul",
                "kesan": "abangnya kecee seruuu",  
                "pesan":"semangat terus kuliahnya bang"# 7
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca Buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangg nya kalem tapi kece",  
                "pesan":"semangatt kuliah bangg"# 8
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya terlihat kalem tapi keren",  
                "pesan":"semangat bang kuliahnnya"# 9
            },
            {
                "nama": "Jeremie Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin Orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Orangnya asikk seruu",  
                "pesan": "semangat terus bang kuliahnya"# 10
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD Tanggerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linkedln , puasa senin kamis dan ngerjaiin tugas",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya kalem sekali",  
                "pesan":"semangat terus kuliahnya kakak"# 11
            },    
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1wKGP9_yT2JA9xSFGiXxR7q72RJAk_ob-", 
            "https://drive.google.com/uc?export=view&id=17HYFsSor4w0JRQfTfoE1QPpM2NGAcwQC", 
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
                "kesan": " kakaknya asik ",  
                "pesan":" semoga sukses terus kak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "orangnya seruu asiikk",  
                "pesan":" semoga berjalan terus apa yang selalu dikerjakan"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lSeMnLeMg51qOPgZr6Jd0RIMWwRfiNQV", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1RLyicG8ayOfmt93eRrYPGttB7qRul5GF", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1FxJxMXevdqviuOpOlTzmN5fBLqb0LNe4", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1rYHuwCfDmLOagQNdGzGhW0h2zM7yj6gI", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1wNVMHjFF9LeF1f4OonQe70znRMTvVG6x", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1Etkf0NfoGMGOnT4-bxGRgtZ1WS1TslIO", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1wn78I1OJnVOgdTwU_4Ry2XTJOVGchJ1C", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1RTCaA9m2pAf8agSDtMkMFYxR-rdxEqay", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1dfWWvOgzEluZUOvurWEb3p8vASk_UGfh", #Kak Okta
            "https://drive.google.com/uc?export=view&id=16XhwgZa8N6ki42OjKmYCSfvLXPpBTQ83", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1LSn0IpxS9wn3a54e97jrYS2oY9pjWIVE", #Bang Jo
            "https://drive.google.com/uc?export=view&id=10mKvfCZEBCjNyuQnovKbw9Gl8WvnQK38", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1__NaGPWdJtJkwKV9aG2rnrXh9nYIh16Y", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=18lNrHCQ5yKHXkddzQ4I5dkzesoOjxPqJ", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1ICJX4zcgzmj5GrwN9yyMZOytWkG_cash", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1uzmtaYc7DbJh4VELQ_uspWPwIZlbPGoM", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=18lNrHCQ5yKHXkddzQ4I5dkzesoOjxPqJ", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1YEDCJ_supouR-C9dY5Ah-8D7JVw_ffoa", #Kak Dini
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
                "kesan": "abangnya keren jiwa tegas ada berwibawa",  
                "pesan":"semoga sukses bangg"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobi": "Memancing Keributan",
                "sosmed": "@elisabethh_",
                "kesan": "asik dan klo ngomong seruu",  
                "pesan":"cepat sukses kak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "kakaknya asik klo dah ngorbol seruu",  
                "pesan":"tetap semangat kak buat kedepanya"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "seruu asik klo adh ngobrol kakaknya",  
                "pesan":"tetap semangat kak dan semoga cepat sukses buat kedepanya "
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "keliatan jiwa pintarnya",  
                "pesan":"semoga cepat sukses kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "dilihat seru asikk",  
                "pesan":"semoga cepat sukses kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "seru abangnya kadang random aja",  
                "pesan":"semoga cepat sukses bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "abangnya seruu asikk klo udah akur",  
                "pesan":"semoga cepat sukses semangat bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kakaknya asik serru",  
                "pesan":"tetap semangat dan cepat sukses"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "abangnya asik banayak ketawa",  
                "pesan":"semoga cepat sukses bang "
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya asik seru klo udah mulai ngobrol ",  
                "pesan":"semoga cepat sukses bang"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "top gamerr nyabkeliatan bang, skena nya oke",  
                "pesan":"tetap semangat terus bang "
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "asik kakaknya ",  
                "pesan":"semoga setiap apapun yang dilakukan permudah"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "asikk seruu",  
                "pesan":"semoga lulus dengan nilai terbaik"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "asikk abanya klo dah ngobrol",  
                "pesan": "semoga dipermudahkan segala perjlanan " #15
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "seru kakaknya asikk",  
                "pesan": "terus semangatt kak" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "keknya pendiem tapi klo dah ngobrol asik ",  
                "pesan": "semoga sukses terus " #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "orang baik seru",  
                "pesan": "tetep semangat terus kak" #18
            },       
            ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tJ_AH_-ofZ1tDKjuu-EA7oIjJ7JTCVFx", #Bg Rafi 
            "https://drive.google.com/uc?export=view&id=1UaR3tdvN739c695Nz2wdALNOfQ9e0DJQ", #Kak Anova 
            "https://drive.google.com/uc?export=view&id=1FVlUjo8FxqKxj-gash8LXT70GUqcl3XQ", #Bg Ahmad Akbar 
            "https://drive.google.com/uc?export=view&id=1kyFJ8b1tq8GoEA-8kwtFYoYvox4-A0oQ", #Bg Fadhil 
            "https://drive.google.com/uc?export=view&id=1zY38Ndiqdzyd4ICYdQHRq0OpPEO2MuNV", #Kak Dina 
            "https://drive.google.com/uc?export=view&id=14sl69AoixVfaRm2ABxCxdLdLWQJioEYa", #Kak Dinda 
            "https://drive.google.com/uc?export=view&id=1Ago7FAArO6v0T_PfpOvulJYBHTJ4H28s", #Kak Eta 
            "https://drive.google.com/uc?export=view&id=12ksyAr6awG11WEYkI_v-9AXLoPNFev4s", #Kak Rut  
            "https://drive.google.com/uc?export=view&id=1YEvoUTuyHMNB7bdfdX6covcK0wJlVzSD", #Kak Puspa 
            "https://drive.google.com/uc?export=view&id=1fSVZD0oqTggQ8GqCExDF-jLU2Oo8dqZF", #Bg Eggi 
            "https://drive.google.com/uc?export=view&id=1x_q1qX3JruernLAWuNYr_ujFGeJZdqAi", #Kak Febiya 
            "https://drive.google.com/uc?export=view&id=1kyFJ8b1tq8GoEA-8kwtFYoYvox4-A0oQ", #Bang Happy 
            "https://drive.google.com/uc?export=view&id=12IVTbrLEL7F_vPfZq_8mzej7rDTuCy8z", #Bang Randa 
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
                "kesan": "asik abangnya ",  
                "pesan":"semoga cepat sukses bang dan lulus"
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
        "https://drive.google.com/uc?export=view&id=1CAMYYR2u36AOqQcPpenJgr54YCMEf7Sb", #1 bang  yogy
        "https://drive.google.com/uc?export=view&id=1xxG2kyIPk64jf-v-gS7JUGek2yOC5Obj", #2 kak ramadhita
        "https://drive.google.com/uc?export=view&id=1pGpdje0cJ6SEWXiX-fOXWUlqAw2CsnlA",#3 kak nazwa
        "https://drive.google.com/uc?export=view&id=1fkp8vEbkqcH_d4IcVjZ4UkW0rg9LIbKH", #4 bang batian
        "https://drive.google.com/uc?export=view&id=1oldmJVNtUUs9KWv3dH_MwCKJqQw8XC-J",#5 kak dea
        "https://drive.google.com/uc?export=view&id=1IxNyypZ45UxIsDoVJOPqP4K9h_3zNs8B", #6 kak estia
        "https://drive.google.com/uc?export=view&id=1_IzGZEBhHFz8QKkjsJlqriKnSxdyO4TJ", #7 kak natasya
        "https://drive.google.com/uc?export=view&id=12Xb0VjSEhx_6rfXyr6P-lOL9hy6egBYj",#8 kak novelia
        "https://drive.google.com/uc?export=view&id=1EYV_tjC_nkndGyWj4eq_WXi3r8qA9QcL", #9 kak ratu 
        "https://drive.google.com/uc?export=view&id=14Tb6EMGt3_ZMCOcgbgurCYOww39Cez12", #10 kak tobias
        "https://drive.google.com/uc?export=view&id=1o_UXo1MQSDb_77UcEDmXM4aNTQbhiXk7",#11 kak yohana
        "https://drive.google.com/uc?export=view&id=1X1lZy-IlIoDFDDgn-1oDCTfN6CSpy4iA", #12 kak rizki
        "https://drive.google.com/uc?export=view&id=1Ee4Pzf_i_5pcOWXBEQld80Ruvmz2UZo0", #13 kak arafi
        "https://drive.google.com/uc?export=view&id=1O-PGbW3lpyWgbZqjKT2hXBcfqSdLDcWT",#14 kak asa
        "https://drive.google.com/uc?export=view&id=16prlPhafex7YBl57-0w89xTq8ONGgfYB",#15 chalifia
        "https://drive.google.com/uc?export=view&id=1gmejvgR6eTszCsJQGi03fKtuhcADEHiD",#16 kak irvan
        "https://drive.google.com/uc?export=view&id=1EsiPJezI2pVrJE0c2vATMvO8v2-fI2yF",#17 kak  izza
        "https://drive.google.com/uc?export=view&id=1T63kE5gm9a1KDP6h_2mxFEeEJXjniBI3",#18  kak khaalishah
        "https://drive.google.com/uc?export=view&id=1RAoJ_IaaaESBWvep4jEbAmL8A2oZRRX_", #19 kak  raid
        "https://drive.google.com/uc?export=view&id=1X6AUluzQQTRzMy45gyetcUEa5h28UOLG", #20 kak tria
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
                "kesan": "abangnya kece",  
                "pesan":"Semangat dan cepat lulus bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "seru kakanya",  
                "pesan":"Semoga cepat lulus kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Keren kakaknya",  
                "pesan":"Semoga cepat sukses kak"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Keren abangnya ",  
                "pesan":"Semangat kuliahnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "asikk kakaknya",  
                "pesan":"Semangat kakak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "asikk kakaknya",  
                "pesan":"Semangat kakak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "asikk kakaknya",  
                "pesan":"Semangat kakak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Keren kakaknya",  
                "pesan":"Semangat kakak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Keren kakaknya",  
                "pesan":"Semangat kakak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "bang tobias keren bang kecee",  
                "pesan":"Semangat bang kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Keren kakaknya",  
                "pesan":"Semangat bang kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": " Bikin Portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "abangnya keren kece",  
                "pesan": "Semangat bang kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "abangnya keren kece",  
                "pesan": "Semangat bang kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Lucu, asik, Keren ",  
                "pesan": "Semangat kak asa kuliahnya"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Keren kakaknya asik ",  
                "pesan": "Semangat kak kuliahnya dan semoga cepat lulus"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "abangnya keren kece",  
                "pesan": "Semangat bang kuliahnya"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Asik, keren, aktif juga kak izza ",  
                "pesan": "Semangat kak IZZA kuliahnya"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "kakanya asik seru di liat - liat jiwa kepintaranya tinggi",  
                "pesan": "Semangat kak alyaa kulihanya"
                
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Pendiam dan cara penyampaiaannya mudah dipahami",  
                "pesan": "Semangat bang kuliahnya"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Keren kakaknya asik",  
                "pesan": "Semangat kak kuliahnya dan semoga cepat lulus  "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1OD8Ogdr5VryheHt656uWECbik_MiwyVq",
        "https://drive.google.com/uc?export=view&id=19P6lEpFFL2yKPde1VnxLKoIR7omc_h6d",
        "https://drive.google.com/uc?export=view&id=1NZRM_tg1ws_uHX_TDatfjP2JN4Jh4kGu",
        "https://drive.google.com/uc?export=view&id=1E3cS9dXPfH0CFYMs8U7xY-P-VgkTzszg", 
        "https://drive.google.com/uc?export=view&id=1xEohpSzesYjaodbbE10yHYUcuxzC8O_N",
        "https://drive.google.com/uc?export=view&id=1u_fz3-E-GuIngG0UaCp5v9Dkm4LvTgG_",
        "https://drive.google.com/uc?export=view&id=1qJGapHjm4k4dIIhE2U5-J8N8jOeaB2yZ", 
        "https://drive.google.com/uc?export=view&id=1Ji15SduaRLcMKiYG5szxwUA4r7rEDvQ3",
        "https://drive.google.com/uc?export=view&id=1X7KThopQmM-fhRcPd7nCx21if48-1N8F",
        "https://drive.google.com/uc?export=view&id=1XxHa1TKGE_GItqIqqDRvEduAjyIplhU7", 
        "https://drive.google.com/uc?export=view&id=15EigfCPiiN548uG9bxWJAboZhX5RbnDT",
        "https://drive.google.com/uc?export=view&id=1WAlX8J0V0bCgaRyhfjopyUglZWJfoFJv", 

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
            "kesan": "orangnya asik tegas jiwa semangatt tinggi",
            "pesan": "Sehat dan semangat kuliahnya bang"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "orangnya lembut pendiam lucu ",
            "pesan": "Semangat kuliahnya kak Catherine"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "orangnya tangguh jiwa beraninya keliatan ",
            "pesan": "Semangat kuliah bang untuk berproses "
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Rajabasa",
            "hobi": "Denger musik",
            "sosmed": "@ranniu",
            "kesan": "kak rani lucu asikk ",
            "pesan": "Semangat dan semoga cepat lulus"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "asik banyak serunya bewibawa",
            "pesan": "Semangat kuliahnya bang "
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "kak salwa lucu seru asikk",
            "pesan": "Semangat dan semoga dimudahkan segala prsosnya kak"
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "Asik abangnya",
            "pesan": "Semoga cepat lulus dan semangat bang"
        },
        {
            "nama": "Azizah Kusumah Putri",
            "nim": "122450068",
            "umur": "21",
            "asal": "Lampung Selatan",
            "alamat": "Natar",
            "hobi": "Berkebun",
            "sosmed": "@azizahksmh15",
            "kesan": "Lucu dan asik",
            "pesan": "Semangat kakak buat kuliahnya"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "Asik suka ngelucu kadang",
            "pesan": "Semangat bang buat kuliahnya"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "Keren jiwa pintarnya keliatan",
            "pesan": "Semangat kuliah"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "Asik , seru jiwa asik ada ",
            "pesan": "Semangat ya bang kuliah"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "kece asik kakaknya ",
            "pesan": "Semangat kakak kuliah kak"
        },
    ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16yalWbUPPFuqOotcIMvxnBfGk7KL1WO6", #Bang Andrian
            "https://drive.google.com/uc?export=view&id=1P6zCleQ95mU7H24SJqhQD8DK77D30xPV", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1TS_Ne8liUK6GUgijUCnq78F59n8yA2d3",# Kak Nabila
            "https://drive.google.com/uc?export=view&id=1R-IlmcVF-eVU1ciD59AMym2__D_ateuW",# Kak Nabilah
            "https://drive.google.com/uc?export=view&id=1f1oPekpgZnwST8Fkb9Xlev0KadfSinMZ",# Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1QQ5hCBR8Jshr7eh_Jto8H6tY_mkdTbfP",# Bang Danang
            "https://drive.google.com/uc?export=view&id=1Z-I8X-effcavdvGUQd7VGGAi5wkAMIhK",# Bang Farrel
            "https://drive.google.com/uc?export=view&id=1bAEYhysDO6VORVWcaBqJaiofiQG1_K-M",# Kak Tessa
            "https://drive.google.com/uc?export=view&id=1qym6vPBiVEtHqmPld2H9K7eKau1xiLev",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=15JRFsAjaRaHDwHm-9ZzS00DLNMaq4tkb",# Bang Dhafin
            "https://drive.google.com/uc?export=view&id=1p4a3_LtmXm3DzwTdDDlLT0kVv5gIVTYh",# Kak Elia

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
                "kesan": "abangnya banyak becanda nii kadang",  
                "pesan": "Semangat kuliah bang "
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "kakaknya seruu nii",  
                "pesan": "Semoga cepat lulus kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Lucu dan seruuu kakaknya ",
                "pesan": "semangat kak kuliiahnya"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "kece kakaknya",
                "pesan": "semoga cepat berproses kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "abangnya asik nii seruu juga",
                "pesan": "Semangat kuliahnya bang semoga cepat lulus"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "pandai mencari uang niii",
                "pesan": "Semoga ngalir terus bang cuanya biar bisa banyak gratis stiker"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "abangnya gagah berwibawa",
                "pesan": "semoga proses mencari cuan lancarr bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa cakep kece",
                "pesan": "semoga sukses kak"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kak Alvia seruu , asikkk dan kece",
                "pesan": "semangatt kuliah kak"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "abangnya kek pediem apa dugaan saya salah",
                "pesan": "Semangat kuliah bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kakaknya lucu",
                "pesan": "Semangat buat kakaknya"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1U7pmfUL4dz2mfBVtjDWIR098vzpoutvG", # bang wahyu
            "https://drive.google.com/uc?export=view&id=19gGRM_yzhCP2aOM7qjXXxcHqsVSMGsAd", # kak arsyi
            "https://drive.google.com/uc?export=view&id=1qhKyek2UED1xUjxN9KN85YB9ZH9xoFsQ", # bang kai
            "https://drive.google.com/uc?export=view&id=1GXBXrD-Bh6BCYD_k_p8p9lmHtBJ-oyc0", # bang arsal
            "https://drive.google.com/uc?export=view&id=17NeBjFmSrguBD-R6zu14_yVZ1ZV5wHNx", # kak elok
            "https://drive.google.com/uc?export=view&id=15Ydis5UYWWlk8cousuYU5JCgqO5ea0ZN", # kak juju
            "https://drive.google.com/uc?export=view&id=19_qIJKe1wBnikz7Hqx1YVCgFn9uBj2C5", # kak nel
            "https://drive.google.com/uc?export=view&id=1X7jBZF4EuceH89jao3vNJMyJ7r0--TRR", # kak try yani
            "https://drive.google.com/uc?export=view&id=1r13lGlhi9o-Oph4Q7vD-1tRrBH0-dBMS", # kak dwi
            "https://drive.google.com/uc?export=view&id=1Dwm_um21GM44s031Sy9dAEgUUZ8HSYYP", # bang gym
            "https://drive.google.com/uc?export=view&id=1zf1P5K8CqtI_bwJxjs1onRJqtwvb6twu", # kak nasywa
            "https://drive.google.com/uc?export=view&id=1-XD0IkkizX_pY9bqcfqybSKdu-Kd1es1", # kak priska
            "https://drive.google.com/uc?export=view&id=1kMFgnJbOTRusaPumLt9q-8YkcrlJFJd6", # bang abit
            "https://drive.google.com/uc?export=view&id=1lhcGeQGVH2wti2mLk2MP6i8KMxsLs-a8", # bang hermawan
            "https://drive.google.com/uc?export=view&id=1Ke_va9u9Y2kppFiReMssVqD3IM5Ikcvt", # kak khusnun nisa
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
                "kesan": "Bang Wahyu kece banget",
                "pesan": "Semangat kuliahnya bangg"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Kak Arsyi ini lucu kadang - kadang",
                "pesan": "Semangat dan semoga cepat lulus"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kai asikk ini",
                "pesan": "Semangat bang semoga cepat lulus nilai terbaik"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "boleh lah rekomendasi parfum bang",
                "pesan": "Semoga sehat selalu dan sukses "
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kak elok baik orangnya kek kukira pendiem",
                "pesan": "Sehat sehat dan semangat kak semoga sukses"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "kak juju ini orangnya assik,cantik,baikkk lucuuu kece pulaaa ",
                "pesan": "Semoga sukses di masa depan terus maap kalo sering merepotkan kak juju ,semangattt buat kak juju"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "Kakaknya asikk seruu",
                "pesan": "Semangat dan semoga prosesnya lancar semasa kuliah"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Asik kakaknya seruu juga",
                "pesan": "Semangatt kak kuliahnya "
            },
            {  
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "Scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "Lucu dan asik kakaknya",
                "pesan": "Semangat dan sehat selalu kak"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "kukira abangnya ngga seru ternyata oh ternyata asikkk seruu banyak becanda",
                "pesan": "Semangat bang buat kedepanya sukses teruss bang maap klo ada salah bang , semangatt bang jimm "
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "Asikk seruu the best kakaknya",
                "pesan": "Semangat buat kakaknya"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "Lucu dan asik",
                "pesan": "Sehat selalu dan semangat kak"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "bang abit ini random sekali asikk juga seruuu",
                "pesan": "Semangatt bang abitt semoga sukses kedepanyaa"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Heboh dan asik abiss",
                "pesan": "semangatt bang semoga sukses"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Lucu dan asikkk ,seruuu kakaknya",
                "pesan": "Semangat dan sukses selalu kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
