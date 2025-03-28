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

# === Funzione per generare narrazione ===
def genera_narrazione(R):
    if R == 0:
        return "🫥 Nessuno ne parla. Tutto tace."
    elif R < 20:
        return "🤫 Si dice che qualcosa stia accadendo, ma non è chiaro cosa."
    elif R < 40:
        return "🤨 Si dice che ci sia sotto qualcosa. La voce si fa insistente."
    elif R < 50:
        return "😶‍🌫️ Si dice che nessuno dica la verità."
    elif R < 60:
        return "🌀 Si dice che tutto sia solo la punta dell’iceberg."
    elif R < 70:
        return "🧩 Si dice che qualcuno stia nascondendo qualcosa di grosso."
    elif R < 90:
        return "🗣️ Si dice che tutti inizino a parlarne, ma ognuno ha una versione diversa."
    else:
        return "🔥 Si dice che sia ormai fuori controllo. La voce diventa leggenda."

# === Simulazione della propagazione ===
st.markdown("""---\n🧵 **Narrazione Giorno per Giorno**""")
for giorno in range(1, giorni + 1):
    if R := importanza * ambiguita:
        R_giorno = R + random.randint(-5, 5)
    else:
        R_giorno = 0 if not mitica else random.randint(40, 80)

    narrazione = genera_narrazione(R_giorno)
    st.markdown(f"**Giorno {giorno}:** R={R_giorno}. {narrazione}")

# === Grafico ===
R_valori = [(importanza * ambiguita + random.randint(-5, 5)) if (importanza * ambiguita) else (0 if not mitica else random.randint(40, 80)) for _ in range(giorni)]
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_valori, marker='o')
ax.set_title("Intensità della Voce nel Tempo")
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
st.pyplot(fig)
