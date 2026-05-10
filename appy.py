import streamlit as st

st.set_page_config(
    page_title="Apron Monitoring System",
    page_icon="🛫",
    layout="wide"
)

st.title("🛫 Apron Monitoring System - Weda Bay Airport")
st.caption("Weda Bay Airport • PT. Indonesia WedaBay Industrial Park")

html_path = "apron/apron_system.html"

# Tombol Refresh
if st.button("🔄 Refresh / Load Ulang Halaman"):
    st.rerun()

try:
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.success("✅ File HTML berhasil dimuat")
    
    # Metode utama
    st.components.v1.html(
        html_content,
        height=1800,        # Tinggi lebih besar
        scrolling=True,
        width=None
    )

except Exception as e:
    st.error("Terjadi error saat memuat HTML")
    st.write(str(e))
    st.info("Coba refresh lagi atau hubungi saya untuk optimasi file.")
