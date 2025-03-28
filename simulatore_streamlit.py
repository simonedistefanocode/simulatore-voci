
import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Simulatore di Voci", layout="centered")

st.title("🧠 Simulatore Narrativo di Voci (Shibutani R = i × a)")
st.markdown("Simula la propagazione di una voce in base all'importanza (i) e all'ambiguità (a)")

# Input utente
titolo = st.text_input("Titolo della voce", "Gli alieni sono tra noi")
i = st.slider("Importanza (i)", 0, 10, 5)
a = st.slider("Ambiguità (a)", 0, 10, 5)
giorni = st.slider("Giorni di propagazione", 3, 15, 7)
modalita_mito = st.checkbox("Forza modalità mitica se R = 0")

# Frasi leggendarie
miti = [
    "Gli alieni sono tra noi da anni.",
    "Elvis è ancora vivo, nascosto in Argentina.",
    "Lady Diana non è morta: è tutto un complotto.",
    "Il virus è stato creato in laboratorio.",
    "L'uomo non è mai andato sulla Luna."
]

# Simulazione
R_values = []
narrativa = []

for giorno in range(1, giorni + 1):
    R = i * a
    R_values.append(R)

    if R == 0 and modalita_mito:
        frase = f"[MITO] {random.choice(miti)}"
    elif R >= 40:
        frase = f"Giorno {giorno}: R={R}. Si dice che nessuno dice la verità."
    elif R >= 25:
        frase = f"Giorno {giorno}: R={R}. Si vocifera che ci siano documenti segreti."
    elif R > 0:
        frase = f"Giorno {giorno}: R={R}. Qualcuno ha dei sospetti..."
    else:
        frase = f"Giorno {giorno}: R={R}. Nessuna voce significativa."

    narrativa.append(frase)
    i += random.choice([-1, 0, 1])
    a += random.choice([-1, 0, 1])
    i = max(0, min(10, i))
    a = max(0, min(10, a))

# Output narrativo
st.subheader("📜 Narrazione Giorno per Giorno")
for riga in narrativa:
    st.markdown(f"- {riga}")

# Grafico
st.subheader("📈 Propagazione della Voce")
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_values, marker='o')
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
ax.set_title("Andamento della voce nel tempo")
ax.grid(True)
st.pyplot(fig)
