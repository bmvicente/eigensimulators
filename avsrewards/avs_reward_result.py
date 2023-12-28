
import streamlit as st

from avs_audits import avs_sec_audits
from avs_dual_staking import dual_staking
from avs_reward_calculation_logic import avs_rewards
from avs_revenue import revenue
from avs_tokenomics import tokenomics
from avs_tvl_totalstaked import tvl_total_staked, get_tvl_total_staked
from avs_type import type


def calculate_rewards():
        staker_reward, operator_reward = avs_rewards(revenue, tvl_total_staked, get_tvl_total_staked, dual_staking, type, avs_sec_audits)

        avs_total_staked = get_tvl_total_staked()  # Now it's defined in your main file's scope


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