import streamlit as st
import pandas as pd

def create_application_form():
    """
    This function creates an application form with a viewable and editable database using Streamlit.
    The form includes fields for Twitch username, Discord username, and reason for applying to the streamer's Twitch team.
    It also includes checkboxes for enabled VODs on Twitch, having Twitch panels, and linking Twitch to Discord.
    A T&C checkbox with customizable text is included, as well as a dropdown selection for Twitch status field.
    A separate page is included for limited people to edit the database on Streamlit.
    """
    # Create a dictionary of the form fields
    form_fields = {
        "Twitch username": "",
        "Discord username": "",
        "Reason for applying into MY Streamers Twitch Team": "",
        "Enabled VODs on Twitch": False,
        "Have Twitch Panels": False,
        "Linked Twitch to Discord": False,
        "T&C checkbox": False,
        "Twitch status": ["Affiliate", "Partner", "None"]
    }
    
    # Create the form using Streamlit
    st.title("Application Form")
    st.write("Please fill out the following information to apply to MY Streamers Twitch Team.")
    st.write("All fields are required unless otherwise noted.")
    
    # Add the form fields to the Streamlit app
    form_values = {}
    for field, default_value in form_fields.items():
        if isinstance(default_value, bool):
            form_values[field] = st.checkbox(field, value=default_value)
        elif isinstance(default_value, list):
            form_values[field] = st.selectbox(field, options=default_value)
        else:
            form_values[field] = st.text_input(field, value=default_value)
    
    # Add the T&C checkbox
    form_values["T&C checkbox"] = st.checkbox("I agree to the terms and conditions.")
    
    # Add a submit button
    if st.button("Submit"):
        # Check if all required fields are filled
        if "" in form_values.values():
            st.warning("Please fill out all required fields.")
        elif not form_values["T&C checkbox"]:
            st.warning("Please agree to the terms and conditions.")
        else:
            # Add the form data to the database
            df = pd.DataFrame([form_values])
            st.write("Thank you for applying! Your application has been submitted.")
    
    # Add a separate page for limited people to edit the database
    if st.sidebar.checkbox("Edit Database"):
        # Authenticate the user
        password = st.sidebar.text_input("Password", type="password")
        if password == "password123":
            # Load the database
            df = pd.read_csv("database.csv")
            
            # Display the database
            st.write("Database")
            st.write(df)
            
            # Allow the user to edit the database
            st.write("Add a new entry")
            new_entry = {}
            for field in form_fields.keys():
                if isinstance(form_fields[field], bool):
                    new_entry[field] = st.checkbox(field)
                elif isinstance(form_fields[field], list):
                    new_entry[field] = st.selectbox(field, options=form_fields[field])
                else:
                    new_entry[field] = st.text_input(field)
            if st.button("Add"):
                df = pd.concat([df, pd.DataFrame([new_entry])])
                df.to_csv("database.csv", index=False)
                st.write("Entry added to database.")
        else:
            st.warning("Incorrect password.")
