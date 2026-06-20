import streamlit as st
import random
import time

# ======== PAGE CONFIG ========
# st.set_page_config(
#     page_title="Welcome Setup",
#     page_icon="🧪",
#     layout="wide"
# )

# ======== CUSTOM CSS ========
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

# ======== CUSTOM CSS ========
st.markdown("""
<style>
    /* 1) Header Images fixes from previous pages (removes default rounding) */
    [data-testid="stImage"] img {
        border-radius: 0 !important;
        max-height: 80px;
        width: auto;
    }
    
    /* Improve padding of the main container */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ---------------------------------------------------------------------
       2) BUTTON STYLING (Case Buttons & Weiter Buttons)
       Here you can easily adjust the height and width of your buttons!
       --------------------------------------------------------------------- */
    div.stButton > button, div.stFormSubmitButton > button {
        background-color: #00C1D4 !important; /* TUHH Turquoise */
        color: white !important;
        
        /* ADJUST BUTTON HEIGHT AND WIDTH HERE */
        height: 100px !important;
        width: 100% !important;

        border-radius: 12px !important;
        border: none !important;
        transition: background-color 0.3s;
    }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover {
        background-color: #009fb0 !important;
        color: white !important;
    }
    div.stButton > button:active, div.stFormSubmitButton > button:active {
        background-color: #008291 !important;
        color: white !important;
    }
    
    /* Ensure the text inside the button uses the correct font properties */
    div.stButton > button p, div.stFormSubmitButton > button p {
        font-size: 22px !important;
        font-weight: 600 !important;
        color: white !important;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)


# ======== HEADER ========
col_title, col_logo1, col_logo2 = st.columns([2.5, 1, 1])

with col_title:
    st.title("Willkommen")

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

st.divider()# ======== SESSION STATE INITIALIZATION ========
if "experiment_data" not in st.session_state:
    st.session_state.experiment_data = {}

# ======== HELPER FUNCTIONS ========
def generate_individual_id():
    # Example format: ITU083
    return f"ITU{random.randint(0, 200):03d}"

def navigate_to_next_page():
    # 1) Advance session_state step logic for single-page apps
    if "step" not in st.session_state:
        st.session_state.step = 2
    else:
        st.session_state.step += 1

# ======== MAIN UI ========
st.markdown("### Einzelteilnahme Formular")
with st.form("individual_form"):
    name = st.text_input("Name")
    age = st.number_input("Alter", min_value=0, max_value=120, step=1, value=0)
    occupation = st.text_input("Beruf")
    
    # Center the button and make it slightly wider using columns
    _, btn_col, _ = st.columns([1, 1.5, 1])
    with btn_col:
        submitted = st.form_submit_button("Weiter zur Fallstudie", use_container_width=True)
    
    if submitted:
        # Validation step
        if not name.strip() or age == 0 or not occupation.strip():
            st.error("Bitte füllen Sie alle Felder aus.")
        else:
            # Generate unique ID
            p_id = generate_individual_id()
            
            # Store data in session_state
            st.session_state.experiment_data = {
                "type": "Einzelteilnahme",
                "participant_id": p_id,
                "name": name.strip(),
                "age": age,
                "occupation": occupation.strip()
            }
            
            # Show generated ID on screen
            st.success(f"Erfolgreich registriert! Ihre Teilnehmer ID ist: **{p_id}**. Sie brauchen sich diese ID nicht merken. Diese ID wird für die Datenerfassung verwendet.")
            
            # Brief wait so the user can see their ID
            import time
            time.sleep(3)
            navigate_to_next_page()
            st.rerun()
