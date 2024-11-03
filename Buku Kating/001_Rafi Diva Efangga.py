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
            st.write(f"Hobi           : {data_list[i]['hobi']}")
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
            "https://drive.google.com/uc?export=view&id=1Z_8hFGkASmVVtQheA5C_uYdHoq152yIM",#1
            "https://drive.google.com/uc?export=view&id=16f3FM4fVkA5rXSlItLBFQq3qVN4_nIkH",#2
            "https://drive.google.com/uc?export=view&id=1JlUx1qvykOYKZtVBlgzGDXampO9-brw0",#3
            "https://drive.google.com/uc?export=view&id=1-0c7DbD84urcdTtS1c5_QitobMkbvF7V",#4
            "https://drive.google.com/uc?export=view&id=1LN8mGq1-Nr3dYJoVd4KWQycmETiTG7fy",#5
            "https://drive.google.com/uc?export=view&id=1d9PrTJPI1wzr6raN9EeJnbdfczzq4QFE",#6
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
                "kesan": "abangnya keren jiwa tegas ada",  
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
                "kesan": "asik suka ngomong seruu",  
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
                "kesan": "kakaknya asik klo dah ngorbol",  
                "pesan":"terus semangat kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "seruu asik klo adh ngobrol",  
                "pesan":"tetap semangat kak dan semoga cepat sukses "
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
                "kesan": "seru abangnya",  
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
                "kesan": "abangnya seruu",  
                "pesan":"semoga cepat sukses"
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
                "kesan": "abangnya lucu asik banayak ketawa",  
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
                "kesan": "abangnya lucu seruu ",  
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


# Tambahkan menu lainnya sesuai kebutuhan
