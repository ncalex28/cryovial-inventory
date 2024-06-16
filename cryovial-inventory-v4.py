import streamlit as st
import pandas as pd

## Function for editing table
def info_to_inventory(df):
    new_df = pd.DataFrame()

    for _, row in df.iterrows():
        # Extract values from the current row
        date = row['Date']
        cell_id = row['Cell Line']
        density = row['Cell Density']
        benchling_id = row['Benchling ID']
        cryovials = int(row['Number of Vials'])

        # Repeat the row for the number of cryovials
        repeated_rows = pd.DataFrame({'Date': [date] * cryovials,
                                      'Cell Line': [cell_id] * cryovials,
                                      'Cell Density': [density] * cryovials,
                                      'Benchling ID': [benchling_id] * cryovials
                                      })

        # Append the repeated rows to the new DataFrame
        new_df = pd.concat([new_df, repeated_rows], ignore_index=True)
        
    return new_df

## Streamlit
st.title("IPSC Bio Cryovial Info to Inventory")
st.divider()
st.write("Paste cell line information along with the number of vials being added to inventory.")
with st.form("cryovial_info_form"):
    st.write("Paste table below:")
    df_input = pd.DataFrame([{"Date": "date", "Cell Line": "sample", "Cell Density": 0, "Benchling ID": "INK0000-IPSC000", "Number of Vials": 0}])
    edited_df_input = st.data_editor(df_input, num_rows="dynamic")
    submitted = st.form_submit_button("Submit")

    if submitted:
        df_output = info_to_inventory(edited_df_input)
        st.data_editor(df_output, num_rows="dynamic")

