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
# CSS KUSTOM (Konsisten dengan gaya sebelumnya)
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
# SIDEBAR
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
    st.write("Hari ini kita akan mempelajari bagaimana cara meringkas sekumpulan data menjadi satu angka yang representatif menggunakan Mean, Median, dan Modus.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="info-card">
        <b>🎯 Tujuan Pembelajaran:</b><br>
        1. Menghitung Mean, Median, dan Modus data tunggal.<br>
        2. Menginterpretasi data dari tabel frekuensi.<br>
        3. Memilih ukuran pemusatan yang tepat sesuai konteks data.
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
        <div class="fase-text">Jika nilai ulanganmu adalah 70, 80, dan 90, berapa nilai rata-ratamu?</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ⌨️ Input Data")
    input_data = st.text_input("Masukkan data (pisahkan dengan koma):", "70, 80, 90")
    
    try:
        data = [float(x.strip()) for x in input_data.split(",")]
        rata_rata = mean(data)
        
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
        st.error("Format salah! Gunakan angka dan koma (contoh: 70, 85, 90)")

# ══════════════════════════════════════════
# KP 2 — MEDIAN & MODUS
# ══════════════════════════════════════════
elif tab_choice == "⚖️ KP 2 — Median & Modus":
    st.markdown("## ⚖️ Kegiatan 2: Median (Nilai Tengah) & Modus")
    
    input_data = st.text_input("Masukkan data untuk dianalisis:", "65, 70, 75, 75, 80")
    
    try:
        data = sorted([float(x.strip()) for x in input_data.split(",")])
        med = median(data)
        mod = multimode(data)
        
        st.write(f"**Data Terurut:** {', '.join(map(str, data))}")
        
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
            
    except Exception as e:
        st.warning("Silakan masukkan data yang valid.")

# ══════════════════════════════════════════
# EKSPLORASI DATA
# ══════════════════════════════════════════
elif tab_choice == "📈 Eksplorasi Data":
    st.markdown("## 📈 Visualisasi & Interpretasi Data")
    
    st.markdown("""
    <div class="fase-box" style="border-color:#70AD47; background:#F0FBF0;">
        <div class="fase-label" style="color:#70AD47;">③ Data Collection — Eksplorasi</div>
        <div class="fase-text">Mari kita lihat bagaimana distribusi data dalam bentuk diagram batang[cite: 1].</div>
    </div>
    """, unsafe_allow_html=True)

    # Contoh data tabel frekuensi dari RPP[cite: 1]
    df = pd.DataFrame({
        'Nilai': [60, 65, 70, 75, 80, 85, 90],
        'Frekuensi': [2, 3, 5, 8, 7, 4, 1]
    })
    
    st.write("### Tabel Frekuensi Nilai Ulangan")
    st.table(df.T)
    
    # Visualisasi
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df['Nilai'].astype(str), df['Frekuensi'], color='#2E75B6')
    ax.set_ylabel('Banyak Siswa')
    ax.set_xlabel('Nilai')
    ax.set_title('Diagram Batang Nilai Ulangan')
    st.pyplot(fig)
    
    with st.expander("🔍 Lihat Analisis Detektif"):
        st.markdown("""
        1. **Modus:** Nilai 75 (muncul 8 kali).
        2. **Mean:** 75.17 (rata-rata penguasaan materi cukup baik).
        3. **Interpretasi:** Sebagian besar siswa berada di level nilai 75-80[cite: 1].
        """)
