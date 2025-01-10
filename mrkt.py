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
  
# Check if required columns exist  
required_columns = ['Education', 'Marital_Status', 'Year_Birth']  
for col in required_columns:  
    if col not in data.columns:  
        st.error(f"Column '{col}' is missing from the dataset.")  
        st.stop()  
  
# Multi-filter for user selection  
st.subheader("Filter Data")  
education_level = st.multiselect("Select Education Level", data['Education'].unique())  
marital_status = st.multiselect("Select Marital Status", data['Marital_Status'].unique())  
birth_years = st.multiselect("Select Birth Year", data['Year_Birth'].unique())  
  
# Apply filters with error handling  
filtered_data = data[  
    (data['Education'].isin(education_level) if education_level else True) &  
    (data['Marital_Status'].isin(marital_status) if marital_status else True) &  
    (data['Year_Birth'].isin(birth_years) if birth_years else True)  
]  
  
st.write(f"Filtered data: {filtered_data.shape[0]} rows")  
  
# Show distribution of income based on filters  
st.subheader("Income Distribution")  
fig, ax = plt.subplots()  
sns.histplot(filtered_data['Income'], kde=True, ax=ax)  
st.pyplot(fig)  
  
# Correlation heatmap  
st.subheader("Correlation Heatmap")  
  
# Ensure all columns are numeric and handle NaN values  
numeric_data = filtered_data.select_dtypes(include=[float, int]).fillna(0)  
if not numeric_data.empty:  
    corr_matrix = numeric_data.corr()  
  
    fig, ax = plt.subplots(figsize=(10, 8))  
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)  
    st.pyplot(fig)  
else:  
    st.write("No numeric data available for correlation.")  
  
# Visualize Marketing Campaign Responses  
st.subheader("Marketing Campaign Responses")  
response_counts = filtered_data[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']].sum()  
st.bar_chart(response_counts)  
  
# Additional analysis - Recency vs Income  
st.subheader("Recency vs Income")  
fig, ax = plt.subplots()  
sns.scatterplot(data=filtered_data, x='Recency', y='Income', ax=ax)  
st.pyplot(fig)  
