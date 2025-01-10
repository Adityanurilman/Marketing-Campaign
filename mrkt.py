import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache_data
def load_data():
    file_path = 'marketing_campaign.csv'
    data = pd.read_csv(file_path, delimiter=';')
    return data

data = load_data()

# Title of the web app
st.title("Data Science Project: Marketing Campaign Analysis")
st.write("This is an interactive web application for analyzing marketing campaign data.")

# Show dataset in the app
st.subheader("Dataset Overview")
st.write(data.head())

# Show basic statistics
st.subheader("Dataset Statistics")
st.write(data.describe())

# Interactive filtering for user selection
st.subheader("Filter Data")
education_level = st.selectbox("Select Education Level", data['Education'].unique())
filtered_data = data[data['Education'] == education_level]

st.write(f"Showing data for education level: {education_level}")
st.write(filtered_data)

# Show distribution of income
st.subheader("Income Distribution")
fig, ax = plt.subplots()
sns.histplot(data['Income'], kde=True, ax=ax)
st.pyplot(fig)

# Correlation heatmap
st.subheader("Correlation Heatmap")
corr_matrix = data.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Visualize Marketing Campaign Responses
st.subheader("Marketing Campaign Responses")
response_counts = data[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']].sum()
st.bar_chart(response_counts)

# Additional analysis - Recency vs Income
st.subheader("Recency vs Income")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Recency', y='Income', ax=ax)
st.pyplot(fig)

# Sidebar for interactive options
st.sidebar.header("Filters")
marital_status = st.sidebar.selectbox("Select Marital Status", data['Marital_Status'].unique())
st.sidebar.write(f"Selected Marital Status: {marital_status}")
filtered_marital = data[data['Marital_Status'] == marital_status]
st.sidebar.write(filtered_marital)
