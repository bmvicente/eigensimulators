import streamlit as st
import requests
import pandas as pd

# Function to fetch AVS data from the EigenExplorer API
@st.cache_data(ttl=60)  # Cache data for 60 seconds to optimize performance
def fetch_avs_data():
    url = "https://api.eigenexplorer.com/avs"
    params = {
        "withTVL": "true",                 # Request TVL data explicitly
        "withCuratedMetadata": "true",    # Include curated metadata
        "sortByTVL": "desc",              # Sort by TVL in descending order
        "take": 100                       # Number of records to fetch
    }
    headers = {"x-api-key": "your_api_key_here"}  # Replace with your actual API key

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch AVS data: {response.status_code}")
        return None

# Streamlit app
st.set_page_config(page_title="EigenExplorer: Raw AVS Data", layout="wide")
st.title("EigenExplorer: Raw AVS Data Table")

# Fetch and display the raw AVS data
avs_data = fetch_avs_data()
if avs_data and "data" in avs_data:
    # Convert the raw JSON data directly into a DataFrame
    avs_df = pd.DataFrame(avs_data["data"])

    # Check if TVL is present in the dataset
    if "tvl" in avs_df.columns:
        st.write("✅ TVL data is included in the results.")
    else:
        st.write("⚠️ TVL data is not included. Check the API response or query parameters.")

    # Display the raw DataFrame with all columns
    st.dataframe(avs_df, use_container_width=True)
else:
    st.write("No AVS data available to display.")
