
import streamlit as st


def avs_avg_operator_reputation():

        # AVS Average Operator Reputation
        st.markdown("""
                <style>
                .header-style {
                        font-size: 18px;
                        font-weight: bold;
                        margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">AVS Average Operators\' Reputation</p>', unsafe_allow_html=True)

        avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}

        avs_avg_operator_reputation_weight = 1 * 1      # Likelihood 1, Impact 1

        avs_avg_operator_reputation_score = avs_avg_operator_reputation_risk[avs_avg_operator_reputation]

        operator_rep_risk_score = avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight


        with st.expander("Logic"):
                st.markdown("""s
                        Although being a qualitative metric, the Average Operator Reputation opted into the AVS for validating its chosen modules offers a useful glimpse into the AVS’s security profile. The user should consider operators’ historical slashing record and the overall validation and uptime performance, which are crucial for assessing overall operator-related risk, including potential malicious collusions.
                        """)
                
        return operator_rep_risk_score

avs_avg_operator_reputation_result = avs_avg_operator_reputation()