
import streamlit as st

from avs_tvl_totalstaked import selected_avs_tvl_total_staked_adjustment, selected_avs_total_staked
from avs_revenue import selected_avs_revenue_adjustment
from avs_audits import selected_avs_audits_adjustment
from avs_dual_staking import selected_avs_dual_staking_adjustment
from avs_type import selected_avs_type_adjustment


profit_percentage = 0.20
staker_percentage = 0.40
operator_percentage = 0.60


def reward_sum(selected_avs_tvl_total_staked_adjustment, selected_avs_revenue_adjustment, selected_avs_audits_adjustment, selected_avs_dual_staking_adjustment, selected_avs_type_adjustment):
        return selected_avs_tvl_total_staked_adjustment + selected_avs_revenue_adjustment + selected_avs_audits_adjustment + selected_avs_dual_staking_adjustment + selected_avs_type_adjustment

reward_result = reward_sum(selected_avs_tvl_total_staked_adjustment, selected_avs_revenue_adjustment, selected_avs_audits_adjustment,selected_avs_dual_staking_adjustment,selected_avs_type_adjustment)



def staker_reward(profit_percentage, staker_percentage):
        return selected_avs_revenue_adjustment * profit_percentage * staker_percentage

staker_reward_result = staker_reward(profit_percentage, staker_percentage)


def operator_reward(profit_percentage, operator_percentage):
        return selected_avs_revenue_adjustment * profit_percentage * operator_percentage

operator_reward_result = operator_reward(profit_percentage, operator_percentage)




if selected_avs_total_staked != 0:
                staker_reward_percentage = (staker_reward / selected_avs_total_staked) * 100
                operator_reward_percentage = (operator_reward / selected_avs_total_staked) * 100

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
                        <h2 style="color: black; margin:0; font-size: 1.5em;">Staker Reward: <span style="font-size: 1.2em;">{staker_reward_result:.2f}%</span></h2>
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
                                <h2 style="color: black; margin:0; font-size: 1.5em;">Operator Reward: <span style="font-size: 1.2em;">{operator_reward_result:.2f}%</span></h2>
                        </div>
                        """, 
                        unsafe_allow_html=True
                        )