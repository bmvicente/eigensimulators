
import streamlit as st
from avs_reward_calculation_logic import dual_staking_balance_adjustment


### DUAL STAKING MODEL

def get_avs_token_percentage():
    # Capture AVS token percentage from user input using Streamlit slider
    return st.slider("**% $AVS**", min_value=10, max_value=90, value=50, key="avs_token_percentage")

def get_xeth_percentage(avs_token_percentage):
    # Calculate xETH percentage based on AVS token percentage
    return 100 - avs_token_percentage

def dual_staking():
    st.markdown('<p class="header-style">AVS Dual Staking Model</p>', unsafe_allow_html=True)
    st.write("  \n")

    col7, col8 = st.columns([1,1], gap="small")
    
    with col7: 
        # Capture the AVS token percentage from the user
        avs_token_percentage = get_avs_token_percentage()

    with col8:
        # Calculate the xETH percentage based on the AVS token percentage
        xeth_percentage = get_xeth_percentage(avs_token_percentage)
        
        st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, key="xeth_percentage")


    adjustment = dual_staking_balance_adjustment(avs_token_percentage,xeth_percentage)

    # Display the xETH percentage using a disabled slider for display purposes

    st.write("&#8226; **Dual Staking Balance**: {}% $AVS : {}% xETH".format(avs_token_percentage, xeth_percentage))

    st.write("\n")

    with st.expander("Logic"):
                st.markdown("""
                        Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess risks and potential rewards.

                        \$AVS is the AVS native token. xETH is any ETH-backed LST, such as stETH, rETH or cbETH.

                        Dual staking, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the network's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                        A greater \$xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a % \$AVS > % xETH pool balance makes sense to be a higher-reward event.
                """)
    
    return adjustment

selected_avs_dual_staking_adjustment = dual_staking()  # This will also render the selection box and explanation