
import streamlit as st


### DUAL STAKING MODEL

def get_avs_token_percentage():
    # Capture AVS token percentage from user input using Streamlit slider
    return st.slider("**% $AVS**", min_value=10, max_value=90, value=50, key="avs_token_percentage")

def get_xeth_percentage():
    # Calculate xETH percentage based on AVS token percentage
    avs_token_percentage = get_avs_token_percentage()
    return 100 - avs_token_percentage

def dual_staking():
    st.markdown("""...""")  # Your existing styling code

    st.markdown('<p class="header-style">AVS Dual Staking Model</p>', unsafe_allow_html=True)
    st.write("  \n")

    # Use columns to layout sliders if needed
    col5, col6 = st.columns(2)

    # Get AVS token percentage using the defined function
    with col5:
        avs_token_percentage = get_avs_token_percentage()

    # Get xETH percentage using the defined function
    with col6:
        xeth_percentage = get_xeth_percentage()
        # Display xETH percentage as a slider (disabled) just for showing the value
        st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, key="xeth_percentage")


        st.write("&#8226; **Dual Staking Balance**: {}% $AVS : {}% xETH".format(avs_token_percentage, xeth_percentage))

        with st.expander("Logic"):
                st.markdown("""
                        Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess risks and potential rewards.

                        \$AVS is the AVS native token. xETH is any ETH-backed LST, such as stETH, rETH or cbETH.

                        Dual staking, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the network's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                        A greater \$xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a % \$AVS > % xETH pool balance makes sense to be a higher-reward event.
                """)

selected_avs_dual_staking = dual_staking()  # This will also render the selection box and explanation