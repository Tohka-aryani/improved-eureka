import streamlit as st
import pandas as pd

# Create a DataFrame to store the application data
data = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Address'])

# Streamlit application
def main():
    st.title("Application Form")

    # Display the form inputs
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_input("Address")

    # Submit button
    if st.button("Submit"):
        # Add the form inputs to the DataFrame
        data.loc[len(data)] = [name, email, phone, address]

        # Clear the form inputs
        st.text_input("Name", value='')
        st.text_input("Email", value='')
        st.text_input("Phone", value='')
        st.text_input("Address", value='')

    # Display the database table
    st.subheader("Application Database")
    st.dataframe(data)

if __name__ == "__main__":
    main()
