import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#st.map Kullanımı
#st.map fonksiyonu bir Pandas DataFrame'e ihtiyaç duyar.
######################################################
#Ayrıca, herhangi bir Streamlit metodunu çağırmadan uygulamanıza yazabilirsiniz. 
#Çünkü Streamlit, "st.write()" komutunu otomatik destekler, yani bu komutu hiç kullanmanıza gerek kalmaz !
df = pd.DataFrame({
  'S1': [1, 2, 3, 4],
  'S2': [10, 20, 30, 40]
})
df
st.divider()

#st write
x = 42
st.write("Değişkenin değeri:", x)
st.divider()
data = {'Ad': ['Ali', 'Ayşe', 'Mehmet'],
        'Yaş': [25, 30, 22]}
df = pd.DataFrame(data)
st.write("Veri tablosu:", df)
st.divider()
# Veriler
x = np.linspace(0, 50, 100)
y = np.sin(x)

# Grafik oluşturma
fig, ax = plt.subplots()
ax.plot(x, y)
#ax: Bu grafik alanının içine yerleştirilen bir ekseni (axis) temsil eder. 
#Genellikle bir eksen, x ve y eksenlerinin olduğu bir çizim alanını ifade eder.

# Grafik yazdırma
st.write(fig)
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






