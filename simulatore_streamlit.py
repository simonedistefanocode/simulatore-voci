import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Simulatore di Voci", layout="centered")

st.title("🧠 Simulatore Narrativo di Voci\n(Shibutani R = i × a)")
st.write("Simula la propagazione di una voce in base all'importanza (i) e all'ambiguità (a)")

# === Input dell'utente ===
titolo_voce = st.text_input("Scrivi qui la notizia del giorno", "Qualcosa si sta muovendo dietro le quinte")
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
st.markdown("---\n🧵 **Narrazione Giorno per Giorno**")
R_valori = []
for giorno in range(1, giorni + 1):
    if importanza * ambiguita:
        R_giorno = importanza * ambiguita + random.randint(-5, 5)
    else:
        R_giorno = 0 if not mitica else random.randint(40, 80)

    R_valori.append(R_giorno)
    st.markdown(f"**Giorno {giorno}:** R={R_giorno}. {genera_narrazione(R_giorno)}")

# === Grafico ===
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_valori, marker='o')
ax.set_title("Intensità della Voce nel Tempo")
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
st.pyplot(fig)

# === Generatore di rumor da notizia reale ===
st.markdown("---")
attiva_rumor = st.checkbox("✅ Attiva modalità crea rumor da notizia reale")

# === Funzione dinamica ===
def genera_rumor(notizia):
    notizia = notizia.lower()
    if any(parola in notizia for parola in ["energia", "nucleare", "gas", "petrolio"]):
        return "Si dice che dietro il nuovo piano energetico ci sia un accordo segreto con aziende estere."
    elif any(parola in notizia for parola in ["covid", "virus", "pandemia", "vaccino"]):
        return "Si dice che alcuni laboratori stessero studiando queste mutazioni da tempo, senza informare il pubblico."
    elif any(parola in notizia for parola in ["ai", "intelligenza artificiale", "hacker", "algoritmo", "dati"]):
        return "Si dice che una falla nell’algoritmo abbia permesso a gruppi esterni di accedere a dati sensibili."
    elif any(parola in notizia for parola in ["governo", "parlamento", "politici"]):
        return "Si dice che alcune decisioni siano state influenzate da pressioni occulte esterne."
    elif any(parola in notizia for parola in ["omicidio", "scomparsa", "cold case", "sparizione"]):
        return "Si dice che qualcuno sappia più di quanto abbia dichiarato, ma stia coprendo la verità."
    else:
        return "Si dice che dietro le apparenze si nasconda una verità che pochi vogliono vedere."

def genera_contenuto_social(rumor):
    return f"🔍 {rumor} Documenti riservati farebbero pensare a una regia nascosta. Coincidenze o segnali? #rumor #nonènutizia #connessioni"

if attiva_rumor:
    st.subheader("🧪 Generatore di rumor da notizia reale")
    notizia_input = st.text_area("Scrivi qui la notizia del giorno", titolo_voce)
    if st.button("Genera rumor plausibile ma falso"):
        rumor = genera_rumor(notizia_input)
        social = genera_contenuto_social(rumor)
        st.markdown("### 💬 Rumor plausibile generato:")
        st.write(rumor)
        st.markdown("### 📣 Contenuto social suggerito:")
        st.info(social)
