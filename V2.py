import streamlit as st
import pandas as pd

def save_submission_data(submission_data):
    # Save the submission data to a file or database
    # Here, we'll save it to a CSV file
    df = pd.DataFrame(submission_data)
    df.to_csv('data.csv', mode='a', header=not os.path.exists('submissions.csv'), index=False)

def main():
    st.title("Application Form")

    # Paragraph fields
    twitch_name = st.text_input("Twitch Name")
    discord_name = st.text_input("Discord Name")
    reason = st.text_area("Reason for application")

    # Checkboxes
    connected_twitch_discord = st.checkbox("Connected Twitch to Discord")
    enabled_vods = st.checkbox("Enabled VODs")
    twitch_panels = st.checkbox("Twitch Panels")

    # T&C checkbox agreement
    tnc_agreement = st.checkbox("I agree to the Terms and Conditions")

    # Submit button
    if st.button("Submit"):
        # Validate form
        if not twitch_name or not discord_name or not reason:
            st.error("Please fill in all the required fields.")
        elif not tnc_agreement:
            st.error("You must agree to the Terms and Conditions.")
        else:
            # Create a dictionary to hold the submission data
            submission_data = {
                'Twitch Name': twitch_name,
                'Discord Name': discord_name,
                'Reason for application': reason,
                'Connected Twitch to Discord': connected_twitch_discord,
                'Enabled VODs': enabled_vods,
                'Twitch Panels': twitch_panels
            }

            # Save the submission data
            save_submission_data(submission_data)

            st.success("Your application has been submitted successfully.")

if __name__ == '__main__':
    main()


    
