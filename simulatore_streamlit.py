import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Simulatore di Voci", layout="centered")

st.title("🧠 Simulatore Narrativo di Voci\n(Shibutani R = i × a)")
st.write("Simula la propagazione di una voce in base all'importanza (i) e all'ambiguità (a)")

# === Input dell'utente ===
titolo_voce = st.text_input("Titolo della voce", "Gli alieni sono tra noi")
importanza = st.slider("Importanza (i)", 0, 10, 5)
ambiguita = st.slider("Ambiguità (a)", 0, 10, 5)
giorni = st.slider("Giorni di propagazione", 3, 15, 7)
mitica = st.checkbox("Forza modalità mitica se R = 0")

# === Frasi narrative possibili ===
frasi_possibili = [
    "😐 Si dice che nessuno dica la verità.",
    "😏 Si dice che ci sia sotto qualcosa. La voce si fa insistente.",
    "🧊 Si dice che è solo la punta dell'iceberg. La voce si propaga.",
    "🕵️ Si dice che qualcuno ha interesse a insabbiare tutto. La voce si propaga.",
    "🧙‍♂️ Qualcuno parla di forze occulte. Nessuno può più fermarla.",
    "🌀 La voce si trasforma in leggenda. Nessuno sa dove inizia e dove finisce.",
]

# === Simulazione della propagazione ===
st.markdown("""---\n🧵 **Narrazione Giorno per Giorno**""")
R_valori = []

for giorno in range(1, giorni + 1):
    if R := importanza * ambiguita:
        R_giorno = R + random.randint(-5, 5)
    else:
        R_giorno = 0 if not mitica else random.randint(40, 80)

    frase_del_giorno = frasi_possibili[(giorno - 1) % len(frasi_possibili)]
    st.markdown(f"**Giorno {giorno}:** R={R_giorno}. {frase_del_giorno}")
    R_valori.append(R_giorno)

# === Grafico ===
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_valori, marker='o')
ax.set_title("Intensità della Voce nel Tempo")
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
st.pyplot(fig)
