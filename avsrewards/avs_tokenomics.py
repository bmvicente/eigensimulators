
import streamlit as st


### AVS TOKENOMICS

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

st.markdown('<p class="header-style">$AVS Tokenomics [Optional]</p>', unsafe_allow_html=True)

st.write("  \n")

avs_inf_def_rate = st.slider("**$AVS Inflation/Deflation Rate**", 
                            min_value=-50, 
                            max_value=50, 
                            value=0,
                            format="%d%%")

if avs_inf_def_rate > 0:
    st.write(f"&#8226; **$AVS Inflation Rate**: {avs_inf_def_rate}%")

elif avs_inf_def_rate < 0:
    st.write(f"&#8226; **$AVS Deflation Rate**: {(avs_inf_def_rate)}%")

st.write("  \n")

col3, col4 = st.columns([3, 3])

with col3:
    avs_circ_supply = st.number_input("**$AVS Circulating Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, help="Circulating Supply should never exceed Total Supply")

with col4:
    avs_total_supply = st.number_input("**$AVS Total Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000)
        
with st.expander("Logic"):
    st.markdown("""
        **\$AVS Tokenomics** do not influence the reward calculation herein, since they might influence rewards only in an indirect way. 
                    
        Nevertheless, including **\$AVS Inflation/Deflation Rate**, **Circulating** and **Total Token Supplies** can provide an enlightened assessment of what potential future rewards could look like.
        Understanding this rate helps gauge how quickly new tokens are entering circulation, which can impact the token's value and hence the value of rewards. The Circulating vs Total Supply ratio provides a snapshot of how much of the total supply is active in the market, influencing supply-demand dynamics too.

        For \$AVS tokenomics to be considered a valuable metric in this context, one must assume token demand remains constant through time.
                """)