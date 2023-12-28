
import streamlit as st


staker_reward, operator_reward = avs_rewards(avs_revenue, avs_tvl, avs_total_staked, avs_token_percentage, xeth_percentage, avs_type, security_audits)        

if avs_total_staked != 0:
        staker_reward_percentage = (staker_reward / avs_total_staked) * 100
    else:
        staker_reward_percentage = 0.00

st.markdown(
    f"""
    <div style="
        border: 2px solid;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        margin: 10px 0;
        background-color: white;">
        <h2 style="color: black; margin:0; font-size: 1.5em;">Staker Reward: <span style="font-size: 1.2em;">{staker_reward_percentage:.2f}%</span></h2>
    </div>
    """, 
        unsafe_allow_html=True
        )


with col2:

    if avs_total_staked != 0:
        operator_reward_percentage = (operator_reward / avs_total_staked) * 100
    else:
        operator_reward_percentage = 0.00

    st.markdown(
        f"""
        <div style="
            border: 2px solid;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            margin: 10px 0;
            background-color: white;">
            <h2 style="color: black; margin:0; font-size: 1.5em;">Operator Reward: <span style="font-size: 1.2em;">{operator_reward_percentage:.2f}%</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
    )