import streamlit as st
import pandas as pd
import requests

GITHUB_API_URL = "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"
REPO_OWNER = "Tohka_aryani"
REPO_NAME = "improved-eureka"
FILE_PATH = "data.csv"

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
            
            # Save the submission to the CSV file on GitHub
            save_submission(submission)
            
            st.success("Your application has been submitted successfully!")

def save_submission(submission):
    # Load existing data from GitHub
    existing_data = load_data_from_github()
    
    # Add the new submission to the existing data
    existing_data.append(submission)
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(existing_data)
    
    # Convert the DataFrame to CSV string
    csv_data = df.to_csv(index=False)
    
    # Commit the updated CSV file to GitHub
    commit_changes(csv_data)

def load_data_from_github():
    # Get the contents of the data file from GitHub
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.json()
        csv_data = content["content"]
        data = pd.read_csv(io.BytesIO(base64.b64decode(csv_data)))
        return data.to_dict("records")
    else:
        return []

def commit_changes(csv_data):
    # Get the current SHA of the file on GitHub
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    response = requests.get(url)
    if response.status_code == 200:
        sha = response.json()["sha"]
    else:
        sha = None
    
    # Create the commit payload
    payload = {
        "message": "Update data.csv",
        "content": base64.b64encode(csv_data.encode()).decode(),
        "sha": sha
    }
    
    # Send the commit request to GitHub
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        "Authorization": f"Bearer {GITHUB_ACCESS_TOKEN}"
    }
    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        st.session_state.submissions = True
    else:
        st.warning("Failed to save the data to GitHub.")

def display_submitted_data():
    st.title("Submitted Data")
    
    # Display the submitted data
    submissions = load_data_from_github()
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
    st.session_state.submissions = False  # Initialize the session state
    main()



