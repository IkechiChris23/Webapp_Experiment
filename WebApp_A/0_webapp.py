import streamlit as st
import pandas as pd
from io import BytesIO
import datetime
import os

# Automatically change the working directory to the location of 0_webapp.py.
# This ensures that sub-pages and image assets resolve correctly when deployed 
# inside a subfolder on hosting platforms like Streamlit Community Cloud.
dir_path = os.path.dirname(os.path.realpath(__file__))
if dir_path:
    os.chdir(dir_path)

# ======== MAIN APP ENTRY POINT CONFIG ========
st.set_page_config(
    page_title="Experiment Web App",
    page_icon="🧪",
    layout="wide"
)

# ======== SESSION STATE FOR NAVIGATION ========
# Initialize step variable if it doesn't exist
if "step" not in st.session_state:
    st.session_state.step = 1

if "completed_rounds" not in st.session_state:
    st.session_state.completed_rounds = 0

# Router helper function using exec to ensure compatibility 
# without modifying the structure of the individual scripts too much.
def run_page(path):
    with open(path, encoding="utf-8") as f:
        # Compile and execute within a pristine global environment 
        # but maintaining the Streamlit execution context natively.
        code = compile(f.read(), path, "exec")
        exec(code, globals())

# ======== START ROUTING LOGIC ========
if st.session_state.step == 1:
    run_page("1_explanation.py")
    
elif st.session_state.step == 2:
    run_page("2_welcome.py")
    
elif st.session_state.step == 3:
    run_page("3_Framework.py")
    
elif st.session_state.step == 4:
    # Round 1: Choose first case
    run_page("4_cases.py")
    
elif st.session_state.step == 5:
    # Round 1 Ideation (Dynamic condition)
    if st.session_state.get("round_1_condition") == "MIT":
        run_page("6_MitFramework.py")
    else:
        run_page("5_OhneFramework.py")

elif st.session_state.step == 6:
    # Round 2: Choose second case
    run_page("4_cases.py")

elif st.session_state.step == 7:
    # Round 2 Ideation (opposite of Round 1 selection)
    if st.session_state.get("round_1_condition") == "MIT":
        run_page("5_OhneFramework.py")
    else:
        run_page("6_MitFramework.py")

elif st.session_state.step >= 8:
    # ======== END PAGE & CSV EXPORT ========
    st.success("🎉 Das Experiment ist beendet! Vielen Dank für Ihre Teilnahme.")
    st.info("Bitte laden Sie Ihre Ergebnisse herunter, um die Studie abzuschließen.")
    
    # 1. Gather Data
    exp_data = st.session_state.get("experiment_data", {})
    
    # Basic Participant Info
    p_type = "Einzelteilnahme"
    p_id = exp_data.get("participant_id", "Keine ID")
    
    names_str = exp_data.get("name", "")
    ages_str = str(exp_data.get("age", ""))
    occ_str = exp_data.get("occupation", "")
    
    # Experimental Setup Info
    first_case = exp_data.get("first_case", "")
    second_case = exp_data.get("second_case", "")
    
    # Since selected method is constant across rounds now
    method_ohne = exp_data.get("selected_method", "")
    method_mit = exp_data.get("fw_selected_method", "")
    
    # 2. Build rows for CSV
    rows = []
    
    def process_entries(entries_list, condition_val, case_val):
        for entry in entries_list:
            if isinstance(entry, dict):
                text = entry.get("entry_text", "")
                stype = entry.get("space_type", "")
                tstamp = entry.get("timestamp", "")
                etag = entry.get("entry_tag", "")
                iid = entry.get("idea_id", None)
            else:
                # Fallback in case of raw string entries
                text = str(entry)
                stype = "unknown"
                tstamp = ""
                etag = ""
                iid = None
            
            rows.append({
                " ID": p_id,
                "name": names_str,
                "age": ages_str,
                "Occupation": occ_str,
                "Participation_mode": p_type,
                "condition": condition_val,
                "case_number": case_val,
                "method": etag,
                "timestamp": tstamp,
                "space_type": stype,
                "entry_text": text,
                "Idea_id": iid if iid is not None else ""
            })

    # Determine which case was solved under which condition
    if st.session_state.get("round_1_condition") == "MIT":
        mit_case = first_case
        ohne_case = second_case
    else:
        ohne_case = first_case
        mit_case = second_case

    # Add Round 1 (Ohne Framework) data
    ohne_p = exp_data.get("ohne_problem_entries", [])
    ohne_k = exp_data.get("ohne_knowledge_entries", [])
    ohne_i = exp_data.get("ohne_ideation_entries", [])
    process_entries(ohne_p, "Ohne Framework", ohne_case)
    process_entries(ohne_k, "Ohne Framework", ohne_case)
    process_entries(ohne_i, "Ohne Framework", ohne_case)
        
    # Add Round 2 (Mit Framework) data
    mit_p = exp_data.get("fw_problem_entries", [])
    mit_k = exp_data.get("fw_knowledge_entries", [])
    mit_i = exp_data.get("fw_ideation_entries", [])
    process_entries(mit_p, "Mit Framework", mit_case)
    process_entries(mit_k, "Mit Framework", mit_case)
    process_entries(mit_i, "Mit Framework", mit_case)

    # 3. Create DataFrame and CSV
    if rows:
        df = pd.DataFrame(rows)
        # Sort chronologically by timestamp
        if "timestamp" in df.columns:
            df = df.sort_values(by="timestamp", na_position="last").reset_index(drop=True)
            
        # Reorder columns as requested: " ID, name, age, Occupation, Participation_mode, condition, case_number, method, timestamp, space_type, entry_text, Idea_id"
        column_order = [" ID", "name", "age", "Occupation", "Participation_mode", "condition", "case_number", "method", "timestamp", "space_type", "entry_text", "Idea_id"]
        for col in column_order:
            if col not in df.columns:
                df[col] = ""
        df = df[column_order]
        
        # Convert to Excel readable CSV (sep=';', decimal=',') or standard CSV (sep=',')
        csv_data = df.to_csv(index=False, sep=";").encode('utf-8')
        
        filename = f"experiment_data_{p_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Ergebnisse als CSV herunterladen",
                data=csv_data,
                file_name=filename,
                mime="text/csv",
                type="primary",
                use_container_width=True
            )
            
    else:
        st.warning("Es wurden keine Ideendaten gefunden, um sie zu exportieren.")
    
    st.markdown("<br><hr>", unsafe_allow_html=True)
    # Allow restarting for testing
    if st.button("Neustart / Restart", use_container_width=True):
        st.session_state.clear() # Reset all states completely
        st.session_state.step = 1
        st.rerun()
