import streamlit as st

# Configurazione della pagina web
st.set_page_config(page_title="Sistema di Verifica", page_icon="🔒", layout="centered")

# --- INIZIO INIEZIONE CSS PER BACKGROUND ---
st.markdown(
    """
    <style>
    /* Applica lo sfondo all'intero container dell'applicazione */
    .stApp {
        background-color: #ffe8f2; /* Colore di base rosa pastello */
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 24 24'%3E%3Cpath fill='%23ffb3d9' opacity='0.6' d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E");
    }
    
    /* Applica un bordo semi-trasparente ai contenitori di testo per mantenere la leggibilità */
    [data-testid="stMarkdownContainer"] {
        background-color: rgba(255, 255, 255, 0.6);
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- FINE INIEZIONE CSS ---
# 1. INIZIALIZZAZIONE DELLE VARIABILI DI STATO
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

# 2. STRUTTURA DATI DEL QUESTIONARIO (ZONA DI PERSONALIZZAZIONE)
quiz_data = [
    {
        "domanda": "Qual è il luogo esatto del nostro primo incontro?",
        "opzioni": ["Piazza Navona", "Stazione Centrale", "Parco degli Acquedotti", "Bar Roma"],
        "risposta_corretta": "Parco degli Acquedotti",
        "messaggio_ok": "Risposta validata.",
        "messaggio_err": "Dato non corretto. Memoria fallace."
    },
    {
        "domanda": "Quale film stavamo guardando quando ci siamo addormentati la prima volta?",
        "opzioni": ["Interstellar", "Inception", "Il Signore degli Anelli", "Matrix"],
        "risposta_corretta": "Interstellar",
        "messaggio_ok": "Risposta validata. Ottima ritenzione del dato.",
        "messaggio_err": "Errore di calcolo."
    },
    {
        "domanda": "Qual è la meta concordata per il prossimo viaggio?",
        "opzioni": ["Giappone", "Islanda", "Norvegia", "Perù"],
        "risposta_corretta": "Islanda",
        "messaggio_ok": "Parametro corretto.",
        "messaggio_err": "Destinazione non riconosciuta dai sistemi."
    }
]

# 3. INTERFACCIA E LOGICA DI CONTROLLO
st.title("Terminale di Autenticazione")
st.write("---")

# Verifica se ci sono ancora domande nel vettore
if st.session_state.current_index < len(quiz_data):
    # Estrazione dei dati della domanda corrente
    q_data = quiz_data[st.session_state.current_index]
    
    st.subheader(f"Iterazione {st.session_state.current_index + 1} di {len(quiz_data)}")
    st.write(q_data["domanda"])
    
    # Generazione dei radio button per la selezione
    scelta = st.radio("Selezionare il parametro corretto:", q_data["opzioni"], index=None)
    
    # Pulsante di validazione
    if st.button("Invia Dati"):
        if scelta == q_data["risposta_corretta"]:
            st.success(q_data["messaggio_ok"])
            st.session_state.score += 1
        else:
            st.error(q_data["messaggio_err"])
        
        # Incremento dell'indice e forzatura del ricaricamento dell'interfaccia
        st.session_state.current_index += 1
        st.rerun()

# 4. OUTPUT FINALE
else:
    st.write("### Procedura Completata")
    st.write(f"Percentuale di successo: {(st.session_state.score / len(quiz_data)) * 100:.1f}%")
    
    if st.session_state.score == len(quiz_data):
        st.balloons()
        st.success("Tutti i parametri sono corretti. [Inserire qui la ricompensa, es. link a una prenotazione o un messaggio finale].")
    else:
        st.warning("Prestazione sub-ottimale. Sono richiesti ulteriori cicli di addestramento.")
        if st.button("Reinizializza Sistema"):
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.rerun()
