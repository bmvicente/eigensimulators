
import streamlit as st


# AVS Restaking Modality

def avs_restaking_modality():

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


    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    restaking_mods_weight = 2 * 3         # Likelihood 2, Impact 3

    selected_restaking_mod = st.selectbox("", ["LST LP Restaking", "ETH LP Restaking", "LST Restaking", "Native Restaking"])

    restaking_mod_score = restaking_mods_risk[selected_restaking_mod]
    restaking_mod_risk_score = restaking_mod_score * restaking_mods_weight


    with st.expander("Logic"):
        st.markdown("""
            EigenLayer offers four different types of restaking modalities for AVSs: LST LP Restaking, ETH LP Restaking, LST Restaking, and Native Restaking. 
                """)
        
    return restaking_mod_risk_score

avs_restaking_modality_risk_score_result = avs_restaking_modality()  # This will also render the selection box and explanation