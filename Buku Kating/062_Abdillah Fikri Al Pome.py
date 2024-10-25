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
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Nyubit",
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
                "hobi": "minum kopi",
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
                "hobi": "Sholat",
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
                "hobi": "Nabok orang",
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
                "hobi": "Denger lagu",
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
                "hobi": "Review Cheatsheet orang",
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
                "hobi": "Menjadi Skena",
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
                "hobi": "Membaca Webtoon",
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
                "hobi": "Dengerin jusy lucy",
                "sosmed": "@sahid_maul19",
                "kesan": "",  
                "pesan":""
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"lampung",
                "alamat": "kota batu",
                "hobi": "menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "",  
                "pesan":""
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Banga Belitung",
                "alamat": "Sukarame",
                "hobi": "Ngegame",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "",
                "asal":"",
                "alamat": "",
                "hobi": "",
                "sosmed": "",
                "kesan": "",  
                "pesan":""
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()


# Tambahkan menu lainnya sesuai kebutuhan
