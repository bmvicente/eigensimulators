

import streamlit as st


security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
relayer_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
validator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
code_complexity_risk = {"High": 10, "Medium": 5, "Low": 2}
operator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
evm_equivalence_risk = {"Incompatible": 10, "Compatible": 5, "Equivalent": 1}
validator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
evm_client_div_risk = {"Poorly Diverse": 10, "Moderately Diverse": 5, "Highly Diverse": 1}
operator_entrenchment_level_risk = {"High Entrenchment": 10, "Moderate Entrenchment": 5, "Low Entrenchment": 1}
engine_api_risk = {True: 1, False: 2}
dvt_mec_risk = {True: 1, False: 2}
sybil_mec_risk = {True: 1, False: 2}
relayer_da_solution_risk = {True: 1, False: 2}
validator_abci_usage_risk = {True: 1, False: 2}
da_sol_mec_risk = {True: 1, False: 2}
lockup_mec_risk = {True: 1, False: 2}
fast_fin_ss_mec_risk = {True: 1, False: 2}
tee_mec_risk = {True: 1, False: 2}
encrypted_mempool_mec_risk = {True: 1, False: 2}
relayer_merkle_risk = {True: 1, False: 2}
oracle_bridge_mec_risk = {True: 1, False: 2}




def omni_risk(security_audits, business_model, relayer_reputation, relayer_da_solution,
                relayer_merkle, evm_client_div, evm_equivalence, sybil_mec, encrypted_mempool_mec, code_complexity,
                tee_mec, operator_reputation, operator_centralization, operator_entrenchment_level, engine_api,
                validator_abci_usage, dvt_mec, oracle_bridge_mec, lockup_mec, fast_fin_ss_mec, validator_reputation, 
                da_sol_mec, validator_centralization):

        security_audits_score = security_audits_risk[security_audits]
        business_model_score = business_model_risk[business_model]
        relayer_reputation_score = relayer_reputation_risk[relayer_reputation]
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

        return (security_audits_score, business_model_score, relayer_reputation_score, 
                    operator_reputation_score, code_complexity_score, evm_equivalence_score,
                    operator_centralization_score, validator_centralization_score, validator_reputation_score, 
                    dvt_mec_score, evm_client_div_score, operator_entrenchment_level_score, da_sol_mec_score,
                    sybil_mec_score, relayer_da_solution_score, validator_abci_usage_score, engine_api_score,
                    lockup_mec_score, fast_fin_ss_mec_score, tee_mec_score, encrypted_mempool_mec_score,
                    relayer_merkle_score, oracle_bridge_mec_score)


def main():
    st.set_page_config(layout="wide")

    st.image("images/omni.jpeg", width=450)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Interoperability Network AVS: Omni Underlying Risk & Slashing Conditions Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
                    The consensus layer is implemented by the Omni consensus client, halo, and uses CometBFT for consensus on XMsgs and Omni EVM blocks.

            The Simulator takes six of the AVS-generic parameters to simulate their Risk Score and four parameters that specifically compose a Shared Sequencer AVS like Omni. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            A good deal of the logic behind the right side of the Simulator (OMNI-SPECIFIC METRICS) was researched on Nethermind's recent whitepaper [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581), specifically for Omni.
                    
            The most significant parameter is the first: Cost-of-Corruption/Profit-from-Corruption relationship, since it poses the greatest weight on an AVS being corrupted or cryptoeconomically secure. 
        """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate utility or scenario for Omni as a Interoperability AVS.")

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
        st.session_state.relayer_reputation = "Renowned"  # Set default value
    if 'relayer_reputation_score' not in st.session_state:
        if st.session_state.relayer_reputation in relayer_reputation_risk:  # Check if code complexity exists in the dictionary
            st.session_state.relayer_reputation_score = relayer_reputation_risk[st.session_state.relayer_reputation]
        else:
            st.session_state.relayer_reputation_score = 0

    if 'operator_reputation' not in st.session_state:
        st.session_state.operator_reputation = "Renowned"  # Set default value
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
        st.session_state.operator_centralization = "Decentralized"  # Set default value
    if 'operator_centralization_score' not in st.session_state:
        if st.session_state.operator_centralization in operator_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.operator_centralization_score = operator_centralization_risk[st.session_state.operator_centralization]
        else:
            st.session_state.operator_centralization_score = 0

    if 'validator_centralization' not in st.session_state:
        st.session_state.validator_centralization = "Decentralized"  # Set default value
    if 'validator_centralization_score' not in st.session_state:
        if st.session_state.validator_centralization in validator_centralization_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_centralization_score = validator_centralization_risk[st.session_state.validator_centralization]
        else:
            st.session_state.validator_centralization_score = 0

    if 'validator_reputation' not in st.session_state:
        st.session_state.validator_reputation = "Renowned"  # Set default value
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

    if 'evm_client_div' not in st.session_state:
        st.session_state.evm_client_div = "Highly Diverse"  # Set default value
    if 'evm_client_div_score' not in st.session_state:
        if st.session_state.evm_client_div in evm_client_div_risk:  # Check if code complexity exists in the dictionary
            st.session_state.evm_client_div_score = evm_client_div_risk[st.session_state.evm_client_div]
        else:
            st.session_state.evm_client_div_score = 0

    if 'operator_entrenchment_level' not in st.session_state:
        st.session_state.operator_entrenchment_level = "Low Entrenchment"  # Set default value
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
        st.session_state.validator_abci_usage = "False"  # Set default value
    if 'validator_abci_usage_score' not in st.session_state:
        if st.session_state.validator_abci_usage in validator_abci_usage_risk:  # Check if code complexity exists in the dictionary
            st.session_state.validator_abci_usage_score = validator_abci_usage_risk[st.session_state.validator_abci_usage]
        else:
            st.session_state.validator_abci_usage_score = 0

    if 'engine_api_score' not in st.session_state:
        st.session_state.engine_api = "False"  # Set default value
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
        st.session_state.relayer_merkle = "False"  # Set default value
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
            restaked_eth_del = st.number_input("", min_value=0, max_value=100000000000, step=100000000)
            st.write(f"&#8226; Total Restaked ETH to Omni: **${restaked_eth_del:,.0f}**")


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
            st.write(f"&#8226; Total Restaked TVL on Omni: **${restaked_tvl:,.0f}**")


            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")



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

            # Displaying the custom styled header
            st.markdown('<p class="header-style">AVS Business Model</p>', unsafe_allow_html=True)

            # Dropdown menu
            business_model = st.selectbox("", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"], index=1)

        with col48:
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
            st.markdown('<p class="header-style">AVS Dual Staking Model: Native Dual Staking</p>', unsafe_allow_html=True)
            
            st.write("  \n")

            avs_token_percentage = st.slider("**% $OMNI**", min_value=10, max_value=90, value=50, format='%d%%')

            xeth_percentage = 100 - avs_token_percentage
            
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, format='%d%%')

            st.write("&#8226; **Native Dual Staking Balance**: {}% $OMNI : {}% xETH".format(avs_token_percentage, xeth_percentage))

        st.write("-------")

        col44,col45 = st.columns(2, gap="medium")
        with col44:
            business_dual_likelihood = st.slider("*Likelihood* ", min_value=1, max_value=10, value=3, key='afa')
        with col45:
            business_dual_impact = st.slider("*Impact* ", min_value=1, max_value=10, value=7, key='ewe')

        dual_staking_balance = dual_staking_balance_calc(avs_token_percentage, xeth_percentage)
        st.session_state.dual_staking_balance = dual_staking_balance
        
        if st.session_state.business_model != business_model:
            st.session_state.business_model = business_model
            st.session_state.business_model_score = business_model_risk.get(business_model, 0)

        with st.expander("Logic"):
                st.markdown("""
                    Ordering the **Business Models** from EigenLayer [(Section 4.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) by risk: 
                    
                    - ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$AVS), tying closely to its market performance and the AVS's ongoing profitability;
                    - ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $AVS stakers, which introduces complexities in security and token value dynamics;
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
                            
                    Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                    **\$AVS** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$AVS* **>** *% xETH* pool balance makes sense to be a higher-reward event.
                        """)
    
        
        result1 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_dual_likelihood * business_dual_impact

        business_dual_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{business_dual_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{business_dual_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result1):,}</span>
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


            st.markdown('<p class="header-style">AVS Protocol Architecture & Code Complexity</p>', unsafe_allow_html=True)

            code_complexity = st.selectbox("", ["High", "Medium", "Low"], index=1, key="ertr")
            
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

            st.markdown('<p class="header-style">AVS Number of Security Audits</p>', unsafe_allow_html=True)

            security_audits = st.number_input("", min_value=0, max_value=5, step=1, value=2, key="00")

        col35,col36 = st.columns(2, gap="medium")
        with col35:
                    security_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4)
        with col36:
                    security_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8)

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

        result2 = st.session_state.code_complexity_score * st.session_state.security_audits_score * security_likelihood * security_impact


        security_calc = f"""
                    <div style="text-align: center;">
                        <div>
                            <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.code_complexity_score}</span> 
                            <span style="font-size: 24px; font-weight: bold;">&times;</span>
                            <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.security_audits_score}</span> 
                            <span style="font-size: 24px; font-weight: bold;">&times;</span>
                            <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{security_likelihood}</span> 
                            <span style="font-size: 24px; font-weight: bold;">&times;</span>
                            <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{security_impact}</span> 
                            <span style="font-size: 24px; font-weight: bold;"> = </span>
                            <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result2):,}</span>
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
        st.write("  \n")

        # Operator Metrics
        st.markdown("""
                    <style>
                    .header-style {
                        font-size: 18px;
                        font-weight: bold;
                        margin-bottom: 0px;  /* Adjust the space below the header */
                    }
                    </style>
                    """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">AVS Operator Metrics</p>', unsafe_allow_html=True)
 
        st.write("  \n")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
                operator_reputation = st.selectbox("**Operator Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="6783")

        with col101:            
                operator_centralization = st.selectbox("**Operators' Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="674")
            

        operator_entrenchment_level = st.selectbox("**Operators' Entrenchment Level** (on other AVSs)", ["High Entrenchment", "Moderate Entrenchment", "Low Entrenchment"], key="09111")

        st.write("-------")

        col33, col34 = st.columns(2, gap="medium")
        with col33:
            operator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="o0")
        with col34:
            operator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="o1")

        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
                        The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581):
                        
                        "*Full MEV extraction and implementing censorship on shared sequencers pose a significant challenge for an attacker. To ensure the success of such an attack and to collect the entire MEV generated, an attacker would need control over 100% of the validators. In certain sequencer setups, where leader election is lottery-based, there might be an incentive for validators to collude to maximize the amount of MEV distributed to validators as opposed to the chains.*"
                        
                        Given the significant challenge MEV extraction poses to an attacker, it was assigned a somewhat low Likelihood, but still a considerable Impact were the attack to happen.
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
                   st.session_state.operator_entrenchment_level_score * operator_metrics_likelihood * operator_metrics_impact)

        operator_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_reputation_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_centralization_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_entrenchment_level_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{operator_metrics_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{operator_metrics_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result3):,}</span>
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
        st.write(f"&#8226; Total Staked \$OMNI: **${staked_omni:,.0f}**")


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
                CometBFT Consensus Architecture Metrics through Consensus Client (Halo)
            </p>
            """, unsafe_allow_html=True)


        st.write("  \n")

        col38,col39 = st.columns(2, gap="medium")
        with col38:
            engine_api = st.checkbox('**Ethereum Engine API** used by Nodes to pair the Consensus Client (Halo) with the EVM Execution Client', 
                                     value=True, help="The Ethereum Engine API pairs an existing Ethereum Execution Client with a Consensus Client (like halo) that implements CometBFT consensus.")
        with col39:
            validator_abci_usage = st.checkbox('**Engine API uses ABCI++** for seamless state transitions between Omni EVM and CometBFT', value=True,
                                               help="ABCI++ is an adapter that wraps around the CometBFT engine, translating Engine API messages for consensus processing, ensuring Omni's lightweight consensus and quick finality.")

        col42,col43 = st.columns(2, gap="medium")
        with col42:
            tee_mec = st.checkbox('**TEE** Implementation for Effective Key Management', value=False,
                                  help="TEEs consist of secure portions of hardware that generate and securely store validator keys and databases of previously signed data. By design, they enhance security without comprimising scalability, and through increased trust, encourage stake delegation.")
        with col43:
            dvt_mec = st.checkbox('**DVT** Implementation to Reduce Risks of Single Points of Failure from a Subset of Validators', value=False,
                                  help="DVT is a technology that incentivizes client diversity through the distribution of the validation process across multiple operators. It reduces the risk of single points of failure or malicious actions.")

        col50,col51 = st.columns(2, gap="medium")
        with col50:
            oracle_bridge_mec = st.checkbox('**Oracle/Bridge Solution** to Restrict Potential PfC', value=False,
                                            help="To restrict the potential PfC extracted from Omni, a bridge can be set-up to restrict the value flow within the period of slashing, or an oracle can have bounds on the total value transacted within a given period.")
        with col51:
            lockup_mec = st.checkbox('**Withdrawal Lock-Up Periods** Applied to Validators for Security Against Corruption', value=False)

        col52,col53 = st.columns(2, gap="medium")
        with col52:
            da_sol_mec = st.checkbox('**DA Solution** for Horizontal Scaling of Nodes, Mitigating Potential State Explosions and Low Latency', value=False)
        with col53:
            fast_fin_ss_mec = st.checkbox('**Shared Sequencer Pre-Confirmation Solution** for *XMsg* Fast Finality', value=False)

        st.write("-------")

        validator_performance_acc_rate = st.slider("**Validator XBlocks Attestation Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                                   help="**The Performance Accuracy Rate of Validators attesting for XBlocks consists of the timely submission of cross-chain messages, XBlock cache management, and the overall decision-making in including XMsgs in an XBlock.**")
        
        validator_performance_acc_rate_var = validator_performance_acc_rate_calc(validator_performance_acc_rate)
        st.session_state.validator_performance_acc_rate_var = validator_performance_acc_rate_var

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            validator_reputation = st.selectbox("**Validator Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="0990",
                                                help="Attests for a set of validators' trustworthiness in their role of confirming and validating CometBFT blocks and attesting to XBlocks before being submitted on-chain.")
        with col101:           
            validator_centralization = st.selectbox("**Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="3232",
                                                    help="Attests for a set of validators' robustness and stability in dealing with local regulations or targeted international attacks.")
        
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            validator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="v0")
        with col34:
            validator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="v1")

        with st.expander("Logic"):
                st.image("images/omni-comet-diagram.jpg", width=750)

                st.markdown("""
Using the Engine API, Omni nodes pair existing high performance Ethereum execution clients with a new consensus client, referred to as halo, that implements CometBFT consensus.The Engine API allows clients to be substituted or upgraded without breaking the system. This allows the protocol to maintain flexibility on Ethereum and Cosmos technology while promoting client diversity within its execution layer and consensus layer. We consider this new network framework to be a public good that future projects may leverage for their own network designs.
                            
        ABCI++  while introducing benefits at the application layer particularly, also introduce complexity in application design, multi-faceted security vulnerabilities, and performance overhead to the whole process. It is paramount to consider the deterministic design and logic of integrated applications.

        Application BlockChain Interface (ABCI++): Leveraging CometBFT's ABCI, Omni introduces enhancements (potentially hinted at by the name ABCI++) that allow for more complex and flexible application interactions. This includes processing state transitions for the Omni EVM and external VMs without interference.
                Validators compile XMsg into XBlocks, which include metadata for efficient verification and attestation, streamlining the relaying process.
                            
                Engine API Conversion: An ABCI++ adapter wraps around the CometBFT engine, translating Engine API messages for consensus processing, ensuring Omni's lightweight consensus and quick finality.
                    During the consensus, validators utilize ABCI++ to attest to the state of Rollup VMs, running state transition functions for accurate and secure external VM interactions.
                            
                    Leveraging CometBFT's ABCI, Omni introduces enhancements (potentially hinted at by the name ABCI++) that allow for more complex and flexible application interactions. This includes processing state transitions for the Omni EVM and external VMs without interference.
                    
                    Decoupled Consensus and Application Logic: The separation of the consensus engine and application logic via ABCI facilitates the creation of diverse applications, from cryptocurrencies to e-voting systems, without being limited to a specific blockchain's capabilities or language.
                            

                    The Performance Accuracy Rate of Validators attesting for XBlocks consist of:
                    - **Submission of Cross-Chain Messages**: Relayers wait for more than two-thirds of the validators to attest to a source chain block. They then submit the validated XMsgs to the destination chains, along with necessary validator signatures and multi-merkle-proof.
- **Attestation Monitoring and XBlock Cache Management**: Relayers monitor the Omni Consensus Chain for attested XBlocks, maintaining a cache of these blocks for efficient processing and submission readiness.
- **Decision Making for Message Submission**: Relayers decide on the number of XMsgs to submit, balancing transaction cost considerations like data size and gas limits.
                            """)


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

        if st.session_state.validator_reputation != validator_reputation:
            st.session_state.validator_reputation = validator_reputation
            st.session_state.validator_reputation_score = validator_reputation_risk.get(validator_reputation, 0)

        if st.session_state.validator_centralization != validator_centralization:
            st.session_state.validator_centralization = validator_centralization
            st.session_state.validator_centralization_score = validator_centralization_risk.get(validator_centralization, 0)



        result4 = (st.session_state.engine_api_score * st.session_state.validator_abci_usage_score *
                   st.session_state.tee_mec_score * st.session_state.dvt_mec_score * st.session_state.oracle_bridge_mec_score *
                   st.session_state.lockup_mec_score * st.session_state.da_sol_mec_score * st.session_state.fast_fin_ss_mec_score *
                   st.session_state.validator_performance_acc_rate_var * st.session_state.validator_reputation_score *
                   st.session_state.validator_centralization_score *
                    validator_metrics_likelihood * validator_metrics_impact)

        
        validator_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.engine_api_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_abci_usage_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.tee_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dvt_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.oracle_bridge_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.lockup_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.da_sol_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.fast_fin_ss_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_performance_acc_rate_var}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_reputation_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_centralization_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{validator_metrics_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{validator_metrics_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result4):,}</span>
            </div>"""

        st.markdown(validator_calc, unsafe_allow_html=True)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("\n")
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
                EVM Metrics through Execution Client
            </p>
            """, unsafe_allow_html=True)
        

        st.write("  \n")
        
        sybil_mec = st.checkbox('**Anti-Sybil Mechanism** for transactions submitted to the Omni EVM, deterring spam and malicious activities such as DoS attacks', value=True,
                                help="sss")
        
        encrypted_mempool_mec = st.checkbox('**Encrypted Mempool** for increased privacy and security in transactions', value=False,
                                            help="eeee")

        st.write("-------")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            evm_equivalence = st.selectbox("**EVM Compatibility**", ["Incompatible", "Compatible", "Equivalent"], index=2, key="09",
                                           help="**As a product of...")
        with col101:
            evm_client_div = st.selectbox("**EVM Client Diversity**", ["Poorly Diverse", "Moderately Diverse", "Highly Diverse"], key="7877", index=2,
                                          help="**As a product of...** Omni adheres to the Engine API, a standard that all EVM clients also comply with. This adherence ensures that any EVM client, such as Geth, Besu, Erigon, and others, can be seamlessly integrated into the Omni network without the need for specialized modifications. This approach allows the Omni ecosystem to leverage the unique features and optimizations that different clients provide.")
            
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            evm_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="e0")
        with col34:
            evm_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="e1")

        with st.expander("Logic"):
                st.markdown("""
**Execution Consensus**
1. When it is a validator's turn to propose a block, its halo client requests the latest Omni EVM block from its execution client using the Engine API.
2. The execution client builds a block from the transactions in its mempool and returns the block header to the halo client through the Engine API.
3. The halo client packages the new block proposal as a single CometBFT transaction and includes it in the consensus layer block.
4. The block is proposed to the rest of the validator network through the consensus layer’s P2P network.
5. Non-proposing validators use the Engine API and their execution clients to run the state transition function on the proposed block header to verify the block’s validity.
                        
                    OMNI provides an anti-sybil mechanism for transactions submitted to the Omni EVM, deterring spam and malicious activities such as denial-of-service attacks.        
                    
                    Developer Accessibility and EVM Equivalence: By ensuring EVM equivalence, Omni offers a seamless transition for Ethereum developers, making it a more accessible platform for deploying decentralized applications (DApps) without modifications.
                    
                    **Engine API**

                    - **Scalability and Efficiency:** By offloading the transaction mempool and facilitating efficient state translation, the Engine API contributes to Omni's scalability and sub-second transaction finality.
                    - **Flexibility:** Supports the interchangeability and upgrading of execution clients without system disruption, ensuring compatibility with various Ethereum execution clients.
                            
                    This fidelity guarantees that opcode compatibility issues are non-existent, and all developer tooling designed for Ethereum seamlessly works with the Omni EVM.

### Advantages of Omni’s EVM Equivalence

- **Seamless Migration:** Developers can port their DApps to Omni without any modifications, significantly reducing the effort and complexity involved in accessing a new blockchain ecosystem.
- **Developer Tooling Compatibility:** All the tools, libraries, and frameworks designed for Ethereum development are fully compatible with the Omni EVM, streamlining the development process.
- **Future-Proof:** Omni's alignment with Ethereum's upgrade path ensures that developers can leverage the latest features and improvements without delay.
                            
                    Client Diversity and EVM Equivalence: Omni emphasizes running an unmodified version of the Ethereum Virtual Machine (EVM), which guarantees that Ethereum smart contracts and developer tooling work seamlessly. This focus on EVM equivalence and support for diverse client implementations enhances developer accessibility and network resilience.
                            """)

        if st.session_state.encrypted_mempool_mec != encrypted_mempool_mec:
            st.session_state.encrypted_mempool_mec = encrypted_mempool_mec
            st.session_state.encrypted_mempool_mec_score = encrypted_mempool_mec_risk.get(encrypted_mempool_mec, 0)

        if st.session_state.sybil_mec != sybil_mec:
            st.session_state.sybil_mec = sybil_mec
            st.session_state.sybil_mec_score = sybil_mec_risk.get(sybil_mec, 0)

        if st.session_state.evm_equivalence != evm_equivalence:
            st.session_state.evm_equivalence = evm_equivalence
            st.session_state.evm_equivalence_score = evm_equivalence_risk.get(evm_equivalence, 0)

        if st.session_state.evm_client_div != evm_client_div:
            st.session_state.evm_client_div = evm_client_div
            st.session_state.evm_client_div_score = evm_client_div_risk.get(evm_client_div, 0)


        result5 = (st.session_state.sybil_mec_score * st.session_state.encrypted_mempool_mec_score * 
                   st.session_state.evm_equivalence_score * st.session_state.evm_client_div_score * 
                   evm_metrics_likelihood * evm_metrics_impact)

        evm_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.sybil_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.encrypted_mempool_mec_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_equivalence_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.evm_client_div_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{evm_metrics_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{evm_metrics_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result5):,}</span>
            </div>"""

        st.markdown(evm_calc, unsafe_allow_html=True)



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
                Relayer Metrics
            </p>
            """, unsafe_allow_html=True)
        
        
        st.write("  \n")

        relayer_merkle = st.checkbox('Use of **Merkle Multi-Proofs** for efficient XBlock Submission', value=True,
                                     help="ss")
        relayer_da_solution = st.checkbox('**DA Solution** for Complex Verification of Validator Signatures and Merkle Multi-Proofs At Scale', value=False,
                                          help="fe")

        st.write("-------")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            relayer_reputation = st.selectbox("**Relayer Reputation**", ["Unknown", "Established", "Renowned"], index=1, key="43421",
                                              help="hh")
        with col101:
            relayer_performance_acc_rate = st.slider("**Relayer Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                                     help="s")

        relayer_performance_acc_rate_var = relayer_performance_acc_rate_calc(relayer_performance_acc_rate)
        st.session_state.relayer_performance_acc_rate_var = relayer_performance_acc_rate_var

        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            relayer_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="r0")
        with col34:
            relayer_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="r1")

        with st.expander("Logic"):
                st.image("images/omni-relayer-diagram.jpg", width=750)

                st.markdown("""                        
                            Decision Making for Message Submission
A key decision that Relayers face is determining the number of XMsgs to submit to each destination chain. This decision directly influences the cost of transactions due to factors like data size, gas limits, and the computational overhead required for portal contract verification and message processing.
                            Relayer responsible for delivering attested cross-network messages from the Omni network to destination rollup VMs. Monitors the Omni Consensus Layer until ⅔ (>66%) of the validator set attested to the “next” block on each source chain, then proceeds to forwarding the respective XMsg list included in the block.
Relayers are responsible for delivering confirmed cross-network messages from Omni to destination rollups. When 2/3 (>66%) of Omni validators attest to a given XBlock, relayers forward the XBlock’s corresponding XMsg list to destination rollup networks.
                            
                            While Merkle multi-proofs provide a powerful tool for efficient data verification across blockchain networks, careful consideration of these risks and appropriate mitigations are essential to maintaining the security, efficiency, and robustness of blockchain protocols that utilize them.
        
                            - **Decision Making for Message Submission**: A key decision that Relayers face is determining the number of **`XMsg`**s to submit to each destination chain. This decision directly influences the cost of transactions due to factors like data size, gas limits, and the computational overhead required for portal contract verification and message processing. (**PERFORMANCE ACCURACY RATE**)
- **Submission** **Transaction**: For the actual submission to a destination chain, Relayers generate a merkle-multi-proof for the **`XMsg`**s that are to be included, based on the **`XBlock`** attestations root that has reached a quorum. They then craft an EVM transaction containing this data, aiming to ensure its swift inclusion on the destination chain.        
                    At scale, Merkle multi-proofs introduce data availability concerns, complexity in verification, and increased computational cost.
                            
                            Resource Intensiveness: The need for signature and merkle proof verification for each message can be resource-intensive, especially on high-traffic networks.
        Permissionless third-party Relayer (Permissionless — reduces single point of failure likelihood | decentralized): The Relayer plays a pivotal role in the Omni protocol as a permissionless entity that bridges cross-chain messages between source and destination chains. It performs critical functions that ensure the smooth and secure transmission of messages across the network.

        Relayer Submits XBlocks: Relayers construct submissions for each finalized XBlock hash, including validator signatures and merkle proofs of each XMsg's inclusion. (DA CONSTRAINTS AT SCALE)
                Relayer Role Security: While the permissionless relayer mechanism is a strength for interoperability, it also introduces a potential vector for attacks if relayers behave maliciously or if the reputation system is not robust enough to incentivize honest participation.
                            
                To submit XMsgs to a destination chain, Relayers generate a merkle-multi-proof for the XMsgs tied to an attested XBlock. They package this information into an EVM transaction aimed at the destination chain, encapsulating the core of their role in cross-chain communication.
                
                After validators' attestation, relayers submit XBlocks and their messages to destination chains, employing merkle-multi-proofs for verification.
                    Relayer Role Security: While the permissionless relayer mechanism is a strength for interoperability, it also introduces a potential vector for attacks if relayers behave maliciously or if the reputation system is not robust enough to incentivize honest participation.
                            """)


        if st.session_state.relayer_merkle != relayer_merkle:
            st.session_state.relayer_merkle = relayer_merkle
            st.session_state.relayer_merkle_score = relayer_merkle_risk.get(relayer_merkle, 0)

        if st.session_state.relayer_da_solution != relayer_da_solution:
            st.session_state.relayer_da_solution = relayer_da_solution
            st.session_state.relayer_da_solution_score = relayer_da_solution_risk.get(relayer_da_solution, 0)

        if st.session_state.relayer_reputation != relayer_reputation:
            st.session_state.relayer_reputation = relayer_reputation
            st.session_state.relayer_reputation_score = relayer_reputation_risk.get(relayer_reputation, 0)


        result6 = (st.session_state.relayer_merkle_score * st.session_state.relayer_da_solution_score * 
                   st.session_state.relayer_reputation_score * st.session_state.relayer_performance_acc_rate_var * 
                   relayer_metrics_likelihood * relayer_metrics_impact)

        
        relayer_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_merkle_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_da_solution_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_reputation_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.relayer_performance_acc_rate_var}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{relayer_metrics_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{relayer_metrics_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result6):,}</span>
            </div>"""

        st.markdown(relayer_calc, unsafe_allow_html=True)



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


    def normalize_score(original_score, min_original=17, max_original=17700):
        normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
        return normalized_score

    final_result = result1 + result2 + result3 + result4 + result5 + result6
    normalized_risk_score = normalize_score(final_result)

    st.session_state.risk_score = normalized_risk_score

    st.markdown(f"<div style='text-align: center; font-size: 21px; font-weight: bold;'>Non-Normalized <i>Omni</i> Risk Score</div>", unsafe_allow_html=True)
    final_result_html = f"""
            <div style="text-align: center;">
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result1):,}</span> 
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result2):,}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result3):,}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result4):,}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result5):,}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result6):,}</span>
                <span style="font-size: 22px; font-weight: bold;"> = </span>
                <span style="font-size: 24px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(final_result):,}</span>
            </div>
        """

    st.markdown(final_result_html, unsafe_allow_html=True)



#########################################
#########################################
#########################################


    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    




    risk_score = omni_risk(security_audits, business_model, relayer_reputation, relayer_da_solution, relayer_merkle, evm_client_div, evm_equivalence, sybil_mec, encrypted_mempool_mec, code_complexity,
             tee_mec, operator_reputation, operator_centralization, operator_entrenchment_level, engine_api, validator_abci_usage, dvt_mec, oracle_bridge_mec, lockup_mec, fast_fin_ss_mec, validator_reputation, 
             da_sol_mec, validator_centralization)
    
    (st.session_state.security_audits_score, st.session_state.business_model_score,
    st.session_state.relayer_reputation_score, st.session_state.operator_reputation_score,
    st.session_state.code_complexity_score, st.session_state.evm_equivalence_score,
    st.session_state.operator_centralization_score, st.session_state.validator_centralization_score,
    st.session_state.validator_reputation_score, st.session_state.dvt_mec_score,
    st.session_state.evm_client_div_score, st.session_state.operator_entrenchment_level_score,
    st.session_state.sybil_mec_score, st.session_state.relayer_da_solution_score,
    st.session_state.engine_api_score, st.session_state.validator_abci_usage_score,
    st.session_state.da_sol_mec_score, st.session_state.lockup_mec_score,
    st.session_state.fast_fin_ss_mec_score, st.session_state.tee_mec_score,
    st.session_state.encrypted_mempool_mec_score, st.session_state.relayer_merkle_score,
    st.session_state.oracle_bridge_mec_score) = risk_score
    



    if st.session_state.risk_score >= 75:
        color = "#d32f2f"  # Red color for high risk
        background_color = "#fde0dc"  # Light red background
    elif st.session_state.risk_score <= 25:
        color = "#388e3c"  # Green color for low risk
        background_color = "#ebf5eb"  # Light green background
    else:
        color = "black"  # Black color for medium risk
        background_color = "#ffffff"  # White background

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
                The <strong>Omni Risk Score</strong> is normalized to range from 0 to 100 (for easy reading), where 0 indicates the lowest level of risk and 100 represents the highest possible risk. The Risk Score is calculated based on the risk level of each input parameter as well as their weighting, which is determined by the <strong>Likelihood</strong> and <strong>Impact</strong> of that risk to the AVS. 
                </div>
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
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    col11, col12, col13 = st.columns([2,1,2])

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

