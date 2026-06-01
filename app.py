import streamlit as st

# Configurazione della pagina web (DEVE RIMANERE LA PRIMA RIGA)
st.set_page_config(page_title="Verifica Ufficiale per vedere se sei veramente la mia P", page_icon="PATA", layout="centered")

# 1. INIZIALIZZAZIONE DELLA MACCHINA A STATI
if 'fase_sistema' not in st.session_state:
    st.session_state.fase_sistema = 'INTRO'
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

# 2. DEFINIZIONE DEI FOGLI DI STILE (CSS DINAMICO)

# CSS per la schermata Iniziale e Finale (Sfumatura elegante)
css_intro = """
<style>
.stApp {
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
}
[data-testid="stMarkdownContainer"] {
    background-color: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
</style>
"""

# CSS per la fase di Gioco (Pattern cuori rosa)
css_gioco = """
<style>
.stApp {
    background-image: url("https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fit.freepik.com%2Fvettori-gratuito%2Ftema-di-san-valentino-con-cuori-rosa-su-sfondo-rosa_6507872.htm&ved=0CBYQjRxqFwoTCNif1orT5pQDFQAAAAAdAAAAABAF&opi=89978449");
}
[data-testid="stMarkdownContainer"] {
    background-color: rgba(255, 255, 255, 0.7);
    padding: 15px;
    border-radius: 10px;
}
</style>
"""

# 3. VETTORE DEI DATI (DOMANDE E PARAMETRI DI GIOCO)
quiz_data = [
    {
        "domanda": "Dove mi sono innamorato dei tuoi occhi per la prima volta?",
        "opzioni": ["Sul Treno", "Al Patù", "Al PN", "Alla Casina"],
        "risposta_corretta": "Sul Treno",
        "messaggio_err": "PATA HAI SBAGLIATO ??? OVVIO CHE MI SONO INNAMORATO DEI TUOI OCCHI BACIATI DAL SOLE SUL TRENO"
    }
    {
        "domanda": "Quale film stavamo guardando alla casina la prima volta ?",
        "opzioni": ["Jurassic World - La Rinascita", "Zootropolis", "Il Signore degli Anelli", "Matrix"],
        "risposta_corretta": "Jurassic World - La Rinascita",
        "messaggio_err": "E CON CHI ERI ALLORA ??? SEI LA MIA P"
    }
    {   "domanda": "Qual'era il numero del treno dove mi sono innamorato dei tuoi occhi per la prima volta ?",
        "opzioni": ["54632", "4137", "45097", "43439"],
        "risposta_corretta": "4137",
        "messaggio_err": "DAI LO PRENDIAMO TUTTI I GIORNIII, SEI TORNATA INDIETRO PER VEDERE LA SGRIDATA IO LO SO"
    }
    {   "domanda": "e e e e e e quanto mi ami ?",
        "opzioni": ["tanto", "tantissimo", "TANTISSIMOOOOO", "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP"],
        "risposta_corretta": "TANTISSIMO DA MORIREEEEE E PIU DI TE PPP",
        "messaggio_err": "NON SCRIVO NEANCHE NIENTE QUA SO CHE SEI TORNATA INDIETRO PER VEDERE EHEHEHEH"
    }
]

# --- ESECUZIONE DELLA LOGICA DI STATO ---

# STATO 0: SCHERMATA INIZIALE
if st.session_state.fase_sistema == 'INTRO':
    # Iniezione dello stile Intro
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.title("Test per essere la mia sola e unica P (lo sei gia hihihihihi)")
    st.write("---")
    st.markdown(
        """
        **Attenzione:** Accesso a un'area altamente riservata ai soli P.
        
        Per sbloccare il modulo successivo è necessario dimostrare di essere una vera P. Un errore comporterà 
        il blocco del terminale fino all'inserimento del parametro corretto (E UNA BELLA SGRIDATA!!!!).
        """
    )
    
    st.write("---")
    # Transizione di stato
    if st.button("Pronta a dimostrare di essere la vera P ?"):
        st.session_state.fase_sistema = 'Dimostra di essere la mia P'
        st.rerun()


# STATO 1: CICLO DOMANDE (LOGICA A SBARRAMENTO)
elif st.session_state.fase_sistema == 'PLAYING':
    # Iniezione dello stile Gioco (sovrascrive l'Intro nel DOM)
    st.markdown(css_gioco, unsafe_allow_html=True)
    
    st.title("Protocollo di Sicurezza")
    st.write("---")
    
    # Verifica esistenza matrici
    if st.session_state.current_index < len(quiz_data):
        q_data = quiz_data[st.session_state.current_index]
        
        st.subheader(f"Livello {st.session_state.current_index + 1} di {len(quiz_data)}")
        st.write(q_data["domanda"])
        
        scelta = st.radio("Selezionare il parametro corretto:", q_data["opzioni"], index=None)
        
        if st.button("Invia Dati"):
            if scelta == q_data["risposta_corretta"]:
                st.success("SIIIIIIIIIII")
                st.session_state.current_index += 1
                
                # Controllo di transizione allo stato finale
                if st.session_state.current_index == len(quiz_data):
                    st.session_state.fase_sistema = 'END'
                
                st.rerun()
            else:
                st.error(q_data["messaggio_err"])


# STATO 2: PAYLOAD FINALE
elif st.session_state.fase_sistema == 'END':
    # Re-iniezione dello stile Intro per conferire un tono formale alla conclusione
    st.markdown(css_intro, unsafe_allow_html=True)
    
    st.balloons()
    st.title("FINITOOOOO")
    st.write("---")
    st.write("BRAVISSIMA P HAI FATTO TUTTO GIUSTOOOO")
    st.write("SEI LA MIA PPP TI AMO DA MORIRE TI SUPER AMOOOOO")
    
    st.markdown(
        """
     Sei l'amore della mia vita ti amo dal primo giorno ed ogni giorno sempre di più, grazie di amarmi ogni giorno, sto benissimo con te, 
     non sono mai stato cosi bene nella mia vita, ogni volta che ti penso mi si scalda il cuore e mi manchi anche se sei accanto a me, 
     non perche non mi dimostri abbastanza amore ma perche so gia che, nel momento 
     in cui ci separiamo per tornare alle nostre case LONTANISSIME, non vedrò l'ora di rivederti.
     Amo tutto di te, sei la cosa più bella che mi sia mai successa. TI AMO AMORE MIO 
        """
    )
    
    st.write("---")
    # Riavvio globale
    if st.button("Riavvia pure P (mi ricorderò se lo fai perche hai sbagliato qualcosaaa !!!)"):
        st.session_state.fase_sistema = 'INTRO'
        st.session_state.current_index = 0
        st.rerun()
