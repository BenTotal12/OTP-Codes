import streamlit as st
import pyotp

# Define secret keys for users
USER_KEYS = {
    "Tcchino12": "OUQ5MV6WUSKFBTI2RSWLKAZKME",
    "Tcelmonte": "XUCKOGCXLBN6OXD7YZPZ4HWPA4"
}

# Streamlit app
st.title("OTP Generator")

# Dropdown to select user
selected_user = st.selectbox("Select User", list(USER_KEYS.keys()))

# Generate OTP for the selected user
totp = pyotp.TOTP(USER_KEYS[selected_user])
current_otp = totp.now()

# Display the current OTP
st.write(f"**Current OTP for {selected_user}**: {current_otp}")
st.info("The OTP is time-based and refreshes every 30 seconds.")

# Refresh button
if st.button("Refresh OTP"):
    st.rerun()  # Reruns the script to update the OTP
