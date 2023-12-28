
import streamlit as st


### DUAL STAKING MODEL

def dual_staking():

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


        st.markdown('<p class="header-style">AVS Dual Staking Model</p>', unsafe_allow_html=True)
                
        st.write("  \n")

        col5, col6 = st.columns(2)

        with col5:
                avs_token_percentage = st.slider("**% $AVS**", min_value=10, max_value=90, value=50)
        with col6:
                xeth_percentage = 100 - avs_token_percentage
                
                st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True)

        st.write("&#8226; **Dual Staking Balance**: {}% $AVS : {}% xETH".format(avs_token_percentage, xeth_percentage))

        with st.expander("Logic"):
                st.markdown("""
                        Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess risks and potential rewards.

                        \$AVS is the AVS native token. xETH is any ETH-backed LST, such as stETH, rETH or cbETH.

                        Dual staking, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the network's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                        A greater \$xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a % \$AVS > % xETH pool balance makes sense to be a higher-reward event.
                """)