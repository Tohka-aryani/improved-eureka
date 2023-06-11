import streamlit as st
import pandas as pd

def create_database():
    # Create an empty Pandas DataFrame to store the applications
    df = pd.DataFrame(columns=["Twitch Name", "Discord Name", "Email", "Reason for Application",
                               "Uploaded Twitch Panels", "Enabled VODs", "Linked Twitch to Discord"])
    return df

def save_application(df, twitch_name, discord_name, email, reason, uploaded_panels, enabled_vods, linked_twitch_discord):
    # Append the submitted application to the DataFrame
    new_row = {
        "Twitch Name": twitch_name,
        "Discord Name": discord_name,
        "Email": email,
        "Reason for Application": reason,
        "Uploaded Twitch Panels": uploaded_panels,
        "Enabled VODs": enabled_vods,
        "Linked Twitch to Discord": linked_twitch_discord
    }
    df = df.append(new_row, ignore_index=True)
    return df

def main():
    st.title("Application Form")

    # Create or load the database
    if 'database' not in st.session_state:
        st.session_state['database'] = create_database()
    else:
        database = st.session_state['database']

    # Twitch Name
    twitch_name = st.text_input("Twitch Name")

    # Discord Name
    discord_name = st.text_input("Discord Name")

    # Email
    email = st.text_input("Email")

    # Reason for Application
    reason = st.text_area("Reason for Application")

    # Dropdown list for additional options
    st.subheader("Additional Options")
    uploaded_panels = st.selectbox("Uploaded Twitch Panels", ("Yes", "No"))
    enabled_vods = st.selectbox("Enabled VODs", ("Yes", "No"))
    linked_twitch_discord = st.selectbox("Linked Twitch to Discord", ("Yes", "No"))

    if st.button("Submit"):
        # Save the application to the database
        database = save_application(database, twitch_name, discord_name, email, reason, uploaded_panels,
                                    enabled_vods, linked_twitch_discord)
        # Update the session state
        st.session_state['database'] = database
        # Clear the form fields
        twitch_name, discord_name, email, reason = "", "", "", ""
        uploaded_panels, enabled_vods, linked_twitch_discord = "No", "No", "No"
        st.success("Application submitted successfully!")

    # Second page for viewing the submitted data
    st.title("Submitted Applications")
    if len(database) > 0:
        st.write(database)

if __name__ == '__main__':
    main()




