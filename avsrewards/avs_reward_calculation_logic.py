
# AVS Rewards

import streamlit as st


# def avs_rewards(avs_revenue, avs_tvl, avs_total_staked, avs_token_percentage, xeth_percentage, avs_type, security_audits):
    
reward_percentage = 0.20

# Adjusting the base reward based on the AVS token and xETH balance
#dual_staking_balance_adjustment = (avs_token_percentage - xeth_percentage) / 100.0

def dual_staking_balance_adjustment(avs_token_percentage, xeth_percentage):
        ratio = avs_token_percentage / xeth_percentage

        if ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
            return 0.020
        elif ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
            return 0.015
        elif ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.010
        elif ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.005
        elif ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
            return 0  # Neutral adjustment for balanced scenario
        elif ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
            return -0.010
        elif ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
            return -0.015
        else:  # Very low AVS compared to ETH
            return -0.020
        # Higher ratio illustrates the greater weight of the $AVS token in the balance, risk that must be reflected in the reward calc

def calculate_dual_staking_adjustment(avs_token_percentage, xeth_percentage):
    return dual_staking_balance_adjustment(avs_token_percentage, xeth_percentage)



# AVS type adjustment

def avs_type_adjustment(avs_type):
    return 0.02 if avs_type == "Lightweight" else -0.02

def calculate_avs_type_adjustment(avs_type):
    return avs_type_adjustment(avs_type)




# Check the ratio of Total Staked to TVL

def ratio_tvl_totalstaked(avs_total_restaked, avs_tvl):
        
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

def calculate_ratio_tvl_totalstaked(avs_total_restaked, avs_tvl):
    return ratio_tvl_totalstaked(avs_total_restaked, avs_tvl)



# AVS Revenue

def avs_revenue_calc(avs_revenue):

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

def calculate_avs_revenue_calc(avs_revenue):
    return avs_revenue_calc(avs_revenue)




# Security Audits 

def security_audit_adjustment(number_of_audits):
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

def calculate_security_audit_adjustment(number_of_audits):
    return security_audit_adjustment(number_of_audits)


# Last portion:

# Reward Percentage Calculation
#reward_percentage = reward_percentage + dual_staking_adjustment + avs_type_adjustment + calculate_avs_revenue_calc + audit_adjustment + ratio_tvl_totalstaked_adjustment


# Ensure the reward percentage is within reasonable bounds
#reward_percentage = max(min(reward_percentage, 0.30), 0.10)

# Calculate rewards for stakers and operators
#profit_percentage = 0.20
#staker_percentage = 0.40
#operator_percentage = 0.60

#staker_reward = calculate_avs_revenue_calc * profit_percentage * reward_percentage * staker_percentage
#operator_reward = calculate_avs_revenue_calc * profit_percentage * reward_percentage * operator_percentage

#return staker_reward, operator_reward