
import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Simulatore di Voci", layout="centered")

st.title("🧠 Simulatore Narrativo di Voci\n(Shibutani R = i × a)")
st.write("Simula la propagazione di una voce in base all'importanza (i) e all'ambiguità (a)")

# === Sezione: Generatore di rumor da notizia reale ===
attiva_rumor = st.checkbox("🧪 Attiva modalità crea rumor da notizia reale", value=True)

if attiva_rumor:
    st.subheader("🧪 Generatore di rumor da notizia reale")
    notizia_reale = st.text_area("Scrivi qui la notizia del giorno", "Oggi è stato annunciato un nuovo piano energetico nazionale basato sul nucleare.")

    importanza = st.slider("Importanza (i)", 0, 10, 5)
    ambiguita = st.slider("Ambiguità (a)", 0, 10, 5)
    giorni = st.slider("Giorni di propagazione", 3, 15, 7)
    mitica = st.checkbox("Forza modalità mitica se R = 0")

    titolo_voce = notizia_reale  # Collegamento diretto

    # === Simulazione della propagazione ===
    st.markdown("---\n🧵 **Narrazione Giorno per Giorno**")
    for giorno in range(1, giorni + 1):
        if R := importanza * ambiguita:
            R_giorno = R + random.randint(-5, 5)
        else:
            R_giorno = 0 if not mitica else random.randint(40, 80)

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

    # === Funzione per generare rumor plausibile ===
    def genera_rumor(notizia):
        parole_chiave = {
            "energia": "Si dice che dietro il nuovo piano energetico ci sia un accordo segreto con aziende private estere per il controllo delle risorse.",
            "covid": "Si dice che alcuni laboratori stessero studiando queste mutazioni da tempo, senza informare il pubblico.",
            "ai": "Si dice che alcune intelligenze artificiali siano già sfuggite al controllo.",
            "hacker": "Si dice che alcuni attacchi informatici siano insabbiati per non allarmare l’opinione pubblica.",
            "alien": "Si dice che alcuni governi abbiano prove dell’esistenza di vita extraterrestre, mai divulgate."
        }
        testo = notizia.lower()
        for chiave in parole_chiave:
            if chiave in testo:
                return parole_chiave[chiave]
        return "Si dice che dietro le apparenze si nasconda una verità che pochi vogliono vedere."

    def genera_contenuto_social(rumor):
        return f"🔍 {rumor} Alcuni dettagli non tornano e il dubbio cresce. Coincidenze o segnali? #verità #segreti #dubbio"

    if st.button("Genera rumor plausibile ma falso"):
        rumor = genera_rumor(notizia_reale)
        social = genera_contenuto_social(rumor)

        st.markdown("### 💬 Rumor plausibile generato:")
        st.write(rumor)
        st.markdown("### 📣 Contenuto social suggerito:")
        st.info(social)
