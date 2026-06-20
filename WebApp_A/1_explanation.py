# streamlit run explantation.py
import streamlit as st

# ======== PAGE CONFIG ========
# st.set_page_config(
#     page_title="Experiment",
#     page_icon="🧪",
#     layout="wide"
# )

# Asjusting the sizes of the images
st.markdown("""
<style>
    /* Reduce logo sizes by limiting their maximum height */
    [data-testid="stImage"] img {
        max-height: 80px;
        width: auto;
    }
</style>
""", unsafe_allow_html=True)

# ======== CUSTOM CSS ========
# Usage of custom CSS to override Streamlit's default image styling
# which adds border-radius (rounded corners) to images.
# Adjustments for a better look.
st.markdown("""
<style>
    /* Remove rounding from images */
    [data-testid="stImage"] img {
        border-radius: 0 !important;
    }
    
    /* Improve padding of the main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Optional: Style the primary button to be more prominent */
    .stButton > button[data-baseweb="button"] {
        font-weight: bold;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ======== HEADER ========
# We define three columns. The title goes to the left, and logos to the right.
col_title, col_logo1, col_logo2 = st.columns([2.5, 1, 1])

with col_title:
    st.title("Willkommen zum Experiment")

with col_logo1:
    st.image("img/Entre.svg", use_container_width=True)

with col_logo2:
    st.image("img/TUHH_logo_rgb.svg", use_container_width=True)

st.divider()

# ======== SECTION 1: Das Experiment ========
st.subheader("Das Experiment")

st.markdown("""
Das folgende Experiment ist Teil einer Masterarbeit und untersucht, wie Kreativitätsmethoden (engl. *Creative Workflow Methods (CWM)*) durch den Einsatz von **Künstlicher Intelligenz (KI)** unterstützt werden können. Hierzu wurde ein einfaches Framework entwickelt. 
""")

# Use columns for a nicer layout
col_text, col_times = st.columns([2, 1])

with col_text:
    st.markdown("""
    **Im Verlauf des Experiments werden Sie:** 
    - Zwei Fallbeispiele bearbeiten (mit/ohne Framework) 
    - Eine CWM anwenden
    - Mit ChatGPT arbeiten
    """)

with col_times:
    # Use info box or metrics to make it look professional
    st.info("**Geschätzte Dauer:**\n\n"
            "**Lesezeit:** 15 Min\n\n"
            "👤**Bearbeitungszeit:** 30 min", icon="⏱️")

st.info("""
**Vorgehen bei KI-Unterstützung:**
In einer der Durchführungen werden Sie **ChatGPT** als KI-Unterstützung nutzen. Dafür öffnen Sie ChatGPT in einem separaten Tab und arbeiten dort mit einem vorbereiteten Chat. Letztlich müssen alle Ergebnisse zurück in diese Anwendung übertragen werden.
""", icon="ℹ️")

st.divider()

# ======== SECTION 2: Datenschutz ========
st.subheader("🔒 Datenschutz") 

st.markdown(""" 
Ihre Angaben werden **vertraulich behandelt** und **ausschließlich zu wissenschaftlichen Zwecken** verwendet. 
Die Daten werden **anonymisiert gespeichert** und **nicht** an Dritte weitergegeben.
""")

st.markdown("""
**Für dieses Experiment werden folgende Daten erfasst:** 
- Name, Alter, Beruf
- Ihre Ergebnisse
- Feedback (Abschließend wird es ein kurzes Interview geben.)
""")

st.warning("""
**Hinweis zu ChatGPT:** Bei der Nutzung von ChatGPT gelten die Datenschutzbedingungen des jeweiligen Anbieters. Bitte geben Sie dort keine sensiblen personenbezogenen Daten ein.
""", icon="⚠️")

st.divider()

# ======== SECTION 3: Einverständniserklärung ========
st.subheader("Einverständniserklärung")

st.markdown('Durch das Anklicken des **Akzeptieren & Fortfahren**-Buttons erklären Sie sich mit der anonymisierten Verarbeitung Ihrer Angaben im Rahmen dieses Experiments einverstanden.')

st.write("") # small spacer

# To make the button look prominent, we can use columns to center it
_, col_btn, _ = st.columns([1, 2, 1])

with col_btn:
    # type="primary" makes the button red/pink or blue (Streamlit theme color)
    if st.button("Akzeptieren & Fortfahren", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

 