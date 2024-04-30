

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
relayer_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
validator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
evm_client_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
evm_validator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
evm_validator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
halo_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
code_complexity_risk = {"High": 10, "Medium": 5, "Low": 2}
operator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
evm_equivalence_risk = {"Incompatible": 10, "Compatible": 5, "Equivalent": 2}
validator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
relayer_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
evm_client_div_risk = {"Poorly Diverse": 10, "Moderately Diverse": 5, "Highly Diverse": 2}
operator_entrenchment_level_risk = {"High Entrenchment": 10, "Moderate Entrenchment": 5, "Low Entrenchment": 1}
engine_api_risk = {True: 1, False: 5}
dvt_mec_risk = {True: 1, False: 5}
sybil_mec_risk = {True: 1, False: 5}
relayer_da_solution_risk = {True: 1, False: 5}
validator_abci_usage_risk = {True: 1, False: 5}
da_sol_mec_risk = {True: 1, False: 5}
lockup_mec_risk = {True: 1, False: 5}
fast_fin_ss_mec_risk = {True: 1, False: 5}
tee_mec_risk = {True: 1, False: 5}
encrypted_mempool_mec_risk = {True: 1, False: 5}
relayer_merkle_risk = {True: 1, False: 5}
oracle_bridge_mec_risk = {True: 1, False: 5}



def omni_risk(security_audits, business_model, relayer_reputation, relayer_da_solution, halo_reputation,
                relayer_merkle, evm_client_div, evm_equivalence, sybil_mec, encrypted_mempool_mec, code_complexity,
                tee_mec, operator_reputation, operator_centralization, operator_entrenchment_level, engine_api,
                validator_abci_usage, dvt_mec, oracle_bridge_mec, lockup_mec, fast_fin_ss_mec, validator_reputation, 
                da_sol_mec, validator_centralization, relayer_centralization, evm_validator_reputation,
                evm_validator_centralization, evm_client_reputation):


        evm_client_reputation_score = evm_client_reputation_risk[evm_client_reputation]
        evm_validator_centralization_score = evm_validator_centralization_risk[evm_validator_centralization]
        halo_reputation_score = halo_reputation_risk[halo_reputation]
        evm_validator_reputation_score = evm_validator_reputation_risk[evm_validator_reputation]
        security_audits_score = security_audits_risk[security_audits]
        business_model_score = business_model_risk[business_model]
        relayer_reputation_score = relayer_reputation_risk[relayer_reputation]
        relayer_centralization_score = relayer_centralization_risk[relayer_centralization]
        operator_reputation_score = operator_reputation_risk[operator_reputation]
        code_complexity_score = code_complexity_risk[code_complexity]
        operator_centralization_score = operator_centralization_risk[operator_centralization]
        validator_centralization_score = validator_centralization_risk[validator_centralization]
        evm_equivalence_score = evm_equivalence_risk[evm_equivalence]
        validator_reputation_score = validator_reputation_risk[validator_reputation]
        evm_client_div_score = evm_client_div_risk[evm_client_div]
        operator_entrenchment_level_score = operator_entrenchment_level_risk[operator_entrenchment_level]
        dvt_mec_score = dvt_mec_risk[dvt_mec]
        sybil_mec_score = sybil_mec_risk[sybil_mec]
        relayer_da_solution_score = relayer_da_solution_risk[relayer_da_solution]
        engine_api_score = engine_api_risk[engine_api]
        validator_abci_usage_score = validator_abci_usage_risk[validator_abci_usage]
        da_sol_mec_score = da_sol_mec_risk[da_sol_mec]
        lockup_mec_score = lockup_mec_risk[lockup_mec]
        fast_fin_ss_mec_score = fast_fin_ss_mec_risk[fast_fin_ss_mec]
        tee_mec_score = tee_mec_risk[tee_mec]
        encrypted_mempool_mec_score = encrypted_mempool_mec_risk[encrypted_mempool_mec]
        relayer_merkle_score = relayer_merkle_risk[relayer_merkle]
        oracle_bridge_mec_score = oracle_bridge_mec_risk[oracle_bridge_mec]

        return (security_audits_score, business_model_score, relayer_reputation_score, evm_client_reputation_score,
                    operator_reputation_score, code_complexity_score, evm_equivalence_score, halo_reputation_score,
                    operator_centralization_score, validator_centralization_score, validator_reputation_score, 
                    dvt_mec_score, evm_client_div_score, operator_entrenchment_level_score, da_sol_mec_score,
                    sybil_mec_score, relayer_da_solution_score, validator_abci_usage_score, engine_api_score,
                    lockup_mec_score, fast_fin_ss_mec_score, tee_mec_score, encrypted_mempool_mec_score,
                    relayer_merkle_score, oracle_bridge_mec_score, relayer_centralization_score, 
                    evm_validator_reputation_score, evm_validator_centralization_score)


def main():
    st.set_page_config(layout="wide")

    st.image("images/omni.jpeg", width=450)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Interoperability Network AVS: Omni Underlying Risk & Slashing Conditions Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
            The Simulator takes 9 AVS-generic parameters and 21 parameters that specifically compose an Interoperability Network protocol with a CometBFT consensus architecture to calculate Omni's Risk Score as an EigenLayer AVS. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            
            Most of the research to build this Simulator was derived from [Omni's Docs](https://docs.omni.network/) and [CometBFT's Docs](https://docs.cometbft.com/v0.37/), as well as the images in the "Logic" dropdowns.
                            """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate utility or scenario for Omni as a Interoperability Network AVS. *It is important to bear in mind that since we are at the very early stages of AVS development and little-to-no information is available, the value judgements below are prone to being faulty.*")

    st.write("  \n")
    st.write("  \n")
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
        
    def relayer_performance_acc_rate_calc(relayer_performance_acc_rate):
        if 0 <= relayer_performance_acc_rate <= 10:
            return 9
        elif 11 <= relayer_performance_acc_rate <= 33:
            return 7.5
        elif 34 <= relayer_performance_acc_rate <= 50:
            return 6
        elif 51 <= relayer_performance_acc_rate <= 66:
            return 4
        elif 67 <= relayer_performance_acc_rate <= 90:
            return 3
        elif 91 <= relayer_performance_acc_rate <= 100:
            return 2
        else:
            return None

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

    def evm_val_performance_acc_rate_calc(evm_val_performance_acc_rate):
        if 0 <= evm_val_performance_acc_rate <= 10:
            return 9
        elif 11 <= evm_val_performance_acc_rate <= 33:
            return 7.5
        elif 34 <= evm_val_performance_acc_rate <= 50:
            return 6
        elif 51 <= evm_val_performance_acc_rate <= 66:
            return 4
        elif 67 <= evm_val_performance_acc_rate <= 90:
            return 3
        elif 91 <= evm_val_performance_acc_rate <= 100:
            return 2
        else:
            return None




    if 'business_model' not in st.session_state:
        st.session_state.business_model = "Dual Staking Utility"
    if 'business_model_score' not in st.session_state:
        if st.session_state.business_model in business_model_risk:  # Check if business model exists in the dictionary
            st.session_state.business_model_score = business_model_risk[st.session_state.business_model]
        else:
            st.session_state.business_model_score = 0  # Set a default score if business model is not found

    if 'code_complexity' not in st.session_state:
        st.session_state.code_complexity = "High"  # Set default value
    if 'code_complexity_score' not in st.session_state:
        if st.session_state.code_complexity in code_complexity_risk:  # Check if code complexity exists in the dictionary
            st.session_state.code_complexity_score = code_complexity_risk[st.session_state.code_complexity]
        else:
            st.session_state.code_complexity_score = 0

    if 'security_audits' not in st.session_state:
        st.session_state.security_audits = "2"  # Set default value
    if 'security_audits_score' not in st.session_state:
        if st.session_state.security_audits in security_audits_risk:  # Check if code complexity exists in the dictionary
            st.session_state.security_audits_score = security_audits_risk[st.session_state.security_audits]
        else:
            st.session_state.security_audits_score = 0

    if 'relayer_reputation' not in st.session_state:
        st.session_state.relayer_reputation = "Unknown"  # Set default value
    if 'relayer_reputation_score' not in st.session_state:
        if st.session_state.relayer_reputation in relayer_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.relayer_reputation_score = relayer_reputation_risk[st.session_state.relayer_reputation]
        else:
            st.session_state.relayer_reputation_score = 0

    if 'operator_reputation' not in st.session_state:
        st.session_state.operator_reputation = "Unknown"  # Set default value
    if 'operator_reputation_score' not in st.session_state:
        if st.session_state.operator_reputation in operator_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.operator_reputation_score = operator_reputation_risk[st.session_state.operator_reputation]
        else:
            st.session_state.operator_reputation_score = 0

    if 'evm_equivalence' not in st.session_state:
        st.session_state.evm_equivalence = "Equivalent"  # Set default value
    if 'evm_equivalence_score' not in st.session_state:
        if st.session_state.evm_equivalence in evm_equivalence_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_equivalence_score = evm_equivalence_risk[st.session_state.evm_equivalence]
        else:
            st.session_state.evm_equivalence_score = 0

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

    if 'relayer_centralization' not in st.session_state:
        st.session_state.relayer_centralization = "Decentralized"  # Set default value
    if 'relayer_centralization_score' not in st.session_state:
        if st.session_state.relayer_centralization in relayer_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.relayer_centralization_score = relayer_centralization_risk[st.session_state.relayer_centralization]
        else:
            st.session_state.relayer_centralization_score = 0

    if 'validator_reputation' not in st.session_state:
        st.session_state.validator_reputation = "Unknown"  # Set default value
    if 'validator_reputation_score' not in st.session_state:
        if st.session_state.validator_reputation in validator_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_reputation_score = validator_reputation_risk[st.session_state.validator_reputation]
        else:
            st.session_state.validator_reputation_score = 0

    if 'halo_reputation' not in st.session_state:
        st.session_state.halo_reputation = "Unknown"  # Set default value
    if 'halo_reputation_score' not in st.session_state:
        if st.session_state.halo_reputation in halo_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.halo_reputation_score = halo_reputation_risk[st.session_state.halo_reputation]
        else:
            st.session_state.halo_reputation_score = 0

    if 'evm_client_reputation' not in st.session_state:
        st.session_state.evm_client_reputation = "Unknown"  # Set default value
    if 'evm_client_reputation_score' not in st.session_state:
        if st.session_state.evm_client_reputation in evm_client_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_client_reputation_score = evm_client_reputation_risk[st.session_state.evm_client_reputation]
        else:
            st.session_state.evm_client_reputation_score = 0

    if 'evm_validator_reputation' not in st.session_state:
        st.session_state.evm_validator_reputation = "Unknown"  # Set default value
    if 'evm_validator_reputation_score' not in st.session_state:
        if st.session_state.evm_validator_reputation in evm_validator_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_validator_reputation_score = evm_validator_reputation_risk[st.session_state.evm_validator_reputation]
        else:
            st.session_state.evm_validator_reputation_score = 0

    if 'evm_validator_centralization' not in st.session_state:
        st.session_state.evm_validator_centralization = "Unknown"  # Set default value
    if 'evm_validator_centralization_score' not in st.session_state:
        if st.session_state.evm_validator_centralization in evm_validator_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_validator_centralization_score = evm_validator_centralization_risk[st.session_state.evm_validator_centralization]
        else:
            st.session_state.evm_validator_centralization_score = 0

    if 'dvt_mec' not in st.session_state:
        st.session_state.dvt_mec = "False"  # Set default value
    if 'dvt_mec_score' not in st.session_state:
        if st.session_state.dvt_mec in dvt_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.dvt_mec_score = dvt_mec_risk[st.session_state.dvt_mec]
        else:
            st.session_state.dvt_mec_score = 0

    if 'evm_client_div' not in st.session_state:
        st.session_state.evm_client_div = "Moderately Diverse"  # Set default value
    if 'evm_client_div_score' not in st.session_state:
        if st.session_state.evm_client_div in evm_client_div_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_client_div_score = evm_client_div_risk[st.session_state.evm_client_div]
        else:
            st.session_state.evm_client_div_score = 0

    if 'operator_entrenchment_level' not in st.session_state:
        st.session_state.operator_entrenchment_level = "High Entrenchment"  # Set default value
    if 'operator_entrenchment_level_score' not in st.session_state:
        if st.session_state.operator_entrenchment_level in operator_entrenchment_level_risk:  # Check if code complexity exists in the dictionary
            st.session_state.operator_entrenchment_level_score = operator_entrenchment_level_risk[st.session_state.operator_entrenchment_level]
        else:
            st.session_state.operator_entrenchment_level_score = 0

    if 'da_sol_mec' not in st.session_state:
        st.session_state.da_sol_mec = "False"  # Set default value
    if 'da_sol_mec_score' not in st.session_state:
        if st.session_state.da_sol_mec in da_sol_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.da_sol_mec_score = da_sol_mec_risk[st.session_state.da_sol_mec]
        else:
            st.session_state.da_sol_mec_score = 0

    if 'sybil_mec_score' not in st.session_state:
        st.session_state.sybil_mec = "False"  # Set default value
    if 'sybil_mec_score' not in st.session_state:
        if st.session_state.sybil_mec in sybil_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.sybil_mec_score = sybil_mec_risk[st.session_state.sybil_mec]
        else:
            st.session_state.sybil_mec_score = 0

    if 'relayer_da_solution_score' not in st.session_state:
        st.session_state.relayer_da_solution = "False"  # Set default value
    if 'relayer_da_solution_score' not in st.session_state:
        if st.session_state.relayer_da_solution in relayer_da_solution_risk:  # Check if code complexity exists in the dictionary
            st.session_state.relayer_da_solution_score = relayer_da_solution_risk[st.session_state.relayer_da_solution]
        else:
            st.session_state.relayer_da_solution_score = 0

    if 'validator_abci_usage_score' not in st.session_state:
        st.session_state.validator_abci_usage = "True"  # Set default value
    if 'validator_abci_usage_score' not in st.session_state:
        if st.session_state.validator_abci_usage in validator_abci_usage_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_abci_usage_score = validator_abci_usage_risk[st.session_state.validator_abci_usage]
        else:
            st.session_state.validator_abci_usage_score = 0

    if 'engine_api_score' not in st.session_state:
        st.session_state.engine_api = "True"  # Set default value
    if 'engine_api_score' not in st.session_state:
        if st.session_state.engine_api in engine_api_risk:  # Check if code complexity exists in the dictionary
            st.session_state.engine_api_score = engine_api_risk[st.session_state.engine_api]
        else:
            st.session_state.engine_api_score = 0

    if 'lockup_mec_score' not in st.session_state:
        st.session_state.lockup_mec = "False"  # Set default value
    if 'lockup_mec_score' not in st.session_state:
        if st.session_state.lockup_mec in lockup_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.lockup_mec_score = lockup_mec_risk[st.session_state.lockup_mec]
        else:
            st.session_state.lockup_mec_score = 0

    if 'fast_fin_ss_mec_score' not in st.session_state:
        st.session_state.fast_fin_ss_mec = "False"  # Set default value
    if 'fast_fin_ss_mec_score' not in st.session_state:
        if st.session_state.fast_fin_ss_mec in fast_fin_ss_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.fast_fin_ss_mec_score = fast_fin_ss_mec_risk[st.session_state.fast_fin_ss_mec]
        else:
            st.session_state.fast_fin_ss_mec_score = 0

    if 'tee_mec_score' not in st.session_state:
        st.session_state.tee_mec = "False"  # Set default value
    if 'tee_mec_score' not in st.session_state:
        if st.session_state.tee_mec in tee_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.tee_mec_score = tee_mec_risk[st.session_state.tee_mec]
        else:
            st.session_state.tee_mec_score = 0

    if 'encrypted_mempool_mec_score' not in st.session_state:
        st.session_state.encrypted_mempool_mec = "False"  # Set default value
    if 'encrypted_mempool_mec_score' not in st.session_state:
        if st.session_state.encrypted_mempool_mec in encrypted_mempool_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.encrypted_mempool_mec_score = encrypted_mempool_mec_risk[st.session_state.encrypted_mempool_mec]
        else:
            st.session_state.encrypted_mempool_mec_score = 0

    if 'relayer_merkle_score' not in st.session_state:
        st.session_state.relayer_merkle = "True"  # Set default value
    if 'relayer_merkle_score' not in st.session_state:
        if st.session_state.relayer_merkle in relayer_merkle_risk:  # Check if code complexity exists in the dictionary
            st.session_state.relayer_merkle_score = relayer_merkle_risk[st.session_state.relayer_merkle]
        else:
            st.session_state.relayer_merkle_score = 0

    if 'oracle_bridge_mec_score' not in st.session_state:
        st.session_state.oracle_bridge_mec = "False"  # Set default value
    if 'oracle_bridge_mec_score' not in st.session_state:
        if st.session_state.oracle_bridge_mec in oracle_bridge_mec_risk:  # Check if code complexity exists in the dictionary
            st.session_state.oracle_bridge_mec_score = oracle_bridge_mec_risk[st.session_state.oracle_bridge_mec]
        else:
            st.session_state.oracle_bridge_mec_score = 0

    if 'risk_score' not in st.session_state:
        st.session_state.risk_score = 0


    def format_number(num):
            if num.is_integer():
                return f"{int(num)}"
            else:
                return f"{num:.1f}"
            
    def format_result(num):
            # Check if the number is an integer
            if num.is_integer():
                # Format integer with comma for thousands
                return f"{int(num):,}"
            else:
                # Format float with comma for thousands and period for decimals
                return f"{num:,.2f}"


    st.write("\n")
    

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:

        custom_css = """
            <style>
            .header-style {
                font-size: 16px; /* Existing font size */
                font-weight: bold;
            }

            .large-header-style {
                font-size: 20px; /* Larger font size */
                font-weight: bold;
            }
            </style>
            """

        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 10px;
                padding: 4px;
                text-align: center;
                margin: 5px 0;
                background-color: #4169E1;">
                <h2 class='large-header-style' style="color: white; margin:0;">AVS METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")







        col24, col25 = st.columns(2, gap="medium")
        with col24:

            # Restaked ETH Delegated
            st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            # Displaying the custom styled header
            st.markdown('<p class="header-style">Total Restaked ETH Delegated to Omni</p>', unsafe_allow_html=True)

            # Dropdown menu
            restaked_eth_del = st.number_input("", min_value=0, max_value=100000000000, step=100000000, value=1300000)
            st.write(f"&#8226; Total Restaked ETH to Omni: **{restaked_eth_del:,.0f} ETH**")


            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")


        with col25:

            # Restaked TVL
            st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            # Displaying the custom styled header
            st.markdown('<p class="header-style">Total Restaked TVL on Omni</p>', unsafe_allow_html=True)

            # Dropdown menu
            restaked_tvl = st.number_input("", min_value=0, max_value=10000000000, step=10000000, key="33")
            st.write(f"&#8226; Total Restaked TVL on Omni: **{restaked_tvl:,.0f} ETH**")


            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")


        
        st.markdown('<p class="header-style" style="font-size: 21px;">AVS Business Model</p>', unsafe_allow_html=True)


        col47,col48 = st.columns(2, gap="medium")
        with col47:
            # AVS Business Model
            st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            # Dropdown menu
            business_model = st.selectbox("**AVS Business Model Type**", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"], index=1)

        with col48:
            st.write("  \n")

            # Displaying the custom styled header
            st.markdown('<p class="header-style" style="font-size: 14px;">AVS Dual Staking Model: Native Dual Staking</p>', unsafe_allow_html=True)

            st.write("  \n")

            avs_token_percentage = st.slider("**% $OMNI**", min_value=10, max_value=90, value=10, format='%d%%')

            xeth_percentage = 100 - avs_token_percentage
            
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, format='%d%%')

            st.write("&#8226; **Native Dual Staking Balance**: {}% $OMNI : {}% xETH".format(avs_token_percentage, xeth_percentage))

        st.write("-------")

        col44,col45 = st.columns(2, gap="medium")
        with col44:
            business_dual_likelihood = st.slider("*Likelihood* ", min_value=1, max_value=10, value=3, key='afa', help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            business_dual_likelihood2 = business_dual_likelihood / 2
        with col45:
            business_dual_impact = st.slider("*Impact* ", min_value=1, max_value=10, value=7, key='ewe', help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            business_dual_impact2 = business_dual_impact / 2


        business_dual_likelihood_formatted = format_number(business_dual_likelihood2)
        business_dual_impact_formatted = format_number(business_dual_impact2)


        dual_staking_balance = dual_staking_balance_calc(avs_token_percentage, xeth_percentage)
        st.session_state.dual_staking_balance = dual_staking_balance
        
        if st.session_state.business_model != business_model:
            st.session_state.business_model = business_model
            st.session_state.business_model_score = business_model_risk.get(business_model, 0)

        with st.expander("Logic"):
                st.markdown("""
                    Ordering the **Business Models** from EigenLayer [(Section 4.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) by risk: 
                    
                    - ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$OMNI), tying closely to its market performance and the AVS's ongoing profitability;
                    - ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $OMNI stakers, which introduces complexities in security and token value dynamics;
                    - ***Tokenize the Fee*** model comes with moderate risk involving payments in a neutral denomination (like ETH) and distributing a portion of fees to holders of the AVS's token, thus partly dependent on the AVS token's value;
                    - ***Pure Wallet*** represents the lowest risk, relying on straightforward service fees paid in a neutral denomination, like ETH.

                    Thus, the risk of each model is influenced by its reliance on the AVS's native token and the complexities of its fee and security structures.
                    
                    ```python
                    business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
                            
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
                    ```
                            

                    The Native Dual Staking model was chosen as the default one because it guarantees the highest Cost to Violate Liveness.
                    Particularly in the beginning, too much weight on the $OMNI native token increases the likelihood of the tokens of the dual staking model being toxic. And thus negatively impact liveness, an essential condition for a Shared Sequencer.
                            
                    Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $OMNI/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                    **\$OMNI** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$OMNI* **>** *% xETH* pool balance makes sense to be a higher-reward event.
                        """)
    
        
        result1 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_dual_likelihood2 * business_dual_impact2
        
        result1_formatted = format_result(float(result1))

        business_dual_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{business_dual_likelihood_formatted}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{business_dual_impact_formatted}</span> 
                    <span style="font-size: 23px; font-weight: bold;"> = </span>
                    <span style="font-size: 21px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result1_formatted}</span>
            </div>"""

        st.markdown(business_dual_calc, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


        
        st.markdown('<p class="header-style" style="font-size: 21px;">AVS Protocol Security</p>', unsafe_allow_html=True)


        col27,col28 = st.columns(2, gap="medium")
        with col27:

            # Code Complexity
            st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            code_complexity = st.selectbox("**AVS Protocol Architecture & Code Complexity**", ["High", "Medium", "Low"], index=0, key="ertr")
            
        with col28:
            # Number of Security Audits
            st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            security_audits = st.number_input("**AVS Number of Security Audits**", min_value=0, max_value=5, step=1, value=2, key="00")

        col35,col36 = st.columns(2, gap="medium")
        with col35:
                    security_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=5, help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
                    security_likelihood2 = security_likelihood/2
        with col36:
                    security_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
                    security_impact2 = security_impact/2

        security_likelihood_formatted = format_number(security_likelihood2)
        security_impact_formatted = format_number(security_impact2)


        with st.expander("Logic"):
                        st.markdown("""
                            Accounting for the **number of Security Audits** performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                            
                            While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks (and the risk of honest nodes getting slashed), and, as a result, rewards an AVS is confident to emit and Restakers and Operators to opt into it. 
                            
                            ```python
                            security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1} # 0 security audits poses the greatest risk, 5 the least
                            ```
                                    """)

        if st.session_state.code_complexity != code_complexity:
                st.session_state.code_complexity = code_complexity
                st.session_state.code_complexity_score = code_complexity_risk.get(code_complexity, 0)
            
        if st.session_state.security_audits != security_audits:
                st.session_state.security_audits = security_audits
                st.session_state.security_audits_score = security_audits_risk.get(security_audits, 0)

        result2 = st.session_state.code_complexity_score * st.session_state.security_audits_score * security_likelihood2 * security_impact2
        
        result2_formatted = format_result(float(result2))

        security_calc = f"""
                    <div style="text-align: center;">
                        <div>
                            <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.code_complexity_score}</span> 
                            <span style="font-size: 23px; font-weight: bold;">&times;</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.security_audits_score}</span> 
                            <span style="font-size: 23px; font-weight: bold;">&times;</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{security_likelihood_formatted}</span> 
                            <span style="font-size: 23px; font-weight: bold;">&times;</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{security_impact_formatted}</span> 
                            <span style="font-size: 23px; font-weight: bold;"> = </span>
                            <span style="font-size: 21px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result2_formatted}</span>
                    </div>"""

        st.markdown(security_calc, unsafe_allow_html=True)




        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


        st.markdown('<p class="header-style" style="font-size: 21px;">AVS Operator Profile</p>', unsafe_allow_html=True)

        st.write("  \n")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
                operator_reputation = st.selectbox("**Operator Reputation**", ["Unknown", "Established", "Renowned"], index=0, key="6783")

        with col101:            
                operator_centralization = st.selectbox("**Operators' Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], index=0, key="674")
            

        operator_entrenchment_level = st.selectbox("**Operators' Entrenchment Level** (on other AVSs)", ["High Entrenchment", "Moderate Entrenchment", "Low Entrenchment"], index=0, key="09111")

        st.write("-------")

        col33, col34 = st.columns(2, gap="medium")
        with col33:
            operator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=8, key="o0", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            operator_likelihood2 = operator_metrics_likelihood/2
        with col34:
            operator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=9, key="o1", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            operator_impact2 = operator_metrics_impact/2

        operator_likelihood_formatted = format_number(operator_likelihood2)
        operator_impact_formatted = format_number(operator_impact2)


        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
                    Although being a purely qualitative metrics, the **Reputation Level of the Operator** and the **Geographical Centralization Level of the Operator**  that the AVS chose to be opted in to validate its modules offers a useful glimpse into the AVS’s security profile. The user should consider the Operator's historical slashing record and the overall validation and uptime performance, which are crucial in assessing overall operator-related risk for an AVS, including potential malicious collusions. [Rated Network](https://www.rated.network/) constitutes a good tool to assess this.                     
                    
                    ```python
                    avs_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
                    ```
                                            
                    ```python
                    avs_operator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
                    ```
                                """)

        if st.session_state.operator_reputation != operator_reputation:
                st.session_state.operator_reputation = operator_reputation
                st.session_state.operator_reputation_score = operator_reputation_risk.get(operator_reputation, 0)
        if st.session_state.operator_centralization != operator_centralization:
                st.session_state.operator_centralization = operator_centralization
                st.session_state.operator_centralization_score = operator_centralization_risk.get(operator_centralization, 0)
        if st.session_state.operator_entrenchment_level != operator_entrenchment_level:
                st.session_state.operator_entrenchment_level = operator_entrenchment_level
                st.session_state.operator_entrenchment_level_score = operator_entrenchment_level_risk.get(operator_entrenchment_level, 0)

        result3 = (st.session_state.operator_reputation_score * st.session_state.operator_centralization_score * 
                   st.session_state.operator_entrenchment_level_score * operator_likelihood2 * operator_impact2)
        
        result3_formatted = format_result(float(result3))


        operator_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_reputation_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_centralization_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_entrenchment_level_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{operator_likelihood_formatted}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{operator_impact_formatted}</span> 
                    <span style="font-size: 23px; font-weight: bold;"> = </span>
                    <span style="font-size: 21px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result3_formatted}</span>
                </div>
            """

        st.markdown(operator_calc, unsafe_allow_html=True)



#############################
#############################
#############################




    with col2:


        custom_css = """
            <style>
            .header-style {
                font-size: 16px; /* Existing font size */
                font-weight: bold;
            }

            .large-header-style {
                font-size: 20px; /* Larger font size */
                font-weight: bold;
            }
            </style>
            """

        st.markdown(custom_css, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 10px;
                padding: 4px;
                text-align: center;
                margin: 5px 0;
                background-color: #4169E1;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">OMNI-SPECIFIC METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")



        # Staked OMNI
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                .stExpander {
                    border: none !important;
                    box-shadow: none !important;
                }
                </style>
                """, unsafe_allow_html=True)

            # Displaying the custom styled header
        st.markdown('<p class="header-style">Total Staked $OMNI</p>', unsafe_allow_html=True)

            # Dropdown menu
        staked_omni = st.number_input("", min_value=0, max_value=10000000000, step=10000000, key="212")
        st.write(f"&#8226; Total Staked \$OMNI: **{staked_omni:,.0f} ETH**")


        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")


















        # CometBFT: Validator Metrics

        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        
        st.markdown("""
            <p class="header-style">
                <span style="color: white; background-color: black; border-radius: 50%; padding: 0.5em; font-family: monospace; display: inline-flex; align-items: center; justify-content: center; width: 1.5em; height: 1.5em; font-size: 0.85em; margin-right: 0.5em;">1</span>
                <span style="font-size: 21px;">CONSENSUS LAYER: CometBFT & Consensus Client Profile</span>
            </p>
                """, unsafe_allow_html=True)


        st.write("  \n")

        col38,col39 = st.columns(2, gap="medium")
        with col38:
            engine_api = st.checkbox('**Ethereum Engine API** used by Nodes to pair the Consensus Client (Halo) with the EVM Execution Client', 
                                     value=True, help="**The Ethereum Engine API pairs an existing Ethereum Execution Client with Halo Consensus Client that implements CometBFT consensus.**")
        with col39:
            validator_abci_usage = st.checkbox('**Engine API uses ABCI++** for seamless state transitions between Omni EVM and CometBFT', value=True,
                                               help="**ABCI++ is an adapter that wraps around the CometBFT engine, translating Engine API messages for consensus processing, ensuring Omni's lightweight consensus and quick finality.**")

        col42,col43 = st.columns(2, gap="medium")
        with col42:
            tee_mec = st.checkbox('**TEE** Implementation for Effective Key Management', value=False,
                                  help="**TEEs consist of secure portions of hardware that generate and securely store validator keys and databases of previously signed data. By design, they enhance security without comprimising scalability, and through increased trust, encourage stake delegation.**")
        with col43:
            dvt_mec = st.checkbox('**DVT** Implementation to Reduce Risks of Single Points of Failure from a Subset of Validators', value=False,
                                  help="**DVT is a technology that incentivizes client diversity through the distribution of the validation process across multiple operators. It reduces the risk of single points of failure or malicious actions.**")

        col50,col51 = st.columns(2, gap="medium")
        with col50:
            oracle_bridge_mec = st.checkbox('**Oracle/Bridge Solution** to Restrict Potential PfC', value=False,
                                            help="**To restrict the potential PfC extracted from Omni, a bridge can be set-up to restrict the value flow within the period of slashing, or an oracle can have bounds on the total value transacted within a given period.**")
        with col51:
            lockup_mec = st.checkbox('**Withdrawal Lock-Up Periods** Applied to Validators for Security Against Corruption', value=False)

        col52,col53 = st.columns(2, gap="medium")
        with col52:
            da_sol_mec = st.checkbox('**DA Solution** for Horizontal Scaling of Nodes, Mitigating Potential State Explosions and Low Latency', value=False)
        with col53:
            fast_fin_ss_mec = st.checkbox('**Shared Sequencer Pre-Confirmation Solution** for `XMsg` Fast Finality', value=False)


        if st.session_state.engine_api != engine_api:
            st.session_state.engine_api = engine_api
            st.session_state.engine_api_score = engine_api_risk.get(engine_api, 0)

        if st.session_state.validator_abci_usage != validator_abci_usage:
            st.session_state.validator_abci_usage = validator_abci_usage
            st.session_state.validator_abci_usage_score = validator_abci_usage_risk.get(validator_abci_usage, 0)

        if st.session_state.tee_mec != tee_mec:
            st.session_state.tee_mec = tee_mec
            st.session_state.tee_mec_score = tee_mec_risk.get(tee_mec, 0)

        if st.session_state.dvt_mec != dvt_mec:
            st.session_state.dvt_mec = dvt_mec
            st.session_state.dvt_mec_score = dvt_mec_risk.get(dvt_mec, 0)

        if st.session_state.oracle_bridge_mec != oracle_bridge_mec:
            st.session_state.oracle_bridge_mec = oracle_bridge_mec
            st.session_state.oracle_bridge_mec_score = oracle_bridge_mec_risk.get(oracle_bridge_mec, 0)

        if st.session_state.lockup_mec != lockup_mec:
            st.session_state.lockup_mec = lockup_mec
            st.session_state.lockup_mec_score = lockup_mec_risk.get(lockup_mec, 0)

        if st.session_state.da_sol_mec != da_sol_mec:
            st.session_state.da_sol_mec = da_sol_mec
            st.session_state.da_sol_mec_score = da_sol_mec_risk.get(da_sol_mec, 0)

        if st.session_state.fast_fin_ss_mec != fast_fin_ss_mec:
            st.session_state.fast_fin_ss_mec = fast_fin_ss_mec
            st.session_state.fast_fin_ss_mec_score = fast_fin_ss_mec_risk.get(fast_fin_ss_mec, 0)

        result4 = (st.session_state.engine_api_score * st.session_state.validator_abci_usage_score +
                        st.session_state.tee_mec_score + st.session_state.dvt_mec_score + st.session_state.oracle_bridge_mec_score +
                        st.session_state.lockup_mec_score + st.session_state.da_sol_mec_score + st.session_state.fast_fin_ss_mec_score)

        st.write("  \n")

        validator_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.engine_api_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_abci_usage_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.tee_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dvt_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.oracle_bridge_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.lockup_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.da_sol_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.fast_fin_ss_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result4):,}</span>
            </div>"""

        st.markdown(validator_calc1, unsafe_allow_html=True)


############################################


        st.write("-------")

        halo_reputation = st.selectbox("**Halo (Consensus Client) Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="090888",
                                                help="**Attests for a set of validators' trustworthiness in their role of confirming and validating CometBFT blocks and attesting to `XBlock`s before being submitted on-chain.**")
        st.write("  \n")

        validator_performance_acc_rate = st.slider("**Validator XBlocks Attestation Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                                   help="**The Performance Accuracy Rate of Validators attesting for `XBlock`s consists of the timely submission of cross-chain messages, `XBlock` cache management, and the overall decision-making in including `XMsg`s in an `XBlock`.**")
        validator_performance_acc_rate_var = validator_performance_acc_rate_calc(validator_performance_acc_rate)
        st.session_state.validator_performance_acc_rate_var = validator_performance_acc_rate_var

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            validator_reputation = st.selectbox("**CometBFT Validators' Reputation**", ["Unknown", "Established", "Renowned"], key="0990", index=1,
                                                help="**Attests for a set of validators' trustworthiness in their role of confirming and validating CometBFT blocks and attesting to `XBlock`s before being submitted on-chain.**")
        with col101:           
            validator_centralization = st.selectbox("**CometBFT Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="3232", index=1,
                                                    help="**Attests for a set of validators' robustness and stability in dealing with local regulations or targeted international attacks.**")
        
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            validator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=8, key="v0", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            validator_metrics_likelihood2 = validator_metrics_likelihood / 2

        with col34:
            validator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=9, key="v1", help=f"""
                                                     **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            validator_metrics_impact2 = validator_metrics_impact / 2



        # Directly use the calculated variables
        val_likelihood_formatted = format_number(validator_metrics_likelihood2)
        val_impact_formatted = format_number(validator_metrics_impact2)


        with st.expander("Logic"):
                st.image("images/omni-comet-diagram.jpg", width=750)

                st.markdown("""
Consensus-level Validators package `XMsgs` into `XBlocks` and attest to those `XBlock` hashes during CometBFT consensus. For a more detailed overview check the visualization at the bottom of this Simulator.
            
**Engine API** is a critical component of the Omni protocol, connecting Ethereum execution clients with a consensus client (Halo) for the CometBFT system. It allows clients to be substituted or upgraded without perturbing the system. It offers:

- Scalability and Efficiency: By offloading the transaction mempool and facilitating efficient state translation, the Engine API contributes to Omni's scalability and sub-second transaction finality.
- Flexibility: Supports the interchangeability and upgradability of execution clients without system disruption, ensuring compatibility with various Ethereum execution clients.
                            
                            
**ABCI++** is an adapter that wraps around the CometBFT engine, that enables seamless state translation and efficient conversion of Omni EVM blocks into CometBFT transactions. This feature:

- Streamlines transaction requests by moving the transaction mempool to the execution layer, alleviating network congestion and latency at the CometBFT consensus level;
- Facilitates state translations by wrapping around CometBFT ensuring Omni EVM blocks are efficiently converted into CometBFT transactions.
                            
As per the above checkboxes, we suggest a few features/mechanism that could contribute to the overall efficiency and security of Omni as a protocol and as an AVS. Consideration for `Halo`'s reputation can be added on a later version.
                            
The summation or multiplication of variables revolves around their independence or dependence toward one another, pragmatically speaking.
                            """)


        if st.session_state.halo_reputation != halo_reputation:
            st.session_state.halo_reputation = halo_reputation
            st.session_state.halo_reputation_score = halo_reputation_risk.get(halo_reputation, 0)

        if st.session_state.validator_reputation != validator_reputation:
            st.session_state.validator_reputation = validator_reputation
            st.session_state.validator_reputation_score = validator_reputation_risk.get(validator_reputation, 0)

        if st.session_state.validator_centralization != validator_centralization:
            st.session_state.validator_centralization = validator_centralization
            st.session_state.validator_centralization_score = validator_centralization_risk.get(validator_centralization, 0)
    

        result5 = (st.session_state.validator_performance_acc_rate_var * st.session_state.halo_reputation_score * st.session_state.validator_reputation_score *
                   st.session_state.validator_centralization_score * validator_metrics_likelihood2 * validator_metrics_impact2)
        
        result5_formatted = format_result(float(result5))

        
        validator_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.halo_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{val_likelihood_formatted}</span>         
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{val_impact_formatted}</span>         
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result5_formatted}</span>
                </div>
            </div>"""


        st.markdown(validator_calc2, unsafe_allow_html=True)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")















        # EVM Metrics

        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown("""
            <p class="header-style">
                <span style="color: white; background-color: black; border-radius: 50%; padding: 0.5em; font-family: monospace; display: inline-flex; align-items: center; justify-content: center; width: 1.5em; height: 1.5em; font-size: 0.85em; margin-right: 0.5em;">2</span>
                <span style="font-size: 21px;">EXECUTION LAYER: Execution ClientS Profile</span>
            </p>
        """, unsafe_allow_html=True)

        

        st.write("  \n")
        
        col65,col66 = st.columns(2, gap="medium")
        with col65:
            sybil_mec = st.checkbox('**Anti-Sybil Mechanism**', value=True,
                                help="**Mechanism used in the context of transactions submitted to the Omni EVM, to deter spam and malicious activities such as DoS attacks.**")
        with col66:
            encrypted_mempool_mec = st.checkbox('**Encrypted Mempool** for Increased Privacy and Security', value=False)

        if st.session_state.encrypted_mempool_mec != encrypted_mempool_mec:
            st.session_state.encrypted_mempool_mec = encrypted_mempool_mec
            st.session_state.encrypted_mempool_mec_score = encrypted_mempool_mec_risk.get(encrypted_mempool_mec, 0)

        if st.session_state.sybil_mec != sybil_mec:
            st.session_state.sybil_mec = sybil_mec
            st.session_state.sybil_mec_score = sybil_mec_risk.get(sybil_mec, 0)

        result6 = (st.session_state.sybil_mec_score + st.session_state.encrypted_mempool_mec_score)
        
        st.write("  \n")

        evm_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.sybil_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.encrypted_mempool_mec_score}</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result6):,}</span>
            </div>"""

        st.markdown(evm_calc1, unsafe_allow_html=True)


##################################################


        st.write("-------")

        evm_client_reputation = st.selectbox("**EVM Client Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="877w6", help="**Docs: 'The execution layer is implemented by standard Ethereum execution clients, like  `geth`, `erigon`, etc, to provide the Omni EVM.'**")
        
        st.write("  \n")

        evm_val_performance_acc_rate = st.slider("**EVM Validators' Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%', key="6782")

        evm_val_performance_acc_rate_var = evm_val_performance_acc_rate_calc(evm_val_performance_acc_rate)
        st.session_state.evm_val_performance_acc_rate_var = evm_val_performance_acc_rate_var

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            evm_validator_reputation = st.selectbox("**EVM Validators' Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="976")        
        with col101:           
            evm_validator_centralization = st.selectbox("**EVM Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="2116", index=1)

        st.write("  \n")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            evm_equivalence = st.selectbox("**EVM Compatibility**", ["Incompatible", "Compatible", "Equivalent"], index=2, key="09",
                                           help="**Runs an unmodified version of the original EVM. Since Omni adheres to the Engine API, a standard that all EVM clients also comply with, enabling the seamless integration of any EVM client into the Omni network, without the need for modifications. This approach allows it to leverage the unique advantages that different clients provide.**")
        with col101:
            evm_client_div = st.selectbox("**EVM Client Diversity**", ["Poorly Diverse", "Moderately Diverse", "Highly Diverse"], key="7877", index=0,
                                          help="**Correlated (but not causal) relationship with the level of Equivalence or Compatible of the EVM. EVM Equivalence likely leads to greater Client Diversity.**")
            
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            evm_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="e0", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            evm_metrics_likelihood2 = evm_metrics_likelihood / 2

        with col34:
            evm_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="e1", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            evm_metrics_impact2 = evm_metrics_impact / 2

        # Directly use the calculated variables
        evm_likelihood_formatted = format_number(evm_metrics_likelihood2)
        evm_impact_formatted = format_number(evm_metrics_impact2)

        with st.expander("Logic"):
               st.markdown("""
The several steps at the Omni EVM level include block proposal preparation, payload generation, and consensus-reaching at the Consensus Layer. Upon reaching consensus, the block is finalized and state transitions are applied to the blockchain.
To attest to the EVM's security and versatility, it employs an Anti-Sybil mechanism and EVM equivalence for developer accessibility and compatibility.
                           
- **Seamless Migration**: Developers can effortlessly migrate existing DApps to the Omni EVM without need for changes, enabling easy access to Omni's ecosystem;
- **Developer Tooling Compatibility**: The Omni EVM maintains full compatibility with Ethereum's development tools, ensuring that existing Ethereum developer tooling works without issues;
- **Future-Proof**: By adhering to Ethereum's standards and upgrade paths, the Omni EVM ensures that it remains up-to-date, allowing developers to utilize the latest features as they become available.

We do suggest considering an encrypted mempool for increased privacy and security in transactions processing. Consideration for the different Execution Clients' reputations, nodes' level of centralization, and performance accuracy rates can be added on a later version.                         
                        
The summation or multiplication of variables revolves around their independence or dependence toward one another, pragmatically speaking.
                            """)


        if st.session_state.evm_client_reputation != evm_client_reputation:
            st.session_state.evm_client_reputation = evm_client_reputation
            st.session_state.evm_client_reputation_score = evm_client_reputation_risk.get(evm_client_reputation, 0)

        if st.session_state.evm_validator_reputation != evm_validator_reputation:
            st.session_state.evm_validator_reputation = evm_validator_reputation
            st.session_state.evm_validator_reputation_score = evm_validator_reputation_risk.get(evm_validator_reputation, 0)

        if st.session_state.evm_validator_centralization != evm_validator_centralization:
            st.session_state.evm_validator_centralization = evm_validator_centralization
            st.session_state.evm_validator_centralization_score = evm_validator_centralization_risk.get(evm_validator_centralization, 0)

        if st.session_state.evm_equivalence != evm_equivalence:
            st.session_state.evm_equivalence = evm_equivalence
            st.session_state.evm_equivalence_score = evm_equivalence_risk.get(evm_equivalence, 0)

        if st.session_state.evm_client_div != evm_client_div:
            st.session_state.evm_client_div = evm_client_div
            st.session_state.evm_client_div_score = evm_client_div_risk.get(evm_client_div, 0)


        result7 = (st.session_state.evm_val_performance_acc_rate_var * st.session_state.evm_client_reputation_score * st.session_state.evm_validator_reputation_score *
                   st.session_state.evm_validator_centralization_score * st.session_state.evm_equivalence_score * 
                   st.session_state.evm_client_div_score * evm_metrics_likelihood2 * evm_metrics_impact2)
        
        result7_formatted = format_result(float(result7))


        evm_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_val_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_client_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_validator_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_validator_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_equivalence_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_client_div_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{evm_likelihood_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{evm_impact_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result7_formatted}</span>
            </div>"""

        st.markdown(evm_calc2, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")














  


        # Relayer Metrics

        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown("""
            <p class="header-style">
                <span style="color: white; background-color: black; border-radius: 50%; padding: 0.5em; font-family: monospace; display: inline-flex; align-items: center; justify-content: center; width: 1.5em; height: 1.5em; font-size: 0.85em; margin-right: 0.5em;">3</span>
                <span style="font-size: 21px;">RELAYER</span>
            </p>
                """, unsafe_allow_html=True)
        
        
        st.write("  \n")

        relayer_merkle = st.checkbox('**Merkle Multi-Proofs** used for Efficient XBlock Submission and Verification', value=True)
        
        relayer_da_solution = st.checkbox('**DA Solution** to address Complex Verification and Increased Computational Cost of Validator Signatures and Merkle Multi-Proofs At Scale', value=False)

        if st.session_state.relayer_merkle != relayer_merkle:
            st.session_state.relayer_merkle = relayer_merkle
            st.session_state.relayer_merkle_score = relayer_merkle_risk.get(relayer_merkle, 0)

        if st.session_state.relayer_da_solution != relayer_da_solution:
            st.session_state.relayer_da_solution = relayer_da_solution
            st.session_state.relayer_da_solution_score = relayer_da_solution_risk.get(relayer_da_solution, 0)

        result8 = (st.session_state.relayer_merkle_score + st.session_state.relayer_da_solution_score)
        
        st.write("  \n")

        relayer_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_merkle_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_da_solution_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result8):,}</span>
            </div>"""

        st.markdown(relayer_calc1, unsafe_allow_html=True)


########################################################


        st.write("-------")

        relayer_performance_acc_rate = st.slider("**Relayer Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                                     help="**The Performance Accuracy Rate of the Relayer in the overall `XMsg` submission process to the rollup destination chains with the respective generation of Merkle-multi proofs and signatures.**")
        
        col100, col101 = st.columns(2, gap="medium")
        with col100:
            relayer_reputation = st.selectbox("**Relayer Reputation**", ["Unknown", "Established", "Renowned"], index=0, key="43421",
                                                help="**Attests for a Relayer's trustworthiness in their role of delivering confirmed cross-network messages from Omni to destination rollups. This metric is particularly important for Omni as the Relayer constitutes a permissionless third-party.**")
        with col101:
            relayer_centralization = st.selectbox("**Relayer's Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="321132", index=0,
                                                    help="**Attests for the Relayer's robustness and stability in dealing with local regulations or targeted international attacks, as a permissionless, third-party entity.**")

        relayer_performance_acc_rate_var = relayer_performance_acc_rate_calc(relayer_performance_acc_rate)
        st.session_state.relayer_performance_acc_rate_var = relayer_performance_acc_rate_var

        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            relayer_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=7, key="r0", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            relayer_metrics_likelihood2 = relayer_metrics_likelihood / 2

        with col34:
            relayer_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=9, key="r1", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            relayer_metrics_impact2 = relayer_metrics_impact / 2

        relayer_likelihood_formatted = format_number(relayer_metrics_likelihood2)
        relayer_impact_formatted = format_number(relayer_metrics_impact2)


        with st.expander("Logic"):
                st.image("images/omni-relayer-diagram.jpg", width=750)

                st.markdown("""                        
The **Relayer** in the Omni network acts as a critical intermediary, handling the transfer of attested cross-network messages (`XMsgs`) between the Omni network and the various destination rollup VMs.Things to consider: 

- **Decision Making for Message Submission**: Post collecting `XBlocks` and `XMsgs`, Relayers determine the number of `XMsg`s to include in their submissions, balancing the costs associated with transaction size, computational requirements, and gas limits.
- **Relayer Performance**: Relayers create and submit transactions with Merkle multi-proofs to destination chains based on attested `XBlock` data, ensuring secure and efficient message delivery.
- **Security and Scalability**: As a permissionless service, Relayers reduce central points of failure and uphold the network's decentralized ethos, while managing security risks and computational intensiveness, especially as the network scales.
                            
The summation or multiplication of variables revolves around their independence or dependence toward one another, pragmatically speaking.
                            """)


        if st.session_state.relayer_reputation != relayer_reputation:
            st.session_state.relayer_reputation = relayer_reputation
            st.session_state.relayer_reputation_score = relayer_reputation_risk.get(relayer_reputation, 0)

        if st.session_state.relayer_centralization != relayer_centralization:
            st.session_state.relayer_centralization = relayer_centralization
            st.session_state.relayer_centralization_score = relayer_centralization_risk.get(relayer_centralization, 0)



        result9 = (st.session_state.relayer_reputation_score * st.session_state.relayer_centralization_score *
                   st.session_state.relayer_performance_acc_rate_var * relayer_metrics_likelihood2 * relayer_metrics_impact2)
        
        result9_formatted = format_result(float(result9))


        relayer_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_performance_acc_rate_var}</span>
                    <span style="font-size: 22px; font-weight: bold;">&times;</span> 
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{relayer_likelihood_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{relayer_impact_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result9_formatted}</span>
            </div>"""

        st.markdown(relayer_calc2, unsafe_allow_html=True)















    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    col1, col2, col3 = st.columns([1, 12, 1])

    # Placing the image in the middle column effectively centers it
    with col2:
        st.image("images/omni-main-diagram.jpg", width=1500)
    
    st.markdown("""
        <div style="text-align: center">
            Image from <a href="https://docs.omni.network/protocol/evmengine/dual" target="_blank">Omni Docs</a>
        </div>
        """, unsafe_allow_html=True)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")





#########################################
#########################################
#########################################


    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    risk_score = omni_risk(security_audits, business_model, relayer_reputation, relayer_da_solution, relayer_merkle, evm_client_div, evm_equivalence, sybil_mec, encrypted_mempool_mec, code_complexity,
             tee_mec, operator_reputation, operator_centralization, operator_entrenchment_level, engine_api, validator_abci_usage, dvt_mec, oracle_bridge_mec, lockup_mec, fast_fin_ss_mec, validator_reputation, 
             da_sol_mec, validator_centralization, relayer_centralization, evm_client_reputation, evm_validator_centralization, halo_reputation,
             evm_validator_reputation)
    
    (st.session_state.security_audits_score, st.session_state.business_model_score, st.session_state.evm_client_reputation_score,
    st.session_state.relayer_reputation_score, st.session_state.operator_reputation_score, st.session_state.evm_validator_centralization_score,
    st.session_state.code_complexity_score, st.session_state.evm_equivalence_score, st.session_state.halo_reputation_score,
    st.session_state.operator_centralization_score, st.session_state.validator_centralization_score, st.session_state.evm_validator_reputation_score,
    st.session_state.validator_reputation_score, st.session_state.dvt_mec_score,
    st.session_state.evm_client_div_score, st.session_state.operator_entrenchment_level_score,
    st.session_state.sybil_mec_score, st.session_state.relayer_da_solution_score,
    st.session_state.engine_api_score, st.session_state.validator_abci_usage_score,
    st.session_state.da_sol_mec_score, st.session_state.lockup_mec_score,
    st.session_state.fast_fin_ss_mec_score, st.session_state.tee_mec_score,
    st.session_state.encrypted_mempool_mec_score, st.session_state.relayer_merkle_score,
    st.session_state.oracle_bridge_mec_score, st.session_state.relayer_centralization_score) = risk_score
    


    col56,col57 = st.columns([10,6], gap="large")
    with col56:

        def normalize_score(original_score, min_original=14.25, max_original=77325):
            normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
            return normalized_score

        final_result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9
        normalized_risk_score = normalize_score(final_result)

        st.session_state.risk_score = normalized_risk_score

        st.markdown(f"<div style='text-align: center; font-size: 21px; font-weight: bold;'>Non-Normalized <i>Omni</i> Risk Score</div>", unsafe_allow_html=True)
        final_result_html = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result1_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result2_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result3_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result4):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result5_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result6):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result7_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result8):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result9_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 24px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{final_result:,.2f}</span>
                </div>
            """


        st.markdown(final_result_html, unsafe_allow_html=True)

        if st.session_state.risk_score >= 75:
            color = "#d32f2f"  # Red color for high risk
            background_color = "#fde0dc"  # Light red background
        elif st.session_state.risk_score <= 25:
            color = "#388e3c"  # Green color for low risk
            background_color = "#ebf5eb"  # Light green background
        else:
            color = "black"  # Black color for medium risk
            background_color = "#ffffff"  # White background

        
        st.write("  \n")
        st.write("  \n")

        st.markdown(
        f"""
        <div style="
            border: 2px solid {color};
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            margin: 10px 0;
            background-color: {background_color};">
            <h2 style="color: black; margin:0; font-size: 1.4em;">Normalized <i>Omni</i> Risk Score: <span style="font-size: 1.5em; color: {color};">{st.session_state.risk_score:.0f}</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
        )

        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


        st.markdown("""
                    <style>
                    .big-font {
                        font-size: 18px;  /* Adjust font size as needed */
                    }
                    </style>
                    <div class="big-font">
                    The <strong>Omni Risk Score</strong> is normalized to range from 0 to 100 (for easy reading), where 0 indicates the lowest level of risk and 100 represents the highest possible risk. The Risk Score is calculated based on the risk level of each input parameter as well as their weighting, which is determined by the <strong>Likelihood</strong> and <strong>Impact</strong> of that risk to the protocol as an AVS. 
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.write("**Note**: *It is important to bear in mind that since we are at the very early stages of AVS development and little-to-no information is available, the value judgements below are prone to being faulty.*")

    with col57:

        col111, col121, col131 = st.columns([1,5,4])

        with col111:
            st.write("")

        with col121:
            st.image("images/omni-matrix.jpg", width=600)

        with col131:
            st.write("")














    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    col11, col12, col13 = st.columns([6,3,5])

    with col11:
        st.write("")

    with col12:
        st.image("images/tokensight.png", width=250)

    with col13:
        st.write("")
    
    
    image_url = 'https://img.freepik.com/free-vector/twitter-new-2023-x-logo-white-background-vector_1017-45422.jpg'
    link = 'https://twitter.com/tokensightxyz'
    markdown = f"""
    <a href="{link}" target="_blank">
        <img src="{image_url}" alt="Alt Text" style="display:block; margin-left: auto; margin-right: auto; width: 4%;">
    </a>
    """    
    st.markdown(markdown, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

