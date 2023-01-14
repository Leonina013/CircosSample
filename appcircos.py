import streamlit as st
import pycircos

# Data for the plot
data = [("chr1", 100, 200), ("chr2", 300, 400), ("chr3", 500, 600)]

st.title("Circos Plot")

st.pycircos.circos(data, ideogram_radius=0.6, track_radius=0.8)
