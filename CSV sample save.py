import streamlit as st
import pandas as pd
import base64

# Set up the page layout
st.set_page_config(layout="wide")

# Create a title and subheader
st.title("GitHub CSV Data App")
st.subheader("Data Entry and Saving")

# Create a form to collect data
name = st.text_input("Enter a name")
age = st.number_input("Enter an age")
email = st.text_input("Enter an email")
submit = st.button("Add Entry")

# Load the existing data from GitHub CSV file
data_url = "https://raw.githubusercontent.com/<username>/<repository>/main/data.csv"
df = pd.read_csv(data_url)

# Display the existing data
st.subheader("Existing Data")
st.dataframe(df)

# Add new entry to the DataFrame
if submit:
    new_entry = {'Name': name, 'Age': age, 'Email': email}
    df = df.append(new_entry, ignore_index=True)
    st.success("New entry added successfully!")

# Save the updated data to a new CSV file
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
file_name = "data.csv"
href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)

if __name__ == '__main__':
    st.run_app()
