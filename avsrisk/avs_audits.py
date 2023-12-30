
import streamlit as st

# Number of Security Audits

def avs_audits():

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

    security_audits = st.number_input("", min_value=0, max_value=5, step=1)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 0}
    security_audits_weight = 4 * 4      # Likelihood 4, Impact 4

    security_audit_score = security_audits_risk[security_audits]
    security_audit_risk_score = security_audit_score * security_audits_weight


    with st.expander("Logic"):
        st.markdown("""
            Registering the number of security audits performed onto an AVS provides a good insight into the reliability and robustness of their code structure. While this input is purely quantitaive in terms of the number of audits performed, quantity strongly correlates to quality, in this case we believe.
        """)
    
    return security_audit_risk_score

selected_avs_audits_risk_score_result = avs_audits()