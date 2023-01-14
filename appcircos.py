import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualization App", page_icon=":chart_with_upwards_trend:", layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Data Visualization App")

# Accept CSV file from user
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    # Read the CSV file
    data = pd.read_csv(file)

    # Show the data
    st.dataframe(data.head())

    # Create a selectbox to choose the visualization type
    viz_type = st.selectbox("Select visualization type", ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram", "Pie Chart"])

    # Show the appropriate visualization based on the user's choice
    if viz_type == "Bar Chart":
        # Get the columns to use for the X and Y axis
        x_col = st.selectbox("Select the column for the X axis", data.columns)
        y_col = st.selectbox("Select the column for the Y axis", data.columns)
        plt.barh(data[y_col], data[x_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()
    elif viz_type == "Line Chart":
        # Get the columns to use for the X and Y axis
        x_col = st.selectbox("Select the column for the X axis", data.columns)
        y_col = st.selectbox("Select the column for the Y axis", data.columns)
        plt.plot(data[x_col], data[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()

    elif viz_type == "Scatter Plot":
        # Get the columns to use for the X and Y axis
        x_col = st.selectbox("Select the column for the X axis", data.columns)
        y_col = st.selectbox("Select the column for the Y axis", data.columns)
        plt.scatter(data[x_col], data[y_col])
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        st.pyplot()
    elif viz_type == "Histogram":
        # Get the column to use for the X axis
        x_col1 = st.selectbox("Select the first column for the X axis", data.columns)
        x_col2 = st.selectbox("Select the second column for the X axis", data.columns)
        x_col3 = st.selectbox("Select the third column for the X axis", data.columns)
        y_col = st.selectbox("Select the column for the Y axis", data.columns)
   
    # Create the histogram
        plt.hist([data[x_col1], data[x_col2], data[x_col3], data[y_col]], stacked=True, label=[x_col1, x_col2, x_col3])
        plt.xlabel("X axis columns")
        plt.ylabel(y_col)
        plt.legend()
        st.pyplot()
    else:
        # Get the column to use for the Pie chart
        x_col = st.selectbox("Select the column for the Pie chart", data.columns)
        st.write("Pie chart of "+x_col)
        st.pyplot()
        data[x_col].value_counts().plot.pie(autopct='%1.1f%%')

else:
    st.warning("Please upload a CSV file.")
