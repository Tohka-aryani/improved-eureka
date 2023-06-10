import streamlit as st
import pandas as pd

# Create a DataFrame to store the application data
data = pd.DataFrame(columns=['Name', 'Email', 'Twitch Status', 'Application Status'])

# Dropdown options
twitch_status_options = ['Affiliate', 'Partner', 'None']
application_status_options = ['Accepted', 'Pending', 'Rejected']

# Streamlit application
def main():
    st.title("Application Form")
    
    st.write("Please fill out the following information:")
    
    # Form input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    twitch_status = st.selectbox("Twitch Status", twitch_status_options)
    application_status = st.selectbox("Application Status", application_status_options)
    
    # Submit button
    if st.button("Submit"):
        # Add data to the DataFrame
        data.loc[len(data)] = [name, email, twitch_status, application_status]
        st.success("Application submitted successfully!")
    
    # Display the current database
    st.subheader("Current Applications")
    st.dataframe(data)
    
# Page for limited people to edit the database
def admin_page():
    st.title("Admin Page")
    
    # Authenticate admin access
    password = st.text_input("Password", type="password")
    if password != "admin123":
        st.error("Incorrect password!")
        return
    
    # Display the editable database
    st.subheader("Edit Applications")
    st.dataframe(data)
    
    # Allow editing of the application status
    application_index = st.number_input("Enter the index of the application to edit", min_value=0, max_value=len(data)-1, value=0)
    new_status = st.selectbox("Update Application Status", application_status_options)
    
    # Update the application status upon button click
    if st.button("Update"):
        data.loc[application_index, 'Application Status'] = new_status
        st.success("Application status updated successfully!")
    
# Navigation menu
menu = ["Application Form", "Admin Page"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Application Form":
    main()
elif choice == "Admin Page":
    admin_page()


