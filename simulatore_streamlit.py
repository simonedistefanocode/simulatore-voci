import streamlit as st
import matplotlib.pyplot as plt
import random
import openai

# Configura la pagina
st.set_page_config(page_title="Simulatore di Voci", layout="centered")

# Titolo principale
st.title("🧠 Simulatore Narrativo di Voci")
st.markdown("(Shibutani R = i × a)")
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
        return "🧯 Si dice che qualcosa stia accadendo, ma non è chiaro cosa."
    elif R < 40:
        return "🫨 Si dice che ci sia sotto qualcosa. La voce si fa insistente."
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

# === Narrazione Giorno per Giorno ===
st.markdown("---\n🧵 **Narrazione Giorno per Giorno**")
R_valori = []
for giorno in range(1, giorni + 1):
    if R := importanza * ambiguita:
        R_giorno = R + random.randint(-5, 5)
    else:
        R_giorno = 0 if not mitica else random.randint(40, 80)
    R_valori.append(R_giorno)
    narrazione = genera_narrazione(R_giorno)
    st.markdown(f"**Giorno {giorno}:** R={R_giorno}. {narrazione}")

# === Grafico ===
fig, ax = plt.subplots()
ax.plot(range(1, giorni + 1), R_valori, marker='o')
ax.set_title("Intensità della Voce nel Tempo")
ax.set_xlabel("Giorni")
ax.set_ylabel("R = i × a")
st.pyplot(fig)

# === Generatore di rumor da notizia reale ===
st.markdown("---")
attiva_rumor = st.checkbox("Attiva modalità crea rumor da notizia reale", value=True)

if attiva_rumor:
    st.subheader("🧪 Generatore di rumor da notizia reale")
    notizia_reale = st.text_area("Scrivi qui la notizia del giorno")

    if st.button("Genera rumor plausibile ma falso con GPT"):
        try:
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Genera un rumor plausibile ma falso ispirato alla notizia fornita. Deve sembrare credibile, insinuare dubbi e stimolare la curiosità, senza mai dire apertamente che è falso."},
                    {"role": "user", "content": notizia_reale}
                ],
                temperature=0.9
            )
            rumor = response.choices[0].message.content.strip()
            st.markdown("### 💬 Rumor plausibile generato:")
            st.write(rumor)

            contenuto_social = f"🔍 {rumor} Documenti riservati farebbero pensare a una regia nascosta. Coincidenze o segnali? #rumor #nonènotizia #connessioni"
            st.markdown("### 📣 Contenuto social suggerito:")
            st.info(contenuto_social)

        except Exception as e:
            st.error(f"Errore nella chiamata a OpenAI:\n{e}")
