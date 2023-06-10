import streamlit as st

def main():
    page = st.sidebar.selectbox("Select a page", ["Application Form", "View Submitted Data"])
    
    if page == "Application Form":
        display_application_form()
    elif page == "View Submitted Data":
        display_submitted_data()

def display_application_form():
    st.title("Application Form")
    
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
            st.session_state.submissions.append({
                "Twitch Name": twitch_name,
                "Discord Name": discord_name,
                "Reason for application": reason,
                "Connected Twitch to Discord": connected,
                "Enabled VODs": enabled_vods,
                "Twitch Panels": twitch_panels
            })
            st.success("Your application has been submitted successfully!")

def display_submitted_data():
    st.title("Submitted Data")
    
    # Display the submitted data
    submissions = st.session_state.submissions
    if not submissions:
        st.info("No data submitted yet.")
    else:
        selected_submissions = st.multiselect("Select entries", submissions, format_func=lambda submission: submission["Twitch Name"])
        if selected_submissions:
            st.write("Selected Entries:")
            for submission in selected_submissions:
                st.write(submission)
        else:
            st.write("All Entries:")
            for submission in submissions:
                st.write(submission)

if __name__ == "__main__":
    st.session_state.submissions = []  # Initialize the list to store the submissions
    main()

    
