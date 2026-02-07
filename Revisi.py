import streamlit as st
import pandas as pd
from datetime import datetime

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Sistem Revisi Proposal",
    layout="wide"
)

# =============================
# LOGIN GOOGLE (STREAMLIT CLOUD)
# =============================
user = st.experimental_user

if not user or not user.email:
    st.warning("🔐 Silakan login menggunakan akun Gmail terlebih dahulu.")
    st.stop()

# =============================
# INFO USER
# =============================
st.sidebar.title("👤 Akun Login")
st.sidebar.write(f"**Nama:** {user.name}")
st.sidebar.write(f"**Email:** {user.email}")

# =============================
# INISIALISASI DATA
# =============================
if "data_revisi" not in st.session_state:
    st.session_state.data_revisi = []

# =============================
# FILTER DATA PER USER
# =============================
data_user = [
    d for d in st.session_state.data_revisi
    if d["Email"] == user.email
]

# =============================
# DASHBOARD
# =============================
st.title("📑 Dashboard Revisi Proposal")
st.caption("Semua data tersimpan otomatis berdasarkan akun Gmail")

# =============================
# FORM INPUT REVISI
# =============================
with st.form("form_revisi"):
    st.subheader("📝 Input Revisi Proposal")

    col1, col2 = st.columns(2)

    with col1:
        judul = st.text_input("Judul Proposal")
        mahasiswa = st.text_input("Nama Mahasiswa")

    with col2:
        dosen = st.text_input("Nama Dosen Pembimbing")
        status = st.selectbox(
            "Status Revisi",
            ["Belum ACC", "Revisi Lanjutan", "ACC"]
        )

    revisi_sebelum = st.text_area("✏️ Revisi Sebelum", height=150)
    revisi_sesudah = st.text_area("✅ Revisi Sesudah", height=150)

    submit = st.form_submit_button("💾 Simpan Revisi")

# =============================
# SIMPAN DATA
# =============================
if submit:
    now = datetime.now()
    st.session_state.data_revisi.append({
        "Email": user.email,
        "Nama Akun": user.name,
        "Judul Proposal": judul,
        "Nama Mahasiswa": mahasiswa,
        "Dosen Pembimbing": dosen,
        "Revisi Sebelum": revisi_sebelum,
        "Revisi Sesudah": revisi_sesudah,
        "Status": status,
        "Tanggal": now.strftime("%Y-%m-%d"),
        "Waktu": now.strftime("%H:%M:%S"),
        "Hari": now.strftime("%A")
    })
    st.success("✅ Revisi berhasil disimpan")

# =============================
# TAMPILKAN RIWAYAT REVISI
# =============================
st.subheader("📊 Riwayat Revisi Saya")

if data_user:
    df = pd.DataFrame(data_user)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Belum ada revisi yang tersimpan untuk akun ini.")
