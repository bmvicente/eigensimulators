
# AVS Rewards

from avs_audits import avs_sec_audits
from avs_dual_staking import dual_staking
from avs_revenue import revenue
from avs_tvl_totalstaked import tvl_total_staked
from avs_type import avs_type


# Adjusting the base reward based on the AVS token and xETH balance
#dual_staking_balance_adjustment = (avs_token_percentage - xeth_percentage) / 100.0

def calc_dual_staking(avs_token_percentage, xeth_percentage):
        dual_staking_ratio = avs_token_percentage / xeth_percentage

        if dual_staking_ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
            return 0.020
        elif dual_staking_ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
            return 0.015
        elif dual_staking_ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.010
        elif dual_staking_ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.005
        elif dual_staking_ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
            return 0  # Neutral adjustment for balanced scenario
        elif dual_staking_ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
            return -0.010
        elif dual_staking_ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
            return -0.015
        else:  # Very low AVS compared to ETH
            return -0.020
        # Higher ratio illustrates the greater weight of the $AVS token in the balance, risk that must be reflected in the reward calc

selected_avs_token_percentage, selected_xeth_percentage = dual_staking()

dual_staking_final = calc_dual_staking(selected_avs_token_percentage, selected_xeth_percentage)  



# AVS type adjustment

def calc_avs_type(avs_type):
    return 0.02 if avs_type == "Lightweight" else -0.02

selected_avs_type = avs_type()

# Use the selected_avs_type as an argument to calculate the reward adjustment
avs_type_final = calc_avs_type(selected_avs_type)




# Check the ratio of Total Staked to TVL

def calc_tvl_total_staked(avs_total_restaked, avs_tvl):
        
        if avs_tvl == 0:
            return 0
        
        ratio = (avs_total_restaked / 2) / avs_tvl

        if ratio > 2:
            return -0.03
        elif ratio > 1.5:
            return -0.02
        elif ratio > 1:
            return -0.01
        elif ratio == 1:
            return 0
        elif ratio < 1:
            return 0.01
        elif ratio < 0.5:
            return 0.02
        elif ratio < 0.25:
            return 0.03
        else:
             return 0
        # Higher ratio illustrates a greater total restaked, which contributes to greater security, thus lower rewards

selected_avs_tvl, selected_avs_total_staked = tvl_total_staked()

tvl_total_staked_final = calc_tvl_total_staked(selected_avs_tvl, selected_avs_total_staked)



# AVS Revenue

def calc_revenue(avs_revenue):

        # Revenue-based adjustment
        if avs_revenue > 100000000:  # Greater than $100M
            return 0.01
        elif avs_revenue > 50000000:  # Greater than $50M
            return 0.02
        elif avs_revenue > 20000000:  # Greater than $20M
            return 0.03
        elif avs_revenue > 5000000:   # Greater than $5M
            return 0.04
        elif avs_revenue > 1000000:   # Greater than $1M
            return 0.05
        else:
            return 0
        # Greater revenue assures greater AVS security, therefore a gradual reduction in the reward level as the revenue grows is sensible

selected_avs_revenue = revenue()

avs_revenue_final = calc_revenue(selected_avs_revenue)  # This will also render the selection box and explanation



# Security Audits 

def calc_avs_sec_sudits(number_of_audits):
        
        if number_of_audits == 5:
            return -0.025  # Lower reward for more audits
        elif number_of_audits == 4:
            return -0.01
        elif number_of_audits == 3:
             return 0
        elif number_of_audits == 2:
            return 0.01
        elif number_of_audits == 1:
            return 0.025  # Higher reward for fewer audits
        else:
            return 0  # Neutral adjustment for moderate number of audits

selected_number_audits = avs_sec_audits()

avs_audits_final = calc_avs_sec_sudits(selected_number_audits)
