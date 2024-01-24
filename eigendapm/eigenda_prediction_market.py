
import streamlit as st
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


def map_to_multiplier(value, category):
    if category == "risk_score":
        return 2.5 if value > 6.66 else 0 if value > 3.33 else -2.5
    elif category == "tx_cost":
        # Here, we reverse the logic: Expensive transactions result in a higher multiplier
        return 2.5 if value == "Expensive" else 0 if value == "Medium" else -2.5
    elif category == "tx_throughput":
        return 2.5 if value == "Slow" else 0 if value == "Average" else -2.5
    elif category == "resol_time":
        today = datetime.today().date()
        event_date = today + timedelta(days=value)
        days_until_event = (event_date - today).days
        return 2.5 if days_until_event >= 540 else 0 if days_until_event >= 180 else -2.5 # in days


def calculate_odds(risk_score, transaction_cost, transaction_throughput, days_until_event, user_demand, amount_betted):
    risk_multiplier = map_to_multiplier(risk_score, "risk_score")
    cost_multiplier = map_to_multiplier(transaction_cost, "tx_cost")
    throughput_multiplier = map_to_multiplier(transaction_throughput, "tx_throughput")
    time_multiplier = map_to_multiplier(days_until_event, "resol_time")
    user_demand_multiplier = (50 - user_demand) / 10  # Centering and scaling the user demand

    # Constants for maximum, minimum, and base odds
    MAX_ODDS = 10
    MIN_ODDS = 1
    BASE_ODDS = 5

    # Calculate the combined impact of risk, cost, throughput, and time multipliers
    combined_multiplier = (risk_multiplier + cost_multiplier + throughput_multiplier + time_multiplier) / 4

    # Adjust the base odds based on the combined impact of the four variables
    adjusted_base_odds = BASE_ODDS + combined_multiplier

    # Adjust odds further based on user demand
    odds_a = adjusted_base_odds + user_demand_multiplier
    odds_b = adjusted_base_odds - user_demand_multiplier

    # Normalize odds to be within the range
    odds_a = max(min(odds_a, MAX_ODDS), MIN_ODDS)
    odds_b = max(min(odds_b, MAX_ODDS), MIN_ODDS)

    return odds_a, odds_b



# Streamlit app for prediction market scenario
def prediction_market_app():
    st.set_page_config(layout="wide")  # Make Streamlit app wide

    st.image("images/eigenda.jpeg")

    st.title("EigenDA: Presidential Election Prediction Market")

    with st.expander("How this Simulator Works"):
        st.markdown("""
            Odds in a traditional prediction market are influenced by bettors' preferences, volume of bets, and market liquidity for a particular event. 
            
            In the case of an **AVS as a source of truth** for a prediction market, the reliability and data processing capabilities of AVS' oracles also affect those odds.
                    Truth in this context is achieved based on the level of the associated risks and the economic security of that AVS, adding a layer of complexity to the odds calculation. 

            Potential returns distribution were also taken into account for every involved party: Winning bettors, EigenDA, Rio Network (LRT issuer), Rollup service, tokensight, Operators, and Restakers.
                            
            *P.S.*: The idea to build this simulator came from David Hoffman's [tweet](https://twitter.com/TrustlessState/status/1746114818845667736).
                        """)
        
    st.write("\n")
    st.write("\n")

    # Create two columns for input parameters
    col1, col2 = st.columns([1,1], gap="large")

    with col1:
        st.write("**AVS Metrics**")
        # AVS risk score as number input
        avs_risk_score = st.number_input("**EigenDA Risk Score**", 0.0, 10.0, 5.0, step=0.10, format="%.2f")
        st.write("\n")
        # Transaction cost as dropdown list
        transaction_cost = st.selectbox("**EigenDA Transaction Cost**", ["Expensive", "Medium", "Cheap"], index=1)
        st.write("\n")
        # Transaction throughput as dropdown list
        transaction_throughput = st.selectbox("**EigenDA Transaction Throughput**", ["Slow", "Average", "Fast"], index=1)

    with col2:
        st.write("**Event/Market Metrics**")

        # User's total amount betted every step 100k, with no decimals
        total_amount_betted = st.number_input("**User Total Amount Betted**", min_value=0, max_value=10000000, value=1000000, step=100000, format="%d")

        st.write(f"• Total Amount Betted: ${total_amount_betted:,.0f}")

        st.write("\n")

        # User demand for candidate A
        user_demand_a = st.slider("**Bettors' Demand for Candidate A (%)**", 0, 100, 50)

        st.write(f"• Bettors' Demand for Candidate A: *{user_demand_a}%*   |   • Bettors' Demand for Candidate B: *{100 - user_demand_a}%*")

        st.write("\n")

        # Days until event resolution as a calendar input
        today = datetime.today().date()
        event_date = st.date_input("**Event Resolution Date**", datetime(2024, 12, 31).date())
        days_until_event = (event_date - today).days if event_date > today else 0

        st.write(f"• Days until Event Resolution: {days_until_event} days")

    # Calculate and display potential returns based on odds
    st.write("### **Odds**")

    odds_a, odds_b = calculate_odds(avs_risk_score, transaction_cost, transaction_throughput, days_until_event, user_demand_a, total_amount_betted)

    st.write(f"*Odds for Candidate A*: **{odds_a:.2f}**")
    st.write(f"*Odds for Candidate B*: **{odds_b:.2f}**")

    st.write("\n")
    st.write("\n")

    st.write("### **Potential Returns**")

    st.write(f"***• Total Amount Betted***: *${total_amount_betted:,.0f}*")

    st.write("\n")

    st.write("Basing our calculations on the *Total Amount Betted*, let's assume that *50%* would be distributed to the **Winning Bettors**, to **EigenDA** *20%*, to **Operators** *12.5%*, to **Rio Network** (LRT protocol w/ reETH token) *7.5%*, to **Tokensight** *5%*, to the **Rollup Service** *4%*, and to **Restakers** *1%*.")
    
    st.write("\n")

    # Distribution percentages
    winning_bettors_pct = 50
    eigenda_pct = 20
    operators_pct = 12.5
    rio_pct = 7.5
    tokensight_pct = 5
    rollup_pct = 4
    restakers_pct = 1

    # Calculate distributions
    winning_bettors_amount = total_amount_betted * (winning_bettors_pct / 100)
    eigenda_amount = total_amount_betted * (eigenda_pct / 100)
    operators_amount = total_amount_betted * (operators_pct / 100)
    rio_amount = total_amount_betted * (rio_pct / 100)
    tokensight_amount = total_amount_betted * (tokensight_pct / 100)
    rollup_amount = total_amount_betted * (rollup_pct / 100)
    restakers_amount = total_amount_betted * (restakers_pct / 100)

    distributions = {
        "Winning Bettors": winning_bettors_amount,
        "EigenDA": eigenda_amount,
        "Operators": operators_amount,
        "Rio Network": rio_amount,
        "Tokensight": tokensight_amount,
        "Rollup Service": rollup_amount,
        "Restakers": restakers_amount
    }

    threshold = 5  # 5% threshold

    st.write("\n")

    # Create two columns
    col1, col2 = st.columns([1,1], gap= "large")

    # Display the pie chart in the first column
    with col1:

        blue_yellow_palette = [
            "#1f77b4",  # blue
            "#ff7f0e",  # yellow
            "#aec7e8",  # light blue
            "#ffbb78",  # light yellow
            "#7f7f7f",  # grey
            "#c7c7c7",  # light grey
            "#ffff00" # yellow
        ]

        fig, ax = plt.subplots(figsize=(8, 8))  # Increase figure size
        explode = [0.1 if value < threshold else 0 for value in distributions.values()]

        # Use '%.2f%%' for 2 decimals, and remove the '.00' if it's not needed
        autopct_format = lambda p: f'{p:.2f}%' if p % 1 != 0 else f'{p:.0f}%'
        wedge, texts, autotexts = ax.pie(distributions.values(), labels=distributions.keys(), autopct=autopct_format,
                                startangle=90, explode=explode, colors=blue_yellow_palette)

        # Adjust font size
        plt.setp(autotexts, size=8, weight="bold")
        plt.setp(texts, size=8)

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)


    # Display calculated amounts in the second column
    with col2:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

        st.write(f"**Winning Bettors**: ${winning_bettors_amount:,.0f}")
        st.write(f"**EigenDA**: ${eigenda_amount:,.0f}")
        st.write(f"**Operators**: ${operators_amount:,.0f}")
        st.write(f"**Rio Network**: ${rio_amount:,.0f}")
        st.write(f"**Tokensight**: ${tokensight_amount:,.0f}")
        st.write(f"**Rollup Service**: ${rollup_amount:,.0f}")
        st.write(f"**Restakers**: ${restakers_amount:,.0f}")



    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    col11, col12, col13 = st.columns([2,1,2])

    with col11:
        st.write("")

    with col12:
        st.image("images/tokensight.png", width=250)

    with col13:
        st.write("")
    
    
    image_url = 'https://img.freepik.com/free-vector/twitter-new-2023-x-logo-white-background-vector_1017-45422.jpg'
    link = 'https://twitter.com/tokensightxyz'
    markdown = f"""
    <a href="{link}" target="_blank">
        <img src="{image_url}" alt="Alt Text" style="display:block; margin-left: auto; margin-right: auto; width: 4%;">
    </a>
    """    
    st.markdown(markdown, unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    prediction_market_app()
