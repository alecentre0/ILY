import streamlit as st

# Configurazione della pagina web
st.set_page_config(page_title="TI AMO", page_icon="PATA", layout="centered")

# --- ZONA DI CONFIGURAZIONE IMMAGINI ESTERNE ---
URL_SFONDO_INTRO = "https://i.etsystatic.com/20432923/r/il/7f58db/3960105404/il_570xN.3960105404_ilu4.jpg" 
URL_SFONDO_GIOCO = "https://st2.depositphotos.com/1954507/9938/v/950/depositphotos_99381044-stock-illustration-pink-background-with-hearts.jpg" 
# -----------------------------------------------

# 1. INIZIALIZZAZIONE DELLA MACCHINA A STATI
if 'fase_sistema' not in st.session_state:
    st.session_state.fase_sistema = 'INTRO'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 2. DEFINIZIONE DEI FOGLI DI STILE (CSS DINAMICO AVANZATO)

# CSS per la schermata Iniziale e Finale (Pulsante a Cuore CENTRATO)
css_intro = f"""
<style>
.stApp {{
    background-image: url("{URL_SFONDO_INTRO}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stMarkdownContainer"] {{
    background-color: rgba(255, 255, 255, 0.90);
    padding: 40px 30px !important; 
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    text-align: center;
}}
[data-testid="stMarkdownContainer"] p {{
    font-size: 1.4rem !important;
    line-height: 1.6 !important;
    color: #333333 !important;
}}
[data-testid="stMarkdownContainer"] h1 {{
    font-size: 2.2rem !important;
    color: #ff66b2 !important;
    margin-bottom: 10px !important;
}}
[data-testid="stMarkdownContainer"] h3 {{
    font-size: 1.8rem !important;
    color: #ff66b2 !important;
}}

/* PULSANTE A CUORE CENTRATO (Senza quadratino fantasma) */
div.stButton {{
    display: block !important;
    width: 100% !important;
    background-color: transparent !important;
}}
div.stButton > button * {{
    background-color: transparent !important;
    box-shadow: none !important;
}}
div.stButton > button {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 20px auto 10px auto !important; /* CENTRATO */
    background-color: #ff66b2 !important;
    color: #ffffff !important;
    font-size: 1.4rem !important;
    font-weight: bold !important;
    width: 140px !important;
    height: 130px !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    
    border: none !important;
    border-radius: 0 !important; 
    box-shadow: none !important;
    outline: none !important;
    padding: 0 0 12px 0 !important;
    
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E") !important;
    -webkit-mask-size: 100% 100% !important;
    -webkit-mask-repeat: no-repeat !important;
    -webkit-mask-position: center !important;
    mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E") !important;
    mask-size: 100% 100% !important;
    mask-repeat: no-repeat !important;
    mask-position: center !important;
    
    filter: drop-shadow(0px 6px 8px rgba(255, 102, 178, 0.4)) !important;
}}
div.stButton > button:focus,
div.stButton > button:active {{
    box-shadow: none !important;
    outline: none !important;
    border: none !important;
    background-color: #ff007f !important;
    color: #ffffff !important;
}}
div.stButton > button:hover {{
    transform: translateY(-5px) scale(1.05) !important;
    background-color: #ff3399 !important;
    box-shadow: none !important;
    filter: drop-shadow(0px 12px 15px rgba(255, 51, 153, 0.6)) !important;
}}
</style>
"""

# CSS per la fase di Gioco (Pulsante a Cuore NON CENTRATO)
css_gioco = f"""
<style>
.stApp {{
    background-image: url("{URL_SFONDO_GIOCO}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stMarkdownContainer"] {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}}
div.stRadio > div[role="radiogroup"] {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px; 
    margin-top: 20px;
}}
div.stRadio > div[role="radiogroup"] > label {{
    background-color: #ffffff !important;
    border: 2px solid #ffb3d9 !important;
    border-radius: 15px !important;
    padding: 22px 20px !important; 
    width: 100% !important; 
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    display: flex !important;
    justify-content: center !important; 
    align-items: center !important; 
}}
div.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] {{
    background-color: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
    width: 100% !important;
    text-align: center !important;
}}
div.stRadio > div[role="radiogroup"] > label div[data-testid="stMarkdownContainer"] p {{
    font-size: 1.65rem !important; 
    font-weight: 700 !important; 
    margin: 0 !important;
    text-align: center !important; 
    color: #2c3e50 !important;
}}
div.stRadio > div[role="radiogroup"] > label > div:first-child {{
    display: none !important;
}}
div.stRadio > div[role="radiogroup"] > label:hover {{
    transform: translateY(-8px) !important; 
    box-shadow: 0 12px 24px rgba(255, 179, 217, 0.6) !important;
    background-color: #fff0f5 !important;
}}
div.stRadio > div[role="radiogroup"] > label:focus-within {{
    background-color: #ffb3d9 !important;
    transform: scale(1.03) !important;
    border-color: #ff66b2 !important;
}}

/* PULSANTE "INVIA" A FORMA DI CUORE (NON CENTRATO E SENZA QUADRATI NATIVI) */
div.stButton {{
    display: block !important;
    width: 100% !important;
    background-color: transparent !important;
}}
div.stButton > button * {{
    background-color: transparent !important;
    box-shadow: none !important;
}}
div.stButton > button {{
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 20px 0 10px 0 !important; /* NON CENTRATO (Allineato a sinistra nativamente) */
    background-color: #ff66b2 !important;
    color: #ffffff !important;
    font-size: 1.4rem !important;
    font-weight: bold !important;
    width: 130px !important;
    height: 120px !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    
    border: none !important;
    border-radius: 0 !important; 
    box-shadow: none !important;
    outline: none !important;
    padding: 0 0 12px 0 !important;
    
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E") !important;
    -webkit-mask-size: 100% 100% !important;
    -webkit-mask-repeat: no-repeat !important;
    -webkit-mask-position: center !important;
    mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E") !important;
    mask-size: 100% 100% !important;
    mask-repeat: no-repeat !important;
    mask-position: center !important;
    
    filter: drop-shadow(0px 6px 8px rgba(255, 102, 178, 0.4)) !important;
}}
div.stButton > button:focus,
div.stButton > button:active {{
    box-shadow: none !important;
    outline: none !important;
    border: none !important;
    background-color: #ff007f !important;
    color: #ffffff !important;
}}
div.stButton > button:hover {{
    transform: translateY(-5px) scale(1.05) !important;
    background-color: #ff3399 !important;
    box-shadow: none !important; 
    filter: drop-shadow(0px 12px 15px rgba(255, 51, 153, 0.6)) !important;
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
        "opzioni": ["Avatar", "Zootropolis", "Jurassic World - La Rinascita", "Matrix"],
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
    
    st.markdown(
        """
        # Test di verifica per dimostrare di essere la mia sola e unica P eheh
        ---
        **Attenzione:** Accesso a un'area altamente riservata ai soli P.
        
        Per sbloccare il modulo successivo è necessario dimostrare di essere una vera P. Un errore comporterà UNA BELLA SGRIDATA!!!!
        ---
        *Sei pronta a dimostrare di essere la vera P?*
        """
    )
    
    if st.button("Pronta!"):
        st.session_state.fase_sistema = 'PLAYING'
        st.rerun()


elif st.session_state.fase_sistema == 'PLAYING':
    st.markdown(css_gioco, unsafe_allow_html=True)

    if st.session_state.current_index < len(quiz_data):
        q_data = quiz_data[st.session_state.current_index]
        
        st.write(f"### {q_data['domanda']}")
        
        scelta = st.radio("Seleziona la risposta:", q_data["opzioni"], index=None, label_visibility="collapsed")
        
        if st.button("Invia"):
            if scelta == q_data["risposta_corretta"]:
                st.success("SIIIIIIIIIII")
                st.session_state.current_index += 1
                
                if st.session_state.current_index == len(quiz_data):
                    st.session_state.fase_sistema = 'END'
                
                st.rerun()
            else:
                st.error(q_data["messaggio_err"])


elif st.session_state.fase_sistema == 'END':
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .cuore-cadente {
            position: fixed;
            top: -10%;
            z-index: 9999;
            user-select: none;
            animation-name: caduta-cuori;
            animation-timing-function: linear;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
        }
        @keyframes caduta-cuori {
            0% { transform: translateY(0vh) scale(1); opacity: 1; }
            100% { transform: translateY(110vh) scale(1.5); opacity: 0; }
        }
        </style>
        <div class="cuore-cadente" style="left: 5%; font-size: 25px; animation-duration: 4s; animation-delay: 0s;">🩷</div>
        <div class="cuore-cadente" style="left: 15%; font-size: 35px; animation-duration: 5s; animation-delay: 0.5s;">🩷</div>
        <div class="cuore-cadente" style="left: 25%; font-size: 20px; animation-duration: 3.5s; animation-delay: 1s;">🩷</div>
        <div class="cuore-cadente" style="left: 35%; font-size: 40px; animation-duration: 6s; animation-delay: 0.2s;">🩷</div>
        <div class="cuore-cadente" style="left: 45%; font-size: 30px; animation-duration: 4.5s; animation-delay: 1.5s;">🩷</div>
        <div class="cuore-cadente" style="left: 55%; font-size: 25px; animation-duration: 5.5s; animation-delay: 0.8s;">🩷</div>
        <div class="cuore-cadente" style="left: 65%; font-size: 35px; animation-duration: 4s; animation-delay: 2s;">🩷</div>
        <div class="cuore-cadente" style="left: 75%; font-size: 20px; animation-duration: 6.5s; animation-delay: 0.3s;">🩷</div>
        <div class="cuore-cadente" style="left: 85%; font-size: 40px; animation-duration: 4.2s; animation-delay: 1.2s;">🩷</div>
        <div class="cuore-cadente" style="left: 95%; font-size: 30px; animation-duration: 5.2s; animation-delay: 0.6s;">🩷</div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        # FINITOOOOO
        ---
        ### BRAVISSIMA P HAI FATTO TUTTO GIUSTOOOO
        ### SEI LA MIA PPP TI AMO DA MORIRE TI SUPER AMOOOOO
        
        Sei l'amore della mia vita ti amo dal primo giorno ed ogni giorno sempre di più, grazie di amarmi ogni giorno, sto benissimo con te, 
        non sono mai stato cosi bene nella mia vita, ogni volta che ti penso mi si scalda il cuore e mi manchi anche se sei accanto a me, 
        non perche non mi dimostri abbastanza amore ma perche so gia che, nel momento 
        in cui ci separiamo per tornare alle nostre case LONTANISSIME, non vedrò l'ora di rivederti.
        
        Amo tutto di te, sei la cosa più bella che mi sia mai successa. **TI AMO AMORE MIO** 🩷
        ---
        *Vuoi riavviare pure P? (Mi ricorderò se lo fai perché hai sbagliato qualcosaaa !!!)*
        """
    )
    
    if st.button("Riavvia P"):
        st.session_state.fase_sistema = 'INTRO'
        st.session_state.current_index = 0
        st.rerun()
