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
            "https://drive.google.com/uc?export=view&id=138YG1WnVXAiNZSzrTrFdEXoYh1ryNSkN",
            "https://drive.google.com/uc?export=view&id=1L2CDQakXGiDLW1otx7P3QzqzXtfc2uwX",
            "https://drive.google.com/uc?export=view&id=1VtH6gtYMZmP4X1NckmZ7IS5hrrLd18dB",
            "https://drive.google.com/uc?export=view&id=1HXfkNlixI7zd7ei8LUr1TvQdz_R6WOpZ",
            "https://drive.google.com/uc?export=view&id=1htFol76dNLMmOXWlSyenJkSbdNs0MOiP",
            "https://drive.google.com/uc?export=view&id=1VTYjQi5uXt02NkTFl_gLFim77JObhWSc",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Dengar musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Abang ini berkarisma dan asik untuk ngobrol",  
                "pesan": "Semoga lulus tepat waktu"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal": "Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main Gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Asik dan informatif",  
                "pesan": "Semangat kuliah dan ngaspraknya !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak baik banget, informatif jawab pertanyaan",  
                "pesan": "Semangat nerusin surat menyuratnya kak !!!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak ini agak pendiam",  
                "pesan": "Semangat kuliah dan ngurus bendaharanya kak !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh",
                "alamat": "Jl. Nangka IV",
                "hobi": "Dengerin Bang Pandra gitar",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakaknya lucu, baik juga",  
                "pesan": "Semangat kuliah dan tugas sekretarisnya kak !!!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Kakak ini baik, seru juga",  
                "pesan": "Semangat ngurus keuangan himpunan kak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dnsku-PsUCCMPsAQ1fbHjLQbh8hJpvR9", #1
            "https://drive.google.com/uc?export=view&id=1sO0E7fAOroXtxBgWMxYREUJ1Jzik7Qfz", #2
            "https://drive.google.com/uc?export=view&id=1hcmisSbjn0QQOS6G79YhWVc6qjovX22x", #3
            "https://drive.google.com/uc?export=view&id=1dlITh6jrEIjoFrKdJVe8dNNOWgP_BuKr", #4
            "https://drive.google.com/uc?export=view&id=1eduqIQ8qsLaZkRLPzfl86UUm5dvm_Svl", #5
            "https://drive.google.com/uc?export=view&id=1K6MLmUYS__FbrCC_Iv9CnGxYMsBcmq4k", #6
            "https://drive.google.com/uc?export=view&id=1sW5fDqHqubPZvXUApPYnO9OR5hZ0wy9u", #7
            "https://drive.google.com/uc?export=view&id=10KxRK7yH0o36m12acpn0SgNWCbuaCxTB", #8
            "https://drive.google.com/uc?export=view&id=1NamXOptVY8VwE-rsbJlK5tAoQOQxOoVr", #9
            "https://drive.google.com/uc?export=view&id=1lD5urM5arHyWSzTBJUTliLbnctx5m96q", #10
            "https://drive.google.com/uc?export=view&id=1R5sivbKS--ja_7kqutNqapEAicWhuJLL", #11
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal": "Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexcity",
                "sosmed": "@trimurniaa_",
                "kesan": "Kakak ini lucu dan suka ngobrol",  
                "pesan":"Semangat ngasprak nya kakk!!!" #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Style nya lucu banget kak",  
                "pesan":"Tetap on point ya kak stylenya !!!" #2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kakak ini baik banget mau berbagi pengalaman magang di Telkom",  
                "pesan":"Semoga lulus kerja di Telkom ya kak, Spill portofolionya kak !!!" #3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Malang",
                "alamat": "jati agung",
                "hobi": "Baca Webtoon",
                "sosmed": "@anisadini10",
                "kesan": "Kakak mirip banget sama Shakira COC",  
                "pesan":"Semoga nilai di kuliah memuaskan ya kak !!!" #4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Kakak cantik banget",  
                "pesan":"semangat terus kuliahnya kakak !!!" #5
            },
             {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta, Jawa Timur",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "Abang ini baik, salfok sama kumisnya ",  
                "pesan":"semangat kuliah dan ngaspraknya bang !!!" #6
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal": "Sumatera Selatan",
                "alamat": "Depan koban",
                "hobi": "baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Abang ini seru di ajak ngobrol",  
                "pesan":"semangat kuliah dan organisasinya bang !!!" #7
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini stylenya bagus",  
                "pesan":"Semangat terus bang kuliahnya dan tugas-tugasnya !!!" #8
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Kakak ini lucu banget",  
                "pesan":"Semangat kuliah dan panitia acaranya kakk !!!" #9
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"BSD",
                "alamat": "Teluk",
                "hobi": "Suka liat linked in, Puasa senin kamis, Ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Kakak ini hobinya banyak banget pasti seru",  
                "pesan":"semangat kuliah dan puasa senin kamisnya kak !!!" #10
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar lampung",
                "alamat": "Bandar lampung",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Abang ini seru, asik di ajak bercanda",  
                "pesan":"Semangat nugasnya bang !!!" #11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oRaRIzD3ctpVJas-sdo2o-SyRFUkbzWl", 
            "https://drive.google.com/uc?export=view&id=1es9HLza1teh2N7zHorj3ifBpI4clGS0E", 
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
                "kesan": "Kakaknya seru, jelasinnya asik banget",  
                "pesan":"Semangat nyelesain proposalnya kak!"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini lucu, kocak tapi tegas, baik jugaa",  
                "pesan":"Semangat terus jadi ketangnya bang!"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hr_Tn0fpnA-iqFoST3Dl9tkgyUTLKcfJ", #Bg Ericson
            "https://drive.google.com/uc?export=view&id=1O0IqIw5-Di3x8vJmhX5O1-vMg4g8vYgR", #Kak Abet
            "https://drive.google.com/uc?export=view&id=1Su2IOxYZPsjdDeRtyTHhM1BVTXqP8aex", #Kak Afifah
            "https://drive.google.com/uc?export=view&id=1wSE58M3jBddq_20JdfjFbBukUyemOG3J", #Kak Allya
            "https://drive.google.com/uc?export=view&id=1fjTnli27K-ejLCQFQOS-hIiNiHdcrtwB", #Kak Eksanty
            "https://drive.google.com/uc?export=view&id=1LNoYMQNcpaE4VkSXGbAfWZzZq3umwTrO", #Kak Anum
            "https://drive.google.com/uc?export=view&id=19Q8RjT709Gzu5c49_z0XQglAJe1B2ILz", #Bang Ferdy
            "https://drive.google.com/uc?export=view&id=1bRQbvR8cufq4Vp5G8ca2fWUEDDZOtbFg", #Bang Deri
            "https://drive.google.com/uc?export=view&id=1Jw8iHVZZFE8jSwSwo6VPjmGsxa2OP9Fs", #Kak Okta
            "https://drive.google.com/uc?export=view&id=1JvSlqpdoCZLdo-Rv6_5cUsoPkk9PGdUQ", #Bang Deyvan
            "https://drive.google.com/uc?export=view&id=1yFq1e-LLyekZJjnzozqzFdpdNqvxhJSd", #Bang Jo
            "https://drive.google.com/uc?export=view&id=1khS3iyBuzGjzaJsI4a896pIAFOYeeXpn", #Bang Kemas
            "https://drive.google.com/uc?export=view&id=1vIFt8veRCC63iHimW7nnic-JhjBxGbKS", #Kak Rafa
            "https://drive.google.com/uc?export=view&id=1XVfdTTay7hMC1ZxKlALPXssONttsB_aM", #Bang Sahid
            "https://drive.google.com/uc?export=view&id=1W0cGKbUMSXNLxXPaLcyfyCrI4dEVGnL0", #Bang Ateng
            "https://drive.google.com/uc?export=view&id=1hKSdVMxCnwgzgkj4Ka3kWjWS5aLQql5o", #Kak Jaclin
            "https://drive.google.com/uc?export=view&id=1XzaE0C4YpfRTbxzLYC6-wV3YG3qWLnhz", #Bang Rafly
            "https://drive.google.com/uc?export=view&id=1Kr117OrrnDhxUE4qNsBcay8q8CEIOdsx", #Kak Dini
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
                "kesan": "berwibawa dan lugas",  
                "pesan":"semangat kuliah dan semoga cepat lulus bang!!!"
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450123",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kos, Sukarame",
                "hobi": "Mencari keributan",
                "sosmed": "@elisabethh_",
                "kesan": "kakaknya lucuu",  
                "pesan":"semangat terus ya kak, semoga kuliahnya lancar!!!"
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "gak nyangka kakak ketuplaknya",  
                "pesan":"semangat terus kuliahnya kak, semoga sehat selalu"
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Baik dan informatif bangett",  
                "pesan":"semanagat kuliahnya ya kakk"
            },
            {
                "nama": "Eksanty Febriana Sukma Islamiaty",
                "nim": "122450001",
                "umur": "20",
                "asal":"Teluk Hantu",
                "alamat": "Kampung Baru, dekat UNILA",
                "hobi": "Shalat",
                "sosmed": "@eksantyfebriana",
                "kesan": "kakaknya terkenal sama kepintarannya",  
                "pesan":"semoga selalu dimudahkan kuliahnya ya kak"
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "kakaknya baik dan ternyata orang Padang",  
                "pesan":"Semangat terus kuliahnya kak, semoga nilai bagus semua"
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "baik abangnya dan informatif",  
                "pesan":"Semangat kuliahnya bang, tugas jangan kendor ya bang"
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "baik banget abangnya, lembut ngomongnya",  
                "pesan":"Semangat terus ya bang buat kuliah nya, jangan lupa tugasnya bang"
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Kakaknya baik dan anggun",  
                "pesan":"Semangat kuliahnya kak, sehat selalu ya kak"
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Abangnya humoris dan baik banget",  
                "pesan":"Semoga cepat lulus ya bang, semangat basketnya bang"
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "abangnya baik banget, asik dan informatif",  
                "pesan":"Semangat ngaspraknya bang, jaga kesehatannya ya bang"
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Style abangnya keren banget, suka vibesnya",  
                "pesan":"Sehat selalu bang, semangat kuliah dan ngaspraknya bang"
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakaknya pendiam tapi baik banget dan informatif",  
                "pesan":"Semangat kuliahnya kak, dan semangat buat tarinya kak"
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abangnya baik dan keren",  
                "pesan":"Semangat ngeband nya bang, semoga kuliahnya lancar ya bang"
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abangnya baik dan berwawasan banget",  
                "pesan":"Semangat kuliahnya bang dan semangat buat list lomba-lombanya bang"
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal":"Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kakaknya baik dan informatif banget",  
                "pesan":"Semangat kuliahnya kak, sehat selalu ya kak"
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal":"Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya baik banget dan infomratif juga",  
                "pesan":"Sehat selalu bang dan tetap semangat menjalankan tugasnya"
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakaknya kalem banget, sekilas kakaknya mirip kak okta",  
                "pesan":"Sehat selalu ya kak, semangat kuliahnya dan hari-harinya"
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=18AW-oVHCWFsH_kae1I1YP0j4Xh_qNWvn", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1pEFHv8m5qN27DK3OXism8KKDpBO4hn5V", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1NZkN5IRdQH0MS9S0wD651DEPFedGNXyQ", #Bg Ahmad Akbar ok
            "https://drive.google.com/uc?export=view&id=1QcJ6cUv3bGIe5ctRwWUKiHqAQqXaQ15R", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=1mwTCsNRr9BbB-fs1LrjgSmqC31BrEfTk", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1QqsgTYdKKidR6Rer2SGEZ7Tj4bhK8scj", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1qmPOj-xcuKBwnpBQkaQwJ0we3ruXVWlc", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1Cm08ABIBQwDOHFfCKs_fKfnOps9vwu9s", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1DYrxGG34fkkdLyBzQSqsUqfMab7i1f5e", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1WIg2xeppXK9G4PSMQ_vds9UJQTMFkCK_", #Bg Eggi 
            "https://drive.google.com/uc?export=view&id=1PitnG7fzxlFXSVLNUVba6l79KRyiEumE", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=14qm-w5bnviRzij8rFe1fOeucBmbPHD2z", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1Gb7i_QbVFog0LjsJYrqpshkbBz_wGzqc", #Bang Randa ok
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
                "kesan": "Abangnya baik banget dan informatif tentang perkuliahan juga",  
                "pesan":"Semangat bang kuliahnya dan semoga cepat lulus dengan nilai memuaskan"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kakaknya cantik dan baik banget",  
                "pesan":"Semangat kuliahnya kak dan sehat selalu ya kak"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abangnya baik dan informatif",  
                "pesan":"Semoga sukses selalu ya bang, semoga rajin terus olahraganya"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abangnya baik, pertama kali liat abangnyaa di fg pas jadi pdd",  
                "pesan":"Semangat bang kuliahnya, jangan keseringan main game ya bang"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Kakaknya baik dan suka vibesnya, ternyata kakaknya kembar sama kak andini orba",  
                "pesan":"Semangat kuliahnya kak, semoga kompak selalu dengan kak dini"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakaknya kalem banget yaa",  
                "pesan":"Semangat terus kak kuliahnya, lebih semangat ya kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakaknya baik dan lucu bangetttt",  
                "pesan":"Semangat kak untuk kuliahnya, sehat selalu ya kak dan semoga sukses"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakaknya pendiem tapi baik banget",  
                "pesan":"Semangat kak ngasprak, tetap jadi yang seperti sekarang ya kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakaknya baik dan keliatan kalem banget, cantik juga",  
                "pesan":"Semangat kak kuliahnya, semangat juga buat ngaspraknyaa"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Abang ini keliatan pinter ngoding, asik juga cara ngejelasinnya",  
                "pesan":"Semangat terus ngodingnya bang, semoga lancar terus kuliahnya"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakaknya baik banget, seru pas ngobrol bareng kakak ini",  
                "pesan":"Sukses selalu kak buat kuliahnya"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Main Game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abangnya keren cara ngomonnya, unik banget namanya",  
                "pesan":"Semoga selalu happy ya bang sesuai nama abang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abang ini asik banget dan sabar banget ngejelasinnya",  
                "pesan":"Semangat terus ngaspraknya, jangan bosen berbagi ilmu ya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=11OSa98FDG0OCjrbicRiJVF0wEHsIUEjS", #Bg Yogy ok
        "https://drive.google.com/uc?export=view&id=1CtlDTEYeqK7urtpXnbyhOeeY_3-fXdi1", #Kak Ramadhita ok
        "https://drive.google.com/uc?export=view&id=1M17aQ3q_Bd-2A6WMVmGVw5ZPdF-vYnag", #Kak Nazwa ok 
        "https://drive.google.com/uc?export=view&id=1XbFE4Jicp2EzEJxylgxAeLfGM-uj9YlA", #Bg Bastian ok
        "https://drive.google.com/uc?export=view&id=1va8JP1EqS10Xdjx06zP_F51W38o5YtRk", #Kak Dea ok
        "https://drive.google.com/uc?export=view&id=14M43mNyILc0t00bhV2DYWh0azwdfVRXh", #Kak Esteria ok
        "https://drive.google.com/uc?export=view&id=1uKxInMOgKoOa28O6nglGdORYPNEQ-G4p", #Kak Natasya ok
        "https://drive.google.com/uc?export=view&id=11VioWxKwOyet43MxOf0ODyxV6tDCj6nM", #Kak Novelia ok
        "https://drive.google.com/uc?export=view&id=1f-_GSR0OMuxysu557gfYCkuUR5Wb2Wyf", #Kak Ratu ok
        "https://drive.google.com/uc?export=view&id=1_di9Ol-n_wLa6IWLk7Bm3qiBAciL5M-a", #Bg Tobias ok
        "https://drive.google.com/uc?export=view&id=1xR6CV5BIo9lI4bOus5baTkCClZcnekSU", #Kak Yohana ok 
        "https://drive.google.com/uc?export=view&id=1ofu9CazkU9WGsBINVQKCsxlt1AvYBEyA", #Bg Rizki ok 
        "https://drive.google.com/uc?export=view&id=1hDL1rG0qQzvchBZ11POhKB6WwpubuZoy", #Bg Arafi ok
        "https://drive.google.com/uc?export=view&id=1l6YtDS0bhHulEny-wRpZk2ycxplrxViq", #Kak uyi ok
        "https://drive.google.com/uc?export=view&id=12L56rd1TcLNKwFgKeMk6DMlVASOTNt2i", #Kak Chalifia ok
        "https://drive.google.com/uc?export=view&id=1oHSUiELbhXhvsCulavXXZKtQ-wyMT7Ny", #Bang Irvan ok
        "https://drive.google.com/uc?export=view&id=1GdUsK-DVAeewOfRjnrln0NIIoir725AK", #Kak Izza ok 
        "https://drive.google.com/uc?export=view&id=1JUak5e05qTmxwW5gP9Dh_Yj88Bd7Wehh", #Kak Khaalishah ok
        "https://drive.google.com/uc?export=view&id=1Mjc_fT8DIHJ6-ul9lqV33_QGcF-9ftCQ", #Bang Raid ok
        "https://drive.google.com/uc?export=view&id=1GNx9ToNg4g6AQL--mWdvHt1zLM80lZHd", #Kak Tria ok
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
                "kesan": "Abangnya asik pembawannya, bercanda mulu tapi baik",  
                "pesan":"Semangat kuliahnya bang, semoga dimudahkan segala sesuatunya"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Kakaknya baik banget, asik pembawaannya",  
                "pesan":"Tetap semangat ngelajanin perkuliahannya ya kakkk"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakaknya cantik banget, kirain jutek taunya baik banget",  
                "pesan":"Semangat terus ya kak, sukses buat kuliah dan jangan lupa tugasnya"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "keren abangnya, tinggi banget abangnya, informatif juga omongannya",  
                "pesan":"Semangat kuliahnya bang, jangan sering-sering telat ya bang ngampusnya"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kakaknya asik banget diajak bercanda, baik banget dan informatif kata-katanya",  
                "pesan":"Semangat kuliahnya kak, semoga selalu baik ke semua orang ya kak"
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Kakaknya cantik dan lucu, tapi pendiem kakaknya",  
                "pesan":"Semangat terus kak, jangan terlalu sering nonton ya kakkk"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Kakaknya baik dan informatif bangettt, lucu jugaa",  
                "pesan":"Tetap semangat kak, semangat jadi cp hmsd ya kakk"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakaknya cantik dan lembut banget ngomongnya",  
                "pesan":"Tetap semangat kak, jangan terlalu sering tidur ya kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Kakaknya seru banget, pembawaannya asik banget",  
                "pesan":"Sehat selalu ya kak, banyakin minum air putih juga ya kak"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini bisa menyesuaikan diri, pembawaan nya jadi beda pas wawancara",  
                "pesan":"Tetap semangat menjalani segala kegiatan ya bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakaknya gak terlalu banyak ngomong tapi baik banget aslinya",  
                "pesan":"Sehat selalu kak, semangat belajarnya kak"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Abangnya baik banget, lembut juga cara ngomongnya",  
                "pesan": "Semangat terus bang, semangat juga bikin portofolionya bang"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abangnya kalem tapi suka bercanda juga",  
                "pesan": "Sehat selalu bang, jangan lupa masaknya yang sehat-sehat ya bang"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakaknya asik banget ngobrolnya, semangat banget ngomongnya",  
                "pesan": "Semangat kak buat proker-prokernya kak"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Kakaknya kalem dan lucu banget",  
                "pesan": "Sehat selalu ya kak, semangat ngereview jurnalnya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Abangnya asik banget dan suka bercanda tapi informatif",  
                "pesan": "Semangat terus bang kuliahnya dan semangat proker pengmasnya bang"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakaknya mengayomi sekali dan keliatan suka berinteraksi",  
                "pesan": "Semangat mengajarnya kak di semua kegiatan pengmas"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakaknya baik dan asik banget, cantikk",  
                "pesan": "Semoga tetap semangat ya kak untuk kedepannya"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Abangnya pendiem tapi baik banget",  
                "pesan": "Semangat buat ngaspraknya bang, semoga sukses dan sehat selalu"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Kakaknya baik, cantik dan ceria banget",  
                "pesan": "Semoga tetap ceria ya kakk"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
        "https://drive.google.com/uc?export=view&id=1UVmCSh2GXgDjsNj-Ym6iDJ0bBLaCB7Ks", 
        "https://drive.google.com/uc?export=view&id=1BpmO1UkJONRB61MEGJOgPPLMU78OXJw0", 
        "https://drive.google.com/uc?export=view&id=15yC6IpcL3vDR_IflFH8Vuh1luuZPGXCT",
        "https://drive.google.com/uc?export=view&id=18lesv-IeN4cM5-gXhPJ8BG-69IwL8nAY",
        "https://drive.google.com/uc?export=view&id=1RhLbRGCesoZnh9F8im1cwtViO9ZVLEFp", 
        "https://drive.google.com/uc?export=view&id=1asJUGwjECG48T1XGf9mkGpUw-aLtnWmx", 
        "https://drive.google.com/uc?export=view&id=1e_rOjLSnyRFKMn8R4Qc0yWtFOD0mssaF", 
        "https://drive.google.com/uc?export=view&id=10ncBf2HNN5YSVQ9QqQOagZZ8_oV6SBJ9", 
        "https://drive.google.com/uc?export=view&id=1S-1Z3LL1KtX6Ep7VF04RGFnK2YBlUNQ4", 
        "https://drive.google.com/uc?export=view&id=19LBkUYJdn_uRP_01ty0kkUzK7qTV6shK", 
        "https://drive.google.com/uc?export=view&id=1wEboMQTER3RmGnAjMIN9Psg6CiHb3KUQ", 
        "https://drive.google.com/uc?export=view&id=12xIwalpNTR6-iYEnc7gRXMdn2WIJ-mv9", 

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
                "kesan": "Abangnya berwibawa dan jelas banget kata-katanya",
                "pesan": "Semangat terus bang kuliahnya dan semangat terus sampai lulus ya bang"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Kakaknya cantik dan kalem banget, tapi semua pertanyan dijawab dengan baik",
                "pesan": "Semangat kak kuliahnya, semoga tetap suka membaca ya kak"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "12145006",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Ngoding",
                "sosmed": "@akbar_resdika",
                "kesan": "Abangnya keliatan kalem tapi ternyata asik ngobrolnya",
                "pesan": "Semangat buat riuh november nanti ya bang"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "Rajabasa",
                "hobi": "Denger musik",
                "sosmed": "@rannipu",
                "kesan": "Kakaknya ini baik banget, lembut juga omongannya walaupun keliatan tomboy",
                "pesan": "Semangat terus kak buat semua kegiatannya, sehat selalu dan tetap tersenyum ya kak"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobi": "Ngaji",
                "sosmed": "@rednraepr",
                "kesan": "Abang ini humoris banget, seru banget ngobrol sama abang ini",
                "pesan": "Tetap menjadi orang yang menyenangkan ya bang, jangan lupa ngaji juga bang"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Jl. Airan",
                "hobi": "Renang Tapi Gabisa Renang",
                "sosmed": "@slwfhn_694",
                "kesan": "Kakak ini keibuan banget pembawaannya",
                "pesan": "Semangat kak semoga bisa renang nantinya"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Abangnya vibesnya adem banget",
                "pesan": "Semoga konsisten olahraganya ya bang, semangat bang"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kakak ini kalem dan pendiem",
                "pesan": "Semangat berkebunnya kak"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "12145001",
                "umur": "21",
                "asal": "Pematang Siantar",
                "alamat": "Gya Kos",
                "hobi": "Nonton Film",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Abangnya kalem banget tapi seru obrolannya",
                "pesan": "Semangat terus bang kuliahnya, nontonnya di imbangi sama belajar juga ya bang"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@meiralsty_",
                "kesan": "Kakaknya ramah banget dan baik banget",
                "pesan": "Semangat kak buat riuh nanti dan semoga sehat selalu"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kos Benawang",
                "hobi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Abangnya lucu dan asik banget",
                "pesan": "Tetap tersenyum dan semangat kuliahnya bang"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "Kakaknya baik, lucu dan asik",
                "pesan": "Semangat menjalani harinya kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1S1W7bQrvlPhBcXEdQrkW020tOaZmUulR", #Bang Andrian
            "https://drive.google.com/uc?export=view&id=1SDBcjJLPFv2YYcolom7QJVM8M_XMA6BO", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1YqKNDBKloaQgFWhwOQWNiAZ0aywPlrRY",# Kak Nabila
            "https://drive.google.com/uc?export=view&id=1pNKE25H4CmoMXSP-x6g3zDZL9tlvNUAK",# Kak Nabilah
            "https://drive.google.com/uc?export=view&id=1QBA3c3UkIA-wLJzU_Z6xNhQuEdtKV1cy",# Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1GmyFatE8sofL4ODK-kAi9JdClJGEmncH",# Bang Danang
            "https://drive.google.com/uc?export=view&id=1Yi8U5cRD1Tz3rVKzx2Wm8JS6nxB1FEr0",# Bang Farrel
            "https://drive.google.com/uc?export=view&id=1NavgdUWNpMCui9SZlNZK-ggPqtsFkLLn",# Kak Tessa
            "https://drive.google.com/uc?export=view&id=13lgADEwyoYsOQHL9M4qBRG6KZh8A0q_O",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=1pb8zRtpYLqVCDFcobqdkIqWmZGvZTdSm",# Bang Dhafin
            "https://drive.google.com/uc?export=view&id=1OYQYAOaWl-CfbgB_pdtdDNPmSI0DZ0gy",# Kak Elia

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
                "kesan": "Keren abangnya ikut PMW",  
                "pesan": "Semangat kuliah bang, semoga cepet lulus"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kakaknya cantik banget",  
                "pesan": "Semoga cepat lulus dan semangat kuliahnya kak!"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kakaknya cantik dan lembut ngomongnya!",
                "pesan": "Semangat menghitung uangnya kak dan semangat juga kuliahnya kak!"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "Kakaknya baik dan keren!",
                "pesan": "Hobi kita sama kak suka tidur hihi, semangat kuliahnya kak"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Pertama kali liat abangnya keliatan banget orang Padang",
                "pesan": "Saya juga orang Padang loh bang, semangat kuliahnya ya bang!"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "Asik banget ngobrol abang ini",
                "pesan": "Semoga bisnisnya terus berlanjut ya bang, semoga cepet lulus bang!"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "Dari awal ketemu abangnya keren dan baik banget",
                "pesan": "Semoga sehat selalu dan lancar terus kuliahnya ya bang!"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tessa baik banget dan asik banget!",
                "pesan": "Semangat kuliah nya kak!"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kak Alvia cantik banget dan asik diajak bercanda",
                "pesan": "Sehat selalu ya kak dan semangat kuliahnya kak!"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Abangnya keliatan pendiem",
                "pesan": "Semangat kuliah nya bang semoga lancar selalu!!"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "lucu banget kakaknya dan baik banget",
                "pesan": "Semangat buat kuliahnya kak"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-F8OUOqHM2_dnOXSAqA4aB8AY96WkAd1", # bang wahyu
            "https://drive.google.com/uc?export=view&id=1QwiNQnaDyQCOB5qgNroSv0qeqD635Bz7", # kak arsyi
            "https://drive.google.com/uc?export=view&id=1c14OT1QnR1yPpLNzMRaLY5U9-6-NkEXD", # bang kai
            "https://drive.google.com/uc?export=view&id=17dYvuQe3CjtZ16oc-BTW8ZplboRNDXJ5", # bang arsal
            "https://drive.google.com/uc?export=view&id=1qUVY-yIeqPAcqonQo8rH2nZrYCubAxC2", # kak elok
            "https://drive.google.com/uc?export=view&id=1GhNd5k3paOjBfQDyYyqXtxNkae4iIRJw", # kak juju
            "https://drive.google.com/uc?export=view&id=1WhBGZnCdpeK7eO2l-6f5J1oTlRly7ei9", # kak nel
            "https://drive.google.com/uc?export=view&id=1xfFW03l-spJeVJMsmzPjAn0kdMjbHCMS", # kak try yani
            "https://drive.google.com/uc?export=view&id=1mbes2Glvzi5787RDGE6T74LzeWuFPrm1", # kak dwi
            "https://drive.google.com/uc?export=view&id=1OtISkiKFXqeo9IW4aAAIWufOqYwcSI05", # bang gym
            "https://drive.google.com/uc?export=view&id=1e2nGLwyg5414goApSs9iNC_8rBAEuFit", # kak nasywa
            "https://drive.google.com/uc?export=view&id=1mSOnzxBr-jTW8Be8TQqLQ8bF6BBqkctC", # kak priska
            "https://drive.google.com/uc?export=view&id=1WRDrRCOnUNIOp-AcbnImY_CHynbQHYFQ", # bang abit
            "https://drive.google.com/uc?export=view&id=1Fn6hp3yV6vdRz_K_Aw_al4rRdAcWgMEL", # bang hermawan
            "https://drive.google.com/uc?export=view&id=1ax8iNsF--rb8IpUSCzsWTZPoTeNZVSK9", # kak khusnun nisa
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
                "kesan": "Kaget pas abang bilang dari Makassar!",
                "pesan": "Semangat kuliahnya bang, semoga cepet lulus!"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Kak Arsyi cantik banget",
                "pesan": "Semangat ngontennya kak, lancar terus kuliahnya ya kak!"
            },
            {
                "nama": "Muhammad Kaisar Firdaus",
                "nim": "121450135",
                "umur": "21",
                "asal": "Pesawaran",
                "alamat": "Pulau Damar Way Kandis",
                "hobi": "Lagi Nyari",
                "sosmed": "@dino_lapet",
                "kesan": "Bang Kai baik banget!",
                "pesan": "Semangat terus kuliahnya ya bang"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "Abangnya lucu",
                "pesan": "Sehat dan semangat terus kuliahnya bang, info parfum yang tahan lama bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok cantik banget",
                "pesan": "Sehat selalu kak, semangat ngaspraknya kak!!!"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Kak juu baik, lucu, cantikkk kesayangan",
                "pesan": "Sehat selalu kak, semangat terus kuliahnya, tetep jadi kak juju yang baik ya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Neli baik dan lucu banget",
                "pesan": "Semangat terus kak kuliahnya, semangat juga ngontennya kakk!"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "Baik dan asik banget kakaknya",
                "pesan": "Semangat terus kuliahnya ya kak!!!"
            },
            {  
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "Scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "Aku kira kakak orangnya pendiem",
                "pesan": "Sehat selalu ya kak, semangat kuliahnya"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Abang the best deh pokoknya",
                "pesan": "Semangat kuliah dan kerjanya bang, sehat selalu ya bang Gymm"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "Seru banget kakaknya, kakak mirip ka izza pengmas sekilas",
                "pesan": "Semangat kuliahnya ya kak, semoga konsisten hobinya"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "Kakaknya lucuuu",
                "pesan": "Sehat selalu ya kak, semangat terus kak"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "Abang lucu dan asik",
                "pesan": "Sehat selalu dan semoga tetap produktif ya bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Seru banget abangnya",
                "pesan": "Semangat kuliahnya dan semoga tetap semangat"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kakaknya baik dan lucu banget tapi tegas",
                "pesan": "Semoga sehat selalu dan semangat kuliahnya kak"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan
