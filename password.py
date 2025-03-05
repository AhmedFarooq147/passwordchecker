import re
import streamlit as st #type: ignore

st.set_page_config(page_title="Password Strength Meter By Ahmed", page_icon="🌘", layout="centered")

st.title("🔒Password Strength Meter")
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
    
    else:
        st.warning("Please enter password")







