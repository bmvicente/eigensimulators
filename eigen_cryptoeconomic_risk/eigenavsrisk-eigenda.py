

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

bls_alt_risk = {True: 1, False: 10}
rollup_fast_proof_risk = {True: 1, False: 10}
kzg_erasure_coding_risk = {True: 1, False: 10}
kzg_multi_proofs_risk = {True: 1, False: 10}
disperser_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
rollup_backup_disperser_risk = {True: 1, False: 10}
disperser_operator_risk = {"Disperser Run by Rollup": 8, "Disperser Run by Third-Party (like EigenLabs)": 2}


def eigenda_risk(security_audits, business_model, code_complexity, operator_reputation, operator_centralization, 
                 operator_entrenchment_level, tee_mec, dvt_mec, validator_reputation, validator_centralization,
                 bls_alt, rollup_fast_proof, disperser_centralization, kzg_erasure_coding, 
                 kzg_multi_proofs, rollup_backup_disperser, disperser_operator):

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

    bls_alt_score = bls_alt_risk[bls_alt]
    rollup_fast_proof_score = rollup_fast_proof_risk[rollup_fast_proof]
    disperser_centralization_score = disperser_centralization_risk[disperser_centralization]
    kzg_erasure_coding_score = kzg_erasure_coding_risk[kzg_erasure_coding]
    kzg_multi_proofs_score = kzg_multi_proofs_risk[kzg_multi_proofs]
    rollup_backup_disperser_score = rollup_backup_disperser_risk[rollup_backup_disperser]
    disperser_operator_score = disperser_operator_risk[disperser_operator]


    return (security_audits_score, business_model_score, code_complexity_score, operator_reputation_score, operator_centralization_score,
            operator_entrenchment_level_score, tee_mec_score, dvt_mec_score, validator_reputation_score, validator_centralization_score, 
            bls_alt_score, rollup_fast_proof_score, disperser_centralization_score, kzg_erasure_coding_score, kzg_multi_proofs_score, 
            rollup_backup_disperser_score, disperser_operator_score)




def main():
    st.set_page_config(layout="wide")

    st.image("images/eigenda.jpeg", width=250)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Data Availability AVS: EigenDA Underlying Risk & Slashing Conditions Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
            The Simulator takes 9 AVS-generic parameters and 21 parameters that specifically compose an Interoperability Network protocol with a CometBFT consensus architecture to calculate EigenDA's Risk Score as an EigenLayer AVS. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            
            Most of the research to build this Simulator was derived from [EigenDA's Docs](https://docs.omni.network/) and [CometBFT's Docs](https://docs.cometbft.com/v0.37/), as well as the images in the "Logic" dropdowns.
                            """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate Risk Profile for EigenDA as a Interoperability Network AVS. *It is important to bear in mind that since we are at the very early stages of AVS development and little-to-no information is available, the value judgements below are prone to being faulty.*")

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
            return 2
        elif 11 <= rollup_bandwidth_rate <= 33:
            return 3
        elif 34 <= rollup_bandwidth_rate <= 50:
            return 4
        elif 51 <= rollup_bandwidth_rate <= 66:
            return 6
        elif 67 <= rollup_bandwidth_rate <= 90:
            return 7.5
        elif 91 <= rollup_bandwidth_rate <= 100:
            return 9
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

    if 'rollup_backup_disperser' not in st.session_state:
        st.session_state.rollup_backup_disperser = "True"
    if 'rollup_backup_disperser_score' not in st.session_state:
        if st.session_state.rollup_backup_disperser in rollup_backup_disperser_risk:
            st.session_state.rollup_backup_disperser_score = rollup_backup_disperser_risk[st.session_state.rollup_backup_disperser]
        else:
            st.session_state.rollup_backup_disperser_score = 0

    if 'disperser_operator' not in st.session_state:
        st.session_state.disperser_operator = "True"
    if 'disperser_operator_score' not in st.session_state:
        if st.session_state.disperser_operator in disperser_operator_risk:
            st.session_state.disperser_operator_score = disperser_operator_risk[st.session_state.disperser_operator]
        else:
            st.session_state.disperser_operator_score = 0

    
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
                background-color: #000080;">
                <h2 class='large-header-style' style="color: white; margin:0;">AVS-GENERIC METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")




        col59, col60 = st.columns(2)
        with col59:
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

            st.markdown('<p class="header-style">OBJECTIVE SECURITY: Total ETH Restaked on EigenDA</p>', unsafe_allow_html=True)

            restaked_eth_del = st.number_input("", min_value=0, max_value=100000000000, step=100000000, value=2900000)
            st.write(f"&#8226; Total ETH Restaked on EigenDA: **{restaked_eth_del:,.0f} ETH**")


        with col60:

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

            st.markdown('<p class="header-style">INTERSUBJECTIVE SECURITY: Total $bEIGEN Staked</p>', unsafe_allow_html=True)

            restaked_eth_del = st.number_input("", min_value=0, max_value=100000000000, step=100000000, value=0, key="1111ee")
            st.write(f"&#8226; Total $bEIGEN Staked: **{restaked_eth_del:,.0f} ETH**")

        st.write("\n")
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

            business_model = st.selectbox("**AVS Business Model Type**", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"], index=1)

        with col48:
            st.write("  \n")

            st.markdown('<p class="header-style" style="font-size: 14px;">AVS Dual Staking Model: Native Dual Staking</p>', unsafe_allow_html=True)

            st.write("  \n")

            avs_token_percentage = st.slider("**% $ROLLUP**", min_value=10, max_value=90, value=10, format='%d%%')

            xeth_percentage = 100 - avs_token_percentage
            
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, format='%d%%')

            st.write("&#8226; **Native Dual Staking Balance**: {}% $ROLLUP : {}% xETH".format(avs_token_percentage, xeth_percentage))

        st.write("\n")

        dual_quorum = st.checkbox("**Dual Quorum**: ETH Quorum & ROLLUP Quorum", value=True, help="ff")

        st.write("-------")

        col44,col45 = st.columns(2, gap="medium")
        with col44:
            business_dual_likelihood = st.slider("*Likelihood* ", min_value=1, max_value=10, value=3, key='afyya', help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            business_dual_likelihood2 = business_dual_likelihood / 2
        with col45:
            business_dual_impact = st.slider("*Impact* ", min_value=1, max_value=10, value=7, key='eywe', help=f"""
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
                    
                    - ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$ROLLUP), tying closely to its market performance and the AVS's ongoing profitability;
                    - ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $ROLLUP stakers, which introduces complexities in security and token value dynamics;
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
                    Particularly in the beginning, too much weight on the $ROLLUP native token increases the likelihood of the tokens of the dual staking model being toxic. And thus negatively impact liveness, an essential condition for a Shared Sequencer.
                            
                    Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $ROLLUP/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                    **\$OMNI** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$ROLLUP* **>** *% xETH* pool balance makes sense to be a higher-reward event.
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

            code_complexity = st.selectbox("**AVS Protocol Architecture & Code Complexity**", ["High", "Medium", "Low"], index=1, key="er7tr")
            
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

            security_audits = st.number_input("**AVS Number of Security Audits**", min_value=0, max_value=5, step=1, value=2, key="0890")


        coverage_perc = st.slider("**GitHub Code Coverage Percentage**", min_value=0, max_value=100, value=56, format='%d%%', help="**Coverage percentage refers to the proportion of code that is tested by automated tests, typically measured by the number of lines or branches of code executed during testing compared to the total number of lines or branches in the codebase. It indicates how thoroughly the codebase is tested, with higher coverage percentages indicating greater test coverage and potentially lower risk of undetected bugs or issues.**")

        coverage_perc_var = coverage_perc_calc(coverage_perc)
        st.session_state.coverage_perc_var = coverage_perc_var


        st.write("------")



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
                            Accounting for the **number of Security Audits** performed onto an AVS and its underlying **Protocol and Code complexities** provides a good insight into its reliability and robustness.
                            
                            While these input is purely qualitative and quantitative, respectively, a strong correlation exists with its underlying smart contract risks and the risk of honest nodes getting potentially slashed. 
                            
                            ```python
                            security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1} # 0 security audits poses the greatest risk, 5 the lowest
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
                operator_reputation = st.selectbox("**Operator Reputation**", ["Unknown", "Established", "Renowned"], index=0, key="678893")

        with col101:            
                operator_centralization = st.selectbox("**Operators' Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], index=0, key="61174")
            

        operator_entrenchment_level = st.selectbox("**Operators' Entrenchment Level** (on other AVSs)", ["High Entrenchment", "Moderate Entrenchment", "Low Entrenchment"], index=0, key="0933111")

        st.write("-------")

        col33, col34 = st.columns(2, gap="medium")
        with col33:
            operator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=8, key="o09", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            operator_likelihood2 = operator_metrics_likelihood/2
        with col34:
            operator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=9, key="o1r", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            operator_impact2 = operator_metrics_impact/2

        operator_likelihood_formatted = format_number(operator_likelihood2)
        operator_impact_formatted = format_number(operator_impact2)


        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
                    Although being purely qualitative metrics, the **Reputation Level of the Operator** and the **Geographical Centralization Level of the Operator**  that the AVS chose to be opted in to validate its modules offers a useful glimpse into the AVS’s security profile. The user should consider the Operator's historical slashing record and the overall validation and uptime performance, which are crucial in assessing overall operator-related risk for an AVS, including potential malicious collusions. [Rated Network](https://www.rated.network/) constitutes a good tool to assess this.                     
                    
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
                background-color: #000080;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">EIGENDA METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")




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
        st.markdown('<p class="header-style">Total $ROLLUP Staked</p>', unsafe_allow_html=True)

                # Dropdown menu
        staked_eigenda = st.number_input("", min_value=0, max_value=10000000000, step=10000000, key="212234")
        st.write(f"&#8226; Total \$ROLLUP Staked: **{staked_eigenda:,.0f} ETH**")

        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")














  


        # ROLLUP Metrics

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
                <span style="font-size: 21px;">ROLLUPS</span>
            </p>
                """, unsafe_allow_html=True)
        
        
        st.write("  \n")

        rollup_fast_proof = st.checkbox('**Fast-Proof Certification**', value=False, help="ee")

        rollup_backup_disperser = st.checkbox('**Backup Disperser**', value=False, help="ee")

        rollup_censorship_res = st.checkbox('**Effective Censorship Resistance through Single Leader/Block Proposer Decentralization**', value=True, help="ee")


        if st.session_state.rollup_backup_disperser != rollup_backup_disperser:
            st.session_state.rollup_backup_disperser = rollup_backup_disperser
            st.session_state.rollup_backup_disperser_score = rollup_backup_disperser_risk.get(rollup_backup_disperser, 0)

        if st.session_state.rollup_fast_proof != rollup_fast_proof:
            st.session_state.rollup_fast_proof = rollup_fast_proof
            st.session_state.rollup_fast_proof_score = rollup_fast_proof_risk.get(rollup_fast_proof, 0)

        result8 = (st.session_state.rollup_fast_proof_score + st.session_state.rollup_backup_disperser_score)
        
        st.write("  \n")

        rollup_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result8):,}</span>
            </div>"""

        st.markdown(rollup_calc1, unsafe_allow_html=True)


########################################################


        st.write("-------")


        rollup_blob_rate = st.slider("**Rollup Blob Dispatching Accuracy Rate**", min_value=0, max_value=100, value=100, format='%d%%')

        rollup_blob_rate_var = rollup_blob_rate_calc(rollup_blob_rate)
        st.session_state.rollup_blob_rate_var = rollup_blob_rate_var



        rollup_bandwidth_rate = st.slider("**Percentage of Rollups Reserving Additional Bandwidth**", min_value=0, max_value=100, value=0, format='%d%%')

        rollup_bandwidth_rate_var = rollup_bandwidth_rate_calc(rollup_bandwidth_rate)
        st.session_state.rollup_bandwidth_rate_var = rollup_bandwidth_rate_var
        


        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            rollup_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=7, key="ruih0", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            rollup_metrics_likelihood2 = rollup_metrics_likelihood / 2

        with col34:
            rollup_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=9, key="r7y91", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            rollup_metrics_impact2 = rollup_metrics_impact / 2

        rollup_likelihood_formatted = format_number(rollup_metrics_likelihood2)
        rollup_impact_formatted = format_number(rollup_metrics_impact2)


        with st.expander("Logic"):
                st.image("images/omni-relayer-diagram.jpg", width=750)

                st.markdown("""                        
The **Relayer** in the Omni network acts as a critical intermediary, handling the transfer of attested cross-network messages (`XMsgs`) between the Omni network and the various destination rollup VMs.Things to consider: 

- **Decision Making for Message Submission**: Post collecting `XBlocks` and `XMsgs`, Relayers determine the number of `XMsg`s to include in their submissions, balancing the costs associated with transaction size, computational requirements, and gas limits.
- **Relayer Performance**: Relayers create and submit transactions with Merkle multi-proofs to destination chains based on attested `XBlock` data, ensuring secure and efficient message delivery.
- **Security and Scalability**: As a permissionless service, Relayers reduce central points of failure and uphold the network's decentralized ethos, while managing security risks and computational intensiveness, especially as the network scales.
                            
The summation or multiplication of variables revolves around their independence or dependence toward one another, pragmatically speaking.
                            """)


        result9 = (st.session_state.rollup_bandwidth_rate_var * st.session_state.rollup_blob_rate_var * rollup_metrics_likelihood2 * rollup_metrics_impact2)
        
        result9_formatted = format_result(float(result9))


        rollup_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_bandwidth_rate_var}</span>
                    <span style="font-size: 22px; font-weight: bold;">&times;</span> 
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_blob_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{rollup_likelihood_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{rollup_impact_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result9_formatted}</span>
            </div>"""

        st.markdown(rollup_calc2, unsafe_allow_html=True)





        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")















        # DISPERSER Metrics

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
                <span style="font-size: 21px;">DISPERSER</span>
            </p>
        """, unsafe_allow_html=True)

        

        st.write("  \n")
        
        col65,col66 = st.columns(2, gap="medium")
        with col65:
            kzg_erasure_coding = st.checkbox("**KZG Erasure Coding Rate**", value=True,
                                help="**ddd**")
        with col66:
            kzg_multi_proofs = st.checkbox("**KZG Multi-Reveal Proofs**", value=True,
                                           help="**ddd**")

        st.write("  \n")

        kzg_encoding_rate = st.slider("**KZG Erasure Encoding Rate**", min_value=0, max_value=100, value=50, format='%d%%', key="6212782")

        kzg_encoding_rate_var = kzg_encoding_rate_calc(kzg_encoding_rate)
        st.session_state.kzg_encoding_rate_var = kzg_encoding_rate_var


        if st.session_state.kzg_erasure_coding != kzg_erasure_coding:
            st.session_state.kzg_erasure_coding = kzg_erasure_coding
            st.session_state.kzg_erasure_coding_score = kzg_erasure_coding_risk.get(kzg_erasure_coding, 0)

        if st.session_state.kzg_multi_proofs != kzg_multi_proofs:
            st.session_state.kzg_multi_proofs = kzg_multi_proofs
            st.session_state.kzg_multi_proofs_score = kzg_multi_proofs_risk.get(kzg_multi_proofs, 0)

        result6 = (st.session_state.kzg_erasure_coding_score + st.session_state.kzg_multi_proofs_score)
        
        st.write("  \n")

        disperser_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_erasure_coding_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_multi_proofs_score}</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result6):,}</span>
            </div>"""

        st.markdown(disperser_calc1, unsafe_allow_html=True)


##################################################


        st.write("-------")

        disperser_performance_acc_rate = st.slider("**Disperser Blob-to-Chunk & Dispatching Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%', key="612782")

        disperser_performance_acc_rate_var = disperser_performance_acc_rate_calc(disperser_performance_acc_rate)
        st.session_state.disperser_performance_acc_rate_var = disperser_performance_acc_rate_var
        
        col20,col21 = st.columns(2)
        with col20:
            disperser_centralization = st.selectbox("**Disperser Centralization Level**", ["Centralized", "Semi-Decentralized", "Decentralized"], index=1, key="28816")
        
        with col21:
            disperser_operator = st.selectbox("**Disperser Operator**", ["Disperser Run by Rollup", "Disperser Run by Third-Party (like EigenLabs)"], index=0, key="285816")


        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            disperser_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="e09u890", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            disperser_likelihood2 = disperser_likelihood / 2

        with col34:
            disperser_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="ejin1", help=f"""
                                                      **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            disperser_impact2 = disperser_impact / 2

        # Directly use the calculated variables
        disperser_likelihood_formatted = format_number(disperser_likelihood2)
        disperser_impact_formatted = format_number(disperser_impact2)

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


        if st.session_state.disperser_centralization != disperser_centralization:
            st.session_state.disperser_centralization = disperser_centralization
            st.session_state.disperser_centralization_score = disperser_centralization_risk.get(disperser_centralization, 0)

        if st.session_state.disperser_operator != disperser_operator:
            st.session_state.disperser_operator = disperser_operator
            st.session_state.disperser_operator_score = disperser_operator_risk.get(disperser_operator, 0)


        result7 = (st.session_state.disperser_performance_acc_rate_var * st.session_state.disperser_centralization_score * 
                   st.session_state.disperser_operator_score * disperser_likelihood2 * disperser_impact2)
        

        result7_formatted = format_result(float(result7))


        disperser_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_operator_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{disperser_likelihood_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{disperser_impact_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result7_formatted}</span>
            </div>"""

        st.markdown(disperser_calc2, unsafe_allow_html=True)








        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")        
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")












        # BFT: Validator Metrics

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
                <span style="font-size: 21px;">CONSENSUS LAYER: BFT</span>
            </p>
                """, unsafe_allow_html=True)


        st.write("  \n")


        bls_alt = st.checkbox('**BLS-Like Alternative** for Operator Signature Batching at Scale', 
                                     value=True, help="**The Ethereum Engine API pairs an existing Ethereum Execution Client with Halo Consensus Client that implements CometBFT consensus.**")


        proof_custody = st.checkbox('**Proof of Custody**', value = True)

        direct_unicast = st.checkbox('**Operator Direct Blob Unicast vs P2P**', value = True)


        col42,col43 = st.columns(2, gap="medium")
        with col42:
            tee_mec = st.checkbox('**TEE** Implementation for Secure Management of Validator Keys', value=False,
                                  help="**TEEs consist of secure portions of hardware that generate and securely store validator keys and databases of previously signed data. By design, they enhance security without comprimising scalability, and through increased trust, encourage stake delegation.**")
        with col43:
            dvt_mec = st.checkbox('**DVT** Implementation to Reduce Risks of Single Points of Failure from a Subset of Validators', value=False,
                                  help="**DVT is a technology that incentivizes client diversity through the distribution of the validation process across multiple operators. It reduces the risk of single points of failure or malicious actions.**")


        if st.session_state.bls_alt != bls_alt:
            st.session_state.bls_alt = bls_alt
            st.session_state.bls_alt_score = bls_alt_risk.get(bls_alt, 0)

        if st.session_state.tee_mec != tee_mec:
            st.session_state.tee_mec = tee_mec
            st.session_state.tee_mec_score = tee_mec_risk.get(tee_mec, 0)

        if st.session_state.dvt_mec != dvt_mec:
            st.session_state.dvt_mec = dvt_mec
            st.session_state.dvt_mec_score = dvt_mec_risk.get(dvt_mec, 0)

        result4 = (st.session_state.bls_alt_score +
                        st.session_state.tee_mec_score + st.session_state.dvt_mec_score)

        st.write("  \n")

        bft_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.bls_alt_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.tee_mec_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dvt_mec_score}</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result4):,}</span>
            </div>"""

        st.markdown(bft_calc1, unsafe_allow_html=True)


############################################


        st.write("-------")

        validator_performance_acc_rate = st.slider("**Validator Performance Accuracy Rate in sending signatures back to Disperser**", min_value=0, max_value=100, value=50, format='%d%%',
                                                   help="**The EigenDA nodes verify the chunks they receive against the KZG commitment using the multireveal proofs, persist the data, then generate and return a signature back to the Disperser for aggregation.**")
        validator_performance_acc_rate_var = validator_performance_acc_rate_calc(validator_performance_acc_rate)
        st.session_state.validator_performance_acc_rate_var = validator_performance_acc_rate_var


        perc_light_nodes = st.slider("**% of Light Client Nodes**", min_value=0, max_value=100, value=50, format='%d%%',
                                                   help="**The Performance Accuracy Rate of Validators attesting for `XBlock`s consists of the timely submission of cross-chain messages, `XBlock` cache management, and the overall decision-making in including `XMsg`s in an `XBlock`.**")
        perc_light_nodes_var = perc_light_nodes_calc(perc_light_nodes)
        st.session_state.perc_light_nodes_var = perc_light_nodes_var


        col100, col101 = st.columns(2, gap="medium")
        with col100:
            validator_reputation = st.selectbox("**CometBFT Validators' Reputation**", ["Unknown", "Established", "Renowned"], key="0977790", index=1,
                                                help="**Attests for a set of validators' trustworthiness in their role of confirming and validating CometBFT blocks and attesting to `XBlock`s before being submitted on-chain.**")
        with col101:           
            validator_centralization = st.selectbox("**CometBFT Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="30'232", index=1,
                                                    help="**Attests for a set of validators' robustness and stability in dealing with local regulations or targeted international attacks.**")
        
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            bft_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=5, key="v660", help=f"""
                                                          **Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.**

                                                          1 == Unlikely | 10 == Very Likely""")
            bft_metrics_likelihood2 = bft_metrics_likelihood / 2

        with col34:
            bft_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="v90901", help=f"""
                                                     **Assesses the impact that risk would have on the security of the AVS.**

                                                      1 == Unimpactful | 10 == Very Impactful""")
            bft_metrics_impact2 = bft_metrics_impact / 2


        bft_likelihood_formatted = format_number(bft_metrics_likelihood2)
        bft_impact_formatted = format_number(bft_metrics_impact2)


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


        if st.session_state.validator_reputation != validator_reputation:
            st.session_state.validator_reputation = validator_reputation
            st.session_state.validator_reputation_score = validator_reputation_risk.get(validator_reputation, 0)

        if st.session_state.validator_centralization != validator_centralization:
            st.session_state.validator_centralization = validator_centralization
            st.session_state.validator_centralization_score = validator_centralization_risk.get(validator_centralization, 0)
    

        result5 = ((st.session_state.validator_performance_acc_rate_var * st.session_state.perc_light_nodes_var * st.session_state.validator_reputation_score *
                   st.session_state.validator_centralization_score) * bft_metrics_likelihood2 * bft_metrics_impact2)
        
        result5_formatted = format_result(float(result5))

        
        bft_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.perc_light_nodes_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_reputation_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{bft_likelihood_formatted}</span>         
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{bft_impact_formatted}</span>         
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result5_formatted}</span>
                </div>
            </div>"""


        st.markdown(bft_calc2, unsafe_allow_html=True)










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
        st.image("images/eigenda-diagram.jpeg", width=1000)
    
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



    risk_score = eigenda_risk(security_audits, business_model, code_complexity,
                            operator_reputation, operator_centralization, operator_entrenchment_level,
                            tee_mec, dvt_mec, validator_reputation, validator_centralization, bls_alt, rollup_fast_proof,
                            disperser_centralization, kzg_erasure_coding, 
                            kzg_multi_proofs, rollup_backup_disperser, disperser_operator)

    (st.session_state.security_audits_score, st.session_state.business_model_score,
    st.session_state.code_complexity_score, 
    st.session_state.operator_reputation_score, st.session_state.operator_centralization_score,
    st.session_state.operator_entrenchment_level_score, st.session_state.tee_mec_score, st.session_state.dvt_mec,
    st.session_state.validator_reputation_score, st.session_state.validator_centralization_score,
    st.session_state.bls_alt_score, st.session_state.rollup_fast_proof_score, st.session_state.disperser_centralization_score,
    st.session_state.kzg_erasure_coding_score, st.session_state.kzg_multi_proofs_score, st.session_state.rollup_backup_disperser_score,
    st.session_state.disperser_operator_score) = risk_score



    col56,col57 = st.columns(2, gap="large")
    with col56:

        col111, col121, col131 = st.columns([3,4,1])

        with col111:
            st.write("")

        with col121:
            st.image("images/omni-matrix.jpg", width=600)

        with col131:
            st.write("")

    with col57:

        col111, col121, col131 = st.columns([1,4,3])

        with col111:
            st.write("")

        with col121:
            st.write("")

            st.markdown("""
                    <style>
                    ul.big-font {
                        font-size: 35px; /* Adjust font size for bullet points */
                    }
                    ul.big-font li {
                        font-size: 20px; /* Adjust font size for bullet points */
                        font-weight: normal; /* Reset font weight for bullet points */
                    }
                    </style>
                    <div class="big-font">
                    Most Pressing Risk Attack Vectors Toward EigenDA:
                    <ul class="big-font">
                        <li><strong>Cross-Message Tampering or Stalling</strong></li>
                        <li><strong>Cross-Chain MEV Extraction Risk</strong></li>
                        <li><strong>Cross-Chain Double-Spend Attack Risk</strong></li>
                        <li><strong>Double-Signing Attack Risk</strong></li>
                        <li><strong>State Liveness Degradation Risk</strong></li>
                        <li><strong>Validator Collusion Risk</strong></li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)

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




    def normalize_score(original_score, min_original=15.25, max_original=100450):
            normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
            return normalized_score

    final_result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9
    normalized_risk_score = normalize_score(final_result)

    st.session_state.risk_score = normalized_risk_score

    st.markdown(f"<div style='text-align: center; font-size: 21px; font-weight: bold;'>Non-Normalized <i>EigenDA</i> Risk Score</div>", unsafe_allow_html=True)
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
            <h2 style="color: black; margin:0; font-size: 1.4em;">Normalized <i>EigenDA</i> Risk Score: <span style="font-size: 1.5em; color: {color};">{st.session_state.risk_score:.0f}</span></h2>
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
                    The <strong>EigenDA Risk Score</strong> is normalized to range from 0 to 100 (for easy reading), where 0 indicates the lowest level of risk and 100 represents the highest possible risk. The Risk Score is calculated based on the risk level of each input parameter as well as their weighting, which is determined by the <strong>Likelihood</strong> and <strong>Impact</strong> of that risk to the protocol as an AVS. 
                    </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.write("**Note**: *It is important to bear in mind that since we are at the very early stages of AVS development and little-to-no information is available, the value judgements above are prone to being faulty.*")



    st.write("**ALGORITHMIC GAME-THEORY**")
    st.write("**HOW TO VISUALIZE GAME-THEORY**")
    st.write("**HOW TO COLOURIZE SLASHING CONDITIOS PER FAULT**")
    st.write("**HOW TO VISUALIZE OPERATOR ENTRENCHMENT**")
    st.write("**SEND OPERATOR NETWORK GRAPH TO GEORGE**")













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

    st.write("  \n")

if __name__ == "__main__":
    main()

