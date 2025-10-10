import pandas as pd
import streamlit as st
st.title('Streamlit Customer Radio Widget')

# Loading data from link directly 
df = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')

# Display the dataframe using streamlit
st.dataframe(df)

#creating radio button widget 

choices = st.radio(
    "Choose Gender:",
    options = ["Male", "Female"]
)


#filtered rows based on gender

data_dict = {
    'Male': df[df['Gender'] == 'M'],
    'Female': df[df['Gender'] == 'F']
}
#Displaying results in another chart
st.write(f"You chose: {choices}")
st.dataframe(data_dict[choices])