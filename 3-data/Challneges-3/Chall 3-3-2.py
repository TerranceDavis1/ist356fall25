import streamlit as st 
import pandas as pd 

raw_data = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"

months = ['jan','feb','mar','apr']

st.title('Minmart Non Buyers By Month')
month_option = st.selectbox('Select month',['Jan','feb','mar','apr'], index = 0)

#customers = pd.read_csv(raw_data)