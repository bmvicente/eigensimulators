
import streamlit as st

# Function to calculate AVS risk
def avs_risk(security_audits, business_model, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation):
    # Define the risk scores for each metric (0-10 scale, 10 being riskiest)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 0}
    business_model_risk = {"Pure Wallet": 10, "Fee Tokenization": 7, "AVS Native Token": 4, "Dual Staking (ETH & $AVS)": 1}
    avs_type_risk = {"Lightweight": 10, "Hyperscale": 1}
    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}

    security_audits_weight = 4 * 4                  # Likelihood 4, Impact 4
    business_model_weight = 2 * 3                   # Likelihood 2, Impact 3
    avs_type_weight = 1 * 2                         # Likelihood 2, Impact 2
    restaking_mods_weight = 2 * 3                   # Likelihood 2, Impact 3
    operator_attack_weight = 3 * 5                  # Likelihood 3, Impact 5
    avs_avg_operator_reputation_weight = 1 * 1      # Likelihood 1, Impact 1
    #CVS and CVL based and 51% operator attack dependant

    # Get risk scores from the input values
    security_audit_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    avs_type_score = avs_type_risk[avs_type]
    restaking_mod_score = restaking_mods_risk[restaking_mods]
    avs_avg_operator_reputation_score = avs_avg_operator_reputation_risk[avs_avg_operator_reputation]

    # Now use operator_attack_risk in your total risk score calculation
    total_risk_score = (security_audit_score * security_audits_weight +
                        business_model_score * business_model_weight +
                        avs_type_score * avs_type_weight +
                        operator_attack_risk * operator_attack_weight +  # Use the calculated risk score directly
                        restaking_mod_score * restaking_mods_weight +
                        avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight
                        )

    max_security_audit_score = 10  # Assuming worst case for security audit is 0 audits
    max_business_model_score = 10   # Assuming worst case for business model is "Pure Wallet"
    max_avs_type_score = 10         # Assuming worst case for AVS type is "Hyperscale"
    max_restaking_mod_score = 10    # Assuming worst case for restaking modality is "LST LP Restaking"
    max_operator_attack_score = 10  # Assuming worst case for operator attack risk
    max_avs_avg_operator_reputation_score = 10  # Assuming worst case for operator attack risk

    # Calculate the maximum possible risk score
    max_possible_risk_score = (
        max_security_audit_score * security_audits_weight +
        max_business_model_score * business_model_weight +
        max_avs_type_score * avs_type_weight +
        max_operator_attack_score * operator_attack_weight +
        max_restaking_mod_score * restaking_mods_weight +
        max_avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight)

    # Normalize the risk score
    normalized_risk_score = (total_risk_score / max_possible_risk_score) * 10
    normalized_risk_score = round(normalized_risk_score, 2)

    return normalized_risk_score