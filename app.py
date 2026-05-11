import streamlit as st
# Fungsi sakti untuk menyambungkan CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Panggil file CSS-mu
local_css("style.css")

# --- KODE KAMU YANG LAIN DI BAWAH SINI ---
if 'kuis_mulai' not in st.session_state:
    st.session_state.kuis_mulai = False
if 'skor_akhir' not in st.session_state :
    st.session_state.skor_akhir = None

# Data Soal & Materi (Bisa kamu kembangkan nanti)
# Ini bagian soal sama jawaban
questions = [
    {
        "soal": "Langkah awal yang dilakukan oleh Jepang untuk menguasai Asia adalah?",
        "opsi": [
            "a. Merebut kekuasaan di Indonesia",
            "b. Menyerang pangkalan militer Amerika Serikat di Pearl Harbor",
            "c. Menyerang pusat militer di Amerika Serikat",
            "d. Menyatakan perang dengan negara-negara Sekutu",
            "e. Menguasai wilayah Hongkong"
        ],
        "jawaban": "b. Menyerang pangkalan militer Amerika Serikat di Pearl Harbor"
    },
    {
        "soal": "Pemerintah militer Jepang membentuk badan semimiliter dalam membantu kerja polisi Jepang yang disebut?",
        "opsi": [
            "a. Fujinkai",
            "b. Heiho",
            "c. PETA",
            "d. Keibodan",
            "e. Seinendan"
        ],
        "jawaban": "d. Keibodan"
    },
    {
        "soal": "Sidang pertama BPUPKI digelar pada tanggal?",
        "opsi": [
            "a. 29 Mei–7 Juni 1945", 
            "b. 29 Mei–10 Juli 1945",
            "c. 28 Mei–2 Juni 1945",
            "d. 29 Mei–1 Juni 1945",
            "e. 28 Mei–1 Juni 1945",
        ], 
        "jawaban": "d. 29 Mei–1 Juni 1945"
    },
    {
        "soal": "Pemerintah pendudukan Jepang menaruh perhatian besar dalam bidang sastra dengan mendirikan badan yang dinamakan?",
        "opsi": [
            "a. Jawa Shinbunkai",
            "b. Nederlands-Indische Radio Omroep Maatschappij",
            "c. Keimin Bunka Sidhoso",
            "d. Dokuritsu Junbi Cosakai",
            "e. Kokumin Gakko",
        ], 
        "jawaban": "c. Keimin Bunka Sidhoso"
    },
    {
        "soal": "Dampak pendudukan Jepang di Indonesia dalam bidang ekonomi adalah?",
        "opsi": [
             "a. Dikenalnya berbagai macam tanaman ekspor",
             "b. Membaiknya kesejahteraan petani",
             "c. Makin menurunnya produksi pertanian",
             "d. Meningkatkan produksi pertanian",
             "e. Awal kegiatan ekspor hasil bumi"
         ],
        "jawaban": "c. Makin menurunnya produksi pertanian"
    },
    {
        "soal": "Pembubaran Putera oleh Jepang disebabkan oleh?",
        "opsi": [
             "a. Putera lebih banyak memihak pada Barat",
             "b. Putera lebih banyak bermanfaat bagi bangsa Indonesia",
             "c. Putera banyak melibatkan orang-orang yang tidak jujur dan korup",
             "d. Soekarno mendapat dukungan rakyat untuk menjadi presiden",
             "e. Putera bekerja sama dengan para pejuang"
        ],
        "jawaban": "b. Putera lebih banyak bermanfaat bagi bangsa Indonesia"
    },
    {
        "soal": "Perlawanan terhadap Jepang terjadi di berbagai daerah. Pada tahun 1944, rakyat Indramayu melakukan perlawanan terhadap Jepang yang disebabkan oleh?",
        "opsi": [
            "a. Kewajiban menyetorkan hasil tananam padi kepada Jepang",
            "b. Kewajiban penduduk Indramayu untuk menjadi anggota PETA",
            "c. Pendirian barak-barak militer Jepang di Indramayu",
            "d. Kewajiban menanam kopi dan tebu bagi penduduk Indramayu",
            "e. Penutupan sekolah-sekolah di Indramayu oleh Jepang"
        ],
        "jawaban": "a. Kewajiban menyetorkan hasil tananam padi kepada Jepang"
    },
    {
        "soal": "Pemerintah Jepang ingin menggunakan tokoh-tokoh pergerakan nasional Indonesia dalam rangka?",
        "opsi": [
            "a. Menjalin kerja sama politik dengan bangsa Indonesia",
            "b. Membangun kepercayaan dari bangsa Indonesia",
            "c. Mempersiapkan kemerdekaan Indonesia",
            "d. Membangkitkan perasaan anti-Barat",
            "e. Memperbaiki kehidupan bangsa Indonesia"
        ],
        "jawaban": "b. Membangun kepercayaan dari bangsa Indonesia"
    }, 
    {
        "soal": "Sejak awal masa kekuasaan pemerintah kolonial Jepang, prioritas kebijakan terhadap orang Indonesia adalah?",
        "opsi": [
            "a. Membebaskan penduduk dari kemiskinan",
            "b. Menghapus pengaruh Barat pada penduduk bumiputra",
            "c. Memberantas pasar gelap",
            "d. Memobilisasi penduduk untuk kepentingan Jepang",
            "e. Menjadikan Indonesia sebagai bagian dari wilayah Asia Timur Raya"
        ],
        "jawaban": "d. Memobilisasi penduduk untuk kepentingan Jepang"
    },
    {
        "soal": "Alasan para pemimpin bangsa yang bersedia bekerja sama dengan pemerintah Jepang adalah?",
        "opsi": [
            "a. Mempelajari sistem pemerintahan negara Jepang",
            "b. Mendalami tujuan sebenarnya kedatangan Jepang ke Indonesia",
            "c. Mengembangkan kemampuan berpolitik para tokoh Indonesia",
            "d. Memimpin organisasi-organisasi bentukan Jepang",
            "e. Menyusun strategi dalam mencapai kemerdekaan"
        ],
        "jawaban": "e. Menyusun strategi dalam mencapai kemerdekaan"
    }, 
    {
        "soal": "Dalam bidang pemerintahan, akibat yang ditimbulkan dari pendudukan Jepang di Indonesia adalah?",
        "opsi": [
            "a. Wilayah Indonesia di bawah kekuasaan militer",
            "b. Kaisar memegang kendali utama di negeri jajahan",
            "c. Membagi wilayah Indonesia menjadi 68 karesidenan",
            "d. Diterapkannya sistem pemerintahan atas dasar fasisme",
            "e. Dihapuskannya negara boneka buatan Belanda"
        ],
        "jawaban": "a. Wilayah Indonesia di bawah kekuasaan militer"
    },
    {
        "soal": "Strategi perjuangan nonkooperatif gerakan bawah tanah yang dimaksud adalah?",
        "opsi": [
            "a. Bersifat radikal",
            "b. Kegiatan organisasi kebangsaan bersifat lunak dan terbuka",
            "c. Kegiatan organisasi dilakukan secara sembunyi-sembunyi",
            "d. Kegiatan organisasi dilakukan secara masif dan ekstrimis",
            "e. Organisasi dengan terang-terangan menggalang persatuan"
        ],
        "jawaban": "a. Bersifat radikal"
    },
    ]
st.title("🚀 Smart-Sprint AI")

menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Baca Materi", "Mulai Kuis"])

if menu == "Home":
    st.write("Selamat datang! Pilih menu di samping untuk mulai belajar.")
# ini bagian materi

elif menu == "Baca Materi":
    st.header("📖 Dinamika Pendudukan dan Strategi Perjuangan Masa Tirani Jepang")
    st.info("Ringkasan materi bab 1.")
    st.write("""Masa pendudukan militer Jepang di wilayah Indonesia (1942–1945) dimulai dengan serangan mendadak terhadap
    pangkalan militer Amerika Serikat di Pearl Harbor, Pasifik. Peristiwa besar ini memicu jatuhnya kekuasaan kolonial
    Hindia Belanda secara total. Jepang datang dengan membawa propaganda manis sebagai "Saudara Tua", namun kenyataannya
    prioritas utama mereka hanyalah untuk memobilisasi penduduk demi memenangkan Perang Asia Pasifik. Untuk menyukseskan 
    rencana tersebut, Jepang secara sengaja menggandeng tokoh-tokoh pergerakan nasional Indonesia yang berpengaruh agar 
    dapat membangun kepercayaan rakyat. Mereka berharap rakyat mau menyerahkan tenaga, pikiran, serta sumber daya alam 
    secara sukarela untuk membantu kepentingan militer Jepang.""")
    st.write("""Jepang merombak sistem pemerintahan menjadi pemerintahan militer dengan mendirikan berbagai organisasi
    semimiliter seperti Keibodan untuk membantu tugas polisi di desa-desa. Mereka juga membentuk Putera (Pusat Tenaga Rakyat) 
    sebagai wadah bagi para tokoh nasional untuk memimpin rakyat. Namun, pada akhirnya pihak Jepang memilih untuk membubarkan 
    Putera secara sepihak karena organisasi ini justru dianggap lebih bermanfaat bagi bangsa Indonesia dalam memupuk semangat
    nasionalisme daripada mengabdi pada kepentingan perang Jepang. Pendudukan Jepang mengakibatkan makin menurunnya produksi
    pertanian, tekanan ekonomi yang luar biasa berat, terutama kewajiban setor padi yang sangat mencekik petani, memicu 
    gelombang perlawanan rakyat, seperti yang terjadi di wilayah Indramayu.""")
    st.write("""Menjelang akhir kekuasaan mereka, Jepang mulai menjanjikan kemerdekaan dengan membentuk badan penyelidik atau
    BPUPKI. BPUPKI kemudian menyelenggarakan sidang pertama pada tanggal 29 Mei sampai 1 Juni 1945 dengan agenda utama
    merumuskan dasar negara bagi Indonesia merdeka. Dalam sidang tersebut, tokoh-tokoh besar seperti Soekarno menyampaikan
    pidato mengenai lahirnya Pancasila guna menyusun kerangka pemerintahan masa depan. Jepang mengizinkan proses politik ini 
    semata-mata untuk menjaga loyalitas serta simpati rakyat Indonesia di tengah posisi militer mereka yang semakin terdesak 
    oleh pasukan Sekutu di akhir Perang Dunia II.""")



elif menu == "Mulai Kuis":
    st.header("✍️ Kuis Interaktif")
    
    # Gunakan form agar aplikasi tidak re-run setiap kali satu soal dijawab
    with st.form("kuis_form"):
        jawaban_user = []
        for i, q in enumerate(questions):
            # Sekarang radio button ada di dalam container
                ans = st.radio(f"Soal {i+1}: {q['soal']}", q['opsi'], key=f"q{i}", index=None)
                jawaban_user.append(ans)
        
        # Tombol submit di dalam form
        submitted = st.form_submit_button("Lihat Skor")
        
        if submitted:
            # Cek apakah ada soal yang belum dijawab
            if None in jawaban_user:
                st.warning("Silahkan jawab semua soal terlebih dahulu!")
            else:
                current_score = 0
                for i, q in enumerate(questions):
                    if jawaban_user[i] == q['jawaban']:
                        current_score += 1
                
                # Simpan skor ke session state agar tetap muncul
                st.session_state.skor_akhir = current_score
                st.success(f"Kuis Selesai! Skor kamu: {current_score}/{len(questions)}")
