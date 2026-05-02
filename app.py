import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean, median, multimode

# ─────────────────────────────────────────
# KONFIGURASI HALAMAN
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Detektif Statistika",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────
# CSS KUSTOM
# ─────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

    .main-header {
        background: linear-gradient(135deg, #1A3C6E 0%, #2E75B6 60%, #70AD47 100%);
        color: white; padding: 1.5rem 2rem; border-radius: 16px;
        text-align: center; margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(26,60,110,0.3);
    }
    .fase-box {
        border-left: 5px solid #2E75B6; background: #EBF3FB;
        padding: 0.8rem 1rem; border-radius: 0 10px 10px 0;
        margin: 0.7rem 0;
    }
    .fase-label { font-weight: 800; color: #1A3C6E; font-size: 0.85rem; text-transform: uppercase; }
    .result-display {
        background: linear-gradient(135deg, #1A3C6E, #2E75B6);
        color: white; border-radius: 16px; padding: 1rem;
        text-align: center; font-weight: 800; margin: 0.5rem 0;
    }
    .info-card { background: #F0F7FF; border: 1px solid #BDD7EE; border-radius: 12px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# HEADER UTAMA
# ─────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>📊 Detektif Statistika</h1>
    <p>Kalkulator Ukuran Pemusatan Data • Discovery Learning • SMP Kelas VIII</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# SIDEBAR NAVIGATION
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown('<div style="background:#1A3C6E;color:white;padding:0.7rem;border-radius:10px;font-weight:800;text-align:center;">🧭 Menu Navigasi</div>', unsafe_allow_html=True)
    tab_choice = st.radio("Pilih Kegiatan:", ["🏠 Beranda", "🔍 KP 1 — Mean (Rata-rata)", "⚖️ KP 2 — Median & Modus", "📈 Eksplorasi Data"])
    st.markdown("---")
    st.markdown(f"""
    <div style="font-size:0.78rem;color:#7F7F7F;text-align:center;">
    🎓 Kurikulum Merdeka Fase D<br>
    Penulis: Efti Puji Lestari
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN BERANDA
# ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("## 👋 Selamat Datang, Detektif Data!")
    st.write("Mari meringkas data menjadi satu angka representatif dengan Mean, Median, dan Modus.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
        <b>🎯 Tujuan Pembelajaran:</b><br>
        1. Menghitung Mean, Median, dan Modus data tunggal.<br>
        2. Menginterpretasi data dari tabel frekuensi.<br>
        3. Memilih ukuran pemusatan yang tepat sesuai konteks data[cite: 1].
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.info("Gunakan navigasi di samping untuk mulai!")

# ══════════════════════════════════════════
# KP 1 — MEAN
# ══════════════════════════════════════════
elif tab_choice == "🔍 KP 1 — Mean (Rata-rata)":
    st.markdown("## 🔍 Kegiatan 1: Konsep Mean (Rata-rata)")
    st.markdown('<div class="fase-box"><div class="fase-label">① Stimulation</div>Jika nilaimu 70, 80, dan 90, berapa rata-ratanya?[cite: 1]</div>', unsafe_allow_html=True)

    input_data = st.text_input("Masukkan data (pisahkan dengan koma):", "70, 80, 90")
    
    if input_data:
        try:
            # Membersihkan spasi dan mengabaikan koma di akhir kalimat
            clean_input = input_data.strip().strip(",")
            data = [float(x.strip()) for x in clean_input.split(",") if x.strip() != ""][cite: 1]
            
            if data:
                rata_rata = mean(data)[cite: 1]
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f'<div class="result-display"><div style="font-size:0.8rem;">Mean (x̄)</div><div style="font-size:2.5rem;">{rata_rata:.2f}</div></div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="info-card"><b>Proses:</b><br>({ " + ".join(map(str, data)) }) / {len(data)} = {rata_rata:.2f}</div>', unsafe_allow_html=True)
        except ValueError:
            st.error("⚠️ Gunakan format angka yang benar (contoh: 70, 85, 90)[cite: 1]")

# ══════════════════════════════════════════
# KP 2 — MEDIAN & MODUS
# ══════════════════════════════════════════
elif tab_choice == "⚖️ KP 2 — Median & Modus":
    st.markdown("## ⚖️ Kegiatan 2: Median & Modus")
    input_data = st.text_input("Masukkan data:", "65, 70, 75, 75, 80")
    
    if input_data:
        try:
            clean_input = input_data.strip().strip(",")
            data = sorted([float(x.strip()) for x in clean_input.split(",") if x.strip() != ""])[cite: 1]
            
            if data:
                med = median(data)[cite: 1]
                mod = multimode(data)[cite: 1]
                st.write(f"**Data Terurut:** {', '.join(map(str, data))}")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f'<div class="result-display"><div style="font-size:0.8rem;">Median</div><div style="font-size:2.2rem;">{med}</div></div>', unsafe_allow_html=True)
                with c2:
                    st.markdown(f'<div class="result-display" style="background:linear-gradient(135deg, #70AD47, #2E75B6);"><div style="font-size:0.8rem;">Modus</div><div style="font-size:2.2rem;">{", ".join(map(str, mod))}</div></div>', unsafe_allow_html=True)
        except Exception:
            st.error("⚠️ Input tidak valid[cite: 1]")

# ══════════════════════════════════════════
# EKSPLORASI DATA
# ══════════════════════════════════════════
elif tab_choice == "📈 Eksplorasi Data":
    st.markdown("## 📈 Visualisasi & Interpretasi Data")
    st.markdown('<div class="fase-box" style="border-color:#70AD47; background:#F0FBF0;"><div class="fase-label" style="color:#70AD47;">③ Data Collection</div>Masukkan nilai dan frekuensi![cite: 1]</div>', unsafe_allow_html=True)

    col_input1, col_input2 = st.columns(2)
    with col_input1:
        input_nilai = st.text_input("Daftar Nilai (pisah koma):", "60, 70, 80, 90")
    with col_input2:
        input_frek = st.text_input("Frekuensi (pisah koma):", "2, 5, 8, 3")

    if input_nilai and input_frek:
        try:
            list_nilai = [float(x.strip()) for x in input_nilai.strip().strip(",").split(",") if x.strip() != ""][cite: 1]
            list_frek = [int(x.strip()) for x in input_frek.strip().strip(",").split(",") if x.strip() != ""][cite: 1]

            if len(list_nilai) == len(list_frek):
                df_input = pd.DataFrame({'Nilai': list_nilai, 'Frekuensi': list_frek})[cite: 1]
                st.write("#### 📋 Tabel Frekuensi")
                st.table(df_input.T)[cite: 1]
                
                # Visualisasi
                fig, ax = plt.subplots(figsize=(8, 4))
                ax.bar(df_input['Nilai'].astype(str), df_input['Frekuensi'], color='#70AD47')[cite: 1]
                ax.set_ylabel('Frekuensi')
                ax.set_xlabel('Nilai')
                st.pyplot(fig)[cite: 1]
                
                st.success(f"✅ Total data (n) = {sum(list_frek)} siswa[cite: 1]")
            else:
                st.warning("⚠️ Jumlah Nilai dan Frekuensi harus sama![cite: 1]")
        except ValueError:
            st.error("⚠️ Masukkan angka saja yang dipisahkan koma[cite: 1]")
