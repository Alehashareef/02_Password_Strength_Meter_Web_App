import re
import streamlit as st
import secrets
import string

def check_password_strength(password):
    strength_points = 0
    
    # Check length
    if len(password) >= 8:
        strength_points += 1
    if len(password) >= 12:
        strength_points += 1
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_points += 1
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_points += 1
    
    # Check for numbers
    if re.search(r"[0-9]", password):
        strength_points += 1
    
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    
    # Check for repeating or consecutive characters
    if re.search(r"(\w)\1{2,}", password) or re.search(r"123|abc|qwerty", password, re.IGNORECASE):
        return "Very Weak Password"
    
    # Check against common passwords
    common_passwords = ["123456", "password", "qwerty", "abc123", "111111", "letmein", "welcome"]
    if password.lower() in common_passwords:
        return "Very Weak Password"
    
    # Determine strength level
    if strength_points <= 2:
        return " ⚠️ Weak Password"
    elif strength_points <= 4:
        return " ❌ Moderate Password"
    elif strength_points == 5:
        return " ✅ Strong Password"
    else:
        return " ✅ Very Strong Password"

def generate_strong_password(length=12, use_special_chars=True):
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", layout="centered")

st.title("🗝️ Password Strength Meter")

password = st.text_input("Enter a password to check strength:", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"**Password Strength:** {strength}")
    
    # Strength indicator bar
    progress = strength.count("Strong") + strength.count("Very") * 2
    st.progress(progress / 5)
    
    if "Weak" in strength:
        st.warning("Consider using a mix of uppercase, lowercase, numbers, and special characters.")

# Password Generator
st.subheader(" 🟢 Generate a Strong Password")
password_length = st.slider("Password Length", min_value=8, max_value=32, value=12)
use_special_chars = st.checkbox("Include Special Characters", value=True)

if st.button("Generate Strong Password"):
    new_password = generate_strong_password(password_length, use_special_chars)
    st.success(f"Generated Password: `{new_password}`")

