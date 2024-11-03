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
            "https://drive.google.com/uc?export=view&id=1fvT0zX5JSIJarhL1w20v2Vxydnr4t6f6",
            "https://drive.google.com/uc?export=view&id=1gpzXhQqTal4QMz8n_7-qPp_HX8Kkn5Y8",
            "https://drive.google.com/uc?export=view&id=1gxgLxHUhP_UoJW5X8JNBa6EtWF6zKlw1",
            "https://drive.google.com/uc?export=view&id=1gqBmC_OIUcSZfynv6zMMznH_WCyR3HkI",
            "https://drive.google.com/uc?export=view&id=1glQaLaHMIm4Wvt9laybHa4d0xhjuY4Ho",
            "https://drive.google.com/uc?export=view&id=1gnrcPtts5xTlmE-2ni254VqLN22YxNQ6",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Denger Musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Bang Gumilang orangnya tegas dan asik, serta berwibawa",  
                "pesan":"Semoga sukses dan dimudahkan untuk cepat lulus, dan terimakasih sudah menjadi pemimpin yang keren"
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "20",
                "asal":"Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Keren banget pas pertama kali tau kalo abang jadi SEKJEN",  
                "pesan":"Semangat buat kuliah, semoga cepet lulus, semangat jadi SEKJEN dan selalu jadi yang terkeren bang"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota Baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak keliatanyan orang yang bener-bener sibuk gitu",  
                "pesan":"Semangat buat kakaknya, semoga kuliahnya lancar, semangat juga jadi sekertaris, lancar lancar urusannya kak"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "Jl. Nangka IV",
                "hobi": "Dengerin Bang Pandra Gitaran",
                "sosmed": "@ptrimaulidaaa",
                "kesan": "Sama kaya kak Meliza, kakak kelihatan kaya sibuk banget ",  
                "pesan":"Semangat terus ya kak, semoga kuliahnya lancar, notulensinya juga semangat kak, keren banget kakak"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Pertama kali ngira kakak orangnya pendiem",  
                "pesan":"Semangat terus kak, semoga kuliahnya cepet selesai dan lancar, semangat mengatur keuangan himpunan"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ceria dan asik banget",  
                "pesan":"Semangat buat kak Nadilla, semoga sukses, dan lancar lancar jadi bendahara,serta jaga kesehatan"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gZUhWgalH7N9O5QfIt76SuTJz-vA-abJ",
            "https://drive.google.com/uc?export=view&id=1gMJVGwL0dE99oIpvTdix44klkOmJJN2m",
            "https://drive.google.com/uc?export=view&id=1g3sUuy6GdHKA5QqfVLhclTdxkWskoCUF",
            "https://drive.google.com/uc?export=view&id=1geika8xMp7BPDrLbenLHUg1J3UqS2HOl",
            "https://drive.google.com/uc?export=view&id=1fwMSdL_xd0ofPtzUGK3aYtl_CHXDB7DO",
            "https://drive.google.com/uc?export=view&id=1g7BYSADN56inEIe3SzYqhECspOwUI5Wa",
            "https://drive.google.com/uc?export=view&id=1gHOgTnBtHDcJ6_2q7lNrmsexuw2nfF24",
            "https://drive.google.com/uc?export=view&id=1gGEzSdQr-el2yBHKfeUfV9z67epcFoDG",
            "https://drive.google.com/uc?export=view&id=1gkTql5E06xpdXJSEKu3AKX8XhooJuDcG",
            "https://drive.google.com/uc?export=view&id=1g6G2Nkwv01CLHcMyVVLjm_ByO4P9DcQ7",
            "https://drive.google.com/uc?export=view&id=1gVJiNXzcNm_4t3epbgbW77kWlgCSPjkG",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perpexicity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak lucu dan membawa energi positif",  
                "pesan":"Semangat terus, semoga lancar kuliahnya, dan sukses buat kakaknya, dan semangat juga buat semester ini kak"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Lucu banget, suka sama outfit kakak",  
                "pesan":"Semangat buat kakaknya, spill outfit lucu lucunya kakak, outfit kakak menginspirasi sekali, lucu"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak positive vibes banget dan keliatan orang pinter hehheh",  
                "pesan":"Semangat kak kuliahnya, semoga tahun ini bisa cepat lulus, kak wulan keren banget, pengen jadi kayak kakak"# 1
            },
             {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton Drakor",
                "sosmed": "@anisadini10",
                "kesan": "Pertama kali ngeliat kaya engga asing, ternyata mirip Shakira di COC",  
                "pesan":"Semangat kuliah kak, sukses selalu, semoga bisa sukses juga kaya shakira"# 1
            },
             {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca Jurnal",
                "sosmed": "@dylebee",
                "kesan": "Ternyata kita se Kabupaten hehhehe, kakak lucu, outfitnya juga lucu",  
                "pesan":"Semangat ngampus kak, semoga lancar kuliahnya, semangat terus baca jurnalnya kak, jangan lupa jaga kesehatan"# 1
            },
             {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok Tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak lucu banget, dan asik",  
                "pesan":"Semangat kuliah kak, semoga lancar kuliahnya, semangat buat ngerawat tanamannya kak hehhehe"# 1
            },
             {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang asik banget orangnya",  
                "pesan":"Semangat kuliah bang, sukses selalu, jangan lupa minum air putih bang, kurangin minum kopinya"# 1
            },
             {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abangnya aga sedikit kalem, tapi asik",  
                "pesan":"Semangat kuliah bang, semangat belajarnya di semester ini dan semester berikutnya, rajin rajin baca buku terus ya bang"# 1
            },
             {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": "Abangnya lucu dan pendiam orangnya",  
                "pesan":"Semangat kuliah bang, sukses selalu, semoga selalu terjalani hobi membacanya"# 1
            },
             {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Seperti biasa tidak bisa diam orangnya",  
                "pesan":"Sehat selalu bang, abang satu ini sibuk banget, semangat kuliah dan sukses buat bang jere"# 1
            },
             {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD Tangerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linkedln, puasa senin kamis, dan ngerjain tugas draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakaknya keliatan pendiem",  
                "pesan":"Semangat ngampus dan sukses buat kakaknya, kakaknya masyaallah banget sering puasa senin kamis, jaga kesehatan ya kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ie8zc4N16SH4j__EOrt-bXfQGv_o43KE", 
            "https://drive.google.com/uc?export=view&id=1igx6OX0nYuArUp6BVEgYXV1zBsT3WjCw", 
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
                "kesan": "Kak Luthfi asik banget, bisa ngobrol banyak hal sama kak Luthfi",  
                "pesan":"Semoga sehat selalu, dan cepet lulus kuliah ya kak, ngeliat kak lutfi keren banget, jaga kesehatan ya kak, keren banget pokoknya kakak"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Berwibawa gitu bang bintang, keren banget pokoknya",  
                "pesan":"Semoga sehat selalu, dan semangat ya bang kuliahnya, semangat terus di senat, semoga semua impian abang bisa terwujud"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jG_o9_uY05ItUY230F_r3CK-6EpEZaB8",
            "https://drive.google.com/uc?export=view&id=1jQNZeRmk3owIPAtmOiB8rhOYeEND-ZOd",
            "https://drive.google.com/uc?export=view&id=1jfSs9JkRLYbdm7vIxj9BMo0-8fdenpQW",
            "https://drive.google.com/uc?export=view&id=1jeMHIOERH-fwpPgLMRWkKYWbzDDwsPO_",
            "https://drive.google.com/uc?export=view&id=1jV33EcHsGWS96NUATA6t4szG5mcG-OQ9",
            "https://drive.google.com/uc?export=view&id=1jhUpGz86uS2ycZjaPl11zGBfStjkXgGS",
            "https://drive.google.com/uc?export=view&id=1jTK6zPgGTKZGFJg1KIsDyUBPyrC0Dcv5",
            "https://drive.google.com/uc?export=view&id=1jGIx-Q43MkqAPvLWpZqT7d5j-XqUlq-t", 
            "https://drive.google.com/uc?export=view&id=1jw0CGlyT8NWtEZ6oEIgqCC2aGJU4IqKf",
            "https://drive.google.com/uc?export=view&id=1jwMzc5AyxzsBBs9f9m8GkoRillP4STKh",
            "https://drive.google.com/uc?export=view&id=1juCLovbCKCxhiic510vZbIeYKGDwdX1Q",
            "https://drive.google.com/uc?export=view&id=1jyq5_GcRn8jy59LcO4pvSXVZkXVQp-jN",
            "https://drive.google.com/uc?export=view&id=1jyAjpRLZNcecwhQ-txmqE2RvUoIRHtc3",
            "https://drive.google.com/uc?export=view&id=1FFtXIuA4WPkGpP4kH4Q_-F4qq94Gnq52",
            "https://drive.google.com/uc?export=view&id=1kB8wGqfslheS4EG9V0PFEDmhwdP1t7k-",
            "https://drive.google.com/uc?export=view&id=1k0sSQ9-H1bhCwI1jPajZW9tf1ltHPuc4",
            "https://drive.google.com/uc?export=view&id=1kLSGhTWkLuvojWyMOGKyNX1OEzs6W4nk",
            "https://drive.google.com/uc?export=view&id=1kDSfFWkrZHtgU6o3_ekxkph_G4lYYSYV",
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
                "kesan": "Berwibawa dan keren",  
                "pesan":"Semoga cepat lulus dan semangat kuliahnya bang, lancar lancar segala urusannya ya bang, sehat selalu, terimakasih sudah selalu membimbing kami"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen kos, Sukarame",
                "hobi": "Memancing keributan",
                "sosmed": "@elisabethh_",
                "kesan": "Lucu kak Abeth",  
                "pesan":"Semangat kuliahnya kak, lancar lancar semua urusannya, terimakasih buat kerja keras kakak selama ini "
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak fifah cantik gitu pas pertama ketemu",  
                "pesan":"Semangat dan sehat selalu, selalu happy terus kak, terimakasih sudah menyediakan banyak kesempatan buat kami belajar dan mengenal hal baru"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kemiling",
                "hobi": "Minum Kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Keren dan hebat banget",  
                "pesan":"Semoga sehat selalu, dan semangat kuliahnya kak, semangat juga buat semua kegiatan yang kakak jalani, lancar terus ya kak semua urusannya, jangan lupa buat istirahat"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Pertama kali ngira kakak pendiem gitu",  
                "pesan":"Semangat kuliahnya kak, lancar lancar di kuliahnya kak, dan terimakasih buat ilmu yang pernah kakak sampaikan"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kak hanum cantik dan asik",  
                "pesan":"Semangat buat kuliahnya kak, sehat, dan lancar terus, "
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Pertama kali ngira bang Ferdy orangnya pendiem",  
                "pesan":"Semangat kuliahnya bang Ferdi, terus jadi yang paling keren bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Asik orangnya",  
                "pesan":"Semangat kuliahnya bang, lancar lancar ya bang urusannya"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kak okta asik dan keren",  
                "pesan":"Semangat buat kuliahnya kak, semangat juga belajarnya"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Lucu dan asik banget",  
                "pesan":"Semoga cepat lulus dan semangat kuliahnya"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Asik dan keren banget",  
                "pesan":"Semangat kuliahnya bang jo, semangat juga buat suporteran yang keren"
            },
                        {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Bang kemas keren dan seru",  
                "pesan":"Semangat kuliah dan ngaspraknya bang, dan makasih buat ilmu serta materi yang disampaikan oleh abang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kaka lucu dan pendiem",  
                "pesan":"Semangat buat kuliahnya kak, sehat sehat juga kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Asik dan seru",  
                "pesan":"Semangat kuliahnya bang sahid, ditunggu main gitarnya lagi bang"
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Keren dan aktif banget abangnya",  
                "pesan":"Semangat buat kuliah bang, sehat sehat bang karena dimana mana selalu ada abang"
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Lucu dan cantik",  
                "pesan":"Sehat dan semangat kuliahnya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Pendiem abangnya",  
                "pesan":"Semangat kuliah abang, semoga bisa ngobrol banyak"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i_",
                "kesan": "Kaget kakak punya kembaran, pantes kaya engga asing",  
                "pesan":"Semangat kuliahnya kak, keren selalu"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RC9J863o7UMyHVsW3_NZUI_hdhy-4Jd-",
            "https://drive.google.com/uc?export=view&id=1FIwc6l4g4i4JPkK19-QdSG99S48z_fk9",
            "https://drive.google.com/uc?export=view&id=1lDZuFm0_90mLZxhY6na6nfE7ltz7Oi7O",
            "https://drive.google.com/uc?export=view&id=1lCRz4HJa4IwNMDRL0IuuKvJl1Tjm56re",
            "https://drive.google.com/uc?export=view&id=1l42FXn5Kc1gRO0iUgntnXHQ5gppBhW69",
            "https://drive.google.com/uc?export=view&id=1kSTWp2uH6T-noaLoZ4rfHElt9hMzPPHf",
            "https://drive.google.com/uc?export=view&id=1T9UKqlXVETUyycj_kvAqPP4Z8qR4dsEj",
            "https://drive.google.com/uc?export=view&id=1kzJQEtyx86J6UphZoCt83hLrpMqashqQ",
            "https://drive.google.com/uc?export=view&id=1kNsgY9OXrUSQqwixaspXlwx5qbc_X0Jg",
            "https://drive.google.com/uc?export=view&id=1kcw-TL_V4NQDwi2hDI637N7rwVA0J_OJ",
            "https://drive.google.com/uc?export=view&id=1l4be6ZaVA1i8Bpj6alkl-bngID1japX8",
            "https://drive.google.com/uc?export=view&id=1k_yja_LdK1oOFmHbFTiyXYEn1_fVQq-V",
            "https://drive.google.com/uc?export=view&id=1l4xaB84j4BHhe5KOrvnS4QsJGpkd1beR",
            "https://drive.google.com/uc?export=view&id=1kjnCxd3wO78fvAvGss-AM5_VPqT3XR8Z",
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
                "kesan": "Keren abangnya",  
                "pesan":"Semoga cepat lulus dan semangat kuliahnya, keren keren terus bang, keren banget abang ini"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Keren kak anova",  
                "pesan":"Semangat kuliahnya kak, bentar lagi lulus"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Asik abangnya",  
                "pesan":"Semangat buat kuliahnya bang, semangat buat olahraga terus, dan jangan lupa istirahat"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Asik abangnya",  
                "pesan":"Semangat bang kuliahnya, jangan main game terus ya bang, jaga kesehatan"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Kaget kakak punya kemabaran",  
                "pesan":"Semangat kuliahnya kak, semangat juga baca baca jurnal dan nyari jurnal yang banyak dan ribet itu"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Asik kakaknya",  
                "pesan":"Semangat ya kak kuliahnya, rajin rajin belajarnya ya kak, jangan lupa buat istirahat sejenak kak"
            },
             {
                "nama": "Deva Anjani Khayyuninafsyah",
                "nim": "122450014",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobi": "Menonton film",
                "sosmed": "@anjaniiidev",
                "kesan": "Kak Deva lucu, seru, baik, dan asik orangnya",  
                "pesan":"Semoga sehat selalu, dipermudah urusannya dan semangat ya kak kuliahnya, semoga kita bisa ngobrol banyak banyak kak hehehhe"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Asik kakaknya",  
                "pesan":"Semangat ya kak kuliahnya, lancar terus asprak strukdatnya kak, keren banget kakaknya, mohon bantuannya ya kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Asik kakaknya",  
                "pesan":"Semangat kak buat kuliahnya, review jurnal terus jangan lupa jaga kesehatan, dan jangan lupa makan"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Pertama kali ngeliat kakak orangnya pendiam",  
                "pesan":"Semangat kak puspa kuliahnya, semangat ngeresume SGnya kak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Keren dan asik",  
                "pesan":"Semangat buat kuliahnya bang, ajarin ngoding boleh lah bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "aAsik dan Seru",  
                "pesan":"Semangat kakak kuliahnya, riview jurnalnya juga semangat kak, pasti banyak ni yang di riview"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Asik abangnya",  
                "pesan":"Semangat kuliah bang, rajin belajar ya bang, jangan main game mulu"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Pertama kali ketemu abang jadi asprak matdas tpb 1, keren banget",  
                "pesan":"Semangat kuliahnya bang Randa, jangan sampe sakit, terimakasih buat ilmu yang disampaikan selama jadi asprak di TPB 1"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1FpxFW7aezGSFmxdxosHMQZ-HpB2LS5gk",
        "https://drive.google.com/uc?export=view&id=1H03uRjTt3DCXuvcMzmD4e4Hwb-FXskko", 
        "https://drive.google.com/uc?export=view&id=1GOHXUQVZTG28QLQSDID8kuWeFsB1qlro",
        "https://drive.google.com/uc?export=view&id=1H5CFJv_hKl4llG02l2XtnfIpHhviOHmZ",
        "https://drive.google.com/uc?export=view&id=1GKULmjr4dde49t_8ydPFlpArLr7vInJS",
        "https://drive.google.com/uc?export=view&id=1GYw4UNbofusUiGbXuiEarHIGk5RtraBu", 
        "https://drive.google.com/uc?export=view&id=1GQGRH7EXTYACoPOWKoD17MQn0sQhsHCx", 
        "https://drive.google.com/uc?export=view&id=1GUQcLcCr6GPwQEy8LY2oJscPdxZvyJm9",
        "https://drive.google.com/uc?export=view&id=1GeO8BHgA0ucvW-UBcB5K_f-dUzhKOy8l", 
        "https://drive.google.com/uc?export=view&id=1GHkvQ6VfjURXbbPMD_AiQmunpB-MEhZG", 
        "https://drive.google.com/uc?export=view&id=1GZfLdiztFi5BLv5pJWCWokefWNhJPBbo",
        "https://drive.google.com/uc?export=view&id=1G54DxsmN_DcMKVEVmxlkgyThGSrxwx-c", 
        "https://drive.google.com/uc?export=view&id=1G5r45kJ5TmJ2sc-ewAnC4sFafOxJMJ8N", 
        "https://drive.google.com/uc?export=view&id=1GsIZnGp-G8WaLD9wAX3wNY0WCLAXK89n",
        "https://drive.google.com/uc?export=view&id=1G9yvFhV2NDxowcPqxRxZY9jZ3LcQGYj1",
        "https://drive.google.com/uc?export=view&id=1GhpDqtKAYoPL0-du5lYVuexDPHnEYX4a", 
        "https://drive.google.com/uc?export=view&id=1FuAUjcb6uULfljVog-4D971_1R222OHD", 
        "https://drive.google.com/uc?export=view&id=1G1MhKHRY_ZcG_V1gIQni3kY1AJAusk8E", 
        "https://drive.google.com/uc?export=view&id=1GpatmyRIwclvQq7ZwSDsYS8PM-ayKCkg",
        "https://drive.google.com/uc?export=view&id=1FvcWD2oS1SZDXG5pioc5Nr-LVak1QiQq", 
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
                "kesan": "Keren dan asik",  
                "pesan":"Semangat kuliah dan semoga cepat lulus, dan lancar buat TA nanti, semoga dimudahkan buat nulis TA ya bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Asik dan keren",  
                "pesan":"Semoga sehat dan cepat lulus, lancar lancar nulis TA nanti ya kak, jangan lupa jaga kesehatannya kakak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Keren dan informatif",  
                "pesan":"Semoga cepat lulus dan semangat terus buat kakaknya, semoga dimudahkan kuliahnya di semester ini dan lancar lancar urusannya"
            },
            {
                "nama": "Batian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kuliahnya bang, jangan telat telat kekampus hehheh, semoga bisa datang lebih awal lagi"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya, boleh lah nanti dengerin lagu bareng"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya, info film baru yang bagus kak hehehhe"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya, sehat sehat kakak sibuk banget soalnya, pengen ngobrol sama kak ega, keren banget ngeliat kak ega ada di GENBI ITERA"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya, jangan tidur terus, jangan lupa belajar yang rajin kak, lancar lancar kuliahnya kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Keren dan informatif",  
                "pesan":"Semangat kakak kuliahnya, jangan lupa minum air putih, dikurangi minum tehnya"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Asik, Keren, dan informatif",  
                "pesan":"Semangat kuliahnya abang, semoga bisa terus selalu membaca buku, dimudahkan urusannya, semangat abang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Keren, informatif dan kelihatan pendiam",  
                "pesan":"Semoga sehat selalu dan semangat buat kak Yohana, semangat buat terus belajar kak, lancar lancar urusannya ya kak, semangat selalu"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Asik, keren dan informatif",  
                "pesan": "Semangat abang kuliahnya, semoga cepat lulus, semangat terus buat bikin portofolionya"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat abang kuliahnya, spill resep makanan yang enak bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Lucu, asik, Keren dan informatif",  
                "pesan": "Semangat kak UYI kuliahnya, NIM kita sama kak ujungnya, semoga kita bisa cerita cerita banyak nanti kak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Keren dan informatif",  
                "pesan": "semangat kakak kuliahnya, lancar lancar nyari jurnalnya ya kak, semoga dipermudah mereview jurnalnya"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat ABANG kuliahnya, jangan lupa belajar, lancar terus kegiatannya, dikurangi main gamenya bang hehehh"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Asik, keren, aktif banget, dan informatif sekali kak izza",  
                "pesan": "Semangat kak IZZA kuliahnya, ngaspraknya juga, sehat selalu kak izza"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat kakak kuliahnya, bolehlah nanti kita nyanyi bareng, boleh juga kak spill lagu yang bagus"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Pendiam dan informatif penyampaiaannya",  
                "pesan": "Semangat ABANG kuliahnya, semoga bisa eksplor banyak hal, semoga bisa banyak cerita lagi, karena ngeliat abang selalu diem"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Keren dan informatif",  
                "pesan": "Semangat kakak kuliahnya, banyak baca artikel jangan lupa jaga kesehatan kak, lancar lancar baca artikelnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1RIrZLE8Hfl3dZLDpKbhj9DWiCbQcATKr",
        "https://drive.google.com/uc?export=view&id=1iEEgrMCtj5SPxGzIfAbH_F0q0yETMT_i",
        "https://drive.google.com/uc?export=view&id=1i6Ao1wwRhzB-d1FuITZu2OWXPQB3_Kai",
        "https://drive.google.com/uc?export=view&id=1i417gpTDMzxj5S-OJ_9NUTBhy7MZsTev", 
        "https://drive.google.com/uc?export=view&id=1iB9ywwYOq6CNvFzG0pQ_8a5dwgzzl1VJ",
        "https://drive.google.com/uc?export=view&id=1i1d_ZSe1xDo9vyMlsZZDJIBLoYcjobLe",
        "https://drive.google.com/uc?export=view&id=1idgmpSiec9Bq26eXBsUz_JxSAGYc-8az", 
        "https://drive.google.com/uc?export=view&id=1iNBb7xAUXc1eB06tcn6-RxBUNKpcdsvu",
        "https://drive.google.com/uc?export=view&id=1iaCqQHCSLvk_Cg3_saxdRn7DXp3NoiAr",
        "https://drive.google.com/uc?export=view&id=1iCL_6yb9p4RjQdlalWgtB_yto3CFC78Y", 
        "https://drive.google.com/uc?export=view&id=1iONWXKyD0Q8QX6E2qrrklPGhHc0PmdUU",
        "https://drive.google.com/uc?export=view&id=1iDNHrs1tNr3860gZOKc9Zl5itb5MdZdf", 

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
            "kesan": "Keren banget dan asik",
            "pesan": "Sehat dan semangat kuliahnya bang, keren terus lah abang ini, jaga kesehatan dan jangan lupa istirahat bang dimas"
        },
        {
            "nama": "Catherine Firdhasari Maulina Sinaga",
            "nim": "121450072",
            "umur": "20",
            "asal": "Medan",
            "alamat": "Airan",
            "hobi": "Baca Novel",
            "sosmed": "@catherine.sinagaa",
            "kesan": "Lucu dan cantik",
            "pesan": "Semangat kuliahnya kak, boleh lah kak saran novel yang bagus mau baca novel soalnya tapi bingung hehehhe"
        },
        {
            "nama": "M. Akbar Resdika",
            "nim": "12145006",
            "umur": "20",
            "asal": "Lampung Barat",
            "alamat": "Labuhan Dalam",
            "hobi": "Ngoding",
            "sosmed": "@akbar_resdika",
            "kesan": "Keren dan asik orangnya",
            "pesan": "Semangat kuliah abang, ngodingnya lancar terus bang, semoga tidak banyak ketemu error"
        },
        {
            "nama": "Rani Puspita Sari",
            "nim": "122450030",
            "umur": "20",
            "asal": "Metro",
            "alamat": "Rajabasa",
            "hobi": "Denger musik",
            "sosmed": "@ranniu",
            "kesan": "Keren dan seru banget",
            "pesan": "Semangat dan sehat selalu kak, info lagu yang bagus kak, dan jangan lupa buat jaga kesehatan ya kak"
        },
        {
            "nama": "Rendra Eka Prayoga",
            "nim": "122450112",
            "umur": "20",
            "asal": "Bekasi",
            "alamat": "Belwis",
            "hobi": "Ngaji",
            "sosmed": "@rednraepr",
            "kesan": "Lucu dan keren",
            "pesan": "Semangat kuliah dan ngaspraknya strukdatnya bang, boleh lah nanti saya minta ajarin"
        },
        {
            "nama": "Salwa Farhanatussaidah",
            "nim": "122450055",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Jl. Airan",
            "hobi": "Renang Tapi Gabisa Renang",
            "sosmed": "@slwfhn_694",
            "kesan": "Asik kakaknya",
            "pesan": "Semangat dan semoga keren selalu, semangat buat belajar berenangnya kak"
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
            "pesan": "Semoga cepat lulus dan semangat abang, semangat olahraga juga bang, jangan lupa istirahat sehabis olahraga bang"
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
            "pesan": "Semangat kakak buat kuliahnya, semangat buat jaga kebun dan berkebunnya"
        },
        {
            "nama": "Josua Panggabean",
            "nim": "12145001",
            "umur": "21",
            "asal": "Pematang Siantar",
            "alamat": "Gya Kos",
            "hobi": "Nonton Film",
            "sosmed": "@josuapanggabean16_",
            "kesan": "Asik dan informatif",
            "pesan": "Semangat bang buat kuliahnya, spill film yang bagus bang, lancar lancar terus bang kegiatannya, keren banget"
        },
        {
            "nama": "Meira Listyaningrum",
            "nim": "122450011",
            "umur": "20",
            "asal": "Pesawaran",
            "alamat": "Airan",
            "hobi": "Membaca",
            "sosmed": "@meiralsty_",
            "kesan": "Keren dan asik",
            "pesan": "Semangat kuliah, rajin rajin membaca, semoga kuliahnya dapet A"
        },
        {
            "nama": "Rendi Alexander Hutagalung",
            "nim": "122450057",
            "umur": "20",
            "asal": "Tangerang",
            "alamat": "Kos Benawang",
            "hobi": "Nyanyi",
            "sosmed": "@rexanderr",
            "kesan": "Asik dan keren",
            "pesan": "Semangat ya bang kuliahnya, mau denger suara abang pas nyanyi"
        },
        {
            "nama": "Renta Siahaan",
            "nim": "122450070",
            "umur": "21",
            "asal": "Sumatera Utara",
            "alamat": "Sukarame",
            "hobi": "Membaca",
            "sosmed": "@renta.shn",
            "kesan": "Keren kakaknya",
            "pesan": "Semangat kakak kuliahnya, lancar terus membacanya kak, jangan lupa istirahat sebentar kak, nanti bisa membaca lagi"
        },
    ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ikIJSwocT9imEnuqQp1PfOC4m-LDfCrK", #Bang Andrian
            "https://drive.google.com/uc?export=view&id=1j6uqHb707WyD8dpW4MMODRMhqkAqgt92", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1itM7zI-AA_sA-ILGZ3rSBc-4jE6bF_Si",# Kak Nabila
            "https://drive.google.com/uc?export=view&id=1imMvzMwsIIgrwYFjXucgZ8_EQa0BU7ys",# Kak Nabilah
            "https://drive.google.com/uc?export=view&id=1ipdxgU2mk3Pl-BqQjSQ5QJGAUCZZpFXB",# Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1ixXKkRL4vlD1QRWgZdkr3Ypxpdv1v6nf",# Bang Danang
            "https://drive.google.com/uc?export=view&id=1j7j4PgCr0SPzxL-KZKuRH5oT891N1Xs8",# Bang Farrel
            "https://drive.google.com/uc?export=view&id=1SoADvJDuf-CbejqMI8ADB6jBVTZjg1U0",# Kak Tessa
            "https://drive.google.com/uc?export=view&id=1io6Woz-ES0y2sOijOpvH2HXdOjJQ_-xJ",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=1jG1b-Gt8TzcBH6G5xPWth0heTjzp1zKK",# Bang Dhafin
            "https://drive.google.com/uc?export=view&id=1j8_jCq_-ETVOgDqwJaGxwXlqWWcrb_EL",# Kak Elia

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
                "kesan": "Keren liat abangnya pas pertama kali ketemu lagi megang kamera",  
                "pesan": "Semangat kuliah bang, semoga cepet lulus, sehat sehat juga buat abangnya, terimakasih buat ilmu bisnis hehhh!"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Cantik kakaknya",  
                "pesan": "Semoga tetep cepet lulus dan semangat kuliahnya kak, jangan lupa buat terus belajar, kakak keren pokoknya!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Lucu dan cantik!",
                "pesan": "Sesuai dengan hobi, semangat nyari duit kak hehheh!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "Keren kakaknya!",
                "pesan": "Hobi tidur tapi cuan lanjut terus ya kak, aamiin, semangat cari duit kak, boleh spill cara cari duit hehheh"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Pertama kali ngira abang orangnya pendiem",
                "pesan": "Semangat kuliahnya ya bang, jaga kesehatan dan jangan sampe sakit lagi bang!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "Kere si bang danang ini",
                "pesan": "Semoga bisnis lancar, kuliah juga lancar bang!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "Keren dan baik banget bang",
                "pesan": "Semoga sehat selalu, dan selalu keren, terimakasih bisa memimpin suporteran yang keren ini!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa asik orangnya!",
                "pesan": "Semangat kuliah kak!, semoga bisa nerbitin buku sesuai dengan hobi kakak yang suka menulis"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kak Alvia asik banget",
                "pesan": "Sehat selalu, dan semangat kuliahnya kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Pendiem orangnya",
                "pesan": "Semangat kuliah ya bang, lancar lancar urusannya"
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
                "pesan": "Semangat buat kakaknya, mau denger kakak nyanyi"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lQo48DQvIw78-QqttabBk8JgmZCNYxzS", # bang wahyu
            "https://drive.google.com/uc?export=view&id=1lWizkcqODALyuvAV4z0BhMnnodje-Naq", # kak arsyi
            "https://drive.google.com/uc?export=view&id=1lxmVKblyIr391DzfRcz5wTY5BqXmLA8w", # bang kai
            "https://drive.google.com/uc?export=view&id=1m1KEm0WSJKc4cI7Ja_CjmjJSFV0BAgih", # bang arsal
            "https://drive.google.com/uc?export=view&id=1lFyrI8b1Traj5kT4SOp1a4pgP9MgTWX7", # kak elok
            "https://drive.google.com/uc?export=view&id=1lUlRJZo_wtkMMdTdLjw-HqdhPNJ_uhCU", # kak juju
            "https://drive.google.com/uc?export=view&id=1lX-ngqpu90dmXg_MjWQOND-3zIUI8eFt", # kak nel
            "https://drive.google.com/uc?export=view&id=1lYKOJsgT_OV1I-oBqQH1ze95xIlwhUCE", # kak try yani
            "https://drive.google.com/uc?export=view&id=1mOe51pnxnRmYNGOhPR9oP1IQG_I1uMS5", # kak dwi
            "https://drive.google.com/uc?export=view&id=1T3vb_bLwsFS3uAPDrqroh0pvaGdJQoaa", # bang gym
            "https://drive.google.com/uc?export=view&id=1lZvOKk2kDKtbpPoyoJd78ok7vU5a7IWs", # kak nasywa
            "https://drive.google.com/uc?export=view&id=1lt_xN2d0Le_TNzW32PDDboBDuyjKybJY", # kak priska
            "https://drive.google.com/uc?export=view&id=1m16exuw5d7-tfW4BZBosvwNB3LZuCSnK", # bang abit
            "https://drive.google.com/uc?export=view&id=1lbE0bW7SbxY0fYm63qc8uumNv2C1tsKV", # bang hermawan
            "https://drive.google.com/uc?export=view&id=1m6N2fJxsSih8goynmSurtAp6NYrOynrN", # kak khusnun nisa
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
                "kesan": "Bang Wahyu keren abis si!",
                "pesan": "Semangat kuliahnya bang, cepat lulus dan lancar lancar buat TA nya nanti, gokil terus abang ini!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Kak Arsyi lucu banget",
                "pesan": "Semangat dan sukses selalu kak, ngontennya jangan kasih kendor!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kai asik banget!",
                "pesan": "Semangat bang, sehat selalu, semoga hobinya cepet ketemu"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "Abang lucu banget",
                "pesan": "Sehat dan semangat terus bang, boleh lah bang info parfum yang wangi"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok cantik banget, lucuuuu",
                "pesan": "Sehat sehat dan semangat kak elok ngedit ngeditnya"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Lucu banget kak juju ni, baik, dan canntiiikkk",
                "pesan": "Sehat selalu kak, bahagia selalu, semangat, murah rezeki, dan maafkan aku yang sering merepotkan kakak, terimakasih sudah selalu mengayomi kita"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Nel asik dan luch abis",
                "pesan": "Semangat dan happy terus kak, info ubi cilembu yang enak kak!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Asik abiss",
                "pesan": "Semangat kak buat kuliahnya, jangan lupa belajar, dan terus jadi kakak yang seru hehehh, keren keren"
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
                "pesan": "Semangat dan sehat selalu kak, jangan scroll tiktok terus heheh, semangat buat belajarnya kak, lancar lancar semester ini"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Awal ketemu ngira abang pendiem, tapi best banget si abang satu ini",
                "pesan": "Semangat buat kerjaannya bang, jangan lupa jaga kesehatan, semangat bang, terimakasih sudahh membimbing dan mengayomi kita"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "Asikk banget",
                "pesan": "Semangat buat kakaknya, tambah rajin bersih bersih ya kak"
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
                "pesan": "Sehat selalu dan semangat kak, lancar lancar urusannya"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "Lucu abis si abangnya",
                "pesan": "Sehat sehat ya bang, banyak banget hobi abang soalnya"
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
                "pesan": "Semangat ngasprak alpronya yaa bang, dan semangat juga kuliahnya"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Lucu dan imut kakaknya",
                "pesan": "Semangat dan sukses selalu kak, spill DIY pake printernya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan
