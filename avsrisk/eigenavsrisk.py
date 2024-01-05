
# EigenLayer AVS Risks


import streamlit as st

# Function to calculate AVS risk
def avs_risk(security_audits, business_model, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation):
    # Define the risk scores for each metric (0-10 scale, 10 being riskiest)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 0}
    business_model_risk = {"Pure Wallet": 10, "Fee Tokenization": 7, "AVS Native Token": 4, "Dual Staking (ETH & $AVS)": 1}
    avs_type_risk = {"Lightweight": 10, "Hyperscale": 1}
    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}

    security_audits_weight = 4 * 4                  # Likelihood 4, Impact 4
    business_model_weight = 2 * 3                   # Likelihood 2, Impact 3
    avs_type_weight = 1 * 2                         # Likelihood 2, Impact 2
    restaking_mods_weight = 2 * 3                   # Likelihood 2, Impact 3
    operator_attack_weight = 3 * 5                  # Likelihood 3, Impact 5
    avs_avg_operator_reputation_weight = 1 * 1      # Likelihood 1, Impact 1
    #CVS and CVL based and 51% operator attack dependant

    # Get risk scores from the input values
    security_audit_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    avs_type_score = avs_type_risk[avs_type]
    restaking_mod_score = restaking_mods_risk[restaking_mods]
    avs_avg_operator_reputation_score = avs_avg_operator_reputation_risk[avs_avg_operator_reputation]

    # Now use operator_attack_risk in your total risk score calculation
    total_risk_score = (security_audit_score * security_audits_weight +
                        business_model_score * business_model_weight +
                        avs_type_score * avs_type_weight +
                        operator_attack_risk * operator_attack_weight +  # Use the calculated risk score directly
                        restaking_mod_score * restaking_mods_weight +
                        avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight
                        )

    max_security_audit_score = 10  # Assuming worst case for security audit is 0 audits
    max_business_model_score = 10   # Assuming worst case for business model is "Pure Wallet"
    max_avs_type_score = 10         # Assuming worst case for AVS type is "Hyperscale"
    max_restaking_mod_score = 10    # Assuming worst case for restaking modality is "LST LP Restaking"
    max_operator_attack_score = 10  # Assuming worst case for operator attack risk
    max_avs_avg_operator_reputation_score = 10  # Assuming worst case for operator attack risk

    # Calculate the maximum possible risk score
    max_possible_risk_score = (
        max_security_audit_score * security_audits_weight +
        max_business_model_score * business_model_weight +
        max_avs_type_score * avs_type_weight +
        max_operator_attack_score * operator_attack_weight +
        max_restaking_mod_score * restaking_mods_weight +
        max_avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight)

    # Normalize the risk score
    normalized_risk_score = (total_risk_score / max_possible_risk_score) * 10
    normalized_risk_score = round(normalized_risk_score, 2)

    return normalized_risk_score




# Streamlit app setup
def main():
    st.set_page_config(layout="wide")

    st.image("images/eigenimage.png")

    st.title("AVS Risk Simulator")
    
    st.write("  \n")

    # Creating two major columns
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        # AVS TVL & Total Restaked
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

            # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS TVL & Total Restaked</p>', unsafe_allow_html=True)

        st.write("  \n")

            # Creating two columns for input
        col3, col4 = st.columns([3, 3])

        with col3:
                # Manual input for AVS TVL
                tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

        with col4:
                # Manual input for Total Restaked on AVS
                total_restaked = st.number_input("**AVS Total Restaked ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

        # Convert input strings to float for calculation
        tvl = float(tvl) if tvl else 0
        total_restaked = float(total_restaked) if total_restaked else 0

            # The expander without a visible outline
        with st.expander("Logic"):
                st.markdown("""
                    To take the simplest scenario of the single-AVS restaking by operators [(Section 3.4.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) to begin with: an AVS appears to be most secure when the amount of restaked ETH is at least double the total locked value (TVL) and a 50% quorum is required for a collusion attack to capture the TVL, as any successful attack would result in at least half of the attacker's stake being slashed. If the Total Restaked increases from there compared to the TVL, the risk gets reduced even further.

                    The **TVL/Total Restaked** logic is structured accordingly to desincentivize colluding operators to perform an attack: the greater the CfC (Cost from Corruption) is compared to the PfC (Profit from Corruption), the more secure the AVS is, and vice-versa. 

                    The **risk logic** herein is set so that the greater the *(AVS Total Restaked/2) : AVS TVL* ratio, the safer the AVS is, and vice-versa. If *AVS Total Restaked* and *AVS TVL* are both under $100K, we consider it the maximum risk scenario.

                    Understanding what a reduced risk level should be is not useful for operator-collusion cases only, but also for increasing the [CVS (Cost to Violate Safety) and the CVL (Cost to Violate Liveness)](https://www.blog.eigenlayer.xyz/dual-staking/), i.e. in a Dual Staking Model and Veto Dual Staking context, for example, which are useful to maintain the health of the AVS dual token pool (or AVS TVL, in other words).               
                            """)

        ###################        
        st.write("  \n")
        st.write("  \n")


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

        # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS Business Model</p>', unsafe_allow_html=True)

        # Dropdown menu
        business_model = st.selectbox("", ["Pure Wallet", "Fee Tokenization", "AVS Native Token", "Dual Staking (ETH & $AVS)"])

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                Ordering the **Business Models** from EigenLayer [(Section 4.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) by risk: ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$AVS), tying closely to its market performance and the AVS's ongoing profitability. Then there’s ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $AVS stakers, which introduces complexities in security and token value dynamics. The ***Tokenize the Fee*** model comes with moderate risk involving payments in a neutral denomination (like ETH) and distributing a portion of fees to holders of the AVS's token, thus partly dependent on the AVS token's value. Finally, ***Pure Wallet*** represents the lowest risk, relying on straightforward service fees paid in a neutral denomination, like ETH.

                Thus, the risk of each model is influenced by its reliance on the AVS's native token and the complexities of its fee and security structures.
            """)
        
        ###################
        st.write("  \n")
        st.write("  \n")


        # Number of Security Audits
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

        # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS Number of Security Audits</p>', unsafe_allow_html=True)

        # Dropdown menu
        security_audits = st.number_input("", min_value=0, max_value=5, step=1)

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                Accounting for the **number of Security Audits** performed onto an AVS provides a good insight into the reliability and robustness of their code structure. While this input is purely quantitaive in terms of the number of audits performed, audit quantity strongly correlates to code quality, in this particular case.
            """)

    with col2:
        # AVS Type
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

        # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS Type</p>', unsafe_allow_html=True)

        st.write("  \n")

        # Dropdown menu
        avs_type = st.selectbox("", ["Lightweight", "Hyperscale"])

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                In designing modules for maximal security and minimal centralization risk, EigenLayer suggests two approaches: **Hyperscale and Lightweight AVS** [(Section 3.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper).

                **Hyperscale AVS** involves distributing the computational workload across many nodes, allowing for high overall throughput and reducing incentives for centralized validation. This horizontal scaling minimizes validation costs and amortization gains for any central operator. 

                On the other hand, the **Lightweight** approach focuses on tasks that are redundantly performed by all operators but are inexpensive and require minimal computing infrastructure.

                While it does depend on the needs of an AVS, the Hyperscale-type is more robust and secure due to its decentralized nature, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our simulator.                    
                        """)

        ###################
        st.write("  \n")
        st.write("  \n")


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

        # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS Restaking Modality</p>', unsafe_allow_html=True)

        # Dropdown menu
        restaking_mods = st.selectbox("", ["LST LP Restaking", "ETH LP Restaking", "LST Restaking", "Native Restaking"])

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                EigenLayer introduces a few **Restaking Modalities** for yield stacking on its platform, enhancing the ability for stakers to earn additional yield by securing new AVSs [(Section 2.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper). 

                By order of increasing risk: ***Native Restaking***, where validators restake staked ETH directly to EigenLayer; ***LST Restaking***, involving staking of ETH already restaked via protocols like Lido or Rocket Pool; ***ETH LP Restaking***, where validators stake LP tokens of pairs including ETH; and ***LST LP Restaking***, involving staking LP tokens of pairs with liquid staking ETH tokens. 
                        
                These pathways integrate with different blockchain layers, such as the core protocol, AVS, and DeFi, offering routes like L1 → EigenLayer, DeFi → EigenLayer, and L1 → DeFi → EL yield stacking.         
                        """)

        ###################
        st.write("  \n")
        st.write("  \n")


        # AVS Average Operator Reputation
        st.markdown("""
            <style>
            .header-style {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 0px;  /* Adjust the space below the header */
            }
            </style>
            """, unsafe_allow_html=True)

        # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS Average Operators\' Reputation</p>', unsafe_allow_html=True)

        # Select slider for average operator reputation
        avs_avg_operator_reputation = st.selectbox("", ["Unknown", "Established", "Renowned"])

        # The expander with more information (optional)
        with st.expander("Logic"):
            st.markdown("""
                Although being a qualitative metric, the **Average Operator Reputation** opted into the AVS for validating its chosen modules offers a useful glimpse into the AVS’s security profile. The user should consider operators’ historical slashing record and the overall validation and uptime performance, which are crucial for assessing overall operator-related risk, including potential malicious collusions.                        
                        """)
        

#########################################
#########################################
#########################################


    def calculate_operator_attack_risk(total_restaked, tvl):
        # High risk if either TVL or total restaked is below $50,000
        if tvl < 100000 or total_restaked < 100000:
            return 10
        
        default_minimum_risk = 9

        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, moderate risk
        elif ratio > 0.5:
            return 5  # Less than TVL but not by a wide margin, increased risk
        else:
            return 7

    
    operator_attack_risk = calculate_operator_attack_risk(total_restaked, tvl)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    # Calculate risk
    risk_score = avs_risk(security_audits, business_model, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation)

    # Determine the color and background color based on the risk score
    if risk_score >= 7.5:
        color = "#d32f2f"  # Red color for high risk
        background_color = "#fde0dc"  # Light red background
    elif risk_score <= 2.5:
        color = "#388e3c"  # Green color for low risk
        background_color = "#ebf5eb"  # Light green background
    else:
        color = "black"  # Black color for medium risk
        background_color = "#ffffff"  # White background

    st.markdown(
    f"""
    <div style="
        border: 2px solid {color};
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        margin: 10px 0;
        background-color: {background_color};">
        <h2 style="color: black; margin:0; font-size: 1.5em;">AVS Risk Score: <span style="font-size: 1.2em; color: {color};">{risk_score:.2f}</span></h2>
    </div>
    """, 
    unsafe_allow_html=True
    )

    st.write("  \n")
    st.write("  \n")


    st.write("""
            The **AVS Risk Score** ranges from 0 to 10, where 0 indicates the lowest level of risk and 10 represents the highest possible risk.
            
            The Risk Score is based on the risk level of each input category as well as their weighting, which is composed of their likelihood and impact. For example, the Likelihood of a X risk was considered higher than of the Y, and the Impact of X higher than Y. Both these variants were weighted per inpuit parameter. 
             
            We arrive at the final AVS Risk Score through a 0 to 10 normalization of the product of all the calculated risks per input.
             
            For a deeper dive, please visit the [source code](https://github.com/bmvicente/eigensimulators/blob/master/avsrisk/eigenavsrisk.py).
            """)


    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    col11, col12, col13 = st.columns([2,1,2])

    with col11:
        st.write("")

    with col12:
        st.image("images/tokensight.png", width=250)

    with col13:
        st.write("")
    
    
    image_url = 'https://img.freepik.com/free-vector/twitter-new-2023-x-logo-white-background-vector_1017-45422.jpg'
    link = 'https://twitter.com/tokensightxyz'
    markdown = f"""
    <a href="{link}" target="_blank">
        <img src="{image_url}" alt="Alt Text" style="display:block; margin-left: auto; margin-right: auto; width: 4%;">
    </a>
    """    
    st.markdown(markdown, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

