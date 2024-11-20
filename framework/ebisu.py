import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set up the Streamlit page
st.set_page_config(page_title="Crypto Price Dashboard", layout="wide")

# Function to fetch data from the API
@st.cache_data(ttl=60)  # Cache the result for 60 seconds to limit API calls
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data. Please try again later.")
        return None

# Fetch data
crypto_data = fetch_crypto_data()

# Process and display the data
if crypto_data:
    # Convert data to a DataFrame
    df = pd.DataFrame.from_dict(crypto_data, orient="index").reset_index()
    df.columns = ["Cryptocurrency", "Price (USD)"]

    # Display the last update timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.sidebar.write(f"Last Updated: {timestamp}")

    # Show the current price of Bitcoin as a number
    bitcoin_price = crypto_data.get("bitcoin", {}).get("usd", "N/A")
    st.metric(label="Bitcoin Price (USD)", value=f"${bitcoin_price}")

    # Display a bar chart of all cryptocurrencies
    st.write("### Cryptocurrency Prices")
    fig = px.bar(df, x="Cryptocurrency", y="Price (USD)", title="Crypto Prices")
    st.plotly_chart(fig, use_container_width=True)

