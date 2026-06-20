# pyrefly: ignore [missing-import]
import streamlit as st 
import streamlit.components.v1 as components
import random

# Strict check: if 2 rounds completed, skip case selection entirely and route to step 8 (final page)
if st.session_state.get("completed_rounds", 0) >= 2:
    st.session_state.step = 8
    st.rerun()

# ======== CUSTOM CSS ========
st.markdown("""
<style>
    /* 1) Header Images fixes from previous pages (removes default rounding) */
    [data-testid="stImage"] img {
        border-radius: 0 !important;
        max-height: 80px;
        max-width: 100%;
        width: auto;
        height: auto;
    }
    
    /* Improve padding of the main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* 2) BUTTON STYLING (Case Buttons & Weiter Buttons) */
    div.stButton > button {
        background-color: #00C1D4 !important; /* TUHH Turquoise */
        color: white !important;
        height: 100px !important;
        width: 95% !important;
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
    
    /* Disabled button style */
    div.stButton > button:disabled, 
    div.stButton > button:disabled:hover {
        background-color: #d3d3d3 !important;
        color: #8c8c8c !important;
        cursor: not-allowed !important;
    }
</style>
""", unsafe_allow_html=True)

# ======== HEADER ========
col_title, col_logo1, col_logo2 = st.columns([2, 1, 1.2])

with col_title:
    st.title("Mini Case Studies")

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

# ======== SESSION STATE INITIALIZATION ========
if "experiment_data" not in st.session_state:
    st.session_state.experiment_data = {}

if "round_1_case" not in st.session_state:
    st.session_state.round_1_case = random.choice(["case_1", "case_2"])
    st.session_state.round_2_case = "case_2" if st.session_state.round_1_case == "case_1" else "case_1"

# Detect mapping round
is_round_two = st.session_state.get("step", 4) == 6

if not is_round_two:
    st.session_state.case_selected = st.session_state.round_1_case
else:
    st.session_state.case_selected = st.session_state.round_2_case

st.info("Der Fall wurde automatisch für Sie ausgewählt.")
st.markdown("<br><br>", unsafe_allow_html=True)

# ======== CONFIGURATION FOR CASES ========
# Place for "Aktuelle Situation" information, bullet points below:
case_1_info = [
    "Revolutionäre “Flux”-Technologie mit 50ms Latenz (Industriestandard: 100-120ms)",  
    """Drei potenzielle Zielgruppen:
        \n  **Kreative Berufe** (Designer, Architekten)
        \n  **Büro-Angestellte** (Ingenieure, Berater, Anwälte)
        \n  **Universitäten** (Studenten)""",    
    """Markt-Kontext: 
        \n  **Andere digitale Schreiblösungen** existieren bereits am Markt
        \n  **Papier und Stift** bleiben universell verfügbar und kostengünstig
        \n  **Digitale Transformation** verändert Arbeitsweisen in allen Branchen"""
]  

case_2_info = [
    "16 Bowlingbahnen auf 1.000 m² in der Innenstadt",  
    "Kundenstamm: hauptsächlich Liga-Bowler (Durchschnittsalter 65) und Familien mit Kindern",  
    "Begrenztes Speisenangebot: einfache Pizza, Bier und Softdrinks",
    "Veraltete Einrichtung im 1970er-80er Jahre Stil",  
    "Konkurrenz durch andere Unterhaltungsoptionen, nicht nur andere Bowlingbahnen",  
    "Standort im schnell wachsenden Raleigh (46% Bevölkerungswachstum 2000-2010, Durchschnittsalter 31,9)",
    "47% der Einwohner haben Hochschulabschluss, viele junge Fachkräfte in Tech/Life Sciences"   
]

# Task:
case_1_task = """**Aufgabe**: 
\n Papier und Stift kosten fast nichts, funktionieren überall ohne Akku und sind seit Jahrhunderten bewährt. Wie überzeugt man Menschen, diese Gewohnheit aufzugeben? 
\n Entwickeln Sie mit dem Framework eine Markteintrittsstrategie für reMarkable: Welches Kundensegment sollte priorisiert werden, oder sehen Sie andere innovative Wege, den digitalen Schreibmarkt zu revolutionieren?"""

case_2_task = """**Aufgabe:** 
\n Nutzen Sie das Framework, um strategische Chancen zu identifizieren, die die neue Geschäftsführung verfolgen sollte, um Westlake Lanes in ein florierendes Unternehmen zu verwandeln, das den sich wandelnden demografischen Gegebenheiten der Innenstadt von Raleigh gerecht wird"""

# ======== UI: CASE SECTIONS (Conditional Rendering) ========

def display_case(case_name, title, text_body, info_list, task_text):
    """Render case content dynamically based on selected case parameters."""
    anchor_id = f"{case_name}-section"
    st.markdown(f"<div id='{anchor_id}'></div>", unsafe_allow_html=True)
    
    st.header(title)
    st.markdown(text_body, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Update 1: Add "Aktuelle Situation" Section (Apply to Both Cases)
    st.subheader("Aktuelle Situation")
    for info in info_list:
        st.markdown(f"- {info}")
    st.markdown("<br>", unsafe_allow_html=True)

    # Update 2: Dynamic, Case-Specific Tasks
    st.subheader("Aufgabe")
    st.info(task_text)

case_1_title = "Fall 1: remarkeable"
case_1_text = """Das norwegische Startup reMarkable hat mit seiner revolutionären Technologie "Flux" das sogenannte “Slow-Ink-Problem” gelöst, das viele kennen: Wenn man mit einem digitalen Stift auf einem Tablet schreibt, erscheint die Schrift erst mit Verzögerung auf dem Bildschirm. Diese Verzögerung macht digitales Schreiben frustrierend und unnatürlich. reMarkable hat diese Verzögerung von 120 Millisekunden (etwa ein Achtel einer Sekunde) auf nur 50 Millisekunden reduziert und das ist so schnell, dass es sich wie echtes Papier anfühlt.
<br><br>Das Unternehmen hat bereits einen wichtigen Partner gefunden: E-Ink, die Firma, die die Bildschirme für E-Book-Reader wie den Kindle herstellt. E-Ink wird die speziellen Bildschirme für reMarkable produzieren. Jetzt steht das Unternehmen vor einer wichtigen Entscheidung: An wen soll es sein Produkt verkaufen? Die Marktforschung hat drei verschiedene Kundengruppen identifiziert (Kreative Berufe, Büroangestellte und Studenten), die alle unterschiedliche Bedürfnisse und Budgets haben. Mit begrenzten Ressourcen und Personal muss reMarkable entscheiden, ob es sich auf eine Gruppe konzentriert oder versucht, alle gleichzeitig zu erreichen."""

case_2_title = "Fall 2: Westlake Lanes"
case_2_text = """Westlake Lanes is eine Bowlingbahn mit 16 Bahnen in der Innenstadt von Raleigh, North Carolina. Das Unternehmen wurde in den 1970er Jahren gegründet und war jahrzehntelang profitabel. Seit 2004 sind die Einnahmen jedoch um über 40% gesunken, während die Betriebskosten kontinuierlich gestiegen sind. Das Unternehmen benötigte 2008 eine Notfinanzierung von 100.000 Dollar, um den Betrieb aufrechtzuerhalten.
<br><br>Eine neue Geschäftsführung hat durch Kostensenkungsmaßnahmen den ersten profitablen Monat seit zwei Jahren erreicht. Mit veränderten Marktbedingungen steht das Unternehmen vor grundlegenden Herausforderungen und Westlake braucht noch größere Veränderungen für einen nachhaltigen Erfolg."""

if st.session_state.case_selected == "case_1":
    display_case("case_1", case_1_title, case_1_text, case_1_info, case_1_task)
elif st.session_state.case_selected == "case_2":
    display_case("case_2", case_2_title, case_2_text, case_2_info, case_2_task)

st.markdown("<br>", unsafe_allow_html=True)

# Navigation buttons section
left, right = st.columns([1.5, 1])
with right:
    if not is_round_two:
        # Stacked buttons in Round 1
        if st.button("Weiter MIT Framework", key="btn_mit_fw_r1", use_container_width=True):
            st.session_state.round_1_condition = "MIT"
            st.session_state.experiment_data["first_case"] = st.session_state.case_selected
            st.session_state.step = 5
            st.rerun()
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        if st.button("Weiter OHNE Framework", key="btn_ohne_fw_r1", use_container_width=True):
            st.session_state.round_1_condition = "OHNE"
            st.session_state.experiment_data["first_case"] = st.session_state.case_selected
            st.session_state.step = 5
            st.rerun()
    else:
        # Single button in Round 2 (opposite of Round 1 choice)
        if st.session_state.get("round_1_condition") == "MIT":
            if st.button("Weiter OHNE Framework", key="btn_ohne_fw_r2", use_container_width=True):
                st.session_state.experiment_data["second_case"] = st.session_state.case_selected
                st.session_state.step = 7
                st.rerun()
        else:
            if st.button("Weiter MIT Framework", key="btn_mit_fw_r2", use_container_width=True):
                st.session_state.experiment_data["second_case"] = st.session_state.case_selected
                st.session_state.step = 7
                st.rerun()

# Auto-scroll JavaScript
components.html(
    f"""
    <script>
    const anchor = window.parent.document.getElementById('{st.session_state.case_selected}-section');
    if (anchor) {{
        anchor.scrollIntoView({{behavior: 'smooth', block: 'start'}});
    }}
    </script>
    """,
    height=0
)
