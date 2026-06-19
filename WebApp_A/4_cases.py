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

# ======== UI: CASE SECTIONS (Conditional Rendering) ========

def display_case(case_name, title, text_body):
    """Render case content dynamically based on selected case parameters."""
    anchor_id = f"{case_name}-section"
    st.markdown(f"<div id='{anchor_id}'></div>", unsafe_allow_html=True)
    
    st.header(title)
    st.markdown(text_body, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Aufgabe")
    st.info("""
    Lesen Sie sich die Situation aufmerksam durch. Identifizieren und entwickeln Sie auf dieser Grundlage so viele vielversprechende Ideen und Chancen wie möglich, die zu Verbesserungen führen oder neue Möglichkeiten eröffnen könnten. Schreiben Sie jede Idee klar und verständlich auf. Es gibt keine feste Anzahl an Ideen. Versuchen Sie, innerhalb der vorgegebenen Zeit möglichst viele unterschiedliche Ideen zu entwickeln.
    """)

case_1_title = "Fall 1: Die digitale–haptische Lücke"
case_1_text = """In vielen Arbeits- und Lernumgebungen sind digitale Technologien wie Laptops, Tablets und Online-Kollaborationstools inzwischen fester Bestandteil des Alltags. Diese ermöglichen es, Informationen effizient zu speichern, zu organisieren und zu teilen. Gleichzeitig greifen viele Fachkräfte und Studierende weiterhin auf Papier und Stift zurück, insbesondere wenn sie Ideen entwickeln, Skizzen anfertigen oder Notizen machen.
<br><br>Einige Nutzerinnen und Nutzer berichten, dass digitale Werkzeuge das Gefühl des handschriftlichen Schreibens nicht vollständig ersetzen. Bei bestimmten Aufgaben kann das Tippen oder Schreiben auf einem Bildschirm weniger intuitiv wirken oder den Denkprozess unterbrechen. Daher wechseln viele Menschen während ihrer Arbeit zwischen handschriftlichen Notizen und digitalen Systemen.
<br><br>Dieses Wechseln zwischen physischen und digitalen Formaten kann zusätzliche Schritte im Arbeitsprozess verursachen. Beispielsweise müssen handschriftliche Notizen später in digitale Dokumente übertragen, separat abgelegt oder über andere Systeme mit anderen Personen geteilt werden.
<br><br>Trotz kontinuierlicher Weiterentwicklungen digitaler Geräte und Software kombinieren viele Menschen in ihrem Arbeitsalltag weiterhin physische und digitale Arbeitsweisen."""

case_2_title = "Fall 2: Freizeitangebot in einer Innenstadtlage"
case_2_text = """Eine seit vielen Jahren bestehende Freizeiteinrichtung befindet sich in einer zentralen Innenstadtlage. Ursprünglich wurde sie vor allem für lokale Familien und regelmäßige Besuchergruppen konzipiert, die das Angebot wöchentlich nutzten. Im Laufe der Zeit hat sich jedoch die Umgebung stark verändert: Neue Restaurants, Bars und andere Freizeitangebote ziehen inzwischen ein jüngeres und vielfältigeres Publikum an.
<br><br>Die Einrichtung verfügt über eine größere Innenfläche mit verschiedenen Freizeitmöglichkeiten sowie einem kleinen Bereich für Speisen und Getränke. Ein Großteil der Einrichtung sowie viele Abläufe haben sich über die Jahre kaum verändert. Obwohl es weiterhin einige treue Stammgäste gibt, sind Besucherzahlen und Besuchsmuster insgesamt weniger vorhersehbar geworden.
<br><br>Der Betrieb wird von einem kleinen Team geführt, das sich um den täglichen Ablauf, den Kundenkontakt, die Wartung der Anlagen und grundlegende Marketingaktivitäten kümmert. Einige Gäste besuchen die Einrichtung gezielt wegen des Freizeitangebots, während andere sie eher als Teil eines größeren Freizeitprogramms in der Umgebung betrachten.
<br><br>Gleichzeitig hat sich die Auswahl an Freizeitmöglichkeiten in der Stadt deutlich erweitert. Menschen können heute zwischen vielen verschiedenen Aktivitäten wählen, wenn sie entscheiden, wie sie ihre Freizeit verbringen möchten."""

if st.session_state.case_selected == "case_1":
    display_case("case_1", case_1_title, case_1_text)
elif st.session_state.case_selected == "case_2":
    display_case("case_2", case_2_title, case_2_text)

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
