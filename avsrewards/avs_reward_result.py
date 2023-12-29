
import streamlit as st

from avs_reward_calculation_logic import avs_rewards, get_ratio_tvl_totalstaked_adjustment, get_avs_revenue_adjustment, get_audit_adjustment, get_dual_staking_adjustment, get_avs_type_adjustment
from avs_tvl_totalstaked import get_tvl_total_staked


def calculate_rewards(avs_revenue, total_staked, avs_type, number_of_audits):

        avs_revenue_adjustment = get_avs_revenue_adjustment(avs_revenue)
        ratio_tvl_totalstaked_adjustment = get_ratio_tvl_totalstaked_adjustment(total_staked)
        dual_staking_adjustment = get_dual_staking_adjustment(avs_type)
        avs_type_adjustment = get_avs_type_adjustment(avs_type)
        audit_adjustment = get_audit_adjustment(number_of_audits)
        avs_total_staked = get_tvl_total_staked()

        staker_reward, operator_reward = avs_rewards(avs_revenue_adjustment, ratio_tvl_totalstaked_adjustment, dual_staking_adjustment, avs_type_adjustment, audit_adjustment)


        if avs_total_staked != 0:
                staker_reward_percentage = (staker_reward / avs_total_staked) * 100
                operator_reward_percentage = (operator_reward / avs_total_staked) * 100

        else:
                staker_reward_percentage = 0.00
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
                        <h2 style="color: black; margin:0; font-size: 1.5em;">Staker Reward: <span style="font-size: 1.2em;">{staker_reward_percentage:.2f}%</span></h2>
                        </div>
                        """, 
                        unsafe_allow_html=True
                        )

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