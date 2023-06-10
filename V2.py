import streamlit as st
import pandas as pd

def main():
    st.title("Application Form")
    
    # Page navigation
    page = st.sidebar.radio("Page", ("Form", "View Data"))
    
    if page == "Form":
        show_application_form()
    elif page == "View Data":
        show_data_table()

def show_application_form():
    st.header("Submit Application")
    
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
                "Reason for Application": reason,
                "Connected Twitch to Discord": connected,
                "Enabled VODs": enabled_vods,
                "Twitch Panels": twitch_panels
            }
            st.success("Your application has been submitted successfully!")

def show_data_table():
    st.header("Submitted Applications")
    
    # Check if there is submitted data
    if "submitted_data" not in st.session_state:
        st.warning("No applications have been submitted yet.")
    else:
        # Get the submitted data
        data = st.session_state.submitted_data
        
        # Create a DataFrame from the submitted data
        df = pd.DataFrame([data])
        
        # Display the data in a table
        st.dataframe(df)

if __name__ == "__main__":
    main()


