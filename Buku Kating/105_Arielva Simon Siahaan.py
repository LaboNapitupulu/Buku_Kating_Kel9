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
            "Depertemen MEDKRAF",
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
            "https://drive.google.com/uc?export=view&id=1OT8kifKMI_eAoHdNRsWJCctWZT2gO67Z",
            "https://drive.google.com/uc?export=view&id=15tpruKqGj8dTF4CF81rN98vsVeu1m0-B",
            "https://drive.google.com/uc?export=view&id=1qec4S_zjGE-Sg9Bmk5HzNs7jzDewUqPx",
            "https://drive.google.com/uc?export=view&id=1k6ax9DVVMVMsaS6eeRVqG5SSjK0cdEu7",
            "https://drive.google.com/uc?export=view&id=14pdn8bWUYVR6iZfnzdgZJvL_2JAJibZP",
            "https://drive.google.com/uc?export=view&id=1wbbAmCVk4WH7-tk8VB4MiT83XjSHUtFU"
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pulau Damar",
                "hobi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Bang Kharisma keren bisa seimbangin organisasi dan perkuliahan dengan dapet pengalaman magang di Telkom",  
                "pesan":"Semangat buat kesibukan di himpunan, perkuliahan, dan sukses buat karir mendatang bang" # 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Bawean 2, Sukarame",
                "hobi": "Main gitar",
                "sosmed": "@pndrinsni27",
                "kesan": "Awalnya saya kira bang Pandra angkatan 22, ternyata angkatan 21",  
                "pesan":"semangat TA dan ngasprak alpro RA bang"# 2
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam",
                "alamat": "Kota baru",
                "hobi": "Drakoran",
                "sosmed": "@wulandarimeliza",
                "kesan": "Saya kagum dengan cara kak Meliza berkomunikasi", 
                "pesan":"Semangat kuliah, TA, dan kesibukan di himpunan saat ini kak"# 3
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh",
                "alamat": "JL. Nangka IV",
                "hobi": "Dengarin Bang Pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Di wawancara yang terbatas, kakak ini kelihatan cukup asik",  
                "pesan":"Semangat kuliah, TA, kesibukan himpunan atau hal lain yang sedang dikerjain kak"# 4
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Di wawancara kemarin yang terbatas, kakak Hartiti cenderung agak diem",  
                "pesan":"Semangat buat perkuliahan kak, dan fokus lain yang mungkin lagi ditargetin"# 5
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota baru",
                "hobi": "Membaca",
                "sosmed": "@nadillaandr26",
                "kesan": "Di wawancara kemarin, kak Nadilla keliatan asik",  
                "pesan":"semangat kuliah, ngasprak ADS RA, kesibukan himpunan dan hal lainnya kak"# 6
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1HU9WM-8HyIrD--lG49zjXz5UOg9rdBVp",
            "https://drive.google.com/uc?export=view&id=1ti0XNBtosDbEZlJ9wp5WciZ-iMiccGiI",
            "https://drive.google.com/uc?export=view&id=136VRWd5vj50ftaN1Z9fnD4AQhVkTglML",
            "https://drive.google.com/uc?export=view&id=1oiqbRSbVX2mn_R1Ec2qdzsySHxSoM1CD",
            "https://drive.google.com/uc?export=view&id=1_0giXo-avcfcoNk_Loth38VhIuRBhPmy",
            "https://drive.google.com/uc?export=view&id=1opTZdOKnFmNrHO8UZ0qy9kX5vmzduy4Y",
            "https://drive.google.com/uc?export=view&id=1ly2cTlDDHQvWTgHxtpHVouIpQSfUD-FG",
            "https://drive.google.com/uc?export=view&id=1ucMU-YrgoN0U28CdwFBqck24_91J881l",
            "https://drive.google.com/uc?export=view&id=18qDViapEGwRT0lmkn_qBjdHhWLpIFL00",
            "https://drive.google.com/uc?export=view&id=1ElnzWKvEU7xsUpRli1wCLby_98FfkyyD",
            "https://drive.google.com/uc?export=view&id=16jKm038KCPfMaRvDAeQ_e9tIurjNI8QJ",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobi": "Searching di perplexity",
                "sosmed": "@trimurniaa_",
                "kesan": "kakak ini keren dan tegas sebagai asprak, cukup asik di wawancara",  
                "pesan":"semangat kuliah dan ngasprak Alpro RA kak, sukses buat hal yang ditargetin ke depan" #1
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Baca dan nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "di wawancara, kak Annisa cenderung agak diem",  
                "pesan":"semangat kuliahnya kak, TA, dan kesibukan lainnya"# 2
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@wlsbn0_",
                "kesan": "Kak Wulan keren dengan pengalaman dan skill komunikasinya, kagum dengan pengalaman MBKM-nya",  
                "pesan":"semangat kuliah dan karir mendatang kak, makasih buat sharing ilmu dan pengalamannya di wawancara kak"# 3
            },
            {
                "nama": "Anisa Dini Amalia",
                "nim": "121450081",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobi": "Nonton drakor",
                "sosmed": "@anisadini10",
                "kesan": "sama seperti kesan teman lain, kakak ini mirip salah satu peserta CoC",  
                "pesan":"Semangat kuliahnya kak, pengerjaan TA-nya juga semoga lancar"# 4
            },
            {
                "nama": "Claudhea Angeliani",
                "nim": "121450124",
                "umur": "21",
                "asal":"Salatiga",
                "alamat": "Lampung Timur",
                "hobi": "Baca jurnal",
                "sosmed": "@dylebee",
                "kesan": "Asal kak Claudhea cukup jauh juga, jarang liat temen yang asalnya sekitaran kakak ini",  
                "pesan":"Semangat tahun ke-4 kak, sukses buat perkuliahan dan kesibukan lainnya" #5
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "19",
                "asal":"Buleleng",
                "alamat": "Natar",
                "hobi": "Bercocok tanam",
                "sosmed": "@_.dheamelia",
                "kesan": "Di wawancara yang terbatas, kak Dea cenderung agak pendiem",  
                "pesan":"semangat kuliahnya kak, semnagat juga buat kesibukan lainnya"# 6
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "21",
                "asal":"Surakarta",
                "alamat": "Pahoman",
                "hobi": "Ngopi",
                "sosmed": "@fhrul.pdf",
                "kesan": "kayak pernah ketemu abang ini, tapi gatau dimana",  
                "pesan":"Semangat kuliah dan ngaspraknya bang, sukses buat hal yang mungkin lagi dikerjain"# 7
            },
            {
                "nama": "Feriyadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Sumatera Selatan",
                "alamat": "Depan Koban",
                "hobi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Di wawancara, bang Feri cenderung diam dan keliatan ramah",  
                "pesan":"semangat kuliahnya bang, atau mungkin kesibukan lainnya juga semangat bang"# 8
            },
            {
                "nama": "Mirza Yusuf Mirzani",
                "nim": "1224500118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobi": "Membaca",
                "sosmed": "@myrrinn",
                "kesan": "Abang ini keliatan cool di wawancara",  
                "pesan":"Sukses buat studi, kesibukan himpunan dan kesibukan lainnya bang"# 9
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Balam",
                "alamat": "Balam",
                "hobi": "Gangguin orang",
                "sosmed": "@jeremia_s_",
                "kesan": "Di tpb sering liat abang ini karena cukup aktif",  
                "pesan":"semangat kuliah dan ngaspraknya bang, sukses buat setiap hal yang dikerjain"# 10
            },
            {
                "nama": "Berliana Enda Putri",
                "nim": "122450065",
                "umur": "20",
                "asal":"BSD, Tangerang Selatan",
                "alamat": "Teluk",
                "hobi": "Suka liat linked in, puasa senin kamis, ngerjain tugas di draw io",
                "sosmed": "@berlyyanda",
                "kesan": "Sewaktu wawancara, kak Berliana juga keliatan cenderung pendiem",  
                "pesan":"semangat kuliah dan mungkin kesibukan lainnya kak"# 11
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B2v1o1X1DNwUYdR-b6OpBsSaNhdcXg92", 
            "https://drive.google.com/uc?export=view&id=142cMG-2weH0hBC-ZyA0pFvXSfnmOYaDq"
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
                "kesan": "Gaya komunikasi kak Annisa keren, kagum dan mencoba belajar dari kak Annissa",  
                "pesan": "Semangat kuliahnya kak, wawancara kemarin seru karena cerita kak Annisa buat wawancara kemarin menarik"
            },
            {
                "nama": "Rian Bintang Wijaya",
                "nim": "122450094",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kota Baru",
                "hobi": "Mendengarkan Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan": "Abang ini sangat tegas sewaktu wawancara dan rangkaian kaderisasi",  
                "pesan": "Semangat kuliah, organisasi, kepanitiaan, dan hal lain yang dikerjain bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-hsmE0Mfm74-YlFzG3Nbygi3fNhdz5w_", #1
            "https://drive.google.com/uc?export=view&id=1TjVfWjv1gF_7rSa4g_0e8yOEaP7Rb51Q", #2
            "https://drive.google.com/uc?export=view&id=1pJGyRdgr5SLU3s2uVf-mwZF_dN_siFJS", #3
            "https://drive.google.com/uc?export=view&id=1ERSZ65YIRoEozAV_naqO1bIb33IbPX_h", #10
            "https://drive.google.com/uc?export=view&id=1HgcpzC2ZSOgfQCgvCB-qZwUYXeq95TNE", #15
            "https://drive.google.com/uc?export=view&id=1EOyibI8wPGoSSz47Xj6AjLbyo_D8GgJ-", #4
            "https://drive.google.com/uc?export=view&id=1VtwkbMM6JJ24x31hnVcPgxCza1CSn4Zy", #6
            "https://drive.google.com/uc?export=view&id=1lHLASEPIiMoKvMEVmnW_DwHmxxnG6Qgs", #7
            "https://drive.google.com/uc?export=view&id=1to0KxMO7jYMLa7A7C1Ck93lWcn6QXoj3", #8
            "https://drive.google.com/uc?export=view&id=1nrCDX4tVdMAlNDNwEwrEL9lWfkYLiwpI", #9
            "https://drive.google.com/uc?export=view&id=16h2LeYvmU-I4PbafWzMTeYz4-lLkdni0", #11
            "https://drive.google.com/uc?export=view&id=1YfMKSsPHW8DeJ-s2VSHl2PZstvqn1Xvg", #12
            "https://drive.google.com/uc?export=view&id=1fM_dXme-vtgVCatRfXMx5jSjU07H2SOI", #13
            "https://drive.google.com/uc?export=view&id=154UeRbIQo7H6MnYt8WaoQv0c2Ti-uUry", #14
            "https://drive.google.com/uc?export=view&id=1WmDmyoNC3v5toufIq3Ijcpx7TrtH965F", #16
            "https://drive.google.com/uc?export=view&id=1fZN-ZPh41BetMWWKdMarXUIBqi6DJwyx", #17
            "https://drive.google.com/uc?export=view&id=17V8sN7qn4gAr_P30lGZwvdo9_B7xOA-n", #18
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
                "kesan": "Bang Ericson tegas dan berwibawa, keliatan sebagai koordinator yang keren",  
                "pesan": "Semangat kuliahnya bang, TA, dan kesibukan di himpunan" #1
            },
            {
                "nama": "Elisabeth Claudia Simanjuntak",
                "nim": "122450023",
                "umur": "20",
                "asal":"Tangerang",
                "alamat": "Owen Kos, Sukarame",
                "hobi": "",
                "sosmed": "@elisabethh_",
                "kesan": "Kakak ini tegas namun bisa juga santai menyesuaikan situasi",  
                "pesan": "Semangat kuliahnya kak, kesibukan kepanitiaan dan di himpunan juga semnagat kak" #2
            },
            {
                "nama": "Nisrina Nur Afifah",
                "nim": "122450052",
                "umur": "19",
                "asal":"Bekasi, Jawa Barat",
                "alamat": "Sukarame",
                "hobi": "Cubit Tangan Orang",
                "sosmed": "@afifahhnsrn",
                "kesan": "Kak Nisrina tegas dan berwibawa juga",  
                "pesan": "Semangat kuliah, dan membimbing angkatan 23 kak" #3
            },
            {
                "nama": "Deyvan Loxefal",
                "nim": "121450148",
                "umur": "21",
                "asal":"Riau",
                "alamat": "Kobam, Pulau Damar",
                "hobi": "Belajar",
                "sosmed": "@depanloo",
                "kesan": "Bang Deyvan asik dan seru, tapi tegas juga dalam forum formal seperti wawancara",  
                "pesan": "Semangat buat kuliahnya bang, ceria selalu juga bang" #10
            },
            {
                "nama": "M. Farhan Athaulloh",
                "nim": "121450117",
                "umur": "21",
                "asal":"Lampung",
                "alamat": "Kota Baru",
                "hobi": "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan": "Abang ini cukup santai dan menyenangkan di wawancara",  
                "pesan": "Semangat kuliahnya bang, semangat juga mewadahi minat dan bakat mahasiswa SD" #15
            },
            {
                "nama": "Allya Nurul Islami Pasha",
                "nim": "122450033",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Gang Perwira Belwis",
                "hobi": "Minum kopi",
                "sosmed": "@allyaislami_",
                "kesan": "Kak Allya juga sangat tegas",  
                "pesan": "Semangat kuliahnya dan mengkader kami kak" #4
            },
            {
                "nama": "Farahanum Afifah Ardiansyah",
                "nim": "122450056",
                "umur": "20",
                "asal":"Padang",
                "alamat": "Sukarame",
                "hobi": "Mukul",
                "sosmed": "@farahanumafifahh",
                "kesan": "Kakak ini cukup tegas dan berwibawa juga",  
                "pesan": "Semangat kuliahnya kak, semangat mengkader kami angkatan 23 juga kak" #6
            },
            {
                "nama": "Ferdy Kevin Naibaho",
                "nim": "122450107",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Senopati Raya",
                "hobi": "Dengerin Musik",
                "sosmed": "@ferdy_kevin",
                "kesan": "Abang ini cool dan berwibawa juga, tapi bisa santai juga",  
                "pesan": "Semangat kuliah dan mengkader angkatan 23 bang" #7
            },
            {
                "nama": "M. Deriansyah Okutra",
                "nim": "122450101",
                "umur": "19",
                "asal":"Kayu Agung",
                "alamat": "Jl. Pagar Alam Kedaton",
                "hobi": "Review Cheatsheet",
                "sosmed": "@dransyh_",
                "kesan": "Abang ini tegas namun santai menyesuaikan situasi",  
                "pesan": "Semangat kuliah juga dan mengkader kami bang" #8
            },
            {
                "nama": "Oktavia Nurwenda Puspita Sari",
                "nim": "122450041",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Way Hui",
                "hobi": "Ngeliatin Tingkah Orang",
                "sosmed": "@_oktavianrwnda_",
                "kesan": "Sewaktu wawancara, kak Oktavia cenderung pendiem juga",  
                "pesan": "Semangat kuliahnya kak, dan hal lain yang mungkin lagi dikerjain semangat kak" #9
            },
            {
                "nama": "Johannes Krisjon Silitonga",
                "nim": "122450043",
                "umur": "19",
                "asal":"Tangerang",
                "alamat": "Jl. Lapas",
                "hobi": "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan": "Abang ini tegas dan berwibawa, tapi santai dan asik juga menyesuaikan situasi",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan bang, semangat juga mengkader kami SD 23 bang" #11
            },
            {
                "nama": "Kemas Veriandra Ramadhan",
                "nim": "122450016",
                "umur": "19",
                "asal":"Bekasi",
                "alamat": "Lapangan Golf (Kojo)",
                "hobi": "Styling Skena (diusahakan)",
                "sosmed": "@kemasverii",
                "kesan": "Abang ini keren dan pengetahuan codingnya luas",  
                "pesan": "Semangat belajar dan menghadapi tiap errornya bang" #12
            },
            {
                "nama": "Rafa Aqilla Jungjunan",
                "nim": "122450142",
                "umur": "20",
                "asal":"Pekanbaru",
                "alamat": "Belwis",
                "hobi": "Baca Webtoon",
                "sosmed": "@rafaaqilla",
                "kesan": "Kakak ini cukup pendiam sewaktu wawancara",  
                "pesan": "Semangat kuliahnya juga kak, dilancarkan juga kesibukan lainnya" #13
            },
            {
                "nama": "Sahid Maulana",
                "nim": "122450109",
                "umur": "21",
                "asal":"Kota Depok",
                "alamat": "Airan Raya",
                "hobi": "Main Gitar",
                "sosmed": "@sahid_maul19",
                "kesan": "Abang ini cukup santai dan menyenangkan juga",  
                "pesan": "Semangat kuliahnya bang, semangat juga buat kesibukan di himpunan bang" #14
            },
            {
                "nama": "Jaclin Alcavella",
                "nim": "122450015",
                "umur": "19",
                "asal": "Sumatera Selatan",
                "alamat": "Korpri",
                "hobi": "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan": "Kak Jaclin juga cenderung pendiem sewaktu wawancara",  
                "pesan": "Semangat kuliahnya kak, kesibukan himpunan, dan hal lain yang mungkin lagi dikerjain" #16
            },
            {
                "nama": "Rafly Prabu Darmawan",
                "nim": "122450140",
                "umur": "20",
                "asal": "Bangka Belitung",
                "alamat": "Sukarame",
                "hobi": "Main Game",
                "sosmed": "@raflyy_pd",
                "kesan": "Abangnya cukup pendiam di wawancara dan di kelas juga",  
                "pesan": "Semangat kuliahnya bang, dilancarkan juga hal yang lagi dikerjain" #17
            },
            {
                "nama": "Syalaisha Andini Putriansyah",
                "nim": "122450111",
                "umur": "21",
                "asal": "Tangerang",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan": "Kakak ini di wawwancara keliatan agak pendiem, tapi keliatan aktif diluar wawancara",  
                "pesan": "Semangat kuliahnya kak, semangat juga buat kesibukan kepanitiaan, dan himpunan kak" #18
            },       
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mEThdYVaw_FT1pmBDvXw060KNbcSzELp", #Bg Rafi ok
            "https://drive.google.com/uc?export=view&id=1qI3hEUE2LqdqP1Yx_HFnU0lOZBi7ReO5", #Kak Anova ok
            "https://drive.google.com/uc?export=view&id=1txvidfJMMEz-tu8BRsIodQEo40lU4ajF", #Bg Sahid ok
            "https://drive.google.com/uc?export=view&id=1an8CPoXBSY9maQ-Yj2CFE1EPblv6iyzK", #Bg Fadhil ok
            "https://drive.google.com/uc?export=view&id=12pCBGWKFsMrOK1mjt52HR-9Ww47pqVai", #Kak Dina ok
            "https://drive.google.com/uc?export=view&id=1WJg9uVgL87OyzhkFOpWv4JUq86dOozSB", #Kak Dinda ok
            "https://drive.google.com/uc?export=view&id=1YjiPU-L7VoOe1Wj9Roksln9bdOrGZt0p", #Kak Eta ok
            "https://drive.google.com/uc?export=view&id=1irhEI3sOC4GjMJKqVpXD9BJR66Z7PRoX", #Kak Rut ok 
            "https://drive.google.com/uc?export=view&id=1QtInRqPXhJyvoB4zWUU0bqVIE_XobWBM", #Kak Puspa ok
            "https://drive.google.com/uc?export=view&id=1PjF78Oe0HhADIqbLH3m-ApoORB30ZHgh", #Bg Eggi _
            "https://drive.google.com/uc?export=view&id=1T9UPtFEkcqD2z2_lNYbNpn2OK0YfcvQD", #Kak Febiya _
            "https://drive.google.com/uc?export=view&id=1xBVs7cebA-mZl6ArBOXaTu4YGW85jNP5", #Bang Happy ok
            "https://drive.google.com/uc?export=view&id=1kzHLyqMJ2sQyLJocYkZAWj1mgR-Ek-gi", #Bang Randa ok
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
                "kesan": "Dengan magang di Mikfes, ngelihat kalau bang Rafi sebagai koordinator yang baik",  
                "pesan": "Semangat TA-nya dan sukses karir mendatang bang, semangat juga buat hal yang mungkin lagi dikerjain bang"
            },
            {
                "nama": "Annisa Novantika",
                "nim": "121450005",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Jl. Pulau Sebesi",
                "hobi": "Memasak",
                "sosmed": "@anovavona",
                "kesan": "Kak Annisa cukup pendiem di wawancara kmearin",  
                "pesan": "Semangat buat kuliahnya kak, TA-nya juga dilancarakn"
            },
            {
                "nama": "Ahmad Sahidin Akbar",
                "nim": "122450044",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Sukarame",
                "hobi": "Olahraga",
                "sosmed": "@sahid22__",
                "kesan": "Abang ini cukup pendiem, tapi santai dan cenderung asik juga",  
                "pesan": "Semangat kuliahnya bang, dan kesibukan di mikfesnya"
            },
            {
                "nama": "Fadhil Fitra Wijaya",
                "nim": "122450082",
                "umur": "20",
                "asal":"Bekasi",
                "alamat": "Teluk Betung",
                "hobi": "Main Game",
                "sosmed": "@fadhilfwee",
                "kesan": "Abang ini cukup cool juga sewaktu wawancara",  
                "pesan": "Semangat kuliahnya juga bang, dilancarkan hal yang lagi dikerjakan"
            },
            {
                "nama": "Syalaisha Andina Putriansyah",
                "nim": "122450121",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Gang Yudistira",
                "hobi": "Baca Jurnal",
                "sosmed": "@dkselsd_31",
                "kesan": "Di wawancara juga kak Syalaisha cenderung pendiem",  
                "pesan": "Semangat kuliahnya kak, kesibukan mikfes dan hal lain yang lagi dikerjain"
            },
            {
                "nama": "Dinda Nababan",
                "nim": "122450120",
                "umur": "20",
                "asal":"Medan",
                "alamat": "Jl. Lapas",
                "hobi": "Belajar",
                "sosmed": "@dindanababan_",
                "kesan": "Kakak ini cukup tegas di mikfes, cenderung ramah juga",  
                "pesan": "Semangat kuliahnya kak, kesibukan mikfes, dan kesibukan lainnya dilancarkan kak"
            },
            {
                "nama": "Marleta Cornelia Leander",
                "nim": "122450092",
                "umur": "20",
                "asal":"Depok",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan": "Kakak ini sangat baik di mikfes, koordinasinya sangat baik",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan kak, ramah selalu kak"
            },
            {
                "nama": "Rut Junita Sari Siburian",
                "nim": "122450103",
                "umur": "20",
                "asal":"Kep. Riau",
                "alamat": "Gang Nangka 3",
                "hobi": "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan": "Kakak ini asprak alpro RA, dan baik membimbing juga",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan kak, ramah selalu juga kak"
            },
            {
                "nama": "Syadza Puspadari Azhar",
                "nim": "122450072",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Belwis",
                "hobi": "Resume SG",
                "sosmed": "@puspadrr",
                "kesan": "Kakak ini juga asprak alpro RA, dan baik membimbing",  
                "pesan": "Semangat kuliahnya kak, ngasprak dan kesibukan lainnya juga semangat kak"
            },
            {
                "nama": "Eggi satria",
                "nim": "122450032",
                "umur": "20",
                "asal":"Sukabumi",
                "alamat": "Korpri Raya",
                "hobi": "Ngoding Wisata",
                "sosmed": "@_egistr",
                "kesan": "Kalau abang ini asprak strukdat RA, dan baik juga membimbing, abang ini keren",  
                "pesan": "Semangat kuliahnya dan juga semangat nguliknya bang"
            },
            {
                "nama": "Febiya Jomy Pratiwi",
                "nim": "122450074",
                "umur": "20",
                "asal":"Tulang Bawang",
                "alamat": "Jl. Kelengkeng Raya",
                "hobi": "Review Jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan": "Kakak ini cukup pendiem ketika wawancara",  
                "pesan": "Semangat kuliahnya kak, semangat jjuga kesibukan mikfes ataupun kesibukan lainnya kak"
            },
            {
                "nama": "Happy Syahrul Ramadhan",
                "nim": "122450013",
                "umur": "20",
                "asal":"Lampung Timur",
                "alamat": "Karang Anyar",
                "hobi": "Karang Anyar",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan": "Abang ini kalau ga salah web developer",  
                "pesan": "Semangat kuliah dan belajarnya bang, keren bang"
            },
            {
                "nama": "Randa Andriana Putra",
                "nim": "122450083",
                "umur": "21",
                "asal":"Banten",
                "alamat": "Sukarame",
                "hobi": "Tidur",
                "sosmed": "@randaandriana_",
                "kesan": "Abang ini koor magang mikfes dan baik membimbing juga, pengetahuan coding abang ini juga luas",  
                "pesan": "Semangat kuliah dan juga belajarnya bang, keren bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CaG3CanFqhgz9XbECqTYnPy-mk9ABVRO", #Bg Yogy
            "https://drive.google.com/uc?export=view&id=1Svfcib2B-eaL5IHR6rnYCy6fNHU04KVM", #Kak Ramadhita ok
            "https://drive.google.com/uc?export=view&id=1m48kBFfy25AA-t49VL9Lej2KVh-uwRHN", #Kak Nazwa ok 
            "https://drive.google.com/uc?export=view&id=1Z5NEheJD4i5qnBtqnrK7TiCRTFGZTSKM", #Bg Bastian ok
            "https://drive.google.com/uc?export=view&id=1lynUeFcI4A2EzqwFFv9brH_1dsWBs0pe", #Kak Dea
            "https://drive.google.com/uc?export=view&id=1liJDl7Kl71nN5vnrDBHsR0SeKSe_0P4u", #Kak Esteria ok
            "https://drive.google.com/uc?export=view&id=1lpVmuxwkJlLQS8ixQYo8MMOTjoW0i8A1", #Kak Natasya
            "https://drive.google.com/uc?export=view&id=1ldDwVb7hoAiaCghF_ELRImuYX_n76P8-", #Kak Novelia ok
            "https://drive.google.com/uc?export=view&id=1m30wP_uVkKM9K8KCTJchc-XrM8bn6u-w", #Kak Ratu ok
            "https://drive.google.com/uc?export=view&id=1lr-_xzc_Od78wCNo8LtVxpytdgRYLtVP", #Bg Tobias
            "https://drive.google.com/uc?export=view&id=1ljxy5XW9srF4iCcbKs6lyCgLIO8rbF9v", #Kak Yohana
            "https://drive.google.com/uc?export=view&id=1lzZqLMPxM1gzbaTrezzhrSAYRE5U1vQi", #Bg Rizki ok 
            "https://drive.google.com/uc?export=view&id=1JXcoTIIvjyuvijRk3njmuiPMtDnEEFGp", #Bg Arafi ok
            "https://drive.google.com/uc?export=view&id=1kk_xVyo6NZnpO5YhlJ-byFA_7iFzaKLF", #Kak Uyi 
            "https://drive.google.com/uc?export=view&id=1uTtkC0Lwwo76p1ODo6zIi9yMScgGuEYQ", #Kak Ocha
            "https://drive.google.com/uc?export=view&id=1VDNqwdm_X3TtnSl-WueTeb4W7JzVSJ1w", #Bang Irvan ok
            "https://drive.google.com/uc?export=view&id=1SgLba1oQWC9j-SDx-O4pQxgklVNhklX_", #Kak Izza ok 
            "https://drive.google.com/uc?export=view&id=1lcNHUkmRn7hI5t_uDfC_WFqgfYKepIKl", #Kak Khaalishah ok
            "https://drive.google.com/uc?export=view&id=1THxKIWP3Jbgr87SEbC8CycJja3tsu_08", #Bang Raid ok
            "https://drive.google.com/uc?export=view&id=1CsXaevBQQKFb1Hg3qI1NUfRhRrJYKGIU", #Kak Yuna
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
                "kesan": "Bang Yogy cenderung santai di wawancara",  
                "pesan": "Semangat kuliah, TA, dan mengkoordinir departemen eksternal bang"
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Raja Basa",
                "hobi": "Traveling",
                "sosmed": "@ramadhitatifa",
                "kesan": "Sama seeperti bang Yogy, kak Ramadhita juga cenderung santai di wawancara",  
                "pesan": "Semangat kuliah, TA, dan kesibukan di departemen Eksternal kak"
            },
            {
                "nama": "Nazwa Nabilla",
                "nim": "121450022",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kakak ini juga cukup pendiem di wawancara",  
                "pesan": "Semangat kuliahnya juga kak, dilancarkan hal lain yang mungkin lagi dikerjain"
            },
            {
                "nama": "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "",
                "sosmed": "@rzkdrnnn",
                "kesan": "Bang Rizki cenderung asik juga, membaur dekat juga sewaktu wawancara",
                "pesan": "Semangat kuliahnya juga bang, ramah selalu bang"
            },
            {
                "nama": "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21",
                "asal":"Batam",
                "alamat": "Belwis",
                "hobi": "Telat Ngampus",
                "sosmed": "@bastiansilaban_",
                "kesan": "Abang ini juga cukup pendiem di wawancara",  
                "pesan":"Semangat buat perkuliahan dan hal lain yang mungkin lagi dikerjain bang"
            },
            {
                "nama": "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20",
                "asal":"Sumatera Barat",
                "alamat": "Kos Korinda",
                "hobi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Sering lihat kakak ini, kak Dea cukup aktif",  
                "pesan":"Semangat buat perkuliahan dan kesibukan di kepanitiaan dan himpunan kak"
            },
            {
                "nama": "Estria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Sukabumi",
                "hobi": "Menonton Film",
                "sosmed": "@esteriars",
                "kesan": "Kakak ini diantara aktif dan pendiem",  
                "pesan":"Semangat kuliahnya kak, sukses buat setiap hal yang ditargetin"
            },
            {
                "nama": "Natasya Ega Lina Marbun",
                "nim": "122450024",
                "umur": "21",
                "asal":"Sumatera Utara",
                "alamat": "Jl. Manggis 2",
                "hobi": "Mendengarkan Lagu, Menyanyi",
                "sosmed": "@nateee__15",
                "kesan": "Sepeertinya kakak ini cukup aktif, sering lihat kakak ini",  
                "pesan":"Semangat kuliah dan hal lain yang dikerjakan kak, sukses dan keren selalu kak"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21",
                "asal":"Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kakak ini cukup pendiem juga di wawancara kemarin",  
                "pesan":"Semangat kuliahnya juga kak, ataupun hal lain yang dikerjakan semangat kak"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20",
                "asal":"Bogor",
                "alamat": "Way Kandis",
                "hobi": "Minum Es Teh",
                "sosmed": "@jasminednva",
                "kesan": "Kakak ini keren dengan pengalamannya",  
                "pesan":"Semangat kuliah dan hal lain yang dikerjkan kak, sukses selalu"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20",
                "asal":"Jakarta Selatan",
                "alamat": "Kelengkeng 14 (Pemda)",
                "hobi": "Baca Buku",
                "sosmed": "@tobiassiagian",
                "kesan": "Abang ini aktif, asprak ADS RA juga, tegas tapi santai juga menyesuaikan situasi",  
                "pesan":"Semangat kuliah dan hal lain yang dikerjakan bang, semangat menjadi ketuplak natal SD bang"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "20",
                "asal":"Sumatera Utara",
                "alamat": "Belwis",
                "hobi": "Belajar",
                "sosmed": "@yo_anamnk",
                "kesan": "Kakak ini diantara pendiem dan aktif pas wawancara, tapi di kader kak Yohana tegas",  
                "pesan":"Semangat kuliahnya kak, semangat juga membina kami di kader"
            },
             {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20",
                "asal": "Depok",
                "alamat": "Depan Warjo (TVRI)",
                "hobi": "Memasak",
                "sosmed": "@arafiramadhanmaulana",
                "kesan": "Abang ini juga cukup aktif di wawancara, ramah juga",  
                "pesan": "Semangat kuliahnya bang, dilancarkan hal lain yang mungkin lagi disibukkan"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20",
                "asal": "Muara Enim",
                "alamat": "Jl. Pembangunan Korpri",
                "hobi": "Cari Ice Breaking",
                "sosmed": "@u_yippy",
                "kesan": "Kakak ini sepertinya cukup aktif berkegiatan",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan kak, sukses selalu"
            },
             {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Senopati Raya",
                "hobi": "Mereview Jurnal",
                "sosmed": "@chlfawww",
                "kesan": "Kakak ini diantara aktif dan pendiem juga di wawancara",  
                "pesan": "sukses buat kuliah, kesibukan di himpunan dan hal lainnya kak"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21",
                "asal": "Padang Panjang",
                "alamat": "Sukarame",
                "hobi": "Nonton Youtube, Main Game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Seperti sering lihat abang ini, tapi ga tau dimana, abang ini cukup ceria juga",  
                "pesan": "Semangat kuliahnya juga bang, ceria selalu juga"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobi": "Mengabdi",
                "sosmed": "@izzalutfiaa",
                "kesan": "Kakak ini sepertinya sangat aktif di himpunan dan luar himpunan",  
                "pesan": "Semangat kuliah dan hal lain yang dikerjakan kak, sukses selalu"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Menyanyi",
                "sosmed": "@alyaavanefi",
                "kesan": "Kakak ini diantara aktif dan pendiem juga di wawancara",  
                "pesan": "Semangat kuliahnya juga kak, sukses buat hal yang sedang disibukkan"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "Membuat Jurnal",
                "sosmed": "@rayths_",
                "kesan": "Abang ini juga asprak ADS RA, dan baik membimbing juga",  
                "pesan": "Semangat ngasprak dan kuliahnya bang, sukses buat hal yang ditargetin bang"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20",
                "asal": "Way Kanan Lampung",
                "alamat": "Sukarame",
                "hobi": "Baca Artikel",
                "sosmed": "@tria_y062",
                "kesan": "Kakak ini juga diantara aktif dan pendiem di wawancara",  
                "pesan": "Semangat kuliahnya kak, ataupun kesibukan lainnya sukses kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RF95TCCGRAVaIYRECzNtc3f6U2S7dKDC", #BgDimas, belum
            "https://drive.google.com/uc?export=view&id=1ON1SkyDnYDY-2qMA322NIMGSF01JXTIP", #Kak Catherine, belum
            "https://drive.google.com/uc?export=view&id=1w1vI3aMr7a07NmIGct4aLwVJRaEweUyx", #Bg Akbar ok
            "https://drive.google.com/uc?export=view&id=1Jk2uxKwGi5v4jLFb9yaM8fF92W4NbyZG", #Kak Rani _
            "https://drive.google.com/uc?export=view&id=1diCWAW9QKt9ZNxoQ_yzgLv-5Q1DrZnTN", #Bg Rendra ok
            "https://drive.google.com/uc?export=view&id=19LfsWz24NVQGZ7xzeT52NhIdB9vUZ_3I", #Kak Salwa ok
            "https://drive.google.com/uc?export=view&id=1uLLZBNSLfGYtUwSszJWsFDSTRWAIDgnX", #Bg Ari ok 
            "https://drive.google.com/uc?export=view&id=1OLlXgbTrdJHyfohxgxwkYFeAK9ha8VBM", #Kak Azizah ok
            "https://drive.google.com/uc?export=view&id=1o6cMoUx6aOvmOB7woMHzH87GttQ2cI-Z", #Bg Josua ok
            "https://drive.google.com/uc?export=view&id=1kvHGOqr61Rs1zS3WBup9M0sbf8xBVRh8", #Kak Meira ok
            "https://drive.google.com/uc?export=view&id=1orzupIwtaTiM7EAVqhLfmqVgfTI_-Y-5", #Bg Rendi ok
            "https://drive.google.com/uc?export=view&id=1BvUpb1foX4o0vYYRolVgOvS5tbP17RJL", #kak Renta ok
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
                "kesan": "Bang Dimas sangat aktif, ceria dan baik",
                "pesan": "Semangat kuliah dan setiap hal lain yang direncanakan bang, sukses selalu bang"
            },
            {
                "nama": "Catherine Firdhasari Maulina Sinaga",
                "nim": "121450072",
                "umur": "20",
                "asal": "Medan",
                "alamat": "Airan",
                "hobi": "Baca Novel",
                "sosmed": "@catherine.sinagaa",
                "kesan": "Kakak ini cukup santai kelihatannya, dan baik juga",
                "pesan": "Semangat kuliahnya kak, dilancarkan setiap prosesnya"
            },
            {
                "nama": "M. Akbar Resdika",
                "nim": "12145006",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Dalam",
                "hobi": "Ngoding",
                "sosmed": "@akbar_resdika",
                "kesan": "Abang ini juga cukup santai di wawancara, ceria juga",
                "pesan": "Semangat perkuliahannya juga bang, dilancarkan juga hal lain yang lagi dikerjain"
            },
            {
                "nama": "Rani Puspita Sari",
                "nim": "122450030",
                "umur": "20",
                "asal": "Metro",
                "alamat": "",
                "hobi": "",
                "sosmed": "@",
                "kesan": "Kakak ini diantara aktif dan pendiem di wawancara",
                "pesan": "Semangat kuliahnya juga kak, semangat berorganisasi dan hal lainnya"
            },
            {
                "nama": "Rendra Eka Prayoga",
                "nim": "122450112",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Belwis",
                "hobi": "Ngaji",
                "sosmed": "@rednraepr",
                "kesan": "Abang ini keren dalam pembawaan komunikasinya",
                "pesan": "Semangat kuliahnya juga bang, semangat juga menjadi ketuplak riuh SD-2 bang"
            },
            {
                "nama": "Salwa Farhanatussaidah",
                "nim": "122450055",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Jl. Airan",
                "hobi": "Renang Tapi Gabisa Renang",
                "sosmed": "@",
                "kesan": "Kak Salwa juga cenderung pendiem di wawancara",
                "pesan": "Semangat buat perkuliahannya kak, semangat juga buat hal lain yang disibukkan kak"
            },
            {
                "nama": "Ari Sigit",
                "nim": "121450069",
                "umur": "23",
                "asal": "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobi": "Olahraga",
                "sosmed": "@ari.sigit17",
                "kesan": "Bang Ari juga santai pembawaannya di wawancara kemarin",
                "pesan": "Sukses buat perkuliahannya bang dan hal lainnya"
            },
            {
                "nama": "Azizah Kusumah Putri",
                "nim": "122450068",
                "umur": "21",
                "asal": "Lampung Selatan",
                "alamat": "Natar",
                "hobi": "Berkebun",
                "sosmed": "@azizahksmh15",
                "kesan": "Kak Azizah juga cenderuung pendiem di wawancara",
                "pesan": "Semangat kuliahnya juga kak, dilancarkan juga buat hal lain yang disibukkan"
            },
            {
                "nama": "Josua Panggabean",
                "nim": "12145001",
                "umur": "21",
                "asal": "Pematang Siantar",
                "alamat": "Gya Kos",
                "hobi": "Nonton Film",
                "sosmed": "@josuapanggabean16_",
                "kesan": "Bang Josua asprak yang baik dan ramah, di kelas begitupun di wawancara",
                "pesan": "Sukses buat perkuliahannya bang, dilancarkan setiap hal yang dikerjakan juga, semangat juga ngaspraknya bang"
            },
            {
                "nama": "Meira Listyaningrum",
                "nim": "122450011",
                "umur": "20",
                "asal": "Pesawaran",
                "alamat": "Airan",
                "hobi": "Membaca",
                "sosmed": "@meiralsty_",
                "kesan": "Kak Meira cenderung pendiem di wawancara, tapi tegas di kader",
                "pesan": "Semangat kuliahnya kak, dan kesibukan di himpunan juga semangat kak"
            },
            {
                "nama": "Rendi Alexander Hutagalung",
                "nim": "122450057",
                "umur": "20",
                "asal": "Tangerang",
                "alamat": "Kos Benawang",
                "hobi": "Nyanyi",
                "sosmed": "@rexanderr",
                "kesan": "Bang Rendi juga kelihatan baik dan ramah",
                "pesan": "Semangat selalu buat perkuliahannya bang, ramah selalu juga"
            },
            {
                "nama": "Renta Siahaan",
                "nim": "122450070",
                "umur": "21",
                "asal": "Sumatera Utara",
                "alamat": "Sukarame",
                "hobi": "Membaca",
                "sosmed": "@renta.shn",
                "kesan": "Kak Renta juga diantara aktif dan pendiem di wawancara",
                "pesan": "Kita satu marga kak, sukses selalu buat perkuliahannya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1iN3wLnDPtZ80b4BfbRvJQcYO0NG3xapl", #Bang Andrian
            "https://drive.google.com/uc?export=view&id=1zAzm-8RczutHCbJ4KxQocapjzxm22dAS", #Kak Adisty
            "https://drive.google.com/uc?export=view&id=1K8As1BQduZYiXldU_qY6mZIdq_zzHzcy",# Kak Nabila
            "https://drive.google.com/uc?export=view&id=1znMq6Y_5cvk0fE7GwoJtSU6Me0d9_7Qx",# Kak Nabilah
            "https://drive.google.com/uc?export=view&id=15a7GNgEPh_mMdUrGx16LhfXhYuYVtv2M",# Bang Ahmad
            "https://drive.google.com/uc?export=view&id=1zIIZJIwJbcfCj815rgUn97Oif-jwAUU1",# Bang Danang
            "https://drive.google.com/uc?export=view&id=1LJCI5-NbjsqoxpHzRtnaO3aDTVRafTdj",# Bang Farrel
            "https://drive.google.com/uc?export=view&id=1fFWNmtuACF3GLKiBFYZjTkt3q_QRwAJI",# Kak Tessa
            "https://drive.google.com/uc?export=view&id=1OOn2fwlormU3rPrAKhB_ObvaGB3ORVa4",# Kak Alvia
            "https://drive.google.com/uc?export=view&id=1SCEpC5fJq3P8hUKkw-fQhOV8XGO25KSW",# Kak Dhafin
            "https://drive.google.com/uc?export=view&id=1TC3ywgv7IZA9V0XeDSRmCs38A8gWWsie",# Kak Elia

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
                "kesan": "Kagum dengan cara bang Andrian berkomunikasi",  
                "pesan": "Semangat kuliahnya bang, keren selalu juga bang"
            },
            {
                "nama": "Adisty Syawaida Ariyanto",
                "nim": "121450136",
                "umur": "22",
                "asal":"Metro",
                "alamat": "Sukarame",
                "hobi": "Nonton film",
                "sosmed": "@adistysa_",
                "kesan": "Kak Adisty cukup aktif juga di wawancara",  
                "pesan": "Semangat buat kuliah dan kesibukkan di SSD kak"
            },
            {
                "nama": "Nabila Azhari",
                "nim": "121450029",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Menghitung uang",
                "sosmed": "@zhjung_",
                "kesan": "Kak Nabila cenderung agak pendiem juga di wwawancara",
                "pesan": "Semangat kuliahnya kak, dan hal lain yang diekrjakan juga semangat kak"
            },
            {
                "nama": "Nabilah Andika Fitriati",
                "nim": "121450139",
                "umur": "21",
                "asal": "Kedaton",
                "alamat": "Kedaton",
                "hobi": "Tidur",
                "sosmed": "@nabilahanftn",
                "kesan": "Kak Nabilah cenderung aktif juga di wawancara",
                "pesan": "SSemangat kuliahnya kak, dilancarkan juga hal yang disibukkan"
            },
            {
                "nama": "Ahmad Rizqi",
                "nim": "122450138",
                "umur": "20",
                "asal": "Padang",
                "alamat": "Airan",
                "hobi": "Jalan-jalan",
                "sosmed": "@ahmad.riz45",
                "kesan": "Bang  Ahmad cenderung pendiem tapi lebih ke santai",
                "pesan": "Semangat selalu bang, sukses buat setiap hal yang dikerjakan"
            },
            {
                "nama": "Danang Hilal Kurniawan",
                "nim": "121450085",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Airan",
                "hobi": "Berjualan",
                "sosmed": "@dananghk_",
                "kesan": "Bang Danang aktif banget diwawancara",
                "pesan": "Keren marketing stiker nya bang"
            },
            {
                "nama": "Farrel Julio Akbar",
                "nim": "122450110",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Samping Kedai Calon Sarjana",
                "hobi": "Bebas sih",
                "sosmed": "@farrel__julio",
                "kesan": "Bang Farrel cenderung cool dan tegas",
                "pesan": "Semangat ikut memimpin supporteran Damaskus bang"
            },
            {
                "nama": "Tessa Kania Sagala",
                "nim": "122459940",
                "umur": "20",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Nulis",
                "sosmed": "@tesakanias",
                "kesan": "Kak Tesa diantara pendiem dan aktif di wawancara, cenderung santai juga",
                "pesan": "Sukses selalu kak buat perkuliahan dan hal lainnya"
            },
            {
                "nama": "Alvia Asrinda Br.Gintng",
                "nim": "122450077",
                "umur": "20",
                "asal": "Binjai",
                "alamat": "Korpri",
                "hobi": "Nonton Windah",
                "sosmed": "@alviagnting",
                "kesan": "Kak Alfia cenderung pendiem di wawancara",
                "pesan": "Semangat selalu kak buat peerkuliahan dan hal lain yang dikerjain"
            },
            {
                "nama": "Dhafin Razaqa Luthfi",
                "nim": "122450133",
                "umur": "20",
                "asal": "Balam",
                "alamat": "Jl. Nangka 1",
                "hobi": "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan": "Bang Dhafin pendiem dan agak ramah juga",
                "pesan": "Semangat selalu buat kuliah dan hal lainnya bang"
            },
            {
                "nama": "Elia Meylani Simanjuntak",
                "nim": "122450026",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Korpri",
                "hobi": "Nyanyi",
                "sosmed": "@meylanielia",
                "kesan": "Kak Elia cukup aktif di wawancara",
                "pesan": "Sukses selalu perkuliahannya kak atapun hal lain yang disibukkan"
            },
       ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

else:
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OB-rMNrSYMsYO1PZzoAhdLdRV-TDMF06", # bang tao
            "https://drive.google.com/uc?export=view&id=1XwkfUv7bEeGA4--dqVOiTQPmis9h-3mr", # kak arsyi
            "https://drive.google.com/uc?export=view&id=1gWLuKmpYW6Ru4tqPpZsHNHy8szALtHs8", # bang arsal
            "https://drive.google.com/uc?export=view&id=1rExlZ0a-GL5SSSpkY6jw0WlkpriN81bc", # kak elok
            "https://drive.google.com/uc?export=view&id=1Q216IZ2qClxIKwk4wEBUOrtMyv-OE8Tn", # kak juju
            "https://drive.google.com/uc?export=view&id=1iv0F3SK_JKX4OgyZA_ka3dvm_5WxmWr1", # kak nel
            "https://drive.google.com/uc?export=view&id=1BC-QtmNPJ-ClTrwlntvk2BjZx3cBoQCc", # kak try yani
            "https://drive.google.com/uc?export=view&id=1vJOXybSa3l5v3k6zyq_h2gjgaDELwyIp", # kak dwi
            "https://drive.google.com/uc?export=view&id=1FeuQ_s9Gxmmr68Dgx_U6DajmeEPp106i", # bang gym
            "https://drive.google.com/uc?export=view&id=1ekYa4mTHS1yHi91-5BB-vdzyMcc0-Og3", # kak nasywa
            "https://drive.google.com/uc?export=view&id=1Afqlaw5B88BugN_RA_UQvVzsCRvw2WVO", # kak priska
            "https://drive.google.com/uc?export=view&id=1aGD6C5wNKeuyp2lbiNavhkQoFGn040R-", # bang abit
            "https://drive.google.com/uc?export=view&id=1t1_UAJ45LlAMxNzNuqdDAbZJ7UiBDWaK", # bang hermawan
            "https://drive.google.com/uc?export=view&id=13xCK4phEhK05QpHqiRouklFM3zO2HR13", # kak khusnun nisa
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
                "kesan": "Kagum dari Makassar ke ITERA Lampung bang",
                "pesan": "Sukses selalu bang, keren bisa muncul di feed IG official ITERA"
            },
            {
                "nama": "Arsyiah Azahra",
                "nim": "121450035",
                "umur": "21",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngonten",
                "sosmed": "@arsyiah._",
                "kesan": "Kak Arsyiah aktif di wawancara",
                "pesan": "Sukses selalu kak buat perkuliahan dan hal lainnya"
            },
            {
                "nama": "Muhammad Arsal Ranjana Utama",
                "nim": "121450111",
                "umur": "21",
                "asal": "Depok",
                "alamat": "Nangka III",
                "hobi": "Koleksi Parfum",
                "sosmed": "@arsyiah._",
                "kesan": "Bang Arsal asprak strukdat RA, agak pendiem",
                "pesan": "semangat ngaspraknya bang, terutama perkuliahannya juga semangat bang"
            },
            {
                "nama": "Elok Fiola",
                "nim": "122450051",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngedit",
                "sosmed": "@elokfiola",
                "kesan": "Kak Elok cenderung diem di wawancara, tapi as asprak strukdat baik membimbing",
                "pesan": "Sukses selalu buat perkuliahan dan ngasrpak atapun hal lainnya semangat kak"
            },
            {
                "nama": "Najla Juwairia",
                "nim": "122450037",
                "umur": "19",
                "asal": "Sumatera Utara",
                "alamat": "Airan",
                "hobi": "Baca, Nulis, fangirling",
                "sosmed": "@nanana.minjoo",
                "kesan": "Kak Najla daplok, baik dan ramah",
                "pesan": "Semangat emndampingi kelompok 9 di kaderisasi ya kak"
            },
            {
                "nama": "Rahma Neliyana",
                "nim": "122450036",
                "umur": "20",
                "asal": "Tanggamus",
                "alamat": "Sukarame, Pembangunan 5",
                "hobi": "Makan ubi cilembu",
                "sosmed": "@rahmanellyana",
                "kesan": "Kak Rahma sangat aktif dimanapun",
                "pesan": "Aktif selalu kak, ceria selalu juga, sukses buat kuliahnya juga kak"
            },
            {
                "nama": "Try Yani Rizki Nur Rohmah",
                "nim": "122450020",
                "umur": "20",
                "asal": "Lampung Barat",
                "alamat": "Korpri",
                "hobi": "Nonton",
                "sosmed": "@tryyaniciaaa",
                "kesan": "kak Try juga cenderung santai sewaktu wawancara",
                "pesan": "Semanagat dan sukses selalu kak terhadap apa yang dikerjakan"
            },
            {  
                "nama": "Dwi Ratna Anggraeni",
                "nim": "122450008",
                "umur": "20",
                "asal": "Jambi",
                "alamat": "Pemda",
                "hobi": "Scroll Tiktok",
                "sosmed": "@dwiratnn_",
                "kesan": "Kak Dwi cenderung agak diem sewaktu wawancara",
                "pesan": "Sukses selalu dan semanagt selalu buat setiap hal yang difokusin kak"
            },
            {
                "nama": "Gymnastiar Al Khoarizmy",
                "nim": "122450096",
                "umur": "20",
                "asal": "Serang",
                "alamat": "Lapangan Golf",
                "hobi": "Baca Komik",
                "sosmed": "@jimnn.as",
                "kesan": "Bang Gymnastiar daplok, baik membimbing",
                "pesan": "Semangat mendampingi kami kelompok 9 di kaderisasi bang"
            },
            {
                "nama": "Nasywa Nur Afifah",
                "nim": "122450125",
                "umur": "20",
                "asal": "Bekasi",
                "alamat": "Pemda",
                "hobi": "Bersih-bersih",
                "sosmed": "@nasywanaff",
                "kesan": "Kak Nasywa cendrung ceria",
                "pesan": "Semangat dan sukses selalu kak"
            },
            {
                "nama": "Priska Silvia Ferantiana",
                "nim": "122450053",
                "umur": "20",
                "asal": "Palembang",
                "alamat": "Jl Nangka II",
                "hobi": "Dengarin Musik",
                "sosmed": "@silvi.viii",
                "kesan": "Kak Priska agak pendiem",
                "pesan": "Semangat kuliah dan kesibukan di himpunan kak"
            },
            {
                "nama": "Abit Ahmad Oktarian",
                "nim": "122450042",
                "umur": "19",
                "asal": "Balam",
                "alamat": "Balam",
                "hobi": "Ngoding, Belajar, Ngaji, Desain, Baca Komik",
                "sosmed": "@abitahmad",
                "kesan": "Bang Abit ramah dan baik",
                "pesan": "Ramah dan baik selalu bang"
            },
            {
                "nama": "Hermawan Manurung",
                "nim": "122450069",
                "umur": "20",
                "asal": "Bogor",
                "alamat": "Jalan dekat tol",
                "hobi": "Baca buku, bengong",
                "sosmed": "@hermawan.mnrng",
                "kesan": "Bang Hermawan keren dan tegas",
                "pesan": "Semangat selalu bang buat kuliah dan hal lain yang ditargetin"
            },
            {
                "nama": "Khusnun Nisa",
                "nim": "122450078",
                "umur": "20",
                "asal": "Bakauhueni",
                "alamat": "Belwis",
                "hobi": "DIY pake printer",
                "sosmed": "@khusnun_nisa335",
                "kesan": "Kak Khusnun baik tapi tegas juga",
                "pesan": "Semangat selalu kak buat perkuliahannya dan hal lain yang ditargetin"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
