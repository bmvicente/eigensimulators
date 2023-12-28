
import streamlit as st

### AVS TVL & TOTAL STAKED

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
            
st.markdown('<p class="header-style">AVS TVL & Total Staked</p>', unsafe_allow_html=True)

st.write("  \n")

col3, col4 = st.columns([3, 3])

with col3:
    avs_tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

with col4:
    avs_total_staked = st.number_input("**\$AVS Total Staked ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

    min_tvl = avs_total_staked // 2

with st.expander("Logic"):
    st.markdown(f"""
            To take the simplest scenario of the single-AVS restaking by operators [(Section 3.4.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/readme/whitepaper) to begin with: an AVS where the amount of restaked ETH is at least double the total locked value (TVL) and a 50% quorum is required for a collusion attack to capture the TVL, the system appears secure, as any successful attack would result in at least half of the attacker's stake being slashed. 

            The **TVL/Total Restaked** logic is structured accordingly to desincentivize colluding operators to perform an attack: the greater the CfC (Cost from Corruption) is compared to the PfC (Profit from Corruption), the more secure the AVS is, and vice-versa.

            Based on the values inputted, the **Minimum TVL** to keep the AVS secure should be **\${min_tvl:,}** and the **Sufficiently-High TVL** value to assure a comfortable security level for the AVS should be at least **\${avs_total_staked:,}**. Current TVL equals **\${avs_tvl:,}**. 
            If the TVL increases compared to the Total Staked, the risk gets reduced and the rewards too, therefore.

            Understanding what the minimum and the sufficiently high TVL numbers should be is not useful for operator-collusion cases only, but also for increasing the [CVS (Cost to Violate Safety) and the CVL (Cost to Violate Liveness)](https://www.blog.eigenlayer.xyz/dual-staking/) — in a Dual Staking Model and Veto Dual Staking context such as ours — which are useful to maintain the health of the AVS dual token pool (or AVS TVL, in other words).

            The **rewards** herein are set so that the greater the *(AVS Total Staked/2) : AVS TVL* ratio, the safer the AVS is and the less rewards it should emit therefore, and vice-versa.
                """)