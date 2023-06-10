import streamlit as st

def main():
    st.title("Application Form")
    
    # Page navigation
    page = st.sidebar.selectbox("Page", ("Form", "View Data"))
    
    if page == "Form":
        show_form()
    elif page == "View Data":
        show_data()

def show_form():
    st.subheader("Application Form")
    
    # Paragraph fields
    twitch_name = st.text_input("Twitch Name")
    discord_name = st.text_input("Discord Name")
    reason = st.text_area("Reason for application")
    
    # Checkboxes
    connected = st.checkbox("Connected Twitch to Discord")
    enabled_vods = st.checkbox("Enabled VODs")
    twitch_panels = st.checkbox("Twitch Panels")
    
    # Terms and Conditions checkbox
    agree = st.checkbox("I agree to the Terms and Conditions")
    
    # Submit button
    if st.button("Submit"):
        # Perform validation and processing of form data
        if twitch_name == "":
            st.error("Please enter your Twitch Name.")
        elif discord_name == "":
            st.error("Please enter your Discord Name.")
        elif reason == "":
            st.error("Please provide a reason for your application.")
        elif not agree:
            st.error("You must agree to the Terms and Conditions.")
        else:
            # Process the form data (e.g., send it to a backend, store it in a database, etc.)
            # Replace the print statements with your desired processing logic
            st.session_state.submitted_data = {
                "Twitch Name": twitch_name,
                "Discord Name": discord_name,
                "Reason for application": reason,
                "Connected Twitch to Discord": connected,
                "Enabled VODs": enabled_vods,
                "Twitch Panels": twitch_panels
            }
            st.session_state.form_submitted = True
            st.success("Your application has been submitted successfully!")

def show_data():
    st.subheader("Submitted Data")
    
    if not hasattr(st.session_state, "form_submitted") or not st.session_state.form_submitted:
        st.warning("No data has been submitted yet.")
    else:
        submitted_data = st.session_state.submitted_data
        for field, value in submitted_data.items():
            st.write(f"**{field}:** {value}")

if __name__ == "__main__":
    main()

