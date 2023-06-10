import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.title("Application Form")

    # Sidebar navigation
    page = st.sidebar.selectbox("Page", ["Form", "View Submissions"])

    if page == "Form":
        show_application_form()
    elif page == "View Submissions":
        show_submissions()

def show_application_form():
    st.header("Application Form")

    # Paragraph fields
    twitch_name = st.text_input("Twitch Name")
    discord_name = st.text_input("Discord Name")
    reason = st.text_area("Reason for Application")

    # Checkboxes
    connected_twitch_discord = st.checkbox("Connected Twitch to Discord")
    enabled_vods = st.checkbox("Enabled VODs")
    twitch_panels = st.checkbox("Twitch Panels")

    # Terms and Conditions agreement
    terms_accepted = st.checkbox("I agree to the Terms and Conditions")

    if st.button("Submit"):
        if not terms_accepted:
            st.error("You must agree to the Terms and Conditions to submit the form.")
        else:
            # Process the form submission
            # You can perform further validation or save the form data to a database

            st.success("Form submitted successfully!")

def show_submissions():
    st.header("View Submissions")

    # In this example, we use placeholder data to simulate submitted applications
    submissions = [
        {
            "Twitch Name": "user1",
            "Discord Name": "user1#1234",
            "Reason for Application": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "Connected Twitch to Discord": True,
            "Enabled VODs": False,
            "Twitch Panels": True
        },
        {
            "Twitch Name": "user2",
            "Discord Name": "user2#5678",
            "Reason for Application": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "Connected Twitch to Discord": True,
            "Enabled VODs": True,
            "Twitch Panels": False
        }
    ]

    if len(submissions) == 0:
        st.info("No submissions found.")
    else:
        for i, submission in enumerate(submissions):
            st.subheader(f"Application {i+1}")
            col1, col2 = st.beta_columns(2)
            col1.write(f"Twitch Name: {submission['Twitch Name']}")
            col1.write(f"Discord Name: {submission['Discord Name']}")
            col2.write(f"Reason for Application: {submission['Reason for Application']}")
            col2.write(f"Connected Twitch to Discord: {submission['Connected Twitch to Discord']}")
            col2.write(f"Enabled VODs: {submission['Enabled VODs']}")
            col2.write(f"Twitch Panels: {submission['Twitch Panels']}")

if __name__ == '__main__':
    main()

    
