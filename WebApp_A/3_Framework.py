import streamlit as st
import streamlit.components.v1 as components

# Scroll parent window to top on load
components.html(
    """
    <script>
    window.parent.scrollTo(0, 0);
    </script>
    """,
    height=0
)

# ======== CUSTOM CSS ========
st.markdown("""
<style>
    /* 1) Header Images fixes from previous pages (removes default rounding) */
    [data-testid="column"] [data-testid="stImage"] img,
    [data-testid="stColumn"] [data-testid="stImage"] img {
        border-radius: 0 !important;
        max-height: 80px;
        width: auto;
    }
    
    /* Improve padding of the main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* 2) BUTTON STYLING */
    div.stButton > button {
        background-color: #00C1D4 !important; /* TUHH Turquoise */
        color: white !important;
        height: 80px !important;
        width: 100% !important;
        border-radius: 12px !important;
        border: none !important;
        transition: background-color 0.3s;
    }
    div.stButton > button:hover {
        background-color: #009fb0 !important;
        color: white !important;
    }
    div.stButton > button:active {
        background-color: #008291 !important;
        color: white !important;
    }
    
    div.stButton > button p {
        font-size: 22px !important;
        font-weight: 600 !important;
        color: white !important;
        margin: 0;
    }
    
    .placeholder-box {
        background-color: #f0f2f6;
        border: 2px dashed #cccccc;
        border-radius: 10px;
        padding: 50px;
        text-align: center;
        color: #555555;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ======== HEADER ========
col_title, col_logo1, col_logo2 = st.columns([2.5, 1, 1])

with col_title:
    st.title("Das Framework")

with col_logo1:
    try:
        st.image("img/Entre.svg", use_container_width=True)
    except:
        pass

with col_logo2:
    try:
        st.image("img/TUHH_logo_rgb.svg", use_container_width=True)
    except:
        pass

st.divider()

# Ensure step is tracked
if "step" not in st.session_state:
    st.session_state.step = 3

# ======== CONTENT PLACHOLDERS ========

# Image Framework - a simple version
try:
    st.image("img/Framework_simple.jpg", width='stretch')
except Exception as e:
    st.error(f"Fehler beim Laden des Bildes: {e}")

# Text Body Placeholder
## st.info("""Hier ist eine vereinfachte Version meines Frameworks. Das Framework beschreibt einen Prozess in denen Sie arbeiten werden. Es ist in drei "Spaces" aufgeteilt:""")

st.info("""Hier ist eine einfache Version meines Frameworks. Für Sie ist aktuell nur der **farblich markierte Bereich (Phase 1: Divergenz)** wichtig. Das Framework beschreibt den Prozess, in dem Sie gleich arbeiten werden. Es ist in drei "Spaces" aufgeteilt:

- **Problem Space (Der IST-Zustand):** Halten Sie hier die aktuelle Herausforderung im Ganzen fest. Welchen Bedingungen und Einschränkungen (engl. Constraints) unterliegt die Situation? Es geht darum, das zugrundeliegende Problem tiefgehend zu verstehen und zu dokumentieren, wie die Situation jetzt aussieht.

- **Knowledge Space (Der SOLL-Zustand & Impulse):** Nutzen Sie diesen Bereich (und die Unterstützung der KI), um erste Impulse, Trends und externes Wissen zu sammeln. Was passiert da draußen auf dem Markt? Hier findet das sogenannte „Problem-Seeking“ statt: Sie definieren, wie ein idealer Zustand aussehen könnte und welche ersten theoretischen Möglichkeiten sich unter den erkannten Bedingungen des Problem Spaces ergeben.

- **Ideation Space (Die Lösungsmöglichkeiten):** Hier geht es an die konkrete Ausformulierung von Lösungsansätzen (engl. "Solution-Seeking"). Nehmen Sie die im Knowledge Space angesetzten Ansätze und arbeiten Sie diese zu vollständigen, realistischen Geschäfts- und Lösungsmöglichkeiten aus. Dieser Bereich bildet das Fundament für die spätere Evaluierung in Phase 2. Es gibt hier kein „Richtig“ oder „Falsch“, sondern nur das Ziel, das Denken anzuregen und Ihre Gedanken so detailliert wie möglich auszuschreiben.""")
    

st.markdown("<br><br>", unsafe_allow_html=True)

# ======== NAVIGATION ========
_, btn_col, _ = st.columns([1, 1, 1])

with btn_col:
    if st.button("Weiter zu den Cases", use_container_width=True):
        st.session_state.step = 4
        st.rerun()