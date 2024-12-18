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
            "https://drive.google.com/uc?export=view&id=1ryigRnSEND3brcwM86xJbKZWzX4fCUnL",
            "https://drive.google.com/uc?export=view&id=16lb8PjqAHI5nATgKmGR74gqxtEL_mRzr",
            "https://drive.google.com/uc?export=view&id=1oezSa8bQLpBzAToVGJw96zS_gnHtDEtn",
            "https://drive.google.com/uc?export=view&id=1cJqwr6RQozuprih1imte0uL4wJcCtcei",
            "https://drive.google.com/uc?export=view&id=1oNP7arlzDJvGlZpbfolSFUMHvFKDHGKJ",
            "https://drive.google.com/uc?export=view&id=1NgvNZa6uxPumbcQ1xcJuqbTdC5v_--k2",

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
                "kesan"	    : "sama kayak namanya, berkharisma.",  
                "pesan"	    : "semoga sukses selalu, dan selalau ingat pada HMSD adyatama"#1

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
                "kesan"     : "kakaknya lucu dan baik.",  
                "pesan"     : "selalu semangat kak menjalani hari dengan drakoran."# 3
            },
            {
                "nama": "Putri Maulidia Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "JL. Nangka IV",
                "hobi": "Dengerin bang pandra gitaran ",
                "sosmed": "@ptrimaulidia_",
                "kesan"     : "asik banget cara ngomongnya",  
                "pesan"     : "semangat trus belajarnya sambil dengerin bang pandra dengerin gitar"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan"     : "wong kito galo",  
                "pesan"     : "semoga bisa karaukean bareng kakaknya."# 5
            },
            {
                "nama": "Nadila Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadilaaandr26",
                "kesan"     : "kalem",  
                "pesan"     : "sukses selalu kak."# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zrLPd1ppNTNfQOTQylorInO1U2dcEMAd", #1
            "https://drive.google.com/uc?export=view&id=1FL7ovYX-JqxnMuMzOtJJSdTBhmCzdwtN", #2
            "https://drive.google.com/uc?export=view&id=154v2XNZZDLQPpwfHNBa4RIHuIOAYEQOi", #3
            "https://drive.google.com/uc?export=view&id=1W9IIVAZSjNFP2dawR7TRB0MNGODE4oHB", #4
            "https://drive.google.com/uc?export=view&id=15IKRBE2uRLlvm_4xYwmQnl24vaZz3lpV", #5
            "https://drive.google.com/uc?export=view&id=1yP12nOn4Uj8oGekYtOx62LEE5h6izijk", #6
            "https://drive.google.com/uc?export=view&id=1xs7ExEc2hdF5ab5zPYXJVkVSJajiKZ7i", #7
            "https://drive.google.com/uc?export=view&id=180lcLx3F_QFFKgFCWORYufdhzeVgtxuv", #8
            "https://drive.google.com/uc?export=view&id=1c8Rr_24wxMObz7wJhFHuvrYMqLr5iMAK", #9
            "https://drive.google.com/uc?export=view&id=1qa51OLwixFKrjfVExu7nMi91Q6AoAyqT", #10
            "https://drive.google.com/uc?export=view&id=1BcGDKmcXWISQCDQNJp8NFSvOQ8JjN6A3", #11
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
                "kesan": "kakaknya asik banget",  
                "pesan":"semangat trus kakak "#1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "22",
                "asal":"Tanggerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": " terlihat sangat ramah",  
                "pesan":"semoga diperlancar kuliahnya kak "#2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "1221450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "sangat pintar dan cerdas",  
                "pesan":"semoga cepat lulusnya kakak"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@anisadini",
                "kesan": "ramah dan baik",  
                "pesan":"sukses selalu untuk kakak"# 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "1221450124",
                "umur": "21",
                "asal":"Saltiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "anggun dan ramah",  
                "pesan":" semangat trus kuliah nya kak"# 5
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok Tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "lucu banget suka meghibur",  
                "pesan":" semoga tetap lucu trus sampai lulus kakak"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul",
                "kesan": "cool banget",  
                "pesan":" semoga di perlancar kuliahnya bang"# 7
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca Buku",
                "sosmed": "@fer_yulius",
                "kesan": " berwibawa",  
                "pesan":" selalu sukses untuk abang"# 8
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": " abang ini cool banget dan baik",  
                "pesan":" semoga diperlancar kuliahnya bang"# 9
            },
            {
                "nama": "Jeremie Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin Orang",
                "sosmed": "@jeremia_s_",
                "kesan": "abang nya lucu ",  
                "pesan":" abang idola saya banget di baleg "# 10
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD Tanggerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linkedln , puasa senin kamis dan ngerjaiin tugas",
                "sosmed": "@berlyyanda",
                "kesan": "tenang dan pendiam",  
                "pesan":" semoga sukses selalu"# 11
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1noUZtJA6d5xvySSL5n-xI-bYpO4jXj_g", 
            "https://drive.google.com/uc?export=view&id=1c-GuLTRiyGyNZGn4h8swFpDRmDiNNPBV", 
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
                "kesan": "tegas banget",  
                "pesan": "terus semangat kak meskipun banyak kegiatan"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "aktif banget di banyak kegiatan",  
                "pesan": "semoga sehat selalu dalam menjalani banyaknya kegaitan"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()


elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EFc0YIk0nuq5scP1scA5u82Mgleu81MH", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1iWSjgj1Ka8ihL0movjGPq_howu6mxnsP", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1YshUzR-NT7or-ddi54v7HcWBtkOLbHd-", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1qDdxvlpQ9n8Zlp_GtpXc1BiAqcT1Xf9x", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1Ufk_sQ_K0etttcAABGtAV7_1jQiX5E7X", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1MlT85jHQoUwLOGOfszEQg64pAt4ZhFZZ", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1nzdSMivdUhC7_PXIQGyFkY-iMHyoOv-H", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1vV3AIeAhKHGSv0YO04LuiyE9GG-iIZF4", #Bang Deri
            "https://drive.google.com/uc?export=view&id=12NBvs3ta423Zv7Pjzhi72sFU4f3AVmAA", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1WpaA4iijrW73Mu8yP0nWjsRMOnS65rVC", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=14AwQq3CER-U9uBuxtgzq-tfbjUFhgeES", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1Rxqs4nO3sLFkKbHtGSaEfBn6OlNSdj5Y", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1LL1hD0IxF7hitVrauLKX17BItS4YLz6k", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1GR22N_GLYKgo84oUi7aJi8RcgLsILoZD", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1IIjfChIKv1f6Q_PPhnFcBiXoBGBDcuxz", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1M1VWX6_XZ9nod4UrlWF2cKqZ6NOB0BXh", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1WyDLjGjZc25R4jtPlYSy4x-LTmFZKCyV", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1uWgqxkyNDwqQIGOmkzzzCjwZAq6VglNQ", #Kak Dini
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
                "kesan": "Abangnya Tegas",  
                "pesan": "Semoga lancar disemua rencana abang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kost, Sukarame",
                "hobi": "memancing keributan",
                "sosmed": "@elisabethh_",
                "kesan": "selalu nempel dengan bang jo",  
                "pesan": "semoga langgeng trus ama bang jo"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Nyubit",
                "sosmed": "@afifahhnsrn",
                "kesan": "pas awal ketemu ngiranya pendiam, ternyata tidak",  
                "pesan": "semangat trus kak sebagai ketuplak."
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "tegas banget.",  
                "pesan": "saya sering nyapa dengan senyum, semoga kakak bales nya juga dengan senyuman"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Sholat",
                "sosmed": "@eksantyfebriana",
                "kesan": "selalu ada aja tingkahnya kakak",  
                "pesan": "gapapa kak meskipun banyak tingkah tapi lucu lucu tingkahnya"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Nabok orang",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakak yang paling kalem dari divisi kader",  
                "pesan": "saya suka dengan kekalemannya kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Denger lagu",
                "sosmed": "@ferdy_kevin",
                "kesan": "abangnya agak pendiam, saya jarang melihat abang ngomong",  
                "pesan": "semoga abang bisa sering ngobrol sama angkatan 23"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet orang",
                "sosmed": "@dransyh_",
                "kesan": "samo samo wong kito galo",  
                "pesan": "gek balek kampung bareng e kak"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "kadang senyum, kadang tegas",  
                "pesan": "saya suka liat kakak senyum"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "lucu banget abangnya, bwahh kocyakkk",  
                "pesan":"semoga selalu menghibur dengan tingkah abang sampai nanti lulus dari itera"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "kadang lucu, kadang tegas",  
                "pesan": "mari kita lanjutkan perjalanan suhu"
            },
                        {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Menjadi Skena",
                "sosmed": "@kemasverii",
                "kesan": "pinter, baik, dan asik",  
                "pesan": "semoga mau diskusi ilmu sama saya terus."
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Membaca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "kakaknya jarang ngobrol dengan kami",  
                "pesan": "nanti boleh dong kak ngobrol, atau bagi-bagi lah bacaannya di webtoon"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Dengerin jusy lucy",
                "sosmed": "@sahid_maul19",
                "kesan": "abangnya baik banget bawa in minum saya kemarin pada saat ketinggalan",  
                "pesan": "maaf yaa bang saya jadi ga enak, karena bawain minum saya:)"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"lampung",
                "alamat": "kota batu",
                "hobi": "menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "diem pun tetap lucu abangnya",  
                "pesan": "ajarin saya bang meskipun diem tapi tetap lucu"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "saya sering liat kakak, gara-gara sering memberi informasi perlombaan",  
                "pesan": "terikasih kakak karena informasinya sangat bermanfaat pada saat berjalanny perlombaan"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Banga Belitung",
                "alamat": "Sukarame",
                "hobi": "Ngegame",
                "sosmed": "@raflyy_pd",
                "kesan": "abang nya pendiam",  
                "pesan": "semoga abang lebih aktif berbicara"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "awalnya saya kira kakak dari departemen eksternal",  
                "pesan":"nanti mau dong kak info bacaan buku buku kakak"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()



elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PIa-Yk2BpRsJQPuOC590YkeOpuS8rUSJ", #Bg Rafi 
            "https://drive.google.com/uc?export=view&id=18FoLneMoEqeU6NiXV7rDVZOU4FjelrBE", #Kak Anova 
            "https://drive.google.com/uc?export=view&id=1pZe1Iu7JDZdl4HNOvV8nvcoao1niitzp", #Bg Ahmad Akbar 
            "https://drive.google.com/uc?export=view&id=1n2tyuV0aEq3wuISvBcuTjTRiPvLTqlO5", #Bg Fadhil 
            "https://drive.google.com/uc?export=view&id=1DfjoRu4ZNjwElECmCjcd0eRYd6qfC4-F", #Kak Dina 
            "https://drive.google.com/uc?export=view&id=1BlIxdVok5N9CjJywj05MUHMYd_dHOUxM", #Kak Dinda 
            "https://drive.google.com/uc?export=view&id=11B10vn9Jxvq-mF3NHUKZWlZ22g65CA63", #Kak Eta 
            "https://drive.google.com/uc?export=view&id=1rnJxsSX9ETUXThYgxD_c1AGWrDXh6jT-", #Kak Rut 
            "https://drive.google.com/uc?export=view&id=1ejmvppmuVwWDFL95RKM13I6MDLLCVm1I", #Kak Puspa 
            "https://drive.google.com/uc?export=view&id=1LB7fcYO5o2mS5wIN6OD3II6WXPHtlb3q", #Bg Eggi 
            "https://drive.google.com/uc?export=view&id=1ePVtf8dhGVCIQW4e2H8lW7TpxJ-7tW8I", #Kak Febiya 
            "https://drive.google.com/uc?export=view&id=14CaPxghupELW9mrWZCtoSZqUZWJ5mBu5", #Bang Happy 
            "https://drive.google.com/uc?export=view&id=1ljm6iBrL1vpfNJwU1n4Bmy7wsYy26rGq", #Bang Randa 
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
                "kesan": "abangnya keliatan sangat pintar",  
                "pesan": "boleh nanti bagi bagi ilmu dengan saya"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "berkharisma",  
                "pesan": "sehat selalu yaa kak dalam menjalankan kegiatan kegiatan nya"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "sangar",  
                "pesan": "gas in olahraga bareng bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "abang ini baik sih, kemarin saya sakit di tolongin dia",  
                "pesan": "terimakasih yaa bang atas pertolongannya"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "asyik kakaknya",  
                "pesan": "semangat selalu yaa kak"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "pinter",  
                "pesan": "boleh dong bagi ilmunya bang"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "pinter dan cantik",  
                "pesan": "pengen liat kakak main musik lagi"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "baik dan pinter",  
                "pesan": "mau dong kak hasil dari review jurnal nya"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "baik",  
                "pesan": "semangat terus kakak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "pinter",  
                "pesan": "ajarin coding dong bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "rajin dan pinter",  
                "pesan": "semangat kak, semoga banyak menemuka jurnal yang bagus yaa hehe"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "keren dan asik",  
                "pesan": "tetap semangat bang, dan boleh dong ajarin saya main game"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "informatif abangnya",  
                "pesan": "ati ati bang jangan kebanyakan tidur bang hehe"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()



elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1M-qFX9vpz8EDn4fOJklHLZsd3mi7iKjj", #Bg Yogy 
        "https://drive.google.com/uc?export=view&id=15kUwHCX09IWfZgF7dzVk4T2jp9rKyrHH", #Kak Ramadhita 
        "https://drive.google.com/uc?export=view&id=1JXzAlN6NTLr6z6791OBfezFur1RNbsS8", #Kak Nazwa 
        "https://drive.google.com/uc?export=view&id=1cl1iA5xH4pY4mSCFDubL3Kkxjg2Xe8sf", #Bg Bastian 
        "https://drive.google.com/uc?export=view&id=1hUCgCDDEgUqejnDgtgf_PfCT4JeJgh8F", #Kak Dea 
        "https://drive.google.com/uc?export=view&id=1yeiwbXVlXOY4Pq8Xo0hQbrg7HI_CZBVe", #Kak Esteria 
        "https://drive.google.com/uc?export=view&id=1Wi9hO8nNpzXV-4_LezQ_fFR9jY3RgZw6", #Kak Natasya 
        "https://drive.google.com/uc?export=view&id=1-RmtLaIsa1KHPHn-aqL-gSC7jm21-xK8", #Kak Novelia 
        "https://drive.google.com/uc?export=view&id=1tIwkZfRcY4HlyxDLn9curr-3V6VUarAa", #Kak Ratu 
        "https://drive.google.com/uc?export=view&id=1WuG2DWVESJ7mb8vwMadcX6ktEpHt6gaz", #Bg Tobias 
        "https://drive.google.com/uc?export=view&id=1WFe8W2wxdD4jIQAIpBuL0sRJi6vNn2h3", #Kak Yohana 
        "https://drive.google.com/uc?export=view&id=1hfVFXbIQzEqGjFIZ_lBJoi5mIrdWB9IZ", #Bg Rizki 
        "https://drive.google.com/uc?export=view&id=1HbXRkc3TnxGX8m_ZKQ6ZefdNCYwVq7Pt", #Bg Arafi 
        "https://drive.google.com/uc?export=view&id=15UGoBLCfs4Yudm33aRL7ttaeFTBs8fkR", #kak Asa 
        "https://drive.google.com/uc?export=view&id=1k3DAGWNRTAZ3YCLamX5iXIXaT9cfBZkl", #Kak Chalifia 
        "https://drive.google.com/uc?export=view&id=1nXqEgGqNFiIz4pgqex2Wo3Xf-eL2v8O3", #Bang Irvan 
        "https://drive.google.com/uc?export=view&id=1Scd5rkc6coLUZQ4EzdocolRmUqQVWw4J", #Kak Izza 
        "https://drive.google.com/uc?export=view&id=165Ug6ihb1I9kCbWX1F7GumtjMhBt2pgS", #Kak Khaalishah 
        "https://drive.google.com/uc?export=view&id=1QikXjyr4srlRvalRKOHreaQucwL1g_TX", #Bang Raid 
        "https://drive.google.com/uc?export=view&id=1VqeA-206f2h5L5-a-voqdEePinjCxS1g", #Kak Tria 
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
                "kesan": "seru banget kalo bercanda sama abang ini",  
                "pesan": "semoga nanti kita lebih banyak ngobrol dan bertukar ilmu yaa bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "kakaknya kalem ",  
                "pesan": "sehat selalu yaa kak semoga diperlancar nanti TA nya"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "banyak ilmu yang di bagikan dari kakak ini ",  
                "pesan": "semoga nanti lulus tepat waktu dan dapat nilai yang terbaik yaa kak"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "kece abangnya",  
                "pesan": "semoga tidak telat lagi ke kampus dan selalu semangat abangnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "pas awal saya ngiranya tegas, dan ga seru",  
                "pesan": "ternyata saya salah ternyata hehe, asik banget kakaknya."
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "baik dan asik",  
                "pesan": "infokan film film yang bagus dong kak"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "kalem",  
                "pesan": "boleh dong karauke bareng kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "kakak yang paling imut di eksternal",  
                "pesan": "hati hati kak jangan banyak tidur hehe"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "baik dan keren",  
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "abang abang an gw di eskternal nich",  
                "pesan": "sering sering latihan bang kita, kejer lagi science fest kita"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "tegas banget sih kakaknya",  
                "pesan": "semangat yaa kak menjalankan tugas tugas nyaa"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "abang ini juga lucu dan kocak sih",  
                "pesan": "seru beut pokoknya kalo ngobrol abang ini hehe"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "lucu abangnya, sekali nyeletuk biasanya lansung bikin suasana cair",  
                "pesan": "makasih yaa kak celetukannya, secara tidak sengaja itu yang bikin banyak orang happy"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "aktif kakak ini sama dengan kak iza",  
                "pesan": "semoga tenaga nya tidak pernah hilang kak dan juga terus semangat"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "kalem banget kakaknya",  
                "pesan": "semangat kuliahnya kak semoga lulus tepat waktu"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "asyik dan lucu",  
                "pesan": "infokan mabar dong bang hehe"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "kakak paling ga ada cape cape nya, tenaga nya selalu full",  
                "pesan": "makan yang banyak yaa kak, pasti cape jadi kakak selalu aktif :)"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "kalem dan seru saat bagi bagi ilmu",  
                "pesan": "terimakasih yaa kak ilmu ilmu nya"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "abangnya cukup pendiam",  
                "pesan": "semoga kedepannya saya bisa melihat abang lebih banyak ngobrol dengan kami"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "kakak ter asyik",  
                "pesan": "semangat trus kak, dan sehat selalu"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()



elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1z4A7xJ4pgY53C1rutMbQqaMPVdj5q1iK", #BangDimas 
        "https://drive.google.com/uc?export=view&id=11nPtKl0MpRs6T9B8D0cICU5gyM-YfJze", #Kak Catherine 
        "https://drive.google.com/uc?export=view&id=1VIEkRGFtfwMO372VY34NppKwU7BEHw6i", #Bang Akbar 
        "https://drive.google.com/uc?export=view&id=1ZANVH22VB_oPjfZjbmEfMOrZHOFoZ7vo", #Kak Rani 
        "https://drive.google.com/uc?export=view&id=1L3kfxoSHkKuQOk1jhfZa124NxdXcoHdi", #Bang Rendra 
        "https://drive.google.com/uc?export=view&id=1lp6-xrzjkXbABBjb_Eg_4TbzI6EqD5_L", #Kak Salwa 
        "https://drive.google.com/uc?export=view&id=1U2nESGrxHRfs6xzGVDS-ZpL7MBjCQQc3", #Bang Ari 
        "https://drive.google.com/uc?export=view&id=1s_QwWi2WgxZxqKKyAwoia61b83oPm51f", #Kak Azizah 
        "https://drive.google.com/uc?export=view&id=1C96BrK3166ouKw4jmTKkt2Ow_evkIXn4", #Bang Josua 
        "https://drive.google.com/uc?export=view&id=19RJI_aP2D7EA_4fQ62dPxxzyh9Q-JoAL", #Kak Meira
        "https://drive.google.com/uc?export=view&id=11ywwbH1c3upJAB8uicU7zdvU4e26_7o0", #Bang Rendi 
        "https://drive.google.com/uc?export=view&id=1o9X5L2Ms24djjCAdH70u8Os9MRqPx7Tg", #kak Renta 

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
            "kesan": "abang ini sih ga pernah abis tenaganya",
            "pesan": "boleh dong bang nongkrong bareng, ngobrol2 kita" #1
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "kakaknya kalem",
            "pesan": "semangat terus yaa kak"#2
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "abang nya lucu dan kocak",
            "pesan": "boleh dong bang ajarin coding"#3
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Rajabasa",
            "hobi": "Denger Musik",
            "sosmed": "@ranniu",
            "kesan": "berkharisma kakaknya",
            "pesan": "kasih paham saya kak caranya berkharisma"#4
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "ini mah bro saya di internal, bang rendra",
            "pesan": "kita harus banyak ngobrol sih bang"#5
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "kakak ini juga kalem banget",
            "pesan": "semoga selalu sehat yaa kak dan semangat kuliahnya"#6
        },
        {
            "nama": "Ari Sigit",
            "nim": "121450069",
            "umur": "23",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Ratu",
            "hobi": "Olahraga",
            "sosmed": "@ari.sigit17",
            "kesan": "lucu dan baik",
            "pesan": "ayok kapan kapan olahraga bareng bang"#7
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
            "pesan": "mau dong kak di ajarin berkebun"#8
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "kakak ini pendiam dan alim",
            "pesan": "semangat terus kak dalam menjalankan tugas nya"#9
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "pendiam kakaknya",
            "pesan": "semoga nanti saya bisa melihat kakaknya lebih aktif ngobrol"#10
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "baik dan asik",
            "pesan": "semangat bang kuliahnya"#11
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "kakaknya ini juga agak pendiam",
            "pesan": "semoga nanti saya bisa melihat kakaknya lebih aktif ngobrol dengan kami"#12
        },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()


elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [

            "https://drive.google.com/uc?export=view&id=1QzVkJCkPRVPUr-aX08qDnSzr1UXcQOKN", #Bang adrian 1
            "https://drive.google.com/uc?export=view&id=1lgfb_WvS6qddX6jMtPGOwyk2gRflJXVE", #Kak adisty 2
            "https://drive.google.com/uc?export=view&id=1y3hGNBdfTXHofBQRQawbuMq-NJ4mpeI2", #kak nabila 3
            "https://drive.google.com/uc?export=view&id=1410BkRCKaykxxdxAel5J5mnqyvrid3Zy", #Bang Ahmad 4
            "https://drive.google.com/uc?export=view&id=1oKPV7fpq3hUGz_XSau2YO168pyMhM6M_", #Bang danang 5
            "https://drive.google.com/uc?export=view&id=1P1lqNos_uPq0ftud0aNfKmvgtX6PSvY0", #Bang Farrel 6
            "https://drive.google.com/uc?export=view&id=1ll5BwNKtcMpeULWZslcAKhp3eGxVS9be", #Kak tessa 7
            "https://drive.google.com/uc?export=view&id=1jkPYJu5dnqJ5Hr3zRa6OkY9YrNLzII5X", #Kak firti 8
            "https://drive.google.com/uc?export=view&id=1zTvqqgqK6ynqYLtM4jcrLLObR5PqpMuv", #Kak alvia 9 
            "https://drive.google.com/uc?export=view&id=1HgYi5Wa1SGuVw2zIuknSNbDxR1fCLRVQ", #Bg dafin 10
            "https://drive.google.com/uc?export=view&id=1P0MYBvWRZgf6UdJc2GXSgemh7jUOMbjA", #Kak elia 11

        ]
        data_list = [
            {
                "nama": "Andrian Agustinus Lumban Gaol",
                "nim": "121450090",
                "umur": "21",
                "asal":"Sidikalang",
                "alamat": "Dekat lapas",
                "hobi": "Cari hobi",
                "sosmed": "@andrianlgaol",
                "kesan": "abangnya cerdas",  
                "pesan": "semoga saya bisa diajak ke event2 bisnis"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan": "murah senyum kakaknya",  
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "kalem murah senyum",  
                "pesan": "nanti ajarin saya yaa kak ngitung uang dengan benar"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "asli cool beut abang ini",  
                "pesan": "ajakin dong bang kalo ada kegiatan bisnis"
            },
	    {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "abang paling aktif sih ini",  
                "pesan": "bagi ilmu bang biar pinter bisnis dan bisa jalan jalan kek abang"
            },
	    {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "abang ganteng nya di SSD",  
                "pesan": "sehat selalu bang, apalagi untuk mengurus Damaskus."
            },
      	    {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "kakaknya agak pendiam",  
                "pesan": "saya mau kak di ajarin nulis"
            },
	    {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal":"Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "kakaknya keliatan sangat pintar",  
                "pesan": "semangat trus kak kuliahnya"
            },
	    {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal":"Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "kadang suka neglucu kakaknya",  
                "pesan": "semoga tetap lucu yaa kak"
            },
	    {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "kalem abang ini mah",  
                "pesan": "gas in kita olahraga bareng bang"
            },
	    {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "kakak nya cukup aktif",  
                "pesan": "sehat selalu yaa kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()



else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JlEtTEcM4zBtt5OmXOdY2K46jaoFj00h", #Bang wahyu
            "https://drive.google.com/uc?export=view&id=1Zetx5MXimuHohAJll8XE4fJope0krQlW", #Kak fiola
            "https://drive.google.com/uc?export=view&id=1LCPSP8tjdyBoyPkhc0lNfFBvjQoG5_Lj", #kak arsyiah
            "https://drive.google.com/uc?export=view&id=13Ffkuc36PCbAM3h35dxuXSAIUypZIy8F", #kak najla
            "https://drive.google.com/uc?export=view&id=16NLcxRrornh5m9Z9Jwvg5fKchltMh3oO", #kak rahma
            "https://drive.google.com/uc?export=view&id=16KS3ALB0emnTM-svVfj5MWcPQew9rLPx", #kak try yani
            "https://drive.google.com/uc?export=view&id=1pQzdF5yWr2-h3_jxx5imT6-n6mn2flu1", #bang kaisar
            "https://drive.google.com/uc?export=view&id=1iNmT-Keh8QjWVT5iS9dqMQ82gEcispir", #Kak dwi ratna
            "https://drive.google.com/uc?export=view&id=1KhjjQfckkzFujn3rBCi_b5r-BWjMRJis", #bang gymnastiar
            "https://drive.google.com/uc?export=view&id=16KzFoE4XQFfRVd2nn6SCcWuoYotlhz1o", #kak nasywah
            "https://drive.google.com/uc?export=view&id=16MdsAVQPe1Memu3IB-Xufa32Z5yxzRf4", #Kak priska
            "https://drive.google.com/uc?export=view&id=1yCxGfrrUMW9fcqnEweupX7g8c3drugDk", #Bang arsal
            "https://drive.google.com/uc?export=view&id=1IOb4JLLqNGKOWUG7TUKy3546wXwup7Gk", #Bang abit
            "https://drive.google.com/uc?export=view&id=1jVc3ve5DsAanF75tKrHz2h-gSPYeHCDM", #Bang hermawan
            "https://drive.google.com/uc?export=view&id=1tD5BWJLCddwsRwH4hi_n0e727zCLrTeT", #kak nisa
        ]
        data_list = [
            {
                "nama": "Wahyudiyanto",
                "nim": "121450040",
                "umur": "22",
                "asal":"Makasar",
                "alamat": "Sukarame",
                "hobi": "Nonton",
                "sosmed": "@wahyudnt_0202",
                "kesan": "ternyata abangnya merantau jauh, dari sulawesi",  
                "pesan": "kalau abang balik, boleh lah bang oleh-oleh dari makasarnya"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "kakaknya cantik dan agak pendiam",  
                "pesan": "semoga lebih banyak ngobrol dengan kami ya kak"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "seru, kamerin banyak bercanda pas disuruh foto langsung disuruh kasih paham ala kak gem",  
                "pesan": "sehat selalu kak, dan boleh lah di ajak konten bareng hehe"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal":"Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis,fungirl",
                "sosmed": "@ nanana.minjoo",
                "kesan": "ini kakak fav saya.",  
                "pesan": "maaf yaa kak kalau saya banyak hal yang nyusahin kakak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal":"Tanggamus",
                "alamat": "Sukamare Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "aktif dan selalu berenergi",  
                "pesan": "pengen di ajak konten bareng hehe"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal":"Lampung Barat",
                "alamat": "Kopri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "asyik kakaknya",  
                "pesan": "seru dan asyik kemarin di ajak pose macem-macem pas photo"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal":"Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "cool banget abangnya, murah senyum juga",  
                "pesan": "tetap tersenyum bang meskipun dunia berat."
            },
            {
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal":"Jambi",
                "alamat": "Pemda",
                "hobi": "scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "kakak nya baik hati",  
                "pesan": "sehat selalu kak"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal":"Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "sama hal nya dengan kak najla, bang gym adalah abang fav saya",  
                "pesan": "saya ingin banyak belajar tentang kamera dengan abang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "pemda",
                "hobi": "Bersih bersih",
                "sosmed": "@nasywanaff",
                "kesan": "kakaknya sangat sangat bersahabat",  
                "pesan": "nanti kita pose ala2 medkraf lagi yaa kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "seru dan asik",  
                "pesan": "dengan kakak ini saya pose paling slay"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal":"Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsal.utama",
                "kesan": "baru kenal langsung kek bro banget sih sama abangnya",  
                "pesan": "nanti mau ngobrol2 lagi yaa bang tentang medkraf"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, DesaiN, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "abang yang selalu asyik di ajak ngobrol",  
                "pesan": "nanti kita sering sering ngobrol lagi yaa bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "jalan dekat tol",
                "hobi": "baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "selalu mengulucu abangnya",  
                "pesan": "gw suka gaya abangnya:)"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal":"Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "kakaknya pinter dan kretif",  
                "pesan": "mau dong kak di ajarin bikin DIY"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

# Tambahkan menu lainnya sesuai kebutuhan
