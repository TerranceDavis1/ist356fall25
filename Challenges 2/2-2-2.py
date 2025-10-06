import streamlit as st 

st.title ('Order Total and History ')
#Initialize session state variables
if "total" not in st.session_state:
    st.session_state.total = 0 
if "history" not in st.session_state:
    st.session_state.history = []
if "amount" not in st.session_state:
    st.session_state.amount = 0.0


amount = st.number_input("Enter an amount")

# Total button acumlate amount in total
if st.button("Add to total"):
    st.session_state.total += amount
    st.session_state.history.append(amount)

#Clear button function
if st.button("Clear"):
    st.session_state.total = 0
    st.session_state.history = []
#display
st.write(f"Total: ${st.session_state.total:.2f}")
st.write(f"History of purchases: ${st.session_state.history}")