
import streamlit as st

from avs_reward_calculation_logic import tvl_total_staked_final, selected_avs_total_staked, avs_revenue, avs_audits, dual_staking_ratio, avs_type_adjustment


reward_percentage = 0.20  # Base reward percentage

profit_percentage = 0.20
staker_percentage = 0.40
operator_percentage = 0.60

reward_percentage_adj = reward_percentage + tvl_total_staked_final + avs_audits + dual_staking_ratio + avs_type_adjustment

#reward_percentage_adj = max(min(reward_percentage, 0.30), 0.10)



# Reward Value Sum

def reward_portion(reward_percentage_adj, profit_percentage, selected_avs_revenue_adjustment):
        return selected_avs_revenue_adjustment * profit_percentage * reward_percentage_adj

reward_portion_result = reward_portion(reward_percentage_adj, profit_percentage, avs_revenue)



# Staker Reward

def staker_reward(reward_portion_result, staker_percentage):
        return reward_portion_result * staker_percentage

staker_reward_result = staker_reward(reward_portion_result, staker_percentage)



# Operator Reward

def operator_reward(reward_portion_result, operator_percentage):
        return reward_portion_result * operator_percentage

operator_reward_result = operator_reward(reward_portion_result, operator_percentage)




if selected_avs_total_staked != 0:
                staker_reward_result_perc = (staker_reward_result / selected_avs_total_staked) * 100
                operator_reward_result_perc = (operator_reward_result / selected_avs_total_staked) * 100

else:
                staker_reward_result_perc = 0.00
                operator_reward_result_perc = 0.00