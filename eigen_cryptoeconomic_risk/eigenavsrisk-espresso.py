


import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
validator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
code_complexity_risk = {"High": 10, "Medium": 5, "Low": 2}
operator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
validator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
operator_entrenchment_level_risk = {"High Entrenchment": 10, "Moderate Entrenchment": 5, "Low Entrenchment": 1}
dvt_mec_risk = {True: 1, False: 10}
tee_mec_risk = {True: 1, False: 10}

encrypted_mempool_risk = {True: 1, False: 10}
pbs_risk = {True: 1, False: 10}
sequencer_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
dual_quorum_risk = {True: 1, False: 10}

kzg_erasure_coding_risk = {True: 1, False: 10}
kzg_multi_proofs_risk = {True: 1, False: 10}
disperser_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
disperser_operator_risk = {"Disperser Run by Rollup": 8, "Disperser Run by Third-Party (like EigenLabs)": 2}
proof_custody_risk = {True: 1, False: 10}
direct_unicast_risk = {True: 1, False: 10}
kzg_poly_comm_risk = {True: 1, False: 10}
rollup_censorship_res_risk = {True: 1, False: 10}
fhe_disperser_risk = {"None": 7, "Partial": 5, "Full": 3}
fhe_operator_risk = {"None": 7, "Partial": 5, "Full": 3}
dual_quorum_risk = {True: 1, False: 10}


def eigenda_risk(security_audits, business_model, code_complexity, operator_reputation, operator_centralization, 
                 operator_entrenchment_level, tee_mec, dvt_mec, validator_reputation, validator_centralization,
                 bls_alt, rollup_fast_proof, disperser_centralization, kzg_erasure_coding, 
                 kzg_multi_proofs, disperser_operator, proof_custody, direct_unicast,
                 kzg_poly_comm, rollup_censorship_res, fhe_disperser, fhe_operator, dual_quorum):

    security_audits_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    code_complexity_score = code_complexity_risk[code_complexity]
    operator_reputation_score = operator_reputation_risk[operator_reputation]
    operator_centralization_score = operator_centralization_risk[operator_centralization]
    operator_entrenchment_level_score = operator_entrenchment_level_risk[operator_entrenchment_level]
    tee_mec_score = tee_mec_risk[tee_mec]
    dvt_mec_score = dvt_mec_risk[dvt_mec]
    validator_reputation_score = validator_reputation_risk[validator_reputation]
    validator_centralization_score = validator_centralization_risk[validator_centralization]

    disperser_centralization_score = disperser_centralization_risk[disperser_centralization]
    kzg_erasure_coding_score = kzg_erasure_coding_risk[kzg_erasure_coding]
    kzg_multi_proofs_score = kzg_multi_proofs_risk[kzg_multi_proofs]
    disperser_operator_score = disperser_operator_risk[disperser_operator]
    proof_custody_score = proof_custody_risk[proof_custody]
    direct_unicast_score = direct_unicast_risk[direct_unicast]
    kzg_poly_comm_score = kzg_poly_comm_risk[kzg_poly_comm]
    rollup_censorship_res_score = rollup_censorship_res_risk[rollup_censorship_res]
    fhe_disperser_score = fhe_disperser_risk[fhe_disperser]
    fhe_operator_score = fhe_operator_risk[fhe_operator]
    dual_quorum_score = dual_quorum_risk[dual_quorum]


    return (security_audits_score, business_model_score, code_complexity_score, operator_reputation_score, operator_centralization_score,
            operator_entrenchment_level_score, tee_mec_score, dvt_mec_score, validator_reputation_score, validator_centralization_score, 
            bls_alt_score, rollup_fast_proof_score, disperser_centralization_score, kzg_erasure_coding_score, kzg_multi_proofs_score, 
            disperser_operator_score, proof_custody_score, direct_unicast_score, kzg_poly_comm_score,
            rollup_censorship_res_score, fhe_disperser_score, fhe_operator_score, dual_quorum_score)







def main():
    st.set_page_config(layout="wide")

    #st.image("images/eigenda.jpeg", width=250)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Data Availability AVS: EigenDA Underlying Risk & Slashing Conditions Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
            The Simulator takes 9 AVS-generic parameters and 23 parameters that specifically compose an Data Availability AVS, with a BFT consensus architecture, to calculate EigenDA's Risk Score as an EigenLayer AVS. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            
            Most of the research to build this Simulator was derived from [EigenDA's Docs](https://docs.omni.network/) and [CometBFT's Docs](https://docs.cometbft.com/v0.37/), as well as the images in the "Logic" dropdowns.
                                                """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate Risk Profile for EigenDA as a Data Availability AVS. *It is important to bear in mind that since we are at the very early stages of AVS development and little-to-no information is available, the value judgements below are prone to being faulty.*")

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    st.subheader("**UNDERLYING RISK**")

    st.write("  \n")

    def dual_staking_balance_calc(avs_token_percentage, xeth_percentage):
        ratio = avs_token_percentage / xeth_percentage

        if ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
            return 9
        elif ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
            return 8
        elif ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 7
        elif ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 6
        elif ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
            return 5 # Neutral adjustment for balanced scenario
        elif ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
            return 4
        elif ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
            return 3
        else:  # Very low AVS compared to ETH
            return 2

    def validator_performance_acc_rate_calc(validator_performance_acc_rate):
        if 0 <= validator_performance_acc_rate <= 10:
            return 9
        elif 11 <= validator_performance_acc_rate <= 33:
            return 7.5
        elif 34 <= validator_performance_acc_rate <= 50:
            return 6
        elif 51 <= validator_performance_acc_rate <= 66:
            return 4
        elif 67 <= validator_performance_acc_rate <= 90:
            return 3
        elif 91 <= validator_performance_acc_rate <= 100:
            return 2
        else:
            return None


    def disperser_performance_acc_rate_calc(disperser_performance_acc_rate):
        if 0 <= disperser_performance_acc_rate <= 10:
            return 9
        elif 11 <= disperser_performance_acc_rate <= 33:
            return 7.5
        elif 34 <= disperser_performance_acc_rate <= 50:
            return 6
        elif 51 <= disperser_performance_acc_rate <= 66:
            return 4
        elif 67 <= disperser_performance_acc_rate <= 90:
            return 3
        elif 91 <= disperser_performance_acc_rate <= 100:
            return 2
        else:
            return None

    def kzg_encoding_rate_calc(kzg_encoding_rate):
        if 0 <= kzg_encoding_rate <= 10:
            return 9
        elif 11 <= kzg_encoding_rate <= 33:
            return 7.5
        elif 34 <= kzg_encoding_rate <= 50:
            return 6
        elif 51 <= kzg_encoding_rate <= 66:
            return 4
        elif 67 <= kzg_encoding_rate <= 90:
            return 3
        elif 91 <= kzg_encoding_rate <= 100:
            return 2
        else:
            return None


    def coverage_perc_calc(coverage_perc):
        if 0 <= coverage_perc <= 10:
            return 9
        elif 11 <= coverage_perc <= 33:
            return 7.5
        elif 34 <= coverage_perc <= 50:
            return 6
        elif 51 <= coverage_perc <= 66:
            return 4
        elif 67 <= coverage_perc <= 90:
            return 3
        elif 91 <= coverage_perc <= 100:
            return 2
        else:
            return None
        
    def perc_light_nodes_calc(perc_light_nodes):
        if 0 <= perc_light_nodes <= 10:
            return 9
        elif 11 <= perc_light_nodes <= 33:
            return 7.5
        elif 34 <= perc_light_nodes <= 50:
            return 6
        elif 51 <= perc_light_nodes <= 66:
            return 4
        elif 67 <= perc_light_nodes <= 90:
            return 3
        elif 91 <= perc_light_nodes <= 100:
            return 2
        else:
            return None
    
    def rollup_blob_rate_calc(rollup_blob_rate):
        if 0 <= rollup_blob_rate <= 10:
            return 9
        elif 11 <= rollup_blob_rate <= 33:
            return 7.5
        elif 34 <= rollup_blob_rate <= 50:
            return 6
        elif 51 <= rollup_blob_rate <= 66:
            return 4
        elif 67 <= rollup_blob_rate <= 90:
            return 3
        elif 91 <= rollup_blob_rate <= 100:
            return 2
        else:
            return None

    def rollup_bandwidth_rate_calc(rollup_bandwidth_rate):
        if 0 <= rollup_bandwidth_rate <= 10:
            return 9
        elif 11 <= rollup_bandwidth_rate <= 33:
            return 7.5
        elif 34 <= rollup_bandwidth_rate <= 50:
            return 6
        elif 51 <= rollup_bandwidth_rate <= 66:
            return 4
        elif 67 <= rollup_bandwidth_rate <= 90:
            return 3
        elif 91 <= rollup_bandwidth_rate <= 100:
            return 2
        else:
            return None 

    def rollup_backup_disperser_calc(rollup_backup_disperser):
        if 0 <= rollup_backup_disperser <= 10:
            return 9
        elif 11 <= rollup_backup_disperser <= 33:
            return 7.5
        elif 34 <= rollup_backup_disperser <= 50:
            return 6
        elif 51 <= rollup_backup_disperser <= 66:
            return 4
        elif 67 <= rollup_backup_disperser <= 90:
            return 3
        elif 91 <= rollup_backup_disperser <= 100:
            return 2
        else:
            return None
        


    if 'business_model' not in st.session_state:
        st.session_state.business_model = "Dual Staking Utility"
    if 'business_model_score' not in st.session_state:
        if st.session_state.business_model in business_model_risk:
            st.session_state.business_model_score = business_model_risk[st.session_state.business_model]
        else:
            st.session_state.business_model_score = 0

    if 'code_complexity' not in st.session_state:
        st.session_state.code_complexity = "High"
    if 'code_complexity_score' not in st.session_state:
        if st.session_state.code_complexity in code_complexity_risk:
            st.session_state.code_complexity_score = code_complexity_risk[st.session_state.code_complexity]
        else:
            st.session_state.code_complexity_score = 0

    if 'security_audits' not in st.session_state:
        st.session_state.security_audits = "2"
    if 'security_audits_score' not in st.session_state:
        if st.session_state.security_audits in security_audits_risk:
            st.session_state.security_audits_score = security_audits_risk[st.session_state.security_audits]
        else:
            st.session_state.security_audits_score = 0

    if 'operator_reputation' not in st.session_state:
        st.session_state.operator_reputation = "Unknown"
    if 'operator_reputation_score' not in st.session_state:
        if st.session_state.operator_reputation in operator_reputation_risk:
            st.session_state.operator_reputation_score = operator_reputation_risk[st.session_state.operator_reputation]
        else:
            st.session_state.operator_reputation_score = 0


    if 'operator_centralization' not in st.session_state:
        st.session_state.operator_centralization = "Centralized"  # Set default value
    if 'operator_centralization_score' not in st.session_state:
        if st.session_state.operator_centralization in operator_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.operator_centralization_score = operator_centralization_risk[st.session_state.operator_centralization]
        else:
            st.session_state.operator_centralization_score = 0

    if 'validator_centralization' not in st.session_state:
        st.session_state.validator_centralization = "Centralized"  # Set default value
    if 'validator_centralization_score' not in st.session_state:
        if st.session_state.validator_centralization in validator_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_centralization_score = validator_centralization_risk[st.session_state.validator_centralization]
        else:
            st.session_state.validator_centralization_score = 0


    if 'validator_reputation' not in st.session_state:
        st.session_state.validator_reputation = "Unknown"  # Set default value
    if 'validator_reputation_score' not in st.session_state:
        if st.session_state.validator_reputation in validator_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_reputation_score = validator_reputation_risk[st.session_state.validator_reputation]
        else:
            st.session_state.validator_reputation_score = 0

    if 'dvt_mec' not in st.session_state:
        st.session_state.dvt_mec = "False"  # Set default value
    if 'dvt_mec_score' not in st.session_state:
        if st.session_state.dvt_mec in dvt_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.dvt_mec_score = dvt_mec_risk[st.session_state.dvt_mec]
        else:
            st.session_state.dvt_mec_score = 0

    if 'operator_entrenchment_level' not in st.session_state:
        st.session_state.operator_entrenchment_level = "High Entrenchment"  # Set default value
    if 'operator_entrenchment_level_score' not in st.session_state:
        if st.session_state.operator_entrenchment_level in operator_entrenchment_level_risk:  # Check if code complexity exists in the dictionary
            st.session_state.operator_entrenchment_level_score = operator_entrenchment_level_risk[st.session_state.operator_entrenchment_level]
        else:
            st.session_state.operator_entrenchment_level_score = 0

    if 'bls_alt_score' not in st.session_state:
        st.session_state.bls_alt = "True"  # Set default value
    if 'bls_alt_score' not in st.session_state:
        if st.session_state.bls_alt in bls_alt_risk:  # Check if code complexity exists in the dictionary
            st.session_state.bls_alt_score = bls_alt_risk[st.session_state.bls_alt]
        else:
            st.session_state.bls_alt_score = 0

    if 'tee_mec_score' not in st.session_state:
        st.session_state.tee_mec = "False"  # Set default value
    if 'tee_mec_score' not in st.session_state:
        if st.session_state.tee_mec in tee_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.tee_mec_score = tee_mec_risk[st.session_state.tee_mec]
        else:
            st.session_state.tee_mec_score = 0

    if 'rollup_fast_proof' not in st.session_state:
        st.session_state.rollup_fast_proof = "True"
    if 'rollup_fast_proof_score' not in st.session_state:
        if st.session_state.rollup_fast_proof in rollup_fast_proof_risk:
            st.session_state.rollup_fast_proof_score = rollup_fast_proof_risk[st.session_state.rollup_fast_proof]
        else:
            st.session_state.rollup_fast_proof_score = 0

    if 'disperser_centralization' not in st.session_state:
        st.session_state.disperser_centralization = "Centralized"
    if 'disperser_centralization_score' not in st.session_state:
        if st.session_state.disperser_centralization in disperser_centralization_risk:
            st.session_state.disperser_centralization_score = disperser_centralization_risk[st.session_state.disperser_centralization]
        else:
            st.session_state.disperser_centralization_score = 0

    if 'kzg_erasure_coding' not in st.session_state:
        st.session_state.kzg_erasure_coding = "True"
    if 'kzg_erasure_coding_score' not in st.session_state:
        if st.session_state.kzg_erasure_coding in kzg_erasure_coding_risk:
            st.session_state.kzg_erasure_coding_score = kzg_erasure_coding_risk[st.session_state.kzg_erasure_coding]
        else:
            st.session_state.kzg_erasure_coding_score = 0

    if 'kzg_multi_proofs' not in st.session_state:
        st.session_state.kzg_multi_proofs = "True"
    if 'kzg_multi_proofs_score' not in st.session_state:
        if st.session_state.kzg_multi_proofs in kzg_multi_proofs_risk:
            st.session_state.kzg_multi_proofs_score = kzg_multi_proofs_risk[st.session_state.kzg_multi_proofs]
        else:
            st.session_state.kzg_multi_proofs_score = 0

    if 'disperser_operator' not in st.session_state:
        st.session_state.disperser_operator = "True"
    if 'disperser_operator_score' not in st.session_state:
        if st.session_state.disperser_operator in disperser_operator_risk:
            st.session_state.disperser_operator_score = disperser_operator_risk[st.session_state.disperser_operator]
        else:
            st.session_state.disperser_operator_score = 0

    if 'proof_custody' not in st.session_state:
        st.session_state.proof_custody = "True"
    if 'proof_custody_score' not in st.session_state:
        if st.session_state.proof_custody in proof_custody_risk:
            st.session_state.proof_custody_score = proof_custody_risk[st.session_state.proof_custody]
        else:
            st.session_state.proof_custody_score = 0


    if 'direct_unicast' not in st.session_state:
        st.session_state.direct_unicast = "True"
    if 'direct_unicast_score' not in st.session_state:
        if st.session_state.direct_unicast in direct_unicast_risk:
            st.session_state.direct_unicast_score = direct_unicast_risk[st.session_state.direct_unicast]
        else:
            st.session_state.disperser_operator_score = 0


    if 'kzg_poly_comm' not in st.session_state:
        st.session_state.kzg_poly_comm = "True"
    if 'kzg_poly_comm_score' not in st.session_state:
        if st.session_state.kzg_poly_comm in kzg_poly_comm_risk:
            st.session_state.kzg_poly_comm_score = kzg_poly_comm_risk[st.session_state.kzg_poly_comm]
        else:
            st.session_state.kzg_poly_comm_score = 0


    if 'rollup_censorship_res' not in st.session_state:
        st.session_state.rollup_censorship_res = "True"
    if 'rollup_censorship_res_score' not in st.session_state:
        if st.session_state.rollup_censorship_res in rollup_censorship_res_risk:
            st.session_state.rollup_censorship_res_score = rollup_censorship_res_risk[st.session_state.rollup_censorship_res]
        else:
            st.session_state.rollup_censorship_res_score = 0

    if 'fhe_disperser' not in st.session_state:
        st.session_state.fhe_disperser = "True"
    if 'fhe_disperser_score' not in st.session_state:
        if st.session_state.fhe_disperser in fhe_disperser_risk:
            st.session_state.fhe_disperser_score = fhe_disperser_risk[st.session_state.fhe_disperser]
        else:
            st.session_state.fhe_disperser_score = 0

    if 'fhe_operator' not in st.session_state:
        st.session_state.fhe_operator = "True"
    if 'fhe_operator_score' not in st.session_state:
        if st.session_state.fhe_operator in fhe_operator_risk:
            st.session_state.fhe_operator_score = fhe_operator_risk[st.session_state.fhe_operator]
        else:
            st.session_state.fhe_operator_score = 0

    if 'dual_quorum' not in st.session_state:
        st.session_state.dual_quorum = "True"
    if 'dual_quorum_score' not in st.session_state:
        if st.session_state.dual_quorum in dual_quorum_risk:
            st.session_state.dual_quorum_score = dual_quorum_risk[st.session_state.dual_quorum]
        else:
            st.session_state.dual_quorum_score = 0    

    if 'risk_score' not in st.session_state:
        st.session_state.risk_score = 0

