import re
import streamlit as st #type: ignore

st.set_page_config(page_title="Password Strength Meter By Ahmed", page_icon="🌘", layout="centered")

st.title("🔒Password Strength Meter")

if 'history' not in st.session_state:
    st.session_state.history = []
def check_password(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password is at least 8 characters long")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password contains at least one uppercase and one lowercase letter")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌Password contains at least one number")
    if re.search(r'[!@#$%^&*_-]',password):
        score += 1
    else:
        feedback.append("❌Password contains at least one special character")
    if score == 4:
        st.success("✅Password is strong")
    elif score == 3:
        st.warning("⚠️Password is medium")
        
    else:
        st.error("❌Password is weak")
    if feedback:
        with st.expander("Improve your password"):
            for f in feedback:
                st.write(f)
        
    
    
password = st.text_input("Enter your password", type="password",help="Ensure your password")


if st.button("Check Password Strength "):
    if password:
        check_password(password)  
        if password in st.session_state.history:
            st.error("This password already exists in history. Please choose a different one.")
        
        else:
            # Call a function to check password strength (assuming it's defined)
            st.session_state.show_history_button = True    
    else:
            st.warning("Please enter password")

col1, col2 = st.columns(2)
if "show_history_button" in st.session_state and st.session_state.show_history_button:
    with col1:
        if st.button("Save Password"):
            if password in st.session_state.history:
                st.error("This password is already in history!")
            elif len(password) < 8:
                st.error("Password must be at least 8 characters long.")
            elif not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password):
                st.error("Password must contain at least one uppercase and one lowercase letter.")
            elif not re.search(r"[0-9]", password):
                st.error("Password must contain at least one number.")
            elif not re.search(r'[!@#$%^&*_-]',password):
                st.error("Password must contain at least one special character.")
            elif password == False:
                st.error("Password must contain at least one special character.")
            else:
                st.success("✅ Password saved successfully")
                st.session_state.history.append(password) 
    with col2:
        if st.button("Clear history"):
            st.session_state.history = [] 
            
         
st.subheader("History:")
for index, item in enumerate(st.session_state.history, start=1):
    st.write(f"{index}. {item}")






