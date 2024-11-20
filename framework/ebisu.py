import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set up the Streamlit page
st.set_page_config(page_title="AVS Dashboard", layout="wide")

# Function to fetch data from the AVS API
@st.cache_data(ttl=60)  # Cache the result for 60 seconds to limit API calls
def fetch_avs_data():
    url = "https://api.blockflow.network/rest/fbcc1fb0-7e72-4e5f-a711-879ee3e616ba/avs"
    headers = {"x-api-key": "your_api_key_here"}  # Replace with your actual API key
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return None

# Fetch data
avs_data = fetch_avs_data()

# Process and display the data
if avs_data and "data" in avs_data:
    # Extract the AVS data
    records = avs_data["data"]
    
    # Convert to a DataFrame for better handling
    df = pd.DataFrame(records)
    
    # Add a timestamp for the sidebar
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f"Last Updated: {timestamp}")
    
    # Display the raw data as a table
    st.write("### All Registered AVS Records")
    st.dataframe(df)

    # Example visualization: Total stakers per AVS
    if "metadataName" in df.columns and "totalStakers" in df.columns:
        fig = px.bar(df, x="metadataName", y="totalStakers", title="Total Stakers per AVS")
        st.plotly_chart(fig, use_container_width=True)

else:
    st.write("No data available to display.")
