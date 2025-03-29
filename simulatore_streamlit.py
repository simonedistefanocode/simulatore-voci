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

# === Sezione: Generatore di rumor da notizia reale ===
st.markdown("---")
attiva_rumor = st.checkbox("Attiva modalità crea rumor da notizia reale")

# === Funzione per generare rumor plausibile ===
def genera_rumor(notizia):
    notizia = notizia.lower()
    if any(word in notizia for word in ["energia", "nucleare", "elettricità"]):
        return "Si dice che dietro il piano energetico ci sia un accordo con aziende estere che stanno segretamente comprando il controllo delle infrastrutture."
    elif any(word in notizia for word in ["governo", "ministro", "politica"]):
        return "Si dice che alcune decisioni del governo siano influenzate da lobby internazionali mai ufficialmente registrate."
    elif any(word in notizia for word in ["AI", "intelligenza artificiale", "robot", "algoritmi", "openai", "chatgpt"]):
        return "Si dice che alcune aziende abbiano già creato una AI senziente, ma stiano insabbiando tutto per motivi di sicurezza."
    elif any(word in notizia for word in ["hacker", "cyberattacco", "violazione", "spyware", "dark web"]):
        return "Si dice che il recente attacco informatico sia stato solo una distrazione per un furto dati più grande ancora nascosto."
    elif any(word in notizia for word in ["salute", "vaccino", "virus", "malattia"]):
        return "Si dice che la nuova terapia sia in realtà un esperimento segreto per controllare il comportamento umano."
    elif any(word in notizia for word in ["cold case", "omicidio", "scomparsa", "verità", "cospirazione"]):
        return "Si dice che le indagini siano state bloccate per proteggere figure importanti coinvolte."
    else:
        return "Si dice che dietro la notizia si nasconda una verità che non vogliono farci sapere."

def genera_contenuto_social(rumor):
    return f"🚨 {rumor} Alcuni documenti trapelati suggeriscono una regia occulta dietro le decisioni ufficiali. #dubbi #verità #potere"

if attiva_rumor:
    st.subheader("🧪 Generatore di rumor da notizia reale")
    notizia_reale = st.text_area("Scrivi qui la notizia del giorno", "Oggi è stato annunciato un nuovo piano energetico nazionale basato sul nucleare.")

    if st.button("Genera rumor plausibile ma falso"):
        falso_rumor = genera_rumor(notizia_reale)
        contenuto_social = genera_contenuto_social(falso_rumor)

        st.markdown("### 💬 Rumor plausibile generato:")
        st.write(falso_rumor)

        st.markdown("### 📣 Contenuto social suggerito:")
        st.info(contenuto_social)
