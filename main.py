import streamlit as st
import pandas as pd
import numpy as np
import  warnings



warnings.filterwarnings('ignore')

#streamlit ile sayfa bilgilerini düzenleme --> st.set_page_config
st.set_page_config(page_title="Customer Segmentation", page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: Customer Segmentation")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Sayfa başlığı ve açıklama
st.subheader("Feature Engineering Uygulaması")

# Dosya yükleme widget'ı tanımlama
file_uploader_key = st.file_uploader("Dosyayı Yükleyin", type=["csv", "txt", "xlsx", "xls"], key="uploader")

# Dosya yüklendiğinde işlemleri gerçekleştirme
if file_uploader_key is not None:
    # Dosya adını ve boyutunu kontrol etme
    filename = file_uploader_key.name
    file_size = len(file_uploader_key.getvalue())

    if file_size == 0:
        st.error("Yüklenen dosya boş. Lütfen geçerli bir dosya yükleyin.")
    else:
        # Debug bilgilerini yazdırma (isteğe bağlı)
        st.write(f"Yüklenen dosya adı: {filename}")
        st.write(f"Dosya boyutu: {file_size} byte")

        # Dosya türüne göre veri okuma işlemleri
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(file_uploader_key, encoding="ISO-8859-1")
            elif filename.endswith(('.xls', '.xlsx')):
                df = pd.read_excel(file_uploader_key)

        except Exception as e:
            st.error(f"Dosya okuma sırasında hata oluştu: {e}")
