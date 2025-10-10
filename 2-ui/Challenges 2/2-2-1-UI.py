import streamlit as st



st.title(' Area and Permiter Widget')
if 'length' not in st.session_state:
    st.session_state.length = 0.0

if 'width' not in st.session_state:
    st.session_state.width = 0.0
length = st.number_input("Enter the length", value = st.session_state.length)
width = st.number_input("Enter the width", value = st.session_state.width)
#Buttons
calculate = st.button('Calculate', type='primary')
clear = st.button('clear', type='secondary')

#conditions
if calculate:
    area = length * width
    perimeter = 2 *(length*width)
    st.write(f"The perimeter is:{perimeter} ")
    st.write(f"The area is: {area}")
elif clear:
     st.session_state.length =None
     st.session_state.width = None      
     st.rerun()
    

