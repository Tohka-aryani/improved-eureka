import streamlit as st

def main():
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
            print("Twitch Name:", twitch_name)
            print("Discord Name:", discord_name)
            print("Reason for application:", reason)
            print("Connected Twitch to Discord:", connected)
            print("Enabled VODs:", enabled_vods)
            print("Twitch Panels:", twitch_panels)
            st.success("Your application has been submitted successfully!")

if __name__ == "__main__":
    main()


    
