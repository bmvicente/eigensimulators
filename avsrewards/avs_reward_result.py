

import streamlit as st
from avs_reward_calculation_logic import tvl_total_staked, tvl_total_staked_final, avs_total_staked, avs_revenue_final, avs_audits_final, dual_staking_final, avs_type_final



avs_total_staked, avs_tvl = tvl_total_staked()

reward_percentage = 0.20  # Base reward percentage

profit_percentage = 0.20
staker_percentage = 0.40
operator_percentage = 0.60



reward_percentage_adj = reward_percentage + avs_revenue_final + tvl_total_staked_final + avs_audits_final + dual_staking_final + avs_type_final

#reward_percentage_adj = max(min(reward_percentage, 0.30), 0.10)



# Reward Value Sum

def reward_portion(reward_percentage_adj, profit_percentage, avs_revenue_final):
        return avs_revenue_final * profit_percentage * reward_percentage_adj

reward_portion_result = reward_portion(reward_percentage_adj, profit_percentage, avs_revenue_final)




# Staker Reward

def staker_reward(reward_portion_result, staker_percentage):
        return reward_portion_result * staker_percentage

staker_reward_result = staker_reward(reward_portion_result, staker_percentage)


def calculate_staker_reward_perc(avs_total_staked, reward_portion_result, staker_percentage):
    if avs_total_staked != 0:
        return (reward_portion_result * staker_percentage) / avs_total_staked
    else:
        return 0.00





# Operator Reward

def operator_reward(reward_portion_result, operator_percentage):
        return reward_portion_result * operator_percentage

operator_reward_result = operator_reward(reward_portion_result, operator_percentage)


def calculate_operator_reward_perc(avs_total_staked, reward_portion_result, operator_percentage):
    if avs_total_staked != 0:
        return (reward_portion_result * operator_percentage) / avs_total_staked
    else:
        return 0.00