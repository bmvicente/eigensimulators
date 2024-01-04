
import streamlit as st


# AVS Business Model

def avs_business_model():

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

    st.markdown('<p class="header-style">AVS Business Model</p>', unsafe_allow_html=True)


    selected_avs_business_model = st.selectbox("Select business model:", ["Pure Wallet", "Fee Tokenization", "AVS Native Token", "Dual Staking (ETH & $AVS)"])

    business_model_risk = {"Pure Wallet": 10, "Fee Tokenization": 7, "AVS Native Token": 4, "Dual Staking (ETH & $AVS)": 1}
    business_model_weight = 2 * 3                   # Likelihood 2, Impact 3

    business_model_score = business_model_risk[selected_avs_business_model]
    business_model_risk_score = business_model_score * business_model_weight


    with st.expander("Logic"):
        st.markdown("""
            EigenLayer offers four different types of business models for AVSs: 
            - Pure Wallet
            - Fee Tokenization
            - AVS Native Token
            - Dual Staking Model (ETH & $AVS).
                    """)
    
    return business_model_risk_score

avs_business_model_risk_score_result = avs_business_model()  # This will also render the selection box and explanation