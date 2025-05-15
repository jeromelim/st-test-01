# csv_plotter.py
import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(file_obj):
	return pd.read_csv(file_obj)

st.title("CSV Quick Plotter")
st.sidebar.title("CSV Uploader")
uploaded_file = st.sidebar.file_uploader("Upload your csv here", type="csv")
if 'df' not in st.session_state:
	st.session_state.df = None
if 'data_source_name' not in st.session_state:
	st.session_state.data_source_name = None

if uploaded_file is not None:
	if st.session_state.data_source_name is not uploaded_file.name:
		st.session_state.df = load_csv(uploaded_file)
		st.session_state.data_source_name = uploaded_file.name
	df = st.session_state.df
	st.sidebar.success(f"'{uploaded_file.name}' loaded!")
else:
	df = st.session_state.df
#if uploaded_file is not None:
df = st.session_state.df
if df is not None:
	st.header("Data Preview")
	st.dataframe(df)
	st.header("Create a plot")
	columns = df.columns.tolist()
	numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
	
	if not numeric_columns:
		st.warning("No numeric columns for plotting in data")
	else:
		col1, col2 = st.columns(2)
	with col1:
		x_axis = st.selectbox("Select x-axis", columns)
	with col2:
		y_axis = st.selectbox("Select y-axis", numeric_columns)
	plot_type = st.radio("Select plot type:", ("Bar Chart", "Line Chart"), horizontal=True)
	
	if x_axis and y_axis:
		st.subheader(f"{plot_type} of {x_axis} and {y_axis}")
		if plot_type == 'Bar Chart':
			if df[x_axis].dtype == 'object' and df[x_axis].nunique() < 20:
				st.bar_chart(df.groupby(x_axis)[y_axis].mean())
		if plot_type == 'Line Chart':
			chart_data = df.sort_values(by=x_axis)
			st.line_chart(chart_data.set_index(x_axis)[y_axis])

	with st.expander("View Data Summary"):
		st.write("**Shape:**", df.shape)
		st.write("**Columns:**", df.columns.tolist())
		st.write("**Data Types:**")
		st.dataframe(df.dtypes)
		st.dataframe(df.describe(include='all'))
	st.header("Filter Columns")
	columns = st.multiselect("Select columns", options=numeric_columns)
else:
	st.info("Upload a csv file to get started")
# st.table(df)
# st.bar_chart(df)
# st.line_chart(df)
Could you share some examples of what you think are impressive use of stream