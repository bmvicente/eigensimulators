
import streamlit as st

from avs_tvl_totalstaked import selected_avs_tvl_total_staked_adjustment, selected_avs_total_staked
from avs_revenue import selected_avs_revenue_adjustment
from avs_audits import selected_avs_audits_adjustment
from avs_dual_staking import selected_avs_dual_staking_adjustment
from avs_type import selected_avs_type_adjustment


reward_percentage = 0.20  # Base reward percentage

profit_percentage = 0.20
staker_percentage = 0.40
operator_percentage = 0.60


reward_percentage = reward_percentage + selected_avs_dual_staking_adjustment + selected_avs_type_adjustment + selected_avs_revenue_adjustment + selected_avs_audits_adjustment + selected_avs_tvl_total_staked_adjustment

reward_percentage_adj = max(min(reward_percentage, 0.30), 0.10)


def reward_sum(reward_percentage_adj, profit_percentage, selected_avs_tvl_total_staked_adjustment, selected_avs_revenue_adjustment, selected_avs_audits_adjustment, selected_avs_dual_staking_adjustment, selected_avs_type_adjustment):
        return reward_percentage_adj + profit_percentage + selected_avs_tvl_total_staked_adjustment + selected_avs_revenue_adjustment + selected_avs_audits_adjustment + selected_avs_dual_staking_adjustment + selected_avs_type_adjustment

reward_result = reward_sum(reward_percentage_adj, profit_percentage, selected_avs_tvl_total_staked_adjustment, selected_avs_revenue_adjustment, selected_avs_audits_adjustment,selected_avs_dual_staking_adjustment,selected_avs_type_adjustment)



def staker_reward(reward_percentage_adj, profit_percentage, staker_percentage):
        return selected_avs_revenue_adjustment * reward_percentage_adj * profit_percentage * staker_percentage

staker_reward_result = staker_reward(reward_percentage_adj, profit_percentage, staker_percentage)


def operator_reward(reward_percentage_adj, profit_percentage, operator_percentage):
        return selected_avs_revenue_adjustment * reward_percentage_adj * profit_percentage * operator_percentage

operator_reward_result = operator_reward(reward_percentage_adj, profit_percentage, operator_percentage)




#if selected_avs_total_staked != 0:
#                staker_reward_result = (staker_reward / selected_avs_total_staked) * 100
#                operator_reward_result = (operator_reward / selected_avs_total_staked) * 100

#else:
#                staker_reward_result = 0.00
#                operator_reward_result = 0.00