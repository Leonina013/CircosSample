import streamlit as st
import pandas as pd

# Load the data
st.write("Add the csv file containing your data")
data = st.file_uploader("upload file", type={"csv", "txt"})
if data is not None:
    df = pd.read_csv(data)
st.write(df)

st.title("Data Visualization App")

# Create a selectbox to choose the visualization type
viz_type = st.selectbox("Select visualization type", ["Bar Chart", "Line Chart", "Scatter Plot"])

# Show the appropriate visualization based on the user's choice
if viz_type == "Bar Chart":
    st.bar_chart(data)
elif viz_type == "Line Chart":
    st.line_chart(data)
else:
    st.scatter_chart(data)
