# Goal of this web app 
Participants will work with the implemented Framework to generate and identify opportnity ideas. 
For that they will work with and without framework with the same method to compare the ideas. (Framework with AI and Framework without AI)
Goal is to see what the impact AI has on the creative workflow method (Brainstorming) the participants will be using to generate and identify opportnity ideas.



run streamlit app
# python -m streamlit run explantation.py

## Open Terminal 
->  Ctrl + Shift + Ö


# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
# -> Dann fragt Windows nach Bestätigung → tippe Y und Enter.


# Danach aktivierst du dein venv:
#.\.venv\Scripts\Activate.ps1
# Wenn es geklappt hat, siehst du vorne in der Zeile meist sowas wie (.venv).


# Checklist
# Emojy's
👤 

Implementation Plan: Sequential Streamlit App Flow
This plan details the changes required to establish the exact 8-step sequence requested for the experiment, ensure strict state management, and add CSV generation at the final step.

Proposed Changes
1. 
0_webapp.py
Update the routing logic to map the 8 steps precisely:
Step 1: 
1_explanation.py
Step 2: 
2_welcome.py
Step 3: 
3_cases.py
 (Round 1: Case selection)
Step 4: 
4_OhneFramework.py
 (Ideation without framework)
Step 5: 
6_Evaluation.py
 (Evaluation for Round 1)
Step 6: 
3_cases.py
 (Round 2: Select remaining case)
Step 7: 
5_MitFramework.py
 (Ideation with framework)
Step 8: 
6_Evaluation.py
 (Evaluation for Round 2)
Step 9: End screen & CSV Export
Add CSV export generation logic at Step 9, iterating over all stored ideas and evaluation scores in st.session_state.experiment_data and presenting an st.download_button.
2. 
3_cases.py
Modify the logic to detect if we are in Round 1 (Step 3) or Round 2 (Step 6).
Round 1 (Step 3):
Save the selected case to st.session_state.experiment_data["first_case"].
Show the "Weiter ohne Framework" button.
On click, advance to step 4.
Round 2 (Step 6):
If the user clicks the case chosen in Round 1, show an error: "Du hast diesen Fall bereits ausgewählt. Bitte wählen Sie einen neuen Fall aus."
Save the new choice to st.session_state.experiment_data["second_case"].
Show the "Weiter mit Framework" button.
On click, advance to step 7.
3. 
4_OhneFramework.py
Ensure the chosen method is explicitly saved to st.session_state.experiment_data['method_chosen'].
No major UX changes except making sure state transitions reliably set step = 5.
4. 
5_MitFramework.py
Remove the dropdown for method selection.
Retrieve the method from st.session_state.experiment_data['method_chosen'].
Display the text: "Die Methode, die du zuvor gewählt hast, gilt weiterhin. Du arbeitest erneut mit derselben Methode."
Display the method explanation automatically.
Upon submission, advance to step 8.
5. 
6_Evaluation.py
Modify the file to handle both Round 1 (Step 5) and Round 2 (Step 8).
Round 1:
Load ideas from the "ohne framework" round (experiment_data["ideas_generated"]).
Upon submission, save scores to experiment_data["evaluations_ohne"].
Advance to Step 6.
Round 2:
Load ideas from the "mit framework" ideation space (experiment_data["fw_ideation_entries"]).
Upon submission, save scores to experiment_data["evaluations_mit"].
Advance to Step 9 (CSV Export).
6. CSV Export Structure (Generated in 
0_webapp.py
)
Columns will include:

participant_id (or 
group_id
)
participation_type
first_case
second_case
method_chosen
condition ("Ohne Framework" or "Mit Framework")
idea_number
idea_text
Ratings: novelty, usefulness, feasibility, cost, sustainability, time_to_implement, risk
problem_entry (Joined string of entries, only for "Mit Framework")
knowledge_entry (Joined string of entries, only for "Mit Framework")
Verification Plan
Automated Tests
We will not run automated UI tests, but we will rely on manual verification by running the app locally.
Manual Verification
Start the app using streamlit run 0_webapp.py.
Run-through 1 (Einzelteilnahme):
Walk through all 8 steps.
Verify Case 1 is blocked in Step 6 if selected in Step 3.
Verify the same method is forced in Step 7.
At the end, verify the downloaded CSV has the correct structure and contains all data points.
Run-through 2 (Gruppenteilnahme):
Ensure group IDs and multiple names are captured and represented in the exported data correctly.
Implementing



# Further To Dos

- Change criterias into german 
- add short explanation for each criteria in the evaluation page
- add Framework 
- add evaluation explanation in the evaluation page




