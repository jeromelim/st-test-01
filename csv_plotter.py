# csv_plotter.py
import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(file_obj):
	return pd.read_csv(file_obj)

st.title("CSV Quick Plotter")

file = st.file_uploader("Upload your csv here", type="csv")
