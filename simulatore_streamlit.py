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

# === Frasi narrative dinamiche ===
frasi_base = [
    "😐 Si dice che nessuno dica la verità.",
    "😏 Si dice che ci sia sotto qualcosa. La voce si fa insistente.",
    "🔊 Si dice che sta circolando, ma nessuno sa da dove provenga.",
    "🧙‍♂️ Nessuno conferma, ma tutti ne parlano.",
    "🦜 Qualcuno dice di aver visto cose strane. Nessuno sa cosa pensare.",
    "🧐 Alcuni dicono che è tutto vero, altri che è una montatura.",
    "🚫 I media tacciono. La voce cresce tra la gente.",
    "🧩 Si dice che sia solo la punta dell'iceberg.",
    "🕵️‍♂️ Si dice che qualcuno ha interesse a insabbiare tutto.",
    "🦝 Qualcuno parla di forze occulte. Nessuno può più fermarla.",
    "🛰️ Tutti ne parlano, ma ognuno ha una versione diversa.",
    "🔥 La voce si è trasformata in leggenda."
]

# === Simulazione della propagazione ===
st.markdown("""---\n🧵 **Narrazione Giorno per Giorno**""")
R_valori = []

for giorno in range(1, giorni + 1):
    if R := importanza * ambiguita:
        R_giorno = R + random.randint(-5, 5)
    else:
        R_giorno = 0 if not mitica else random.randint(40, 80)

    frase_del_giorno = frasi_base[(giorno - 1) % len(frasi_base)]
    st.markdown(f"**Giorno {giorno}:** R={R_giorno}. {frase_del_giorno}")
    R_valori.append(R_giorno)

# === Grafico ===
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_valori, marker='o')
ax.set_title("Intensità della Voce nel Tempo")
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
st.pyplot(fig)
