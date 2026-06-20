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
       Adjust spacing, width, and look of primary buttons
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
       Create Turquoise boxes for the 3 distinct areas.
       --------------------------------------------------------------------- */
    .framework-space {
        background-color: rgba(0, 193, 212, 0.1); /* Light turquoise background */
        border: 2px solid #00C1D4;
        border-radius: 12px;
        padding: 15px;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    /* Style for the titles to look clickable */
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
    
    /* Scrollable area for entries */
    .entries-container {
        flex-grow: 1;
        overflow-y: auto;
        margin-bottom: 15px;
        min-height: 250px;
        max-height: 400px;
        padding-right: 5px;
    }
    
    /* Individual entry styling */
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
    st.title("Mit Framework")

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

# ======== PROMPT TEMPLATES CONFIGURATION ========
# USER: You can replace the placeholder text strings for your prompts here.
# There are 5 prompts for each of the three spaces (Problem Space, Knowledge Space, Ideation Space).
# Streamlit's st.code component will display these prompts, allowing participants to copy them with one click.
PROMPTS_CONFIG = {
    "problem_space": [
        # PROMPT MENU OF PROBLEM SPACE:
        "Hinterfrage meine Annahmen: Sind meine gegebenen Bedingungen und der Fokus realistisch für diese Situation?",

        "Vertiefe das Problem: Welche tieferliegenden Aspekte habe ich bei dem Problem noch nicht berücksichtigt?",
        
        "Bringe andere Perspektiven ein: Wie würden andere Stakeholder oder Experten das Problem betrachten?",

        "Hinterfrage meine Annahmen: Sind meine gesetzten Ziele und der Fokus realistisch für diese Situation?",

        "Analysiere die aktuelle Situation mit deinen eigenen Beobachtungen.",
    ],
    "knowledge_space": [
        # PROMPT MENU OF KNOWLEDGE SPACE:
        "Fasse Synergien zusammen: Wie lassen sich meine Gedanken zu einem Konzept kombinieren?",

        "Hinterfrage meine Sichtweise und gebe mir alternative Perspektiven, die es zu diesem Thema gibt.",

        "Identifiziere Vorbilder: Wie gehen andere Organisationen in ähnlichen Situationen um?",
  
        "Gib mir neue Impulse: Welche kreativen Ansätze aus anderen Bereichen könnten hier helfen?",
    
        "Prüfe welche Annahmen bereits durch Daten gestützt sind.",
    ],
    "ideation_space": [
        # PROMPT MENU OF IDEATION SPACE:
        "Entwickle drei mögliche Chancen aus dieser Einschränkung.",
   
        "Wie kann ich meine Gedanken aus z.B. dem Knowledge Space weiter ausbauen, um einen präziseren Ansatz zu formulieren?",

        "Entwickle eine neue Möglichkeit, indem du zwei bestehende Elemente kombinierst.",
     
        "Entwickle eine Veränderung des Falls, die eine bessere Nutzung erlaubt.",
  
        "Entwickle einen ersten Ansatz, den ich dann weiter ausarbeiten kann.",
    ]
}

def render_prompt_menu(space_key):
    """
    Renders an st.expander labeled 'Promptmenü' containing the 5 copyable prompts
    using st.code(..., language=None) for one-click copy capability.
    """
    with st.expander("Promptmenü"):
        for i, prompt_text in enumerate(PROMPTS_CONFIG[space_key], 1):
            st.markdown(f"**Prompt {i}**")
            st.code(prompt_text, language=None)

# ======== SESSION STATE INITIALIZATION ========
# 1. Fallback for standalone testing
if "experiment_data" not in st.session_state:
    st.session_state.experiment_data = {"type": "Einzelteilnahme"} 
    
participation_type = st.session_state.experiment_data.get("type", "Einzelteilnahme")

# 2. Page Navigation States
if "fm_selected_method" not in st.session_state:
    st.session_state.fm_selected_method = None
if "fm_method_understood" not in st.session_state:
    st.session_state.fm_method_understood = False
if "fm_show_info_box" not in st.session_state:
    st.session_state.fm_show_info_box = False
if "fm_framework_understood" not in st.session_state:
    st.session_state.fm_framework_understood = False
if "fm_scroll_to_spaces" not in st.session_state:
    st.session_state.fm_scroll_to_spaces = False

# 3. Space Data Storage
if "fm_problem_entries" not in st.session_state:
    st.session_state.fm_problem_entries = []
if "fm_knowledge_entries" not in st.session_state:
    st.session_state.fm_knowledge_entries = []
if "fm_ideation_entries" not in st.session_state:
    st.session_state.fm_ideation_entries = []

# 4. Input Tracking via string 
if "fm_p_input_box" not in st.session_state:
    st.session_state.fm_p_input_box = ""
if "fm_k_input_box" not in st.session_state:
    st.session_state.fm_k_input_box = ""
if "fm_i_input_box" not in st.session_state:
    st.session_state.fm_i_input_box = ""

# 5. Final Submission
if "fm_confirm_submit" not in st.session_state:
    st.session_state.fm_confirm_submit = False

# ======== 1. AUTO METHOD SELECTION & EXPLANATION ========
st.session_state.fm_selected_method = "Brainstorming"
explanation_text = """**Brainstorming** ist eine Kreativitätstechnnik zur schnellen Ideengenerierung. Für dieses Experiment gilt:

- **Zielgerichtete Quantität vor Qualität:** Generieren Sie so viele Ansätze wie möglich, aber behalten Sie das Ziel im Auge. Die Ideen müssen nicht perfekt ausgearbeitet sein, sollten aber einen logischen und **realistischen Bezug** zum Fallbeispiel haben.
    
- **Fokus auf das Generieren:** Die Bewertung der Ansätze erfolgt erst später.
    
- **Mehr als nur Ideen:** Nutzen Sie die Methode in den drei Spaces gezielt, um Herausforderungen zu definieren, Wissen zu sammeln und konkrete **Geschäftsmöglichkeiten (Opportunities)** zu formulieren."""

st.divider()
st.markdown("<div id='method-explanation'></div>", unsafe_allow_html=True)

st.subheader(f"{st.session_state.fm_selected_method}")
st.info(explanation_text)
st.markdown("<br>", unsafe_allow_html=True)

if not st.session_state.fm_show_info_box:
    _, btn_col_fort, _ = st.columns([1, 1, 1])
    with btn_col_fort:
        if st.button("Fortfahren", use_container_width=True):
            st.session_state.fm_show_info_box = True
            st.rerun()

if st.session_state.fm_show_info_box:
    st.info("""Hier ist die Nutzung mit ChatGPT **erlaubt**. Es können hier auch gerne weitere Impulse aus dem Netz hinzugezogen werden. Hierfür wird ein kleines Promptmenü zur weiteren Ünterstützung mitgegeben.""")
    st.markdown("<br>", unsafe_allow_html=True) 

    if not st.session_state.fm_framework_understood:
        _, btn_col, _ = st.columns([1, 1, 1])
        with btn_col:
            if st.button("Weiter zu Ihrem Arbeitsbereich", use_container_width=True):
                st.session_state.fm_framework_understood = True
                st.rerun()

if not st.session_state.fm_framework_understood:
    components.html("""<script>const a = window.parent.document.getElementById('method-explanation'); if(a) a.scrollIntoView({behavior: 'smooth', block: 'start'});</script>""", height=0)


# ======== 4. THREE FRAMEWORK SPACES ========
if st.session_state.fm_framework_understood:
    st.divider()
    st.markdown("<div id='framework-spaces'></div>", unsafe_allow_html=True)
    
    st.subheader("Ihr Arbeitsbereich")
    
    def add_p():
        val = st.session_state.fm_p_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "problem",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.fm_selected_method
            }
            st.session_state.fm_problem_entries.append(entry)
        st.session_state.fm_p_input_box = ""

    def add_k():
        val = st.session_state.fm_k_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "knowledge",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.fm_selected_method
            }
            st.session_state.fm_knowledge_entries.append(entry)
        st.session_state.fm_k_input_box = ""

    def add_i():
        val = st.session_state.fm_i_input_box.strip()
        if val:
            entry = {
                "entry_text": val,
                "space_type": "ideation",
                "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
                "entry_tag": st.session_state.fm_selected_method,
                "idea_id": len(st.session_state.fm_ideation_entries) + 1
            }
            st.session_state.fm_ideation_entries.append(entry)
        st.session_state.fm_i_input_box = ""

    # Create the 3 equal columns layout
    col_prob, col_know, col_idea = st.columns(3)
    
    # Popover helper text logic via st.popover as required by "pop-up / info box"
    # Note: st.popover is relatively new in Streamlit (1.33+), alternative is st.expander
    
    # -----------------------------
    # 5.1 PROBLEM SPACE
    # -----------------------------
    with col_prob:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        
        # Clickable Info Title
        with st.popover("🧠 Problem Space", width='stretch'):
            st.info("Beschreibe die aktuelle Herauforderung oder das Problem. Wie sieht die aktuelle Lage aus?")
            
        # Add Promptmenü
        render_prompt_menu("problem_space")
            
        # Display existing entries
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for entry in st.session_state.fm_problem_entries:
            st.markdown(f'<div class="entry-bubble">{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input Logic
        st.text_area("Herausforderungen notieren...", key="fm_p_input_box", height=100)
        st.button(" ", icon=":material/send:", key="fm_btn_p", use_container_width=True, on_click=add_p)
                
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # 5.2 KNOWLEDGE SPACE
    # -----------------------------
    with col_know:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        
        # Clickable Info Title
        with st.popover("📚 Knowledge Space", width='stretch'):
            st.info("Sammle hier Impulse wie Fakten, Trends oder Analogien aus anderen bzw. dir bekannten Bereichen. Was könnte helfen, neue Möglichkeiten zu entdecken?")
            
        # Add Promptmenü
        render_prompt_menu("knowledge_space")
            
        # Display existing entries
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for entry in st.session_state.fm_knowledge_entries:
            st.markdown(f'<div class="entry-bubble">{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input Logic
        st.text_area("Impulse hinzufügen...", key="fm_k_input_box", height=100)
        st.button(" ", icon=":material/send:", key="fm_btn_k", use_container_width=True, on_click=add_k)
                
        st.markdown('</div>', unsafe_allow_html=True)

    # -----------------------------
    # 5.3 IDEATION SPACE
    # -----------------------------
    with col_idea:
        st.markdown('<div class="framework-space">', unsafe_allow_html=True)
        
        # Clickable Info Title
        with st.popover("💡 Ideation Space", width='stretch'):
            st.info("Formuliere hier erste Lösungsansätze bzw. Möglichkeiten, die du anhand deiner Impulse für identifizieren konntest. Es gibt keine richtige oder falsche Antwort, wichtig ist, das Denken anzuregen!")
            
        # Add Promptmenü
        render_prompt_menu("ideation_space")
            
        # Display existing entries as numbered list
        st.markdown('<div class="entries-container">', unsafe_allow_html=True)
        for idx, entry in enumerate(st.session_state.fm_ideation_entries):
            st.markdown(f'<div class="entry-bubble"><b>Ansatz {idx+1}:</b><br>{entry["entry_text"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input Logic
        st.text_area("Lösungsansätze festhalten...", key="fm_i_input_box", height=100)
        st.button(" ", icon=":material/send:", key="fm_btn_i", use_container_width=True, on_click=add_i)
                
        st.markdown('</div>', unsafe_allow_html=True)


    st.markdown("<br><hr>", unsafe_allow_html=True)
    
    # ======== 6. FINAL SUBMISSION LOGIC ========
    valid_submit = (len(st.session_state.fm_problem_entries) > 0 or 
                   len(st.session_state.fm_knowledge_entries) > 0 or 
                   len(st.session_state.fm_ideation_entries) > 0)
                   
    if not st.session_state.fm_confirm_submit:
        _, sub_col, _ = st.columns([1, 1, 1])
        with sub_col:
            # Require at least one entry total to submit
            if st.button("Absenden", use_container_width=True, disabled=not valid_submit):
                st.session_state.fm_confirm_submit = True
                st.rerun()
    else:
        # Confirmation Stage
        st.warning("Möchten Sie Ihre Eingaben wirklich absenden?", icon="❓")
        
        conf_col1, conf_col2 = st.columns(2)
        with conf_col1:
            if st.button("Zurück Bearbeiten", use_container_width=True):
                st.session_state.fm_confirm_submit = False
                st.rerun()
                
        with conf_col2:
            if st.button("Endgültig Absenden", use_container_width=True):
                # SUCCESS: Store everything into the global experiment data structure
                st.session_state.experiment_data["fw_selected_method"] = st.session_state.fm_selected_method
                st.session_state.experiment_data["fw_problem_entries"] = list(st.session_state.fm_problem_entries)
                st.session_state.experiment_data["fw_knowledge_entries"] = list(st.session_state.fm_knowledge_entries)
                st.session_state.experiment_data["fw_ideation_entries"] = list(st.session_state.fm_ideation_entries)
                
                # Increment rounds counter
                st.session_state.completed_rounds = st.session_state.get("completed_rounds", 0) + 1
                
                # Route step dynamically
                if st.session_state.completed_rounds >= 2:
                    st.session_state.step = 8
                else:
                    st.session_state.step = 6
                
                # Resets for cleanly revisiting
                st.session_state.fm_selected_method = None
                st.session_state.fm_confirm_submit = False
                st.session_state.fm_method_understood = False
                st.session_state.fm_framework_understood = False
                st.session_state.fm_problem_entries = []
                st.session_state.fm_knowledge_entries = []
                st.session_state.fm_ideation_entries = []
                
                st.rerun()

    if not st.session_state.fm_confirm_submit:
        components.html(
            """
            <script>
            const anchor = window.parent.document.getElementById('framework-spaces');
            if (anchor) {
                anchor.scrollIntoView({behavior: 'smooth', block: 'start'});
            }
            </script>
            """,
            height=0
        )



#### TO DO ####
# 1. Add the method explanations
# 2. Add the framework explanation
# 3. Add the final submission logic
# 4. Add the navigation to the next page
# 5. enhace more visual on the wrinting input box, 
##   so that participants can see what they have written in the input box
