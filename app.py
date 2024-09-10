import streamlit as st

#metin öğeleri
import streamlit as st

st.title("Proje Başlığı")  # Başlık burada yazılacak
st.header("Ana Başlık")  # Ana başlık burada yazılacak
st.subheader("Alt Başlık")  # Alt başlık burada yazılacak
st.text("Bu bölümde düz metin bilgileri paylaşabilirsiniz.")  # Düz metin burada yazılacak
st.markdown("""
### Markdown Başlığı
Markdown formatında metin yazabilirsiniz. 
- Madde 1
- Madde 2

**Kalın metin** ve *eğik metin* kullanabilirsiniz.
""")  # Markdown içeriği burada yazılacak



# Kullanıcıdan metin girdisi alma --> input 
user_input = st.text_area("Lütfen özetlemek istediğiniz metni buraya yapıştırın:")






