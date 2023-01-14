import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv("data.csv")

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
