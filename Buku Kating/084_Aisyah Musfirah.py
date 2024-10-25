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
            st.write(f"Nama          : {data_list[i]['nama']}")
            st.write(f"NIM           : {data_list[i]['nim']}")
            st.write(f"Umur          : {data_list[i]['umur']}")
            st.write(f"Asal          : {data_list[i]['asal']}")
            st.write(f"Alamat        : {data_list[i]['alamat']}")
            st.write(f"Hobi          : {data_list[i]['hobi']}")
            st.write(f"Sosial Media  : {data_list[i]['sosmed']}")
            st.write(f"Kesan         : {data_list[i]['kesan']}")
            st.write(f"Pesan         : {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rFxFPswgUWXkSRpvAVDziRwI3zi96-Rd",
            "https://drive.google.com/uc?export=view&id=160KRFxbOTlh65yuFGVv1zviaz-XmENrG",
            "https://drive.google.com/uc?export=view&id=1QHuI70jB8yxoZIyOueCXmpdxCHKkjb5n",
            "https://drive.google.com/uc?export=view&id=16EOs6rIPUaBMGyEOiw3izEtM3r_HEFoU",
            "https://drive.google.com/uc?export=view&id=1hmlE4HgO2McumkOmZ_og6RUR0ilGM1pW",
            "https://drive.google.com/uc?export=view&id=1WENphSXp1NA7h1ABaufl7jFVJYHLY8rz",
        ]
        data_list = [
            {
                "nama"	    : "Kharisma Gumilang",
                "nim"		: "121450142",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pulau Damar",
                "hobi"		: "Dengar musik",
                "sosmed"	: "@gumilangkharisma",
                "kesan"	    : "Bang Gumi sangatlah berkharisma",  
                "pesan"	    : "Semangat TA bang"# 1

            },
            {
                "nama"	    : "Pandra Insani Putra Azwar",
                "nim"		: "121450137",
                "umur"	    : "21",
                "asal"		:" Lampung Utara",
                "alamat"	: "Jl. Bawean 2, Sukarame",
                "hobi"		: "Main Gitar",
                "sosmed"	: "@pndrinsni27",
                "kesan"	    : "Nggak nyangka pernah sekelompok MSS sama Bang Pandra",  
                "pesan"	    : "Semangat MSS bang"# 2
            },
            {
                "nama"	    : "Meliza Wulandari",
                "nim"		: "121450065",
                "umur"	    : "20",
                "asal"		:" Pagar Alam",
                "alamat"	: "Kota baru",
                "hobi"		: "Drakoran",
                "sosmed"	: "@wulandarimeliza",
                "kesan"	    : "Aku inget banget Kak Meliza yang nyapa aku pas maulidan^^",  
                "pesan"	    : "Kakak kerennn, semangat kak!"# 3
            },
             {
                "nama"	    : "Putri Maulida Chairani",
                "nim"		: "121450050",
                "umur"	    : "21",
                "asal"		:" Payakumbuh",
                "alamat"	: "JL. Nangka IV",
                "hobi"		: "Dengarin Bang Pandra gitaran",
                "sosmed"	: "@ptrimaulidaaa_",
                "kesan"	    : "Nggak nyangka urang awak hehe",  
                "pesan"	    : "Semangat nyekre kak^^"# 4
            },
            {
                "nama"	    : "Hartiti Fadilah",
                "nim"		: "121450031",
                "umur"	    : "21",
                "asal"		:" Palembang",
                "alamat"	: "Pemda",
                "hobi"		: "Nyanyi",
                "sosmed"	: "@hrtfdlh",
                "kesan"	    : "Kakaknya pendiem",  
                "pesan"	    : "Kutunggu debutnya kak"# 5
            },
            {
                "nama"	    : "Nadilla Andhara Putri",
                "nim"		: "121450003",
                "umur"	    : "21",
                "asal"		:" Metro",
                "alamat"	: "Kota baru",
                "hobi"		: "Membaca",
                "sosmed"	: "@nadillaandr26",
                "kesan"	    : "Kakak asprak strukdat RA",  
                "pesan"	    : "Jangan kapok asprakin kita yaa kak"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12X592X0iyyY5tUFgtpuAR_Qal0aZb0pu",
            "https://drive.google.com/uc?export=view&id=1VTuAEnH9u1IZeHdTwwGjufHW8I-KD46t",
            "https://drive.google.com/uc?export=view&id=1HZDc5mPndEWZd-C-oP4ETp2WQO0kLcet",
            "https://drive.google.com/uc?export=view&id=1853QyVYGjQsZmXuG7XLeKSrmvq4tGuLP",
            "https://drive.google.com/uc?export=view&id=1hezfODhirAMNZTGZls72f7LnAEptt9z8",
            "https://drive.google.com/uc?export=view&id=1YydouQ6hNqFaifn2x_VXNWVzBu3I521P", 
            "https://drive.google.com/uc?export=view&id=1HnTYHGxHErVMltYfSm3ma-X0AHW4yWLu",
            "https://drive.google.com/uc?export=view&id=1dviUKg6LYiWdRZBrsYxxNQc2vCHKtuwX",
            "https://drive.google.com/uc?export=view&id=178FvUg8q57WEmkZr0a1a3YeE_G0IUXJK", 
            "https://drive.google.com/uc?export=view&id=1jTRBttbxVyTobK09JEYt6EpSy8NI6JVs",
            "https://drive.google.com/uc?export=view&id=11bOHc0wOybjtxEh9GwFptxZ8weZAjrAE"
        ]
        data_list = [
            {
                "nama"	    : "Tri Murniya Ningsih",
                "nim"		: "121450038",
                "umur"	    : "21",
                "asal"		: "Bogor",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Searching di perpexcity",
                "sosmed"	: "@trimurniaa_",
                "kesan"	    : "Kak Niya good-vibes bangett",  
                "pesan"	    : "Semangat ngasprak RA kak"# 1

            },
            {
                "nama"	    : "Annisa Cahyani Surya",
                "nim"		: "121450114",
                "umur"	    : "21",
                "asal"		: "Tangerang",
                "alamat"	: "Jatimulyo",
                "hobi"		: "Baca dan nonton",
                "sosmed"	: "@annisacahyanisurya",
                "kesan"	    : "Kak Annisa kece hehe",  
                "pesan"	    : "Semangat nyekre kak"# 6
            },
            {
                "nama"	    : "Wulan Sabina",
                "nim"		: "121450150",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@wlsbn0_",
                "kesan"	    : "Pengen ketularan possitive vibesnya Kak Wulan^^",  
                "pesan"	    : "Keep your vibes kak!",
            },
            {
                "nama"	    : "Anisa Dini Amalia",
                "nim"		: "121450081",
                "umur"	    : "21",
                "asal"		: "Medan",
                "alamat"	: "Raden Saleh",
                "hobi"		: "Nonton drakor",
                "sosmed"	: "@anisadini10",
                "kesan"	    : "Kak Anisa mirip Shakira CoC",  
                "pesan"	    : "Semangat nge-stan Svt kak!"# 6
            },
            {
                "nama"	    : "Claudhea Angeliani",
                "nim"		: "121450124",
                "umur"	    : "21",
                "asal"		: "Salatiga",
                "alamat"	: "Lampung Timur",
                "hobi"		: "Baca jurnal",
                "sosmed"	: "@dylebee",
                "kesan"	    : "Vibes kak Claudhea girly bangett",
                "pesan"	    : "Semoga kubisa girly kayak kakak^^"# 2
            },
            {
                "nama"	    : "Dhea Amelia Putri",
                "nim"		: "122450004",
                "umur"	    : "19",
                "asal"		: "Buleleng",
                "alamat"	: "Natar",
                "hobi"		: "Bercocok tanam",
                "sosmed"	: "@_.dheamelia",
                "kesan"	    : "Kak Dhea lucu",
                "pesan"	    : "Semangat nugasnya kak" # 3
            },
            {
                "nama"	    : "Muhammad Fahrul Aditya",
                "nim"		: "121450156",
                "umur"	    : "21",
                "asal"		: "Surakarta",
                "alamat"	: "Pahoman",
                "hobi"		: "Ngopi",
                "sosmed"	: "@fhrul.pdf",
                "kesan"	    : "Kayak sering ngeliat abang tapi dimana yak",  
                "pesan"	    : "Semangat bangggg"# 6
            },
            {
                "nama"	    : "Feriyadi Yulius",
                "nim"		: "122450087",
                "umur"	    : "20",
                "asal"		: "Sumatera Selatan",
                "alamat"	: "Depan Koban",
                "hobi"		: "Baca buku",
                "sosmed"	: "@fer_yulius",
                "kesan"	    : "Ternyata kita mutualan di LinkedIn bang",  
                "pesan"	    : "Semangat bang"# 5
            },
            {
                "nama"	    : "Mirzan Yusuf Rabbani",
                "nim"		: "1224500118",
                "umur"	    : "20",
                "asal"		: "Jakarta",
                "alamat"	: "Korpri",
                "hobi"		: "Membaca",
                "sosmed"	: "@myrrinn",
                "kesan"	    : "Abang ini lucu",  
                "pesan"	    : "Semangat otw semester akhir bang"# 6
            },
            {
                "nama"	    : "Jeremia Susanto",
                "nim"		: "122450022",
                "umur"	    : "20",
                "asal"		: "Balam",
                "alamat"	: "Balam",
                "hobi"		: "Gangguin orang",
                "sosmed"	: "@jeremia_s_",
                "kesan"	    : "Bang Jere suka random datengin kelas anak 23",
                "pesan"	    : "Semangat panitnya bang"# 4
            },
            {
                "nama"	    : "Berliana Enda Putri",
                "nim"		: "122450065",
                "umur"	    : "20",
                "asal"		: "BSD, Tangerang Selatan",
                "alamat"	: "Teluk",
                "hobi"		: "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed"	: "@berlyyanda",
                "kesan"	    : "Kak Berlin pendiem",  
                "pesan"	    : "Semangat kakk"# 6
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YlEIT7a0PjbiOgAzF-LO_tlfsByRBS-C", 
            "https://drive.google.com/uc?export=view&id=1LlDsHIqBxd0qMhwkU5sThke77MPzHmOA"
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
                "kesan": "Kak Upi I like the way you speak",  
                "pesan": "Semoga makin keren kak!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Bang Bintang sepertinya softboy",  
                "pesan": "Semoga next jabatannya adalah senator"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JQR1RXKDcfMeYxaYDlrrrzndfO0euVam", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1VFR2MR-cdzWkkieqiKq8hX8nC5Dh2yRk", #Kak Abet, belum
            "https://drive.google.com/uc?export=view&id=1nOHmFK52G7azu8MgzX-K-IlOvrzS6BPH", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1nItMksj-CcSwWWrfYZFDp4CMrqPp1mls", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1mtk8-ZzQHxyDARFltVBCr0ZOJZYuC-6l", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1n3rhxN02-U-uYXYNEspyh_qgEl0Leupr", #Kak Anum
            "https://drive.google.com/uc?export=view&id=1mwb6fEf717ycFzSAlLg0qJd4-XZBl2Se", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1Ty9ZjS_KUfN4yZBRuNMVRo0aktVmjBcI", #Bang Deri, belum
            "https://drive.google.com/uc?export=view&id=1n6QDrQQMiB40ceOqmJ9_muqb00FX1id4", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1lk0eK24FpFrtf9aliNv2Z8WXrYCMgVTy", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1lbARXNqa7KXmxNMVKflxjociIr2dPOse", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1lq8Sloe1iXe8-81xHkV_zRnYKH8Z8q5x", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1m4w-pYsfwcm82GRLmsx2_bdCNYo5cu7d", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1m4SJe5H5v3MF69o6wftU1TwhpebF1UDF", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1Uh79V4Akmj5j3IM3jDPPTU7fBqScAGbK", #Bang Ateng, belum
            "https://drive.google.com/uc?export=view&id=1mSibl3aqFnNJZnKTnFRRRF6pTW6K-TGp", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1mR2Hln284_WO4xpRnfX9VQSLN4TiAhU2", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1med6ksfzc8KyJwTy09mud7Vr9YsdKinP", #Kak Dini
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
                "kesan": "Sekelas sama beliau di MSS",  
                "pesan": "Semangat MSS Bang"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"",
                "alamat": "Owen Kos, Sukarame",
                "hobi": "",
                "sosmed": "@elisabethh_",
                "kesan": "Kak Abet friendly banget",  
                "pesan": "Semangat nyekre PSDA kak"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Independent woman banget",  
                "pesan": "Semangat ngader kak"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Kak Allya badass banget",  
                "pesan": "Maafin kesalahan saya pas kader kak, plis"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "Vibes pinter banget kakaknya",  
                "pesan": "Semoga lulus tepat waktu kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Tau Kak Hanum dari BC-an bayar atribut",  
                "pesan": "Semangat kak"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Bang Kevin sering nge-MC",  
                "pesan": "Semangat MC bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Bang Deri kocak",  
                "pesan": "Semangat bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya kalem",  
                "pesan": "Pertahankan aura kalemmu kakk"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Tau Bang Deyvan pas FG, beliau nyanyi lagu Opick",  
                "pesan": "Tetap pertahankan kocakmu bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Bang Jo sangat friendly, cocok dengan Kak Abet",  
                "pesan": "Semangat friendly bang"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Tau Bang Kemas dari pra-kader, tutor bikin website",  
                "pesan": "Jangan kapok ngajarin kita yaa bang"
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
                "pesan": "Semangat KKN kakk"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Sepertinya Bang Sahid jago gitaran",  
                "pesan": "Semangat gitaran bang"
            },
                        {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Bang Ateng sangat bapack-able",  
                "pesan": "Semangat supporteran bang"
            },
                        {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kak Jaclin girly banget",  
                "pesan": "See you di MSS kak^^"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Bang Rafly pendiam",  
                "pesan": "Pertahankan vibesmu bang"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak ini lucu",  
                "pesan": "Vibes lucunya jangan sampai luntur yaa kak^^"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o0L33HcxDTYBjYE42lSJhPdkiP5P5enX", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1nebd0GRELYd2phoRMpJoUL0pHN7eI9PW", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1sDzUHDVm1XsoqXQKRNwqv1_BfVCYSQcf", #Bg Sahid ok
            "https://drive.google.com/uc?export=view&id=1suanaCa8NMM2E-dCi1ctF_zMDVz_aAwI", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1sMNnV6nX6bWLkzqh2twz6egNCqg1nNZ0", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1s5pEp5wJOoWBnWZEZRguVn6DTVrEVkE7", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1s6dnCFl_ZV2bPzYvTgJ80wbilpZ9ZfmP", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1rYBuvQkkyk_LfhzBep-8FoKFVbXlxpHE", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1s04M12NOiG5m3iCHG5tA2i4gZF7ZEHSb", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1sy-_wgG77Z2ic5facb5xAPm1nCxV3kNt", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1rYfDcuIcLEugK1vh4TAPA8yLY1Fm2yjJ", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1nuV2lsXvugjsXfHYi7QyMuRY0m0-X3ON", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1sqMAe8pLjI1K9rAx3t05ciG1yM-OCkx_", #Bang Randa ok
            "https://drive.google.com/uc?export=view&id=1rQs7v7TrFuhDxrUV8YCe1IJXZzqFikik", #Bang Regi ok
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
                "kesan": "Aura kadepnya kerasa",  
                "pesan": "Semangat bang, dikit lagi lulus"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kak Anova baikkk",  
                "pesan": "Makasi udah save WA aku kak hehe"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Bang Sahid ini daplok besti aku",  
                "pesan": "Semangat daplokin Azizah bang"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Bang Fadhil anak DC ya?",  
                "pesan": "Hwaiting sunbae-nim!"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Kak Dina lucu",  
                "pesan": "Semangat kakk"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kak Dinda lucu",  
                "pesan": "Semangat mikfes kakk"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kak Eta baik banget, masa aku foto canggung beliau rangkul^^",  
                "pesan": "Keep your vibes kak!"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Asprak alpro RA hehe",  
                "pesan": "Kak Ruth kerennn"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kak Puspa aku save WA kakak loh",  
                "pesan": "Semangat resumenya kak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Asprak strukdat RA",  
                "pesan": "Semoga next jabatan kadiv, atau sekalian kadep yaa bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Hobinya keren kak",  
                "pesan": "Boleh minta salinan reviewnya kak? Hehe"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Karang Anyar",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Namanya unique bang^^",  
                "pesan": "Semangat semester 5 bang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Asprak ADS RA",  
                "pesan": "Bang plis saya tidur jangan dipoto lagi T.T"
            },
            {
                "nama": "Muhammad Regi Abdi Putra Amanta",
                "nim": "122450031",
                "umur": "19",
                "asal": "Palembang",
                "alamat": "Jl. Permadi, Sukarame",
                "hobi": "Nyanyi",
                "sosmed": "@mregiiii_",
                "kesan": "KEREN BGT. Udah Madani, Duta lagi",  
                "pesan": "Semoga saya bisa keren dan multitalent kayak abang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()
# Tambahkan menu lainnya sesuai kebutuhan
