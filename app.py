import streamlit as st
import pandas as pd
import os

# Set the title of the app
st.title("File Upload and Management App")

# Create a directory for uploaded files
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt"])

if uploaded_file is not None:
    # Save the uploaded file to the uploads directory
    file_path = os.path.join("uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name} successfully!")

    # Display the uploaded file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(file_path)
        st.write(df)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(file_path)
        st.write(df)
    else:
        st.text("File uploaded successfully!")

# List all uploaded files
st.subheader("Uploaded Files")
uploaded_files = os.listdir("uploads")
if uploaded_files:
    for file in uploaded_files:
        st.write(file)
        # Add a delete button
        if st.button(f"Delete {file}"):
            os.remove(os.path.join("uploads", file))
            st.success(f"Deleted {file} successfully!")
            st.experimental_rerun()
else:
    st.text("No files uploaded yet.")
