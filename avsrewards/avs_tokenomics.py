
import streamlit as st


### AVS TOKENOMICS

def get_avs_inf_def_rate():
    # Function to capture AVS Inflation/Deflation Rate from user input
    return st.slider("**$AVS Inflation/Deflation Rate**", min_value=-50, max_value=50, value=0, format="%d%%")

def get_avs_circ_supply():
    # Function to capture AVS Circulating Supply from user input
    return st.number_input("**$AVS Circulating Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, help="Circulating Supply cannot exceed Total Supply")

def get_avs_total_supply():
    # Function to capture AVS Total Supply from user input
    return st.number_input("**$AVS Total Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000)

def tokenomics():
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

    # Get values using the defined functions
    avs_inf_def_rate = get_avs_inf_def_rate()

    # Displaying Inflation/Deflation Rate
    if avs_inf_def_rate > 0:
        st.write(f"&#8226; **$AVS Inflation Rate**: {avs_inf_def_rate}%")
    elif avs_inf_def_rate < 0:
        st.write(f"&#8226; **$AVS Deflation Rate**: {(avs_inf_def_rate)}%")
    else:
        st.write("&#8226; **$AVS Inflation/Deflation Rate**: 0%")

    st.write("\n")

    col5, col6 = st.columns([1, 1], gap="small")

    with col5: 
        avs_circ_supply = get_avs_circ_supply()

    with col6:
        avs_total_supply = get_avs_total_supply()


    st.write("  \n")

    with st.expander("Logic"):
        # Your existing logic markdown
        st.markdown(f"""
            **\$AVS Tokenomics** do not influence the reward calculation herein, since they might influence rewards only in an indirect way. 
                        
            Nevertheless, including **\$AVS Inflation/Deflation Rate**, **Circulating** and **Total Token Supplies** can provide an enlightened assessment of what potential future rewards could look like.
            Understanding this rate helps gauge how quickly new tokens are entering circulation, which can impact the token's value and hence the value of rewards. The Circulating vs Total Supply ratio provides a snapshot of how much of the total supply is active in the market, influencing supply-demand dynamics too.

            For \$AVS tokenomics to be considered a valuable metric in this context, one must assume token demand remains constant through time.
                    """)

    return avs_inf_def_rate, avs_circ_supply, avs_total_supply  # Return the values for use elsewhere if needed

# To use the function in your app:
selected_avs_inf_def_rate, selected_avs_circ_supply, selected_avs_total_supply = tokenomics()  # This will also render the input widgets and explanation