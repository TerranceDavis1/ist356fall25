import pandas as pd 
import streamlit as st 

st.title("Contents")

excel_file = st.file_uploader("Upload an Excel file", type="xlsx")

if excel_file is not None:
    df = pd.read_excel(excel_file, sheet_name=0)
    st.dataframe(df)

    json_str = df.to_json(orient='records', indent=1)

    st.download_button(
        label="Download JSON",
        data=json_str,
        file_name="contents.json",
        mime="application/json"
    )