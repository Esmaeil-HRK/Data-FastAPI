import streamlit as st
import requests

# Streamlit form for user input
st.title('Data Submission Form')

with st.form("user_data_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    transfer_limit = st.number_input("Transfer Limit", min_value=0.0, format='%f')
    nid = st.text_input("National ID")
    
    submitted = st.form_submit_button("Submit")
    if submitted:
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "transfer_limit": transfer_limit,
            "nid": nid
        }
        
        response = requests.post("http://localhost:8000/process-data/", json=data)
        if response.status_code == 200:
            result_data = response.json()
            st.success("Data Processed Successfully!")
            st.write(result_data)
        else:
            st.error("An error occurred.")

