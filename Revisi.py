import streamlit as st
import pandas as pd
from datetime import datetime

# =============================
# Konfigurasi Halaman
# =============================
st.set_page_config(
    page_title="Rangkuman Revisi Proposal",
    layout="wide"
)

st.title("📑 Sistem Rangkuman Revisi Proposal")
st.write("Aplikasi untuk mencatat revisi proposal sebelum dan sesudah serta status ACC dosen")

# =============================
# Inisialisasi Data
# =============================
if "data_revisi" not in st.session_state:
    st.session_state.data_revisi = []

# =============================
# Form Input Revisi
# =============================
with st.form("form_revisi"):
    st.subheader("📝 Input Revisi Proposal")

    col1, col2 = st.columns(2)

    with col1:
        judul = st.text_input("Judul Proposal")
        mahasiswa = st.text_input("Nama Mahasiswa")
        dosen = st.text_input("Nama Dosen Pembimbing")

    with col2:
        status = st.selectbox(
            "Status Revisi",
            ["Belum ACC", "Revisi Lanjutan", "ACC"]
        )

    revisi_sebelum = st.text_area("✏️ Revisi Sebelum", height=150)
    revisi_sesudah = st.text_area("✅ Revisi Sesudah", height=150)

    submit = st.form_submit_button("💾 Simpan Revisi")

# =============================
# Simpan Data
# =============================
if submit:
    now = datetime.now()
    data = {
        "Judul Proposal": judul,
        "Nama Mahasiswa": mahasiswa,
        "Dosen Pembimbing": dosen,
        "Revisi Sebelum": revisi_sebelum,
        "Revisi Sesudah": revisi_sesudah,
        "Status": status,
        "Tanggal": now.strftime("%Y-%m-%d"),
        "Waktu": now.strftime("%H:%M:%S"),
        "Hari": now.strftime("%A")
    }
    st.session_state.data_revisi.append(data)
    st.success("✅ Revisi berhasil disimpan")

# =============================
# Tampilkan Data Revisi
# =============================
st.subheader("📊 Riwayat Revisi Proposal")

if st.session_state.data_revisi:
    df = pd.DataFrame(st.session_state.data_revisi)
    st.dataframe(df, use_container_width=True)

    # =============================
    # Export ke Excel
    # =============================
    def convert_excel(df):
        return df.to_excel(index=False, engine="openpyxl")

    st.download_button(
        import io

# =============================
# Export ke Excel (FIXED)
# =============================
output = io.BytesIO()
with pd.ExcelWriter(output, engine="openpyxl") as writer:
    df.to_excel(writer, index=False)

st.download_button(
    label="⬇️ Download Excel",
    data=output.getvalue(),
    file_name="rangkuman_revisi_proposal.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
else:
    st.info("Belum ada data revisi yang disimpan.")

