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
    st.write("Masa pendudukan militer Jepang di wilayah Indonesia (1942–1945) secara drastis dimulai dengan serangan mendadak terhadap pangkalan militer Pearl Harbor di Pasifik. Peristiwa besar ini memicu jatuhnya kekuasaan kolonial Hindia Belanda secara total. Jepang datang dengan membawa propaganda manis sebagai "Saudara Tua", namun kenyataannya prioritas utama mereka hanyalah untuk memobilisasi penduduk demi memenangkan Perang Asia Pasifik. Untuk menyukseskan rencana tersebut, Jepang secara sengaja menggandeng tokoh-tokoh pergerakan nasional Indonesia yang berpengaruh agar dapat membangun kepercayaan rakyat. Mereka berharap rakyat mau menyerahkan tenaga, pikiran, serta sumber daya alam secara sukarela untuk membantu kepentingan militer Jepang.")
    st.write("2. Kloroplas: Organel untuk fotosintesis.")

elif menu == "Mulai Kuis":
    st.header("✍️ Kuis Interaktif")
    score = 0
    for i, q in enumerate(questions):
        ans = st.radio(f"Soal {i+1}: {q['soal']}", q['opsi'], key=f"q{i}")
        if ans == q['jawaban']:
            score += 1
    if st.button("Lihat Skor"):
        st.write(f"Skor kamu: {score}/{len(questions)}")
