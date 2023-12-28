
import streamlit as st


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

business_model = st.selectbox("", ["Pure Wallet", "Fee Tokenization", "AVS Native Token", "Dual Staking (ETH & $AVS)"])

with st.expander("Logic"):
    st.markdown("""
        EigenLayer offers four different types of business models for AVSs: 
        - Pure Wallet
        - Fee Tokenization
        - AVS Native Token
        - Dual Staking Model (ETH & $AVS).
                """)