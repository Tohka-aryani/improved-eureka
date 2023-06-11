import streamlit as st
import pandas as pd

# Create a global DataFrame to store the submitted applications
applications_df = pd.DataFrame(columns=["Twitch Name", "Discord Name", "Email", "Reason for Application",
                                        "Uploaded Twitch Panels", "Enabled VODs", "Linked Twitch to Discord"])

def main():
    st.title("Application Form")

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

    # Submit button
    if st.button("Submit"):
        # Store the submitted application in the DataFrame
        applications_df.loc[len(applications_df)] = [twitch_name, discord_name, email, reason,
                                                     uploaded_panels, enabled_vods, linked_twitch_discord]
        st.success("Application submitted successfully!")

    # Display the submitted applications on a separate page
    if st.button("View Submitted Applications"):
        view_applications()

def view_applications():
    st.title("Submitted Applications")

    if applications_df.empty:
        st.write("No applications submitted yet.")
    else:
        st.dataframe(applications_df)

if __name__ == '__main__':
    main()





