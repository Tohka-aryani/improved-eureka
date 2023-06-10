import streamlit as st
import pandas as pd
import github3

# GitHub credentials
GITHUB_USERNAME = "Tohka_aryani"
GITHUB_TOKEN = "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"
REPO_OWNER = "Tohka_aryani"
REPO_NAME = "improved-eureka"
DATA_FILE_PATH = "data.csv"

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
            # Process the form data
            submission = {
                "Twitch Name": twitch_name,
                "Discord Name": discord_name,
                "Reason for application": reason,
                "Connected Twitch to Discord": connected,
                "Enabled VODs": enabled_vods,
                "Twitch Panels": twitch_panels
            }
            
            # Save the submission to the GitHub repository
            save_submission(submission)
            
            st.success("Your application has been submitted successfully!")

def save_submission(submission):
    # Create a DataFrame from the submission data
    df = pd.DataFrame(submission, index=[0])
    
    # Connect to the GitHub repository
    gh = github3.login(token=GITHUB_TOKEN)
    repo = gh.repository(REPO_OWNER, REPO_NAME)
    
    # Write the DataFrame to a CSV file
    with st.spinner("Saving the submission..."):
        repo.create_file(DATA_FILE_PATH, "Save new submission", df.to_csv(index=False))
    
    st.session_state.submissions = True

def display_submitted_data():
    st.title("Submitted Data")
    
    # Display the submitted data
    submissions = load_submissions()
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

def load_submissions():
    try:
        # Connect to the GitHub repository
        gh = github3.login(token=GITHUB_TOKEN)
        repo = gh.repository(REPO_OWNER, REPO_NAME)
        
        # Get the contents of the data file
        data_file = repo.contents(DATA_FILE_PATH)
        content = data_file.decoded.decode()
        
        # Load the CSV data into a DataFrame
        df = pd.read_csv(pd.compat.StringIO(content))
        return df.to_dict("records")
    except github3.exceptions.NotFoundError:
        return []

if __name__ == "__main__":
    st.session_state.submissions = False  # Initialize the session state
    main()



