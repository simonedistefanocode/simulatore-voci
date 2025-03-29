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
st.markdown("---\n🧵 **Narrazione Giorno per Giorno**")
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
    if any(kw in notizia for kw in ["energia", "clima", "nucleare"]):
        return "Si dice che dietro il nuovo piano energetico ci sia un accordo segreto con aziende estere per il controllo delle risorse."
    elif any(kw in notizia for kw in ["governo", "politica", "decreto", "ministro"]):
        return "Si dice che alcune decisioni politiche siano manovrate da gruppi con interessi oscuri."
    elif any(kw in notizia for kw in ["tecnologia", "5g", "innovazione"]):
        return "Si dice che dietro l'innovazione si nascondano tecnologie di controllo sociale."
    elif any(kw in notizia for kw in ["salute", "vaccino", "pandemia"]):
        return "Si dice che alcune cure siano state nascoste per interessi farmaceutici."
    elif any(kw in notizia for kw in ["ai", "intelligenza artificiale", "hacker", "cyber", "sicurezza", "informatica"]):
        return "Si dice che un algoritmo di intelligenza artificiale stia agendo senza controllo umano."
    elif any(kw in notizia for kw in ["omicidio", "crimine", "cold case"]):
        return "Si dice che il caso irrisolto sia legato a una rete di coperture insospettabili."
    else:
        return "Si dice che dietro le apparenze si nasconda una verità che pochi vogliono vedere."

def genera_contenuto_social(rumor):
    hashtag = "#verità #svelata #dubbi" if "verità" in rumor else "#mistero #rumor #attualità"
    return f"🔍 {rumor} Alcuni dettagli non tornano e il dubbio cresce. Coincidenze o segnali? {hashtag}"

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
