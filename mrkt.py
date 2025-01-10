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
# Explanation of columns  
st.subheader("Column Explanations")  
explanations = {  
    "AcceptedCmp1": "1 if customer accepted the offer in the 1st campaign, 0 otherwise",  
    "AcceptedCmp2": "1 if customer accepted the offer in the 2nd campaign, 0 otherwise",  
    "AcceptedCmp3": "1 if customer accepted the offer in the 3rd campaign, 0 otherwise",  
    "AcceptedCmp4": "1 if customer accepted the offer in the 4th campaign, 0 otherwise",  
    "AcceptedCmp5": "1 if customer accepted the offer in the 5th campaign, 0 otherwise",  
    "Response": "1 if customer accepted the offer in the last campaign, 0 otherwise",  
    "Complain": "1 if customer complained in the last 2 years",  
    "DtCustomer": "Date of customer’s enrolment with the company",  
    "Education": "Customer’s level of education",  
    "Marital": "Customer’s marital status",  
    "Kidhome": "Number of small children in customer’s household",  
    "Teenhome": "Number of teenagers in customer’s household",  
    "Income": "Customer’s yearly household income",  
    "MntFishProducts": "Amount spent on fish products in the last 2 years",  
    "MntMeatProducts": "Amount spent on meat products in the last 2 years",  
    "MntFruits": "Amount spent on fruits products in the last 2 years",  
    "MntSweetProducts": "Amount spent on sweet products in the last 2 years",  
    "MntWines": "Amount spent on wine products in the last 2 years",  
    "MntGoldProds": "Amount spent on gold products in the last 2 years",  
    "NumDealsPurchases": "Number of purchases made with discount",  
    "NumCatalogPurchases": "Number of purchases made using catalogue",  
    "NumStorePurchases": "Number of purchases made directly in stores",  
    "NumWebPurchases": "Number of purchases made through company’s web site",  
    "NumWebVisitsMonth": "Number of visits to company’s web site in the last month",  
    "Recency": "Number of days since the last purchase"  
}  
  
for column, explanation in explanations.items():  
    st.write(f"**{column}:** {explanation}")    
  
# Title of the web app  
st.title("Data Science Project: Marketing Campaign Analysis")  
st.write("This is an interactive web application for analyzing marketing campaign data.")  
  
# Show dataset in the app  
st.subheader("Dataset Overview")  
st.write(data.head())  
  
# Show basic statistics  
st.subheader("Dataset Statistics")  
st.write(data.describe())  
  
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
  
# Show filtered data  
st.subheader("Filtered Data")  
st.write(filtered_data)  
  
# Allow users to download the filtered data  
csv = filtered_data.to_csv(index=False)  
st.download_button(  
    label="Download Filtered Data as CSV",  
    data=csv,  
    file_name='filtered_data.csv',  
    mime='text/csv'  
)  
  
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
