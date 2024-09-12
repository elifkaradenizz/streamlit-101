import streamlit as st
import pandas as pd
import numpy as np
#st write
x = 42
st.write("Değişkenin değeri:", x)
st.divider()
data = {'Ad': ['Ali', 'Ayşe', 'Mehmet'],
        'Yaş': [25, 30, 22]}
df = pd.DataFrame(data)
st.write("Veri tablosu:", df)
st.divider()
#metin öğeleri

st.title("Proje Başlığı")  # Başlık burada yazılacak
st.divider()
st.header("Ana Başlık")  # Ana başlık burada yazılacak
st.divider()
st.subheader("Alt Başlık")  # Alt başlık burada yazılacak
st.divider()
st.text("Bu bölümde düz metin bilgileri paylaşabilirsiniz.")  # Düz metin burada yazılacak
st.divider()
st.markdown("""
### Markdown Başlığı
Markdown formatında metin yazabilirsiniz. 
- Madde 1
- Madde 2

**Kalın metin** ve *eğik metin* kullanabilirsiniz.
""")  # Markdown içeriği burada yazılacak
st.caption("Hadi istediğin bir açıklamayı yaz buraya!") # Caption açıklaması
st.divider()
code= print("Merhaba, streamlit!")
st.code('''
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print("Sonuç:", result)
''', language='python') # Python kodu burada yazılacak
st.divider()
#st.latex() matematiksel ifadeler
st.latex(r'''
E = mc^2
''')  # latex ile Einstein'ın ünlü formülü

st.latex(r'''
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
''')  # latex ile bir integral örneği

st.divider()



########################################################################################

# Kullanıcıdan metin girdisi alma --> input 
user_input = st.text_area("Lütfen özetlemek istediğiniz metni buraya yapıştırın:")






