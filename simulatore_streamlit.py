import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Simulatore di Voci", layout="centered")

st.title("\U0001f9e0 Simulatore Narrativo di Voci\n(Shibutani R = i × a)")
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
        return "\U0001fae5 Nessuno ne parla. Tutto tace."
    elif R < 20:
        return "\U0001f92b Si dice che qualcosa stia accadendo, ma non è chiaro cosa."
    elif R < 40:
        return "\U0001f928 Si dice che ci sia sotto qualcosa. La voce si fa insistente."
    elif R < 50:
        return "\U0001f636‍\U0001f32b️ Si dice che nessuno dica la verità."
    elif R < 60:
        return "\U0001f300 Si dice che tutto sia solo la punta dell’iceberg."
    elif R < 70:
        return "\U0001f9e9 Si dice che qualcuno stia nascondendo qualcosa di grosso."
    elif R < 90:
        return "\U0001f5e3️ Si dice che tutti inizino a parlarne, ma ognuno ha una versione diversa."
    else:
        return "\U0001f525 Si dice che sia ormai fuori controllo. La voce diventa leggenda."

# === Simulazione della propagazione ===
st.markdown("""---\n\U0001f9f5 **Narrazione Giorno per Giorno**""")
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
    notizia_bassa = notizia.lower()

    if any(kw in notizia_bassa for kw in ["energia", "gas", "petrolio", "nucleare"]):
        return "Si dice che dietro il nuovo piano energetico ci sia un accordo segreto con aziende estere per il controllo delle risorse."
    elif any(kw in notizia_bassa for kw in ["governo", "politica", "decreto", "parlamento"]):
        return "Si dice che alcune decisioni siano state prese in ambienti ristretti, lontani dal controllo democratico."
    elif any(kw in notizia_bassa for kw in ["virus", "covid", "vaccino", "sanità", "ospedale"]):
        return "Si dice che alcuni laboratori stessero studiando queste mutazioni da tempo, senza informare il pubblico."
    elif any(kw in notizia_bassa for kw in ["ai", "intelligenza artificiale", "hacker", "cyber", "dati", "algoritmi"]):
        return "Si dice che una falla nell’algoritmo abbia permesso a gruppi esterni di accedere a dati sensibili senza lasciare tracce."
    elif any(kw in notizia_bassa for kw in ["omicidio", "scomparsa", "crimine", "inchiesta", "indagine"]):
        return "Si dice che ci siano troppe coincidenze e che qualcuno stia cercando di insabbiare i veri responsabili."
    else:
        return "Si dice che dietro le apparenze si nasconda una verità che pochi vogliono vedere."

def genera_contenuto_social(rumor):
    hook = random.choice([
        "Alcuni dettagli non tornano e il dubbio cresce.",
        "Documenti riservati farebbero pensare a una regia nascosta.",
        "Le coincidenze iniziano a essere troppe.",
        "E se fosse tutto già deciso da tempo?",
    ])
    hashtag = random.choice([
        "#verità #segreti #dubbio",
        "#rumor #nonènutizia #connessioni",
        "#whistleblower #misteri #inquietudine",
        "#fakenews #controllo #dietrolequinte",
    ])
    return f"🔍 {rumor} {hook} {hashtag}"

# === Blocchi del rumor ===
if attiva_rumor:
    st.subheader("\U0001f9ea Generatore di rumor da notizia reale")
    notizia_reale = st.text_area("Scrivi qui la notizia del giorno", "Oggi è stato annunciato un nuovo piano energetico nazionale basato sul nucleare.")

    if st.button("Genera rumor plausibile ma falso"):
        rumor_generato = genera_rumor(notizia_reale)
        contenuto_social = genera_contenuto_social(rumor_generato)

        st.markdown("### \U0001f4ac Rumor plausibile generato:")
        st.write(rumor_generato)

        st.markdown("### \U0001f4e3 Contenuto social suggerito:")
        st.info(contenuto_social)
