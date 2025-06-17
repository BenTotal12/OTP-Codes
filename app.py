import streamlit as st
import pyotp

# --- User Configuration ---
# The dictionary now includes the new users you provided.
USER_KEYS = {
    "Tcchino12": "OUQ5MV6WUSKFBTI2RSWLKAZKME",
    "Tcelmonte": "XUCKOGCXLBN6OXD7YZPZ4HWPA4",
    "Tccorona": "5RJO4U3POTDE4JF6EXFDHKEUU4",
    "Tceastvale": "EMQM3LVFC54EF243LKZGG342M4",
    "Tcsanb": "FIJP4RBZDZMBLZZ5J2H4CXKAYU"
}

# --- Streamlit App Interface ---

# Set the title of the web application
st.title("OTP Generator")

# Create a dropdown menu for the user to select their username
try:
    # The dropdown will now list all five users.
    selected_user = st.selectbox("Select User", list(USER_KEYS.keys()))

    # --- OTP Generation Logic ---

    # Check if a user is selected
    if selected_user:
        # Initialize the Time-based One-Time Password (TOTP) object
        # with the secret key of the selected user.
        totp = pyotp.TOTP(USER_KEYS[selected_user])

        # Generate the current OTP based on the current time
        current_otp = totp.now()

        # --- Display the OTP ---

        # Display the current OTP for the selected user
        st.write(f"**Current OTP for {selected_user}**: `{current_otp}`")
        st.info("The OTP is time-based and refreshes automatically every 30 seconds.")

        # Add a button to manually trigger a rerun of the script
        if st.button("Refresh OTP"):
            st.rerun()

except Exception as e:
    st.error(f"An error occurred: {e}")
    st.warning("Please ensure your user keys are configured correctly.")
