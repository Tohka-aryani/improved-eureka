import streamlit as st
import pandas as pd

# Define the application form fields
application_form = {
    'Name': '',
    'Email': '',
    'Twitch Status': '',
    'Application Status': ''
}

# Create a DataFrame to store the applications
database = pd.DataFrame(columns=application_form.keys())

# Dropdown options for Twitch Status
twitch_status_options = ['Affiliate', 'Partner', 'None']

# Dropdown options for Application Status
application_status_options = ['Pending', 'Accepted', 'Rejected']

# Define the Streamlit layout
def main():
    # Title of the application form
    st.title('Application Form')
    
    # Display the form fields
    with st.form(key='application_form'):
        col1, col2 = st.beta_columns(2)
        with col1:
            application_form['Name'] = st.text_input('Name')
            application_form['Email'] = st.text_input('Email')
        with col2:
            application_form['Twitch Status'] = st.selectbox('Twitch Status', twitch_status_options)
            application_form['Application Status'] = st.selectbox('Application Status', application_status_options)
        
        # Submit button
        submitted = st.form_submit_button('Submit')
    
    if submitted:
        # Append the form data to the database
        database.loc[len(database)] = application_form
        
        # Clear the form fields
        for field in application_form:
            application_form[field] = ''
    
    # Display the database
    st.title('Database')
    st.dataframe(database)
    
    # Display the editable page
    if st.sidebar.button('Edit Database'):
        edit_database()
        

# Editable page to update the database
def edit_database():
    st.title('Edit Database')
    
    # Display the database as a table with editable cells
    database_editable = database.copy()
    for column in database_editable.columns:
        database_editable[column] = database_editable[column].astype(str)
    st.dataframe(database_editable, editable=True)
    
    # Save changes to the database
    if st.button('Save Changes'):
        st.dataframe(database_editable)
        # You can update the original database here
    
    # Reset the database
    if st.button('Reset Database'):
        database_editable = pd.DataFrame(columns=application_form.keys())
        st.dataframe(database_editable)


if __name__ == '__main__':
    main()

