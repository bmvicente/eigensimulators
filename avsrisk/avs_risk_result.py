
import streamlit as st


def calculate_operator_attack_risk(total_restaked, tvl):
        # High risk if either TVL or total restaked is below $50,000
        if tvl < 100000 or total_restaked < 100000:
            return 10
        
        default_minimum_risk = 9

        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, moderate risk
        elif ratio > 0.5:
            return 5  # Less than TVL but not by a wide margin, increased risk
        else:
            return 7

    
operator_attack_risk = calculate_operator_attack_risk(total_restaked, tvl)

st.write("  \n")
st.write("  \n")

risk_score = avs_risk(security_audits, business_model, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation)


if risk_score >= 7.5:
        color = "#d32f2f"  # Red color for high risk
        background_color = "#fde0dc"  # Light red background
elif risk_score <= 2.5:
        color = "#388e3c"  # Green color for low risk
        background_color = "#ebf5eb"  # Light green background
else:
        color = "black"  # Black color for medium risk
        background_color = "#ffffff"  # White background


st.markdown(
    f"""
    <div style="
        border: 2px solid {color};
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        margin: 10px 0;
        background-color: {background_color};">
        <h2 style="color: black; margin:0; font-size: 1.5em;">AVS Risk Score: <span style="font-size: 1.2em; color: {color};">{risk_score:.2f}</span></h2>
    </div>
    """, 
    unsafe_allow_html=True
    )