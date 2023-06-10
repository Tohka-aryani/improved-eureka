import streamlit as st
import pandas as pd
import git

# Form
name = st.text_input("Name")
age = st.number_input("Age")
submit = st.button("Submit")

if submit:
    # Create DataFrame
    data = {'Name': [name], 'Age': [age]}
    df = pd.DataFrame(data)

    # Save as CSV
    df.to_csv('data.csv', index=False)

    # Clone GitHub repository
    git.Repo.clone_from('https://github.com/Tohka-aryani/improved-eureka/tree/main', 'local_repo')

    # Move CSV to repository folder
    repo_path = 'local_repo'
    file_path = 'data.csv'
    new_file_path = f'{repo_path}/{file_path}'
    shutil.move(file_path, new_file_path)

    # Commit and push changes
    repo = git.Repo(repo_path)
    repo.git.add(new_file_path)
    repo.git.commit('-m', 'Added data.csv')
    repo.git.push()
