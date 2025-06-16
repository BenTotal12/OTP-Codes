import streamlit as st
import pyotp

# Define the secret key
SECRET_KEY = "OUQ5MV6WUSKFBTI2RSWLKAZKME"

# Generate OTP
totp = pyotp.TOTP(SECRET_KEY)
current_otp = totp.now()

# Streamlit app
st.title("OTP Display App")
st.write("Current OTP for tcchino12 key, refresh before pasting.")

# Display the current OTP
st.write(f"**Current OTP**: {current_otp}")
st.info("The OTP is time-based and refreshes every 30 seconds.")

# Refresh button
if st.button("Refresh OTP"):
    st.rerun()  # Reruns the script to update the OTP
