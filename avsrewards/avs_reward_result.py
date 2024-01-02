
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



# Operator Reward

def operator_reward(reward_portion_result, operator_percentage):
        return reward_portion_result * operator_percentage

operator_reward_result = operator_reward(reward_portion_result, operator_percentage)




if avs_total_staked != 0:
                staker_reward_result_perc = (staker_reward_result / avs_total_staked) * 100
                operator_reward_result_perc = (operator_reward_result / avs_total_staked) * 100

else:
                staker_reward_result_perc = 0.00
                operator_reward_result_perc = 0.00