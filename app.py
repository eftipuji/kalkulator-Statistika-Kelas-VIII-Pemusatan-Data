import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean, median, multimode

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Detektif Statistika", layout="wide")

# --- CSS KUSTOM ---
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1A3C6E, #70AD47);
        color: white; padding: 1.5rem; border-radius: 15px;
        text-align: center; margin-bottom: 20px;
    }
    .fase-box {
        border-left: 5px solid #2E75B6; background: #F0F7FF;
        padding: 15px; border-radius: 0 10px 10px 0; margin: 10px 0;
    }
    .result-card {
        background: #1A3C6E; color: white; padding: 20px;
        border-radius: 15px; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>📊 Detektif Statistika</h1><p>Efti Puji Lestari — Matematika Universitas Pekalongan</p></div>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    menu = st.radio("Pilih Menu:", ["🏠 Beranda", "🔍 Mean", "⚖️ Median & Modus", "📈 Eksplorasi Data"])

# --- LOGIKA MENU ---
if menu == "🏠 Beranda":
    st.subheader("Selamat Datang!")
    st.write("Gunakan aplikasi ini untuk mempermudah belajar Statistika secara mandiri.")

elif menu == "🔍 Mean":
    st.markdown('<div class="fase-box"><b>Fase 1: Stimulasi</b><br>Berapa rata-rata dari data yang kamu miliki?</div>', unsafe_allow_html=True)
    txt_input = st.text_input("Input Data (pisahkan dengan koma):", "70, 80, 90")
    
    if txt_input:
        try:
            nums = [float(x.strip()) for x in txt_input.split(",") if x.strip()]
            if nums:
                res = mean(nums)
                st.markdown(f'<div class="result-card"><h3>Rata-rata (Mean)</h3><h1>{res:.2f}</h1></div>', unsafe_allow_html=True)
        except ValueError:
            st.error("Gunakan format angka dan koma saja!")

elif menu == "⚖️ Median & Modus":
    st.markdown('<div class="fase-box"><b>Fase 2: Identifikasi</b><br>Urutkan data untuk mencari nilai tengah!</div>', unsafe_allow_html=True)
    txt_input = st.text_input("Input Data:", "10, 20, 20, 30")
    
    if txt_input:
        try:
            nums = sorted([float(x.strip()) for x in txt_input.split(",") if x.strip()])
            if nums:
                med = median(nums)
                mod = multimode(nums)
                c1, c2 = st.columns(2)
                with c1: st.success(f"**Median:** {med}")
                with c2: st.info(f"**Modus:** {mod}")
        except Exception:
            st.error("Kesalahan format input.")

elif menu == "📈 Eksplorasi Data":
    st.markdown('<div class="fase-box"><b>Fase 3: Pengumpulan Data</b><br>Buat tabel frekuensimu sendiri!</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1: i_nilai = st.text_input("Daftar Nilai (koma):", "60, 70, 80")
    with col2: i_frek = st.text_input("Daftar Frekuensi (koma):", "2, 5, 3")

    if i_nilai and i_frek:
        try:
            val = [x.strip() for x in i_nilai.split(",") if x.strip()]
            frq = [int(x.strip()) for x in i_frek.split(",") if x.strip()]

            if len(val) == len(frq):
                df = pd.DataFrame({"Nilai": val, "Frekuensi": frq})
                st.table(df.T)
                
                fig, ax = plt.subplots()
                ax.bar(val, frq, color='#70AD47')
                ax.set_ylabel("Frekuensi")
                st.pyplot(fig)
            else:
                st.warning("Jumlah Nilai dan Frekuensi tidak sama!")
        except ValueError:
            st.error("Input harus berupa angka.")
