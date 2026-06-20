import streamlit as st
import streamlit.components.v1 as components
import datetime

# ======== CUSTOM CSS ========
st.markdown("""
<style>
    /* 1) Adjust the sizes of the header logos and remove rounding */
    [data-testid="column"] [data-testid="stImage"] img,
    [data-testid="stColumn"] [data-testid="stImage"] img {
        max-height: 50px;
        max-width: 100%;
        width: auto;
        height: auto;
        border-radius: 0 !important;
    }
    
    /* Improve padding of the main container and make it wider */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 95% !important;
    }
    
    /* ---------------------------------------------------------------------
       2) BUTTON STYLING
       --------------------------------------------------------------------- */
    div.stButton > button {
        background-color: #00C1D4 !important; /* TUHH Turquoise */
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        transition: background-color 0.3s;
        height: 50px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
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
        font-size: 18px !important;
        font-weight: 600 !important;
        color: white !important;
        margin: 0;
    }
    
    /* ---------------------------------------------------------------------
       3) FRAMEWORK SPACES STYLING
       --------------------------------------------------------------------- */
    .framework-space {
        background-color: rgba(0, 193, 212, 0.1); 
        border: 2px solid #00C1D4;
        border-radius: 12px;
        padding: 15px;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .space-title {
        text-align: center;
        color: #00C1D4;
        font-weight: bold;
        font-size: 22px;
        margin-bottom: 5px;
        cursor: pointer;
        transition: color 0.2s;
        text-decoration: underline;
        text-decoration-color: transparent;
    }
    .space-title:hover {
        color: #009fb0;
        text-decoration-color: #009fb0;
    }
    
    .entries-container {
        flex-grow: 1;
        overflow-y: auto;
        margin-bottom: 15px;
        min-height: 250px;
        max-height: 400px;
        padding-right: 5px;
    }
    
    .entry-bubble {
        background-color: white;
        border-left: 4px solid #00C1D4;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ======== HEADER ========
col_title, col_logo1, col_logo2 = st.columns([2, 1, 1.2])

with col_title:
    st.title("Ohne das Framework")

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
    st.session_state.experiment_data = {"type": "Einzelteilnahme"} 

participation_type = st.session_state.experiment_data.get("type", "Einzelteilnahme")

if "selected_method" not in st.session_state:
    st.session_state.selected_method = None
    
if "show_ideation" not in st.session_state:
    st.session_state.show_ideation = False
    
if "confirm_submit" not in st.session_state:
    st.session_state.confirm_submit = False

# Workspace Initialization
if "ohne_problem_entries" not in st.session_state:
    st.session_state.ohne_problem_entries = []
if "ohne_knowledge_entries" not in st.session_state:
    st.session_state.ohne_knowledge_entries = []
if "ohne_ideation_entries" not in st.session_state:
    st.session_state.ohne_ideation_entries = []

if "ohne_p_input_box" not in st.session_state:
    st.session_state.ohne_p_input_box = ""
if "ohne_k_input_box" not in st.session_state:
    st.session_state.ohne_k_input_box = ""
if "ohne_i_input_box" not in st.session_state:
    st.session_state.ohne_i_input_box = ""

if "show_info_box" not in st.session_state:
    st.session_state.show_info_box = False

if "step" not in st.session_state:
    st.session_state.step = 5

# ======== 1. AUTO METHOD SELECTION & EXPLANATION ========
st.session_state.selected_method = "Brainstorming"
explanation_text = """**Brainstorming** ist eine Kreativitätstechnnik zur schnellen Ideengenerierung. Für dieses Experiment gilt:

- **Zielgerichtete Quantität vor Qualität:** Generieren Sie so viele Ansätze wie möglich, aber behalten Sie das Ziel im Auge. Die Ideen müssen nicht perfekt ausgearbeitet sein, sollten aber einen logischen und **realistischen Bezug** zum Fallbeispiel haben.
    
- **Fokus auf das Generieren:** Die Bewertung der Ansätze erfolgt erst später.
    
- **Mehr als nur Ideen:** Nutzen Sie die Methode in den drei Spaces gezielt, um Herausforderungen zu definieren, Wissen zu sammeln und konkrete **Geschäftsmöglichkeiten (Opportunities)** zu formulieren."""

st.divider()
st.markdown("<div id='method-explanation-section'></div>", unsafe_allow_html=True)
st.subheader(f"{st.session_state.selected_method}")
st.info(explanation_text)
st.markdown("<br>", unsafe_allow_html=True)

if not st.session_state.show_info_box:
    _, btn_col_fort, _ = st.columns([1, 1, 1])
    with btn_col_fort:
        if st.button("Fortfahren", use_container_width=True):
            st.session_state.show_info_box = True
            st.rerun()

if st.session_state.show_info_box:
    st.info("""
    **Hinweise zur Nutzung mit "Ohne Framework":** 

    Hier ist die Nutzung der KI **nicht** erlaubt. Es können, aber gerne Impulse aus dem Netz hinzugezogen werden.
    """, icon="ℹ️")
    st.markdown("<br>", unsafe_allow_html=True)

    # ======== 2. CONTINUE TO IDEA INPUT ========
    if not st.session_state.show_ideation:
        _, btn_col, _ = st.columns([1, 1, 1])
        with btn_col:
            if st.button("Weiter zu Ihrem Arbeitsbereich", use_container_width=True):
                st.session_state.show_ideation = True
                st.rerun()

if not st.session_state.show_ideation:
    components.html(
        """
        <script>
        const anchor = window.parent.document.getElementById('method-explanation-section');
        if (anchor) {
            anchor.scrollIntoView({behavior: 'smooth', block: 'start'});
        }
        </script>
        """,
        height=0
    )

# ======== 4. THREE FRAMEWORK SPACES (MATCHING MIT-FRAMEWORK) ========
if st.session_state.show_ideation:
    st.divider()
    st.markdown("<div id='idea-input-section'></div>", unsafe_allow_html=True)
    
    st.subheader("Ihr Arbeitsbereich")
    
    def add_p():
        val = st.session_state.ohne_p_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "problem",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.selected_method
            }
            st.session_state.ohne_problem_entries.append(entry)
        st.session_state.ohne_p_input_box = ""

    def add_k():
        val = st.session_state.ohne_k_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "knowledge",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.selected_method
            }
            st.session_state.ohne_knowledge_entries.append(entry)
        st.session_state.ohne_k_input_box = ""

    def add_i():
        val = st.session_state.ohne_i_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "ideation",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.selected_method,
                "idea_id": len(st.session_state.ohne_ideation_entries) + 1
            }
            st.session_state.ohne_ideation_entries.append(entry)
        st.session_state.ohne_i_input_box = ""

    # Create the 3 equal columns layout
    col_prob, col_know, col_idea = st.columns(3)

    # -----------------------------
    # 4.1 PROBLEM SPACE
    # -----------------------------
    
    with col_prob:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        with st.popover("🧠 Problem Space", width='stretch'):
            st.info("Beschreibe die aktuelle Herauforderung oder das Problem. Wie sieht die aktuelle Lage aus?")
            
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for entry in st.session_state.ohne_problem_entries:
            st.markdown(f'<div class="entry-bubble">{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.text_area("Herausforderungen notieren...", key="ohne_p_input_box", height=100)
        st.button(" ", icon=":material/send:", key="btn_p", use_container_width=True, on_click=add_p)
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # 4.2 KNOWLEDGE SPACE
    # -----------------------------

    with col_know:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        with st.popover("📚 Knowledge Space", width='stretch'):
            st.info("Sammle hier Impulse wie Fakten, Trends oder Analogien aus anderen bzw. dir bekannten Bereichen. Was könnte helfen, neue Möglichkeiten zu entdecken?")
            
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for entry in st.session_state.ohne_knowledge_entries:
            st.markdown(f'<div class="entry-bubble">{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.text_area("Impulse hinzufügen...", key="ohne_k_input_box", height=100)
        st.button(" ", icon=":material/send:", key="btn_k", use_container_width=True, on_click=add_k)
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # 4.3 IDEATION SPACE
    # -----------------------------

    with col_idea:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        with st.popover("💡 Ideation Space", width='stretch'):
            st.info("Formuliere hier erste Lösungsansätze bzw. Möglichkeiten, die du anhand deiner Impulse für identifizieren konntest. Es gibt keine richtige oder falsche Antwort, wichtig ist, das Denken anzuregen!")
            
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for idx, entry in enumerate(st.session_state.ohne_ideation_entries):
            st.markdown(f'<div class="entry-bubble"><b>Ansatz {idx+1}:</b><br>{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.text_area("Lösungsansätze festhalten...", key="ohne_i_input_box", height=100)
        st.button(" ", icon=":material/send:", key="btn_i", use_container_width=True, on_click=add_i)
        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("<br><hr>", unsafe_allow_html=True)
    
    # ======== 5. FINAL SUBMISSION LOGIC ========
    valid_submit = (len(st.session_state.ohne_problem_entries) > 0 or 
                   len(st.session_state.ohne_knowledge_entries) > 0 or 
                   len(st.session_state.ohne_ideation_entries) > 0)
                   
    if not st.session_state.confirm_submit:
        _, sub_col, _ = st.columns([1, 1, 1])
        with sub_col:
            if st.button("Absenden", use_container_width=True, disabled=not valid_submit):
                st.session_state.confirm_submit = True
                st.rerun()
    else:
        st.warning("Möchten Sie Ihre Eingaben wirklich absenden?", icon="❓")
        
        conf_col1, conf_col2 = st.columns(2)
        with conf_col1:
            if st.button("Zurück Bearbeiten", use_container_width=True):
                st.session_state.confirm_submit = False
                st.rerun()
                
        with conf_col2:
            if st.button("Endgültig Absenden", use_container_width=True):
                st.session_state.experiment_data["selected_method"] = st.session_state.selected_method
                st.session_state.experiment_data["ohne_problem_entries"] = list(st.session_state.ohne_problem_entries)
                st.session_state.experiment_data["ohne_knowledge_entries"] = list(st.session_state.ohne_knowledge_entries)
                st.session_state.experiment_data["ohne_ideation_entries"] = list(st.session_state.ohne_ideation_entries)
                
                # Increment rounds counter
                st.session_state.completed_rounds = st.session_state.get("completed_rounds", 0) + 1
                
                # Route step dynamically
                if st.session_state.completed_rounds >= 2:
                    st.session_state.step = 8
                else:
                    st.session_state.step = 6
                
                st.session_state.show_ideation = False
                st.session_state.confirm_submit = False
                
                st.session_state.ohne_problem_entries = []
                st.session_state.ohne_knowledge_entries = []
                st.session_state.ohne_ideation_entries = []
                
                st.rerun()
                
    if not st.session_state.confirm_submit:
        components.html(
            """
            <script>
            const anchor = window.parent.document.getElementById('idea-input-section');
            if (anchor) {
                anchor.scrollIntoView({behavior: 'smooth', block: 'start'});
            }
            </script>
            """,
            height=0
        )