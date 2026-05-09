import streamlit as st

# Data Soal & Materi (Bisa kamu kembangkan nanti)
questions = [
    {"soal": "Apa fungsi utama mitokondria?", "opsi": ["Sintesis protein", "Penghasil energi", "Penyimpan air"], "jawaban": "Penghasil energi"},
    {"soal": "Tempat fotosintesis pada tumbuhan adalah?", "opsi": ["Kloroplas", "Ribosom", "Vakuola"], "jawaban": "Kloroplas"}
]

st.title("🚀 Smart-Sprint AI")

menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Baca Materi", "Mulai Kuis"])

if menu == "Home":
    st.write("Selamat datang! Pilih menu di samping untuk mulai belajar.")

elif menu == "Baca Materi":
    st.header("📖 Dinamika Pendudukan dan Strategi Perjuangan Masa Tirani Jepang")
    st.info("Ringkasan materi berdasarkan soal kuis.")
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
    score = 0
    for i, q in enumerate(questions):
        ans = st.radio(f"Soal {i+1}: {q['soal']}", q['opsi'], key=f"q{i}")
        if ans == q['jawaban']:
            score += 1
    if st.button("Lihat Skor"):
        st.write(f"Skor kamu: {score}/{len(questions)}")
