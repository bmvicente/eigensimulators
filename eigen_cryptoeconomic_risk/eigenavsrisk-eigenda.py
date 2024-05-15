

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

    bls_alt_score = bls_alt_risk[bls_alt]
    rollup_fast_proof_score = rollup_fast_proof_risk[rollup_fast_proof]
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

    st.image("images/eigenda.jpeg", width=250)

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


    st.subheader("**INFRASTRUCTURE RISK**")

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




    def format_number(num):
            if num.is_integer():
                return f"{int(num)}"
            else:
                return f"{num:.1f}"
            
    def format_result(num):
            if num.is_integer():
                return f"{int(num):,}"
            else:
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

        dual_quorum = st.checkbox("**Dual Quorum**: ETH Quorum & ROLLUP Quorum", value=True, 
                                  help="**EigenDA has a feature called Dual Quorum, where two separate quorums can be required to attest to the availability of data. As an example, one quorum would be composed of ETH restakers (the ETH quorum), and the second quorum could be composed of stakers of the rollup’s native token. Both quorums are treated as an independent and redundant source of DA, so both quorums have to be compromised before EigenDA can fail.**")
        
        if st.session_state.dual_quorum != dual_quorum:
            st.session_state.dual_quorum = dual_quorum
            st.session_state.dual_quorum_score = dual_quorum_risk.get(dual_quorum, 0)

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

                    **\$ROLLUP** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$ROLLUP* **>** *% xETH* pool balance makes sense to be a higher-reward event.
                        """)
    
        
        result1 = st.session_state.business_model_score * st.session_state.dual_staking_balance * st.session_state.dual_quorum_score * business_dual_likelihood2 * business_dual_impact2
        
        result1_formatted = format_result(float(result1))

        business_dual_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span>
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_quorum_score}</span>                    
                    <span style="font-size: 22px; font-weight: bold;">)</span>
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


        coverage_perc = st.slider("**GitHub Code Coverage %**", min_value=0, max_value=100, value=56, format='%d%%', help="**Coverage percentage refers to the proportion of code that is tested by automated tests, typically measured by the number of lines or branches of code executed during testing compared to the total number of lines or branches in the codebase. It indicates how thoroughly the codebase is tested, with higher coverage percentages indicating greater test coverage and potentially lower risk of undetected bugs or issues.**")

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

        result2 = st.session_state.code_complexity_score * st.session_state.security_audits_score * st.session_state.coverage_perc_var * security_likelihood2 * security_impact2
        
        result2_formatted = format_result(float(result2))

        security_calc = f"""
                    <div style="text-align: center;">
                        <div>
                            <span style="font-size: 22px; font-weight: bold;">(</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.code_complexity_score}</span> 
                            <span style="font-size: 23px; font-weight: bold;">&times;</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.security_audits_score}</span>
                            <span style="font-size: 23px; font-weight: bold;">&times;</span>
                            <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.coverage_perc_var}</span>
                            <span style="font-size: 22px; font-weight: bold;">)</span>
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
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_reputation_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_centralization_score}</span> 
                    <span style="font-size: 23px; font-weight: bold;">&times;</span>
                    <span style="font-size: 21px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_entrenchment_level_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
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

        rollup_censorship_res = st.checkbox('**Censorship Resistance through Decentralization of Single Leader/Block Proposer**', value=True, help="**EigenDA offers higher instantaneous censorship resistance than coupled DA layers. This is because coupled DA architectures usually rely on a single leader or block proposer to linearly order the data blobs, thus creating an instantaneous censorship chokepoint. In contrast, in EigenDA, rollup nodes can directly disperse and receive signatures from a majority of EigenDA nodes, thus improving the censorship resistance to a majority of EigenDA nodes rather than being constricted by a single leader.**")
        # ASK GPT TO SAY THIS IN OTHER WORDS

        if st.session_state.rollup_censorship_res != rollup_censorship_res:
            st.session_state.rollup_censorship_res = rollup_censorship_res
            st.session_state.rollup_censorship_res_score = rollup_censorship_res_risk.get(rollup_censorship_res, 0)

        result4 = st.session_state.rollup_censorship_res_score

        st.write("  \n")

        rollup_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{result4}</span>
            </div>"""

        st.markdown(rollup_calc1, unsafe_allow_html=True)


########################################################


        st.write("-------")


        rollup_blob_rate = st.slider("**Rollup Sequencers Blob Dispatching Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                     help="****")

        rollup_blob_rate_var = rollup_blob_rate_calc(rollup_blob_rate)
        st.session_state.rollup_blob_rate_var = rollup_blob_rate_var


        col90, col91 = st.columns(2)
        with col90:
            rollup_bandwidth_rate = st.slider("**% of Rollups Reserving Additional Bandwidth**", min_value=0, max_value=100, value=0, format='%d%%',
                                              help="****")

            rollup_bandwidth_rate_var = rollup_bandwidth_rate_calc(rollup_bandwidth_rate)
            st.session_state.rollup_bandwidth_rate_var = rollup_bandwidth_rate_var

        with col91:
            rollup_backup_disperser = st.slider("**% of Rollups With Backup Disperser**", min_value=0, max_value=100, value=0, format='%d%%',
                                                help="*****")

            rollup_backup_disperser_var = rollup_backup_disperser_calc(rollup_backup_disperser)
            st.session_state.rollup_backup_disperser_var = rollup_backup_disperser_var



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
                st.write("  \n")

                st.markdown("""                        
                            """)


        result5 = ((st.session_state.rollup_bandwidth_rate_var + st.session_state.rollup_blob_rate_var + st.session_state.rollup_backup_disperser_var) * rollup_metrics_likelihood2 * rollup_metrics_impact2)
        
        result5_formatted = format_result(float(result5))


        rollup_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_blob_rate_var}</span>
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span> 
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_bandwidth_rate_var}</span>
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span> 
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_backup_disperser_var}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{rollup_likelihood_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #E0E0E0; border-radius: 10px; padding: 5px; margin: 2px;">{rollup_impact_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result5_formatted}</span>
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
            kzg_erasure_coding = st.checkbox("**KZG Erasure Coding**", value=True,
                                help="**Efficiently manages data by breaking it into smaller chunks using erasure coding, combined with KZG polynomial commitments. This allows nodes to download only necessary data segments, enhancing storage efficiency and data integrity through validity proofs.**")
        with col66:
            kzg_poly_comm = st.checkbox("**KZG Polynomial Commitment**", value=True,
                                help="**A cryptographic technique for securely committing to data without disclosure. Essential for the integrity and verification of data in distributed systems, serving as the foundation for both KZG Erasure Coding and Multi-Reveal Proofs.**")
            
        kzg_multi_proofs = st.checkbox("**KZG Multi-Reveal Proofs**", value=True,
                                           help="**Enables verification of multiple data segments simultaneously, ensuring data integrity across the network using KZG polynomial commitments. Key for confirming data correctness and security in distributed environments.**")
        # ASK GPT TO SAY THIS IN OTHER WORDS

        st.write("  \n")

        kzg_encoding_rate = st.slider("**KZG Erasure Encoding Rate**", min_value=0, max_value=100, value=50, format='%d%%', 
                                      key="6212782", help="**Usually set between 10% and 50%, depending on the desired level of data redundancy and the storage capacity available across the node network. A higher rate increases redundancy, enhancing data protection and making it more challenging and costly for an attacker to compromise the data integrity, thus reducing their potential profit.**")

        kzg_encoding_rate_var = kzg_encoding_rate_calc(kzg_encoding_rate)
        st.session_state.kzg_encoding_rate_var = kzg_encoding_rate_var


        if st.session_state.kzg_erasure_coding != kzg_erasure_coding:
            st.session_state.kzg_erasure_coding = kzg_erasure_coding
            st.session_state.kzg_erasure_coding_score = kzg_erasure_coding_risk.get(kzg_erasure_coding, 0)

        if st.session_state.kzg_multi_proofs != kzg_multi_proofs:
            st.session_state.kzg_multi_proofs = kzg_multi_proofs
            st.session_state.kzg_multi_proofs_score = kzg_multi_proofs_risk.get(kzg_multi_proofs, 0)

        if st.session_state.kzg_poly_comm != kzg_poly_comm:
            st.session_state.kzg_poly_comm = kzg_poly_comm
            st.session_state.kzg_poly_comm_score = kzg_poly_comm_risk.get(kzg_poly_comm, 0)

        result6 = (st.session_state.kzg_erasure_coding_score * st.session_state.kzg_multi_proofs_score * st.session_state.kzg_poly_comm_score * st.session_state.kzg_encoding_rate_var)
        
        st.write("  \n")

        disperser_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_erasure_coding_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_poly_comm_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_multi_proofs_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.kzg_encoding_rate_var}</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result6):,}</span>
            </div>"""

        st.markdown(disperser_calc1, unsafe_allow_html=True)


##################################################


        st.write("-------")

        disperser_performance_acc_rate = st.slider("**Disperser Blob-to-Chunk, Dispatching & Signature Posting On-Chain Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%', key="612782",
                                                   help="**The EigenDA disperser sidecar erasure encodes the blob into chunks, generates a KZG commitment and multi-reveal proofs for each chunk, and disperses chunks to EigenDA Operators, receiving signatures certifying storage in return. After aggregating the received signatures, the disperser registers the blob onchain by sending a transaction to the EigenDA Manager contract with the aggregated signature and blob metadata.**")

        disperser_performance_acc_rate_var = disperser_performance_acc_rate_calc(disperser_performance_acc_rate)
        st.session_state.disperser_performance_acc_rate_var = disperser_performance_acc_rate_var
        
        
        fhe_disperser = st.selectbox("**Homomorphic Encryption of Data**", ["None", "Partial", "Full"], index=0, key="2328816",
                                                    help="**FHE allows performing operations upon data without ever needing to access the original, unencrypted data, enhancing security and privacy. Although still being an inefficient and highly theoretical concept, it is promising in a DA context. The values assigned to it in this Simulation reflect this uncertainty.**")
        
        col20,col21 = st.columns(2)
        with col20:
            disperser_operator = st.selectbox("**Disperser Operator**", ["Disperser Run by Rollup", "Disperser Run by Third-Party (like EigenLabs)"], index=1, key="285816",
                                              help="**Rollups will be able to run their own disperser, or use a dispersal service that a third party (for example, EigenLabs) operates for convenience and amortization of signature verification costs.**")
        
        with col21:
            disperser_centralization = st.selectbox("**Disperser Centralization Level**", ["Centralized", "Semi-Decentralized", "Decentralized"], index=0, key="28816",
                                                    help="**Depending whether it's used as a centralized service or permissionless, decentralized node network.**")
        # ASK GPT TO SAY THIS IN OTHER WORDS

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

                            """)


        if st.session_state.disperser_centralization != disperser_centralization:
            st.session_state.disperser_centralization = disperser_centralization
            st.session_state.disperser_centralization_score = disperser_centralization_risk.get(disperser_centralization, 0)

        if st.session_state.disperser_operator != disperser_operator:
            st.session_state.disperser_operator = disperser_operator
            st.session_state.disperser_operator_score = disperser_operator_risk.get(disperser_operator, 0)

        if st.session_state.fhe_disperser != fhe_disperser:
            st.session_state.fhe_disperser = fhe_disperser
            st.session_state.fhe_disperser_score = fhe_disperser_risk.get(fhe_disperser, 0)

            
        result7 = ((st.session_state.disperser_performance_acc_rate_var * st.session_state.disperser_centralization_score * st.session_state.disperser_operator_score *
                   st.session_state.fhe_disperser_score) * disperser_likelihood2 * disperser_impact2)
    
        result7_formatted = format_result(float(result7))


        disperser_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.fhe_disperser_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_operator_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.disperser_centralization_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">)</span>
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

        col92, col93 = st.columns(2)
        with col92:
            bls_alt = st.checkbox('**BLS-Like Alternative** for Cost-Effective Operator Signature Dispatching to the Disperser', 
                                     value=True, help="**BLS aggregate signatures are expensive and therefore poses a limitation on the operator set.**")

        with col93:
            proof_custody = st.checkbox('**Proof of Custody**', value = True,
                                        help="**A key mode of operator failure in EigenDA is that nodes sign off on data items without actually storing them for the required period of time. To solve this problem EigenDA uses a mechanism called proof-of-custody, which was originally proposed by Justin Drake and Dankrad Feist of the Ethereum Foundation. With proof-of-custody each operator must routinely compute and commit to the value of a function which can only be computed if they have stored all the blob chunks allocated to them over a designated storage period. If they attest to blobs without computing this function, the ETH held by the node can be slashed by anyone who has access to their data item.**")

        col96,col97 = st.columns(2)
        with col96:
            rollup_fast_proof = st.checkbox('**Fast-Proof Certification**', value=False, 
                                            help="**Methodology to enable EigenDA nodes to verify and underwrite proofs at very low latency.**")
        with col97:
            direct_unicast = st.checkbox('**Operator Direct Blob Unicast vs P2P**', value = True,
                                     help="**Existing DA solutions use a peer-to-peer (P2P) network for transmitting blobs, in which operators receive blobs from their peers, then re-broadcast the same blob to others. This significantly constrains the achievable DA rate. In EigenDA, a Disperser sends blobs directly to EigenDA’s operators. By relying on unicast (direct communication) for dispersing data, EigenDA can confirm DA at native network latency rather than via an expensive gossip protocol. This eliminates the significant gossiping penalties that come with P2P, and results in faster data commitment times.**")

        col94, col95 = st.columns(2)
        with col94:
            dvt_mec = st.checkbox('**DVT** Implementation to Reduce Risks of Single Points of Failure from a Subset of Validators', value=False,
                                  help="**DVT is a technology that incentivizes client diversity through the distribution of the validation process across multiple operators. It reduces the risk of single points of failure or malicious actions.**")

        with col95:
            tee_mec = st.checkbox('**TEE** Implementation for Secure Management of Validator Keys', value=False,
                                  help="**TEEs consist of secure portions of hardware that generate and securely store validator keys and databases of previously signed data. By design, they enhance security without comprimising scalability, and through increased trust, encourage stake delegation.**")
        # ASK GPT TO SAY THIS IN OTHER WORDS


        if st.session_state.bls_alt != bls_alt:
            st.session_state.bls_alt = bls_alt
            st.session_state.bls_alt_score = bls_alt_risk.get(bls_alt, 0)

        if st.session_state.proof_custody != proof_custody:
            st.session_state.proof_custody = proof_custody
            st.session_state.proof_custody_score = proof_custody_risk.get(proof_custody, 0)

        if st.session_state.rollup_fast_proof != rollup_fast_proof:
            st.session_state.rollup_fast_proof = rollup_fast_proof
            st.session_state.rollup_fast_proof_score = rollup_fast_proof_risk.get(rollup_fast_proof, 0)

        if st.session_state.direct_unicast != direct_unicast:
            st.session_state.direct_unicast = direct_unicast
            st.session_state.direct_unicast_score = direct_unicast_risk.get(direct_unicast, 0)

        if st.session_state.tee_mec != tee_mec:
            st.session_state.tee_mec = tee_mec
            st.session_state.tee_mec_score = tee_mec_risk.get(tee_mec, 0)

        if st.session_state.dvt_mec != dvt_mec:
            st.session_state.dvt_mec = dvt_mec
            st.session_state.dvt_mec_score = dvt_mec_risk.get(dvt_mec, 0)



        result8 = (st.session_state.bls_alt_score + st.session_state.proof_custody_score + st.session_state.rollup_fast_proof_score +
                        st.session_state.direct_unicast_score + st.session_state.tee_mec_score + st.session_state.dvt_mec_score)

        st.write("  \n")

        bft_calc1 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.bls_alt_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.proof_custody_score}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.rollup_fast_proof_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.direct_unicast_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dvt_mec_score}</span>
                    <span style="font-size: 22px; font-weight: bold;">&plus;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #FF9999; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.tee_mec_score}</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{int(result8):,}</span>
            </div>"""

        st.markdown(bft_calc1, unsafe_allow_html=True)


############################################


        st.write("-------")

        validator_performance_acc_rate = st.slider("**Validators' Data Storage & Signatures Dispatching Back to Disperser Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%',
                                                   help="**The EigenDA nodes verify the chunks they receive against the KZG commitment using the multireveal proofs, persist the data, then generate and return a signature back to the Disperser for aggregation.**")
        validator_performance_acc_rate_var = validator_performance_acc_rate_calc(validator_performance_acc_rate)
        st.session_state.validator_performance_acc_rate_var = validator_performance_acc_rate_var


        perc_light_nodes = st.slider("**% of Light Nodes**", min_value=0, max_value=100, value=20, format='%d%%',
                                                   help="**The Performance Accuracy Rate of Validators attesting for `XBlock`s consists of the timely submission of cross-chain messages, `XBlock` cache management, and the overall decision-making in including `XMsg`s in an `XBlock`.**")
        perc_light_nodes_var = perc_light_nodes_calc(perc_light_nodes)
        st.session_state.perc_light_nodes_var = perc_light_nodes_var

        fhe_operator = st.selectbox("**Homomorphic Encryption of Data**", ["None", "Partial", "Full"], index=0, key="265816",
                                                    help="**FHE allows performing operations upon data without ever needing to access the original, unencrypted data, enhancing security and privacy. Although still being an inefficient and highly theoretical concept, it is promising in a DA context. The values assigned to it in this Simulation reflect this uncertainty.**")
        
        col100, col101 = st.columns(2, gap="medium")
        with col100:
            validator_reputation = st.selectbox("**BFT Validators' Reputation**", ["Unknown", "Established", "Renowned"], key="0977790", index=1,
                                                help="**Attests for a set of validators' trustworthiness in their role of confirming and validating BFT blocks and attesting to `XBlock`s before being submitted on-chain.**")
        with col101:           
            validator_centralization = st.selectbox("**BFT Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"], key="30'232", index=1,
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
                st.markdown("""
Instead of requiring each node to download and store all data, EigenDA uses erasure coding to split data into smaller chunks, and requires operators to download and store only a single chunk, which is a fraction of the full data blob size. This imposes a lower cost on each operator as compared to storing the full blob, making EigenDA “lightweight” to operate by many nodes. As more nodes join the EigenDA network, the resource costs incurred by every node on the network decreases. This enables EigenDA to be secured by a large set of operators at low and marginally decreasing cost, enabling a philosophy of abundance rather than scarcity.
                            """)
        # ASK GPT TO SAY THIS IN OTHER WORDS, ALL ABOVES


        if st.session_state.validator_reputation != validator_reputation:
            st.session_state.validator_reputation = validator_reputation
            st.session_state.validator_reputation_score = validator_reputation_risk.get(validator_reputation, 0)

        if st.session_state.validator_centralization != validator_centralization:
            st.session_state.validator_centralization = validator_centralization
            st.session_state.validator_centralization_score = validator_centralization_risk.get(validator_centralization, 0)

        if st.session_state.fhe_operator != fhe_operator:
            st.session_state.fhe_operator = fhe_operator
            st.session_state.fhe_operator_score = fhe_operator_risk.get(fhe_operator, 0)


        result9 = ((st.session_state.validator_performance_acc_rate_var * st.session_state.perc_light_nodes_var * st.session_state.fhe_operator_score * st.session_state.validator_reputation_score *
                   st.session_state.validator_centralization_score) * bft_metrics_likelihood2 * bft_metrics_impact2)
        
        result9_formatted = format_result(float(result9))

        
        bft_calc2 = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_performance_acc_rate_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.perc_light_nodes_var}</span> 
                    <span style="font-size: 22px; font-weight: bold;">&times;</span>
                    <span style="font-size: 20px; font-weight: bold; background-color: #87CEEB; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.fhe_operator_score}</span> 
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
                    <span style="font-size: 20px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result9_formatted}</span>
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

    col1, col2, col3 = st.columns([3, 12, 1])

    # Placing the image in the middle column effectively centers it
    with col2:
        st.image("images/eigenda-diagram.jpeg", width=1100)
        st.write("  \n")


    st.markdown("""
        <div style="text-align: center">
            Image from <a href="https://docs.eigenlayer.xyz/eigenda/overview" target="_blank">EigenDA Docs</a>
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
                            kzg_multi_proofs, disperser_operator,
                            proof_custody, direct_unicast, kzg_poly_comm, rollup_censorship_res, fhe_disperser, fhe_operator, dual_quorum)

    (st.session_state.security_audits_score, st.session_state.business_model_score,
    st.session_state.code_complexity_score, 
    st.session_state.operator_reputation_score, st.session_state.operator_centralization_score,
    st.session_state.operator_entrenchment_level_score, st.session_state.tee_mec_score, st.session_state.dvt_mec,
    st.session_state.validator_reputation_score, st.session_state.validator_centralization_score,
    st.session_state.bls_alt_score, st.session_state.rollup_fast_proof_score, st.session_state.disperser_centralization_score,
    st.session_state.kzg_erasure_coding_score, st.session_state.kzg_multi_proofs_score,
    st.session_state.disperser_operator_score, st.session_state.proof_custody_score, st.session_state.direct_unicast_score, 
    st.session_state.kzg_poly_comm_score, st.session_state.rollup_censorship_res_score,
    st.session_state.fhe_disperser_score, st.session_state.fhe_operator_score, st.session_state.dual_quorum) = risk_score






    def normalize_score(original_score, min_original=16, max_original=12499539195000000):
            normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
            return normalized_score

    xeth_percentage_dec = xeth_percentage * 0.01
    avs_token_percentage_dec = avs_token_percentage * 0.01

    final_result = (xeth_percentage_dec * (1/3*(result1) * 1/3*(result2) * 1/3*(result3))) + (avs_token_percentage_dec * (0.2*(result4 * result5) * 0.4*(result6 * result7) * 0.4*(result8 * result9)))
    normalized_risk_score = normalize_score(final_result)

    st.session_state.risk_score = normalized_risk_score

# 12499539195000000
# 126796743360

# ASK GPT: HOW TO REPRESENT RISK SCORE WHEN DOING SUCH MULTIPLICATIONS, INSTEAD OF SUM? THE SCORE COMES OUT MESSED UP
# I KNOW RISK SCORE NORMALIZATION IS NORMALLY DONE BY ADDITION? BUT THAT'S IN THE CASE OF INDEPENDENT VARIABLES, CORRECT? WHAT IF I HAVE DEPENDENT VARIABLES, THAT WOULD THEREFORE NEED MULTIPLICATION TO MAKE SENSE?
# ALSO DO THE GLOBAL WEIGHTING FOR DUAL STAKING IN ANOTHER WAY? BUT IT DOES MAKE SENSE NOW

#585913703765625012224
#3962173320000

   # with st.expander("Logic"):
    #
     #           st.markdown("""
      #      Operational cost. Instead of requiring each node to download and store all data, EigenDA uses erasure coding to split data into smaller chunks, and requires operators to download and store only a single chunk, which is a fraction of the full data blob size. This imposes a lower cost on each operator as compared to storing the full blob, making EigenDA “lightweight” to operate by many nodes. As more nodes join the EigenDA network, the resource costs incurred by every node on the network decreases. This enables EigenDA to be secured by a large set of operators at low and marginally decreasing cost, enabling a philosophy of abundance rather than scarcity.
       #                     """)


    st.markdown(f"<div style='text-align: center; font-size: 21px; font-weight: bold;'>Non-Normalized <i>EigenDA</i> Risk Score</div>", unsafe_allow_html=True)
    final_result_html = f"""
                <div style="text-align: center;">
                    <span style="font-size: 27px; font-weight: bold;">(</span>
                    <span style="font-size: 25px; font-weight: bold; background-color: yellow; padding: 5px; margin: 2px;">{xeth_percentage_dec}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result1_formatted}</span> 
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result2_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result3_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 27px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> + </span>
                    <span style="font-size: 27px; font-weight: bold;">(</span>
                    <span style="font-size: 25px; font-weight: bold; background-color: yellow; padding: 5px; margin: 2px;">{avs_token_percentage_dec}</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result4):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result5_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result6):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result7_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold;">(</span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{int(result8):,}</span>
                    <span style="font-size: 22px; font-weight: bold;"> x </span>
                    <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result9_formatted}</span>
                    <span style="font-size: 22px; font-weight: bold;">)</span>
                    <span style="font-size: 27px; font-weight: bold;">)</span>
                    <span style="font-size: 22px; font-weight: bold;"> = </span>
                    <span style="font-size: 25px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{final_result:,.2f}</span>
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






    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")




    st.subheader("**POTENTIAL RISK VECTORS**")



    st.write("")
    st.write("")



    col56,col57 = st.columns(2, gap="large")
    with col56:

        col111, col121, col131 = st.columns([3,4,1])

        with col111:
            st.write("")

        with col121:
            st.image("images/eigenda-matrix.jpg", width=600)
            st.write("")

        with col131:
            st.write("")

    with col57:

        col111, col121, col131, col132 = st.columns([1,5,3,3])

        with col111:
            st.write("")

        with col121:
            st.write("")

            st.markdown(f"<div style='font-size: 21px; font-weight: bold;'>Risk Attack Vectors Toward EigenDA</div>", unsafe_allow_html=True)
            st.write("")


            # Define HTML content with embedded CSS for styling for the first group
            bullet_points_html = """
            <style>
            .big-font-yellow {
                font-size: 35px; /* Adjust font size for headings */
                color: black; /* Ensure text is clearly visible */
            }
            .big-font-yellow li {
                font-size: 20px; /* Adjust font size for bullet points */
                background-color: yellow; /* Apply yellow background to bullet points */
                padding: 5px 10px; /* Padding around text within bullet points */
                margin: 5px 0; /* Space between bullet points */
                border-radius: 5px; /* Optional: rounded corners for each bullet point */
                display: inline-block; /* Ensure the background covers only the text width */
            }
            </style>
            <div class="big-font-yellow">
                <span style="font-size: 0.5em;">Objectively-Attributable Faults:</span>
            </div>
            <ul class="big-font-yellow" style="font-size: 0.7em;">
                <li><strong>Data Attestation Corruption Risk</strong></li>
                <li><strong>Data Attestation Double-Signing Risk</strong></li>
            </ul>
            </div>
            """
            st.markdown(bullet_points_html, unsafe_allow_html=True)

            # Second group
            bullet_points_html1 = """
            <style>
            .big-font-orange {
                font-size: 35px;
            }
            .big-font-orange li {
                font-size: 20px;
                background-color: orange;
                padding: 5px 10px;
                margin: 5px 0;
                border-radius: 5px;
                display: inline-block;
            }
            </style>
            <div class="big-font-orange">
                <span style="font-size: 0.5em;">Intersubjectively-Attributable Faults:</span>
            </div>
            <ul class="big-font-orange" style="font-size: 0.7em;">
                <li><strong>Data Relaying Censorship Risk</strong></li>
                <li><strong>Data Relaying Stalling Risk</strong></li>
            </ul>
            </div>
            """
            st.markdown(bullet_points_html1, unsafe_allow_html=True)

            # Third group
            bullet_points_html2 = """
            <style>
            .big-font-red {
                font-size: 35px;
            }
            .big-font-red li {
                font-size: 20px;
                background-color: red;
                padding: 5px 10px;
                margin: 5px 0;
                border-radius: 5px;
                display: inline-block;
            }
            </style>
            <div class="big-font-red">
                <span style="font-size: 0.5em;">Non-Attributable Faults:</span>
            </div>
            <ul class="big-font-red" style="font-size: 0.7em;">
                <li><strong>Validator Collusion Risk</strong></li>
            </ul>
            </div>
            """
            st.markdown(bullet_points_html2, unsafe_allow_html=True)



        with col131:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            #curly brackets

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            #curly brackets



        with col132:
            st.write("**Liveness Violation**")

            st.write("**Safety Violation**")



    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")


    col111, col121, col131 = st.columns([8,2,10])

    with col111:
            st.image("images/heatmap1.jpg", width=800)

    with col121:
            st.image("images/centscale.jpg", width=150)

    with col131:
            st.image("images/heatmap2.jpg", width=800)



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
        st.write("")

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

