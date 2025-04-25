import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.write("File uploaded successfully!")
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Statistics")
    st.write(df.describe())

    st.subheader("Filter Data")
    column = df.columns.to_list()
    selected_column = st.selectbox("Select a column to filter", column)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a value to filter by", unique_values)
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", column)
    y_column = st.selectbox("Select Y-axis column", column)

    if st.button("Generate Plot Data"):
        st.line_chart(filtered_df[[x_column, y_column]])

else:
    st.write("Waiting for file upload...")
