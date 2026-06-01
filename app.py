import streamlit as st

# Configurazione della pagina web
st.set_page_config(page_title="Verifica Ufficiale per vedere se sei veramente la mia P", page_icon="PATA", layout="centered")

# --- ZONA DI CONFIGURAZIONE IMMAGINE ESTERNA ---
# Sostituisci la stringa sottostante con il tuo link. DEVE finire in .jpg o .png!
URL_SFONDO = "import streamlit as st

# Configurazione della pagina web
st.set_page_config(page_title="Verifica Ufficiale per vedere se sei veramente la mia P", page_icon="PATA", layout="centered")

# --- ZONA DI CONFIGURAZIONE IMMAGINE ESTERNA ---
# Sostituisci la stringa sottostante con il tuo link. DEVE finire in .jpg o .png!
URL_SFONDO = "import streamlit as st

# Configurazione della pagina web
st.set_page_config(page_title="Verifica Ufficiale per vedere se sei veramente la mia P", page_icon="PATA", layout="centered")

# --- ZONA DI CONFIGURAZIONE IMMAGINE ESTERNA ---
# Sostituisci la stringa sottostante con il tuo link. DEVE finire in .jpg o .png!
URL_SFONDO = "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=1000&auto=format&fit=crop" 
# -----------------------------------------------

# 1. INIZIALIZZAZIONE DELLA MACCHINA A STATI
if 'fase_sistema' not in st.session_state:
    st.session_state.fase_sistema = 'INTRO'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 2. DEFINIZIONE DEI FOGLI DI STILE (CSS DINAMICO AVANZATO)

# CSS per la schermata Iniziale e Finale (Centrata e pulita)
css_intro = """
<style>
.stApp {
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
}
/* Centratura generale dei testi */
[data-testid="stMarkdownContainer"] {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}
/* Centratura del pulsante di avvio */
div.stButton > button {
    display: block;
    margin: 0 auto;
}
</style>
"""

# CSS per la fase di Gioco (Sfondo da URL e UI personalizzata)
css_gioco = f"""
<style>
/* 1. Sfondo esterno con adattamento automatico */
.stApp {{
    background-image: url("{URL_SFONDO}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* 2. Contenitore delle domande centrato */
[data-testid="stMarkdownContainer"] {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}}

/* 3. Layout delle opzioni (Allineamento a colonna centrata) */
div.stRadio > div[role="radiogroup"] {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
}}

/* 4. Il blocco dell'opzione (La "Card") */
div.stRadio > div[role="radiogroup"] > label {{
    background-color: #ffffff !important;
    border: 2px solid #ffb3d9 !important;
    border-radius: 12px !important;
    padding: 15px 30px !important;
    width: 85% !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
    display: flex !important;
    justify-content: center !important;
}}

/* Annulla gli stili di default interni alle card per evitare bug grafici */
div.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] {{
    background-color: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}}

/* 5. Rimozione fisica del pallino radio nativo */
div.stRadio > div[role="radiogroup"] > label > div:first-child {{
    display: none !important;
}}

/* 6. Animazione di sollevamento al passaggio del mouse (Hover) */
div.stRadio > div[role="radiogroup"] > label:hover {{
    transform: translateY(-6px) !important;
    box-shadow: 0 10px 20px rgba(255, 179, 217, 0.6) !important;
    background-color: #fff0f5 !important;
}}

/* 7. Colore Rosa quando il blocco viene selezionato (Focus/Active) */
div.stRadio > div[role="radiogroup"] > label:focus-within {{
    background-color: #ffb3d9 !important;
    transform: scale(1.02) !important;
    border-color: #ff66b2 !important;
}}

/* 8. Stile e centratura del pulsante di invio */
div.stButton > button {{
    display: block;
    margin: 30px auto 10px auto;
    background-color: #ffb3d9;
    color: #333333;
    border: none;
    border-radius: 8px;
    padding: 10px 30px;
    font-weight: bold;
    transition: all 0.2s ease;
}}
div.stButton > button:hover {{
    background-color: #ff99cc;
    color: white;
}}
</style>
"""

# 3. VETTORE DEI DATI 
quiz_data = [
    {
        "domanda": "Dove mi sono innamorato dei tuoi occhi per la prima volta?",
        "opzioni": ["Sul Treno", "Al Patù", "Al PN", "Alla Casina"],
        "risposta_corretta": "Sul Treno",
        "messaggio_err": "PATA HAI SBAGLIATO ??? OVVIO CHE MI SONO INNAMORATO DEI TUOI OCCHI BACIATI DAL SOLE SUL TRENO"
    },
    {
        "domanda": "Quale film stavamo guardando alla casina la prima volta ?",
        "opzioni": ["Jurassic World - La Rinascita", "Zootropolis", "Il Signore degli Anelli", "Matrix"],
        "risposta_corretta": "Jurassic World - La Rinascita",
        "messaggio_err": "E CON CHI ERI ALLORA ??? SEI LA MIA P"
    },
    {
        "domanda": "Qual'era il numero del treno dove mi sono innamorato dei tuoi occhi per la prima volta ?",
        "opzioni": ["54632", "4137", "45097", "43439"],
        "risposta_corretta": "4137",
        "messaggio_err": "DAI LO PRENDIAMO TUTTI I GIORNIII, SEI TORNATA INDIETRO PER VEDERE LA SGRIDATA IO LO SO"
    },
    {
        "domanda": "e e e e e e quanto mi ami ?",
        "opzioni": ["tanto", "tantissimo", "TANTISSIMOOOOO", "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP"],
        "risposta_corretta": "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP",
        "messaggio_err": "NON SCRIVO NEANCHE NIENTE QUA SO CHE SEI TORNATA INDIETRO PER VEDERE EHEHEHEH"
    }
]

# --- ESECUZIONE DELLA LOGICA DI STATO ---

if st.session_state.fase_sistema == 'INTRO':
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.title("Test per essere la mia sola e unica P")
    st.write("---")
    st.markdown(
        """
        **Attenzione:** Accesso a un'area altamente riservata ai soli P.
        
        Per sbloccare il modulo successivo è necessario dimostrare di essere una vera P. Un errore comporterà 
        il blocco del terminale fino all'inserimento del parametro corretto (E UNA BELLA SGRIDATA!!!!).
        """
    )
    
    st.write("---")
    if st.button("Pronta a dimostrare di essere la vera P ?"):
        st.session_state.fase_sistema" 
# -----------------------------------------------

# 1. INIZIALIZZAZIONE DELLA MACCHINA A STATI
if 'fase_sistema' not in st.session_state:
    st.session_state.fase_sistema = 'INTRO'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 2. DEFINIZIONE DEI FOGLI DI STILE (CSS DINAMICO AVANZATO)

# CSS per la schermata Iniziale e Finale (Centrata e pulita)
css_intro = """
<style>
.stApp {
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
}
/* Centratura generale dei testi */
[data-testid="stMarkdownContainer"] {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}
/* Centratura del pulsante di avvio */
div.stButton > button {
    display: block;
    margin: 0 auto;
}
</style>
"""

# CSS per la fase di Gioco (Sfondo da URL e UI personalizzata)
css_gioco = f"""
<style>
/* 1. Sfondo esterno con adattamento automatico */
.stApp {{
    background-image: url("{URL_SFONDO}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* 2. Contenitore delle domande centrato */
[data-testid="stMarkdownContainer"] {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}}

/* 3. Layout delle opzioni (Allineamento a colonna centrata) */
div.stRadio > div[role="radiogroup"] {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
}}

/* 4. Il blocco dell'opzione (La "Card") */
div.stRadio > div[role="radiogroup"] > label {{
    background-color: #ffffff !important;
    border: 2px solid #ffb3d9 !important;
    border-radius: 12px !important;
    padding: 15px 30px !important;
    width: 85% !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
    display: flex !important;
    justify-content: center !important;
}}

/* Annulla gli stili di default interni alle card per evitare bug grafici */
div.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] {{
    background-color: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}}

/* 5. Rimozione fisica del pallino radio nativo */
div.stRadio > div[role="radiogroup"] > label > div:first-child {{
    display: none !important;
}}

/* 6. Animazione di sollevamento al passaggio del mouse (Hover) */
div.stRadio > div[role="radiogroup"] > label:hover {{
    transform: translateY(-6px) !important;
    box-shadow: 0 10px 20px rgba(255, 179, 217, 0.6) !important;
    background-color: #fff0f5 !important;
}}

/* 7. Colore Rosa quando il blocco viene selezionato (Focus/Active) */
div.stRadio > div[role="radiogroup"] > label:focus-within {{
    background-color: #ffb3d9 !important;
    transform: scale(1.02) !important;
    border-color: #ff66b2 !important;
}}

/* 8. Stile e centratura del pulsante di invio */
div.stButton > button {{
    display: block;
    margin: 30px auto 10px auto;
    background-color: #ffb3d9;
    color: #333333;
    border: none;
    border-radius: 8px;
    padding: 10px 30px;
    font-weight: bold;
    transition: all 0.2s ease;
}}
div.stButton > button:hover {{
    background-color: #ff99cc;
    color: white;
}}
</style>
"""

# 3. VETTORE DEI DATI 
quiz_data = [
    {
        "domanda": "Dove mi sono innamorato dei tuoi occhi per la prima volta?",
        "opzioni": ["Sul Treno", "Al Patù", "Al PN", "Alla Casina"],
        "risposta_corretta": "Sul Treno",
        "messaggio_err": "PATA HAI SBAGLIATO ??? OVVIO CHE MI SONO INNAMORATO DEI TUOI OCCHI BACIATI DAL SOLE SUL TRENO"
    },
    {
        "domanda": "Quale film stavamo guardando alla casina la prima volta ?",
        "opzioni": ["Jurassic World - La Rinascita", "Zootropolis", "Il Signore degli Anelli", "Matrix"],
        "risposta_corretta": "Jurassic World - La Rinascita",
        "messaggio_err": "E CON CHI ERI ALLORA ??? SEI LA MIA P"
    },
    {
        "domanda": "Qual'era il numero del treno dove mi sono innamorato dei tuoi occhi per la prima volta ?",
        "opzioni": ["54632", "4137", "45097", "43439"],
        "risposta_corretta": "4137",
        "messaggio_err": "DAI LO PRENDIAMO TUTTI I GIORNIII, SEI TORNATA INDIETRO PER VEDERE LA SGRIDATA IO LO SO"
    },
    {
        "domanda": "e e e e e e quanto mi ami ?",
        "opzioni": ["tanto", "tantissimo", "TANTISSIMOOOOO", "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP"],
        "risposta_corretta": "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP",
        "messaggio_err": "NON SCRIVO NEANCHE NIENTE QUA SO CHE SEI TORNATA INDIETRO PER VEDERE EHEHEHEH"
    }
]

# --- ESECUZIONE DELLA LOGICA DI STATO ---

if st.session_state.fase_sistema == 'INTRO':
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.title("Test per essere la mia sola e unica P")
    st.write("---")
    st.markdown(
        """
        **Attenzione:** Accesso a un'area altamente riservata ai soli P.
        
        Per sbloccare il modulo successivo è necessario dimostrare di essere una vera P. Un errore comporterà 
        il blocco del terminale fino all'inserimento del parametro corretto (E UNA BELLA SGRIDATA!!!!).
        """
    )
    
    st.write("---")
    if st.button("Pronta a dimostrare di essere la vera P ?"):
        st.session_state.fase_sistema" 
# -----------------------------------------------

# 1. INIZIALIZZAZIONE DELLA MACCHINA A STATI
if 'fase_sistema' not in st.session_state:
    st.session_state.fase_sistema = 'INTRO'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 2. DEFINIZIONE DEI FOGLI DI STILE (CSS DINAMICO AVANZATO)

# CSS per la schermata Iniziale e Finale (Centrata e pulita)
css_intro = """
<style>
.stApp {
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
}
/* Centratura generale dei testi */
[data-testid="stMarkdownContainer"] {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    text-align: center;
}
/* Centratura del pulsante di avvio */
div.stButton > button {
    display: block;
    margin: 0 auto;
}
</style>
"""

# CSS per la fase di Gioco (Sfondo da URL e UI personalizzata)
css_gioco = f"""
<style>
/* 1. Sfondo esterno con adattamento automatico */
.stApp {{
    background-image: url("{URL_SFONDO}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* 2. Contenitore delle domande centrato */
[data-testid="stMarkdownContainer"] {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}}

/* 3. Layout delle opzioni (Allineamento a colonna centrata) */
div.stRadio > div[role="radiogroup"] {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 20px;
}}

/* 4. Il blocco dell'opzione (La "Card") */
div.stRadio > div[role="radiogroup"] > label {{
    background-color: #ffffff !important;
    border: 2px solid #ffb3d9 !important;
    border-radius: 12px !important;
    padding: 15px 30px !important;
    width: 85% !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
    display: flex !important;
    justify-content: center !important;
}}

/* Annulla gli stili di default interni alle card per evitare bug grafici */
div.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] {{
    background-color: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
}}

/* 5. Rimozione fisica del pallino radio nativo */
div.stRadio > div[role="radiogroup"] > label > div:first-child {{
    display: none !important;
}}

/* 6. Animazione di sollevamento al passaggio del mouse (Hover) */
div.stRadio > div[role="radiogroup"] > label:hover {{
    transform: translateY(-6px) !important;
    box-shadow: 0 10px 20px rgba(255, 179, 217, 0.6) !important;
    background-color: #fff0f5 !important;
}}

/* 7. Colore Rosa quando il blocco viene selezionato (Focus/Active) */
div.stRadio > div[role="radiogroup"] > label:focus-within {{
    background-color: #ffb3d9 !important;
    transform: scale(1.02) !important;
    border-color: #ff66b2 !important;
}}

/* 8. Stile e centratura del pulsante di invio */
div.stButton > button {{
    display: block;
    margin: 30px auto 10px auto;
    background-color: #ffb3d9;
    color: #333333;
    border: none;
    border-radius: 8px;
    padding: 10px 30px;
    font-weight: bold;
    transition: all 0.2s ease;
}}
div.stButton > button:hover {{
    background-color: #ff99cc;
    color: white;
}}
</style>
"""

# 3. VETTORE DEI DATI 
quiz_data = [
    {
        "domanda": "Dove mi sono innamorato dei tuoi occhi per la prima volta?",
        "opzioni": ["Sul Treno", "Al Patù", "Al PN", "Alla Casina"],
        "risposta_corretta": "Sul Treno",
        "messaggio_err": "PATA HAI SBAGLIATO ??? OVVIO CHE MI SONO INNAMORATO DEI TUOI OCCHI BACIATI DAL SOLE SUL TRENO"
    },
    {
        "domanda": "Quale film stavamo guardando alla casina la prima volta ?",
        "opzioni": ["Jurassic World - La Rinascita", "Zootropolis", "Il Signore degli Anelli", "Matrix"],
        "risposta_corretta": "Jurassic World - La Rinascita",
        "messaggio_err": "E CON CHI ERI ALLORA ??? SEI LA MIA P"
    },
    {
        "domanda": "Qual'era il numero del treno dove mi sono innamorato dei tuoi occhi per la prima volta ?",
        "opzioni": ["54632", "4137", "45097", "43439"],
        "risposta_corretta": "4137",
        "messaggio_err": "DAI LO PRENDIAMO TUTTI I GIORNIII, SEI TORNATA INDIETRO PER VEDERE LA SGRIDATA IO LO SO"
    },
    {
        "domanda": "e e e e e e quanto mi ami ?",
        "opzioni": ["tanto", "tantissimo", "TANTISSIMOOOOO", "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP"],
        "risposta_corretta": "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP",
        "messaggio_err": "NON SCRIVO NEANCHE NIENTE QUA SO CHE SEI TORNATA INDIETRO PER VEDERE EHEHEHEH"
    }
]

# --- ESECUZIONE DELLA LOGICA DI STATO ---

if st.session_state.fase_sistema == 'INTRO':
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.title("Test per essere la mia sola e unica P")
    st.write("---")
    st.markdown(
        """
        **Attenzione:** Accesso a un'area altamente riservata ai soli P.
        
        Per sbloccare il modulo successivo è necessario dimostrare di essere una vera P. Un errore comporterà 
        il blocco del terminale fino all'inserimento del parametro corretto (E UNA BELLA SGRIDATA!!!!).
        """
    )
    
    st.write("---")
    if st.button("Pronta a dimostrare di essere la vera P ?"):
        st.session_state.fase_sistema
