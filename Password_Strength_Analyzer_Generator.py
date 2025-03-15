import streamlit as st
import random
import string
import re
def generate_password(Length,use_digits,use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(Length))

st.title("Password Strength Analyzer & Generator by Mudasir Ali")

length = st.slider("Select Password Length",min_value=6 , max_value=32, value=12)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length,use_digits,use_special)
    st.write(f"Generated Password {password} " )



blacklist = ["password123", "12345678", "qwerty", "letmein", "admin"]

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    else:
        st.write("❌ Password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.write("❌ Include both uppercase and lowercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.write("❌ Include at least one special character (!@#$%^&*).")
    if password not in blacklist:
        score += 1
    else:
        st.write("❌ The password is too common and easily guessable. Choose a different one.")
    if score == 5:
        st.write("✅ Strong Password!")
    elif score >= 3:
        st.write("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.write("❌ Weak Password - Improve it using the suggestions above.")
    return score

st.title("Password Strength Meter")
password = st.text_input("Enter your password", type="password")
if st.button("Check Password Strength"):
    check_password_strength(password)







