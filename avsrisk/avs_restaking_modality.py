
import streamlit as st

# AVS Restaking Modality
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

st.markdown('<p class="header-style">AVS Restaking Modality</p>', unsafe_allow_html=True)

restaking_mods = st.selectbox("", ["LST LP Restaking", "ETH LP Restaking", "LST Restaking", "Native Restaking"])

with st.expander("Logic"):
    st.markdown("""
        EigenLayer offers four different types of restaking modalities for AVSs: LST LP Restaking, ETH LP Restaking, LST Restaking, and Native Restaking. 
            """)