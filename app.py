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
# CSS KUSTOM (Gaya Visual Efti Puji Lestari)
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
    Penulis: Efti Puji Lestari[cite: 1]
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════
# HALAMAN BERANDA
# ══════════════════════════════════════════
if tab_choice == "🏠 Beranda":
    st.markdown("## 👋 Selamat Datang, Detektif Data!")
    st.write("Hari ini kita akan mempelajari bagaimana cara meringkas sekumpulan data menjadi satu angka yang representatif menggunakan Mean, Median, dan Modus[cite: 1].")
    
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
        st.info("Gunakan navigasi di samping untuk mulai bereksplorasi!")

# ══════════════════════════════════════════
# KP 1 — MEAN
# ══════════════════════════════════════════
elif tab_choice == "🔍 KP 1 — Mean (Rata-rata)":
    st.markdown("## 🔍 Kegiatan 1: Konsep Mean (Rata-rata)")
    
    st.markdown("""
    <div class="fase-box">
        <div class="fase-label">① Stimulation — Pemantik</div>
        <div class="fase-text">Jika nilai ulanganmu adalah 70, 80, dan 90, berapa nilai rata-ratamu?[cite: 1]</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⌨️ Input Data")
    input_data = st.text_input("Masukkan data (pisahkan dengan koma):", "70, 80, 90")[cite: 1]
    
    try:
        data = [float(x.strip()) for x in input_data.split(",")][cite: 1]
        rata_rata = mean(data)[cite: 1]
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"""
            <div class="result-display">
                <div style="font-size:0.8rem; opacity:0.9;">Hasil Mean (x̄)</div>
                <div style="font-size:2.5rem;">{rata_rata:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="info-card">
            <b>Rumus:</b><br>
            x̄ = Σx / n[cite: 1]<br><br>
            <b>Proses:</b><br>
            ({ ' + '.join(map(str, data)) }) / {len(data)} = {rata_rata:.2f}
            </div>
            """, unsafe_allow_html=True)
            
    except ValueError:
        st.error("Format salah! Gunakan angka dan koma (contoh: 70, 85, 90)")[cite: 1]

# ══════════════════════════════════════════
# KP 2 — MEDIAN & MODUS
# ══════════════════════════════════════════
elif tab_choice == "⚖️ KP 2 — Median & Modus":
    st.markdown("## ⚖️ Kegiatan 2: Median (Nilai Tengah) & Modus")
    
    input_data = st.text_input("Masukkan data untuk dianalisis:", "65, 70, 75, 75, 80")[cite: 1]
    
    try:
        data = sorted([float(x.strip()) for x in input_data.split(",")])[cite: 1]
        med = median(data)[cite: 1]
        mod = multimode(data)[cite: 1]
        
        st.write(f"**Data Terurut:** {', '.join(map(str, data))}")[cite: 1]
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""<div class="result-display">
                <div style="font-size:0.8rem;">Median</div>
                <div style="font-size:2.2rem;">{med}</div>
            </div>""", unsafe_allow_html=True)
            st.caption("Median adalah nilai tengah setelah data diurutkan[cite: 1].")
            
        with c2:
            st.markdown(f"""<div class="result-display" style="background:linear-gradient(135deg, #70AD47, #2E75B6);">
                <div style="font-size:0.8rem;">Modus</div>
                <div style="font-size:2.2rem;">{', '.join(map(str, mod))}</div>
            </div>""", unsafe_allow_html=True)
            st.caption("Modus adalah nilai yang paling sering muncul[cite: 1].")
            
    except Exception:
        st.warning("Silakan masukkan data yang valid.")[cite: 1]

# ══════════════════════════════════════════
# EKSPLORASI DATA (DINAMIS)
# ══════════════════════════════════════════
elif tab_choice == "📈 Eksplorasi Data":
    st.markdown("## 📈 Visualisasi & Interpretasi Data")
    
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47; background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi</div>
        <div class="fase-text">Mari kita kumpulkan data! Masukkan daftar nilai dan frekuensinya untuk melihat distribusi data dalam bentuk diagram batang[cite: 1].</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("### 📝 Input Tabel Frekuensi")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        input_nilai = st.text_input("Masukkan Daftar Nilai (pisah dengan koma):", "60, 70, 80, 90")[cite: 1]
    with col_input2:
        input_frek = st.text_input("Masukkan Frekuensi (pisah dengan koma):", "2, 5, 8, 3")[cite: 1]

    try:
        list_nilai = [float(x.strip()) for x in input_nilai.split(",")][cite: 1]
        list_frek = [int(x.strip()) for x in input_frek.split(",")][cite: 1]

        if len(list_nilai) == len(list_frek):
            df_input = pd.DataFrame({
                'Nilai': list_nilai,
                'Frekuensi': list_frek
            })[cite: 1]
            
            st.write("#### 📋 Tabel Frekuensi Hasil Input")
            st.table(df_input.T)[cite: 1]
            
            st.write("#### 📊 Visualisasi Data")
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.bar(df_input['Nilai'].astype(str), df_input['Frekuensi'], color='#70AD47')[cite: 1]
            ax.set_ylabel('Banyak Siswa (Frekuensi)')[cite: 1]
            ax.set_xlabel('Nilai')[cite: 1]
            ax.set_title('Diagram Batang Data Siswa')[cite: 1]
            st.pyplot(fig)[cite: 1]

            total_siswa = sum(list_frek)[cite: 1]
            st.success(f"✅ Data berhasil diproses! Total data (n) = {total_siswa} siswa.")[cite: 1]
            
        else:
            st.error("⚠️ Jumlah 'Nilai' dan 'Frekuensi' harus sama! Contoh: Jika ada 4 nilai, maka harus ada 4 frekuensi juga.")[cite: 1]
            
    except ValueError:
        st.warning("⚠️ Pastikan input hanya berupa angka yang dipisahkan dengan koma.")[cite: 1]

    with st.expander("🔍 Petunjuk Detektif"):
        st.markdown("""
        *   **Langkah 1:** Masukkan urutan nilai pada kolom kiri[cite: 1].
        *   **Langkah 2:** Masukkan berapa orang yang mendapat nilai tersebut pada kolom kanan[cite: 1].
        *   **Langkah 3:** Amati bagaimana bentuk diagram batang berubah setiap kali kamu mengganti angka![cite: 1]
        """)
