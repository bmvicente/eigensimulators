
# EigenLayer AVS Risks

import streamlit as st

# Function to calculate AVS risk
def avs_risk(security_audits, business_model, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation):
    # Define the risk scores for each metric (0-10 scale, 10 being riskiest)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
    business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
    avs_type_risk = {"Lightweight": 7, "Hyperscale": 3}
    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}

    security_audits_weight = 4 * 4                  # Likelihood 4, Impact 4
    business_model_weight = 2 * 3                   # Likelihood 2, Impact 3
    avs_type_weight = 1 * 2                         # Likelihood 2, Impact 2
    restaking_mods_weight = 2 * 3                   # Likelihood 2, Impact 3
    operator_attack_weight = 3 * 5                  # Likelihood 3, Impact 5
    avs_avg_operator_reputation_weight = 1 * 1      # Likelihood 1, Impact 1
    #CVS and CVL based and 51% operator attack dependant

    security_audit_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    avs_type_score = avs_type_risk[avs_type]
    restaking_mod_score = restaking_mods_risk[restaking_mods]
    avs_avg_operator_reputation_score = avs_avg_operator_reputation_risk[avs_avg_operator_reputation]

    total_risk_score = (security_audit_score * security_audits_weight +
                        business_model_score * business_model_weight +
                        avs_type_score * avs_type_weight +
                        operator_attack_risk * operator_attack_weight +  # Use the calculated risk score directly
                        restaking_mod_score * restaking_mods_weight +
                        avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight
                        )

    max_security_audit_score = 100  # Assuming worst case for security audit is 0 audits
    max_business_model_score = 100   # Assuming worst case for business model is "Pure Wallet"
    max_avs_type_score = 100         # Assuming worst case for AVS type is "Hyperscale"
    max_restaking_mod_score = 100    # Assuming worst case for restaking modality is "LST LP Restaking"
    max_operator_attack_score = 100  # Assuming worst case for operator attack risk
    max_avs_avg_operator_reputation_score = 100  # Assuming worst case for operator attack risk

    # Calculate the maximum possible risk score
    max_possible_risk_score = (
        max_security_audit_score * security_audits_weight +
        max_business_model_score * business_model_weight +
        max_avs_type_score * avs_type_weight +
        max_operator_attack_score * operator_attack_weight +
        max_restaking_mod_score * restaking_mods_weight +
        max_avs_avg_operator_reputation_score * avs_avg_operator_reputation_weight)

    # Normalize the risk score
    normalized_risk_score = (total_risk_score / max_possible_risk_score) * 100
    normalized_risk_score = round(normalized_risk_score, 2)

    return normalized_risk_score




# Streamlit app setup
def main():
    st.set_page_config(layout="wide")

    st.image("images/eigenimage.png")

    st.title("AVS Risk Simulator")

    
    st.write("  \n")
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
        st.markdown('<p class="header-style">AVS Total Restaked & TVL</p>', unsafe_allow_html=True)

        st.write("  \n")

        col3, col4 = st.columns([3, 3])

        with col3:
                total_restaked = st.number_input("**AVS Total Restaked ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

        with col4:
                tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)
        
        tvl = float(tvl) if tvl else 0
        total_restaked = float(total_restaked) if total_restaked else 0



        # The expander without a visible outline
        with st.expander("Logic"):
                st.markdown("""                        
                    The **TVL/Total Restaked** risk logic herein is set so that the greater the *(AVS Total Restaked/2) : AVS TVL* ratio, the safer the AVS is, and vice-versa.
                    
                    To take the simplest scenario of the single-AVS restaking by operators [(Section 3.4.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) to begin with: an AVS appears to be most secure when the amount of restaked ETH is at least double the total locked value (TVL) and a 50% quorum is required for a collusion attack to capture the TVL, as any successful attack would result in at least half of the attacker's stake being slashed. If *AVS Total Restaked* increases from there compared to the *AVS TVL*, the risk gets reduced even further. If both variables are under $100K, we consider it the maximum risk scenario.

                    Accordingly, the main goal is to maintain the *CfC (Cost from Corruption)* ***above*** *the PfC (Profit from Corruption)* to desincentivize colluding, malicious operators to perform an attack. Appropriate bridges and oracles could be built to restrict the transaction flow within the period of slashing or to have bonds on the transacted value to maximize CfC/minimize PfC.

                    Understanding what a reduced risk level should be is not useful for operator-collusion cases only, but also for increasing the [CVS (Cost to Violate Safety) and the CVL (Cost to Violate Liveness)](https://www.blog.eigenlayer.xyz/dual-staking/), i.e. in a Dual Staking Model and Veto Dual Staking context, for example, which are useful to maintain the health of the AVS dual token pool (or AVS TVL, in other words).               
                            """)



        ###################        
        st.write("  \n")
        st.write("  \n")
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
        business_model = st.selectbox("", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"])

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                Ordering the **Business Models** from EigenLayer [(Section 4.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) by risk: 
                
                - ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$AVS), tying closely to its market performance and the AVS's ongoing profitability;
                - ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $AVS stakers, which introduces complexities in security and token value dynamics;
                - ***Tokenize the Fee*** model comes with moderate risk involving payments in a neutral denomination (like ETH) and distributing a portion of fees to holders of the AVS's token, thus partly dependent on the AVS token's value;
                - ***Pure Wallet*** represents the lowest risk, relying on straightforward service fees paid in a neutral denomination, like ETH.

                Thus, the risk of each model is influenced by its reliance on the AVS's native token and the complexities of its fee and security structures.
            """)

        


        st.write("  \n")
        st.write("  \n")
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
                Accounting for the **number of Security Audits** performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                
                While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks (and the risk of honest nodes getting slashed), and, as a result, rewards an AVS is confident to emit and Restakers and Operators to opt into it. 
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

        st.markdown('<p class="header-style">AVS Type</p>', unsafe_allow_html=True)
        st.write("  \n")

        avs_type = st.selectbox("", ["Lightweight", "Hyperscale"])
        
        with st.expander("Logic"):
            st.markdown("""
                In designing modules for maximal security and minimal centralization risk, EigenLayer suggests two approaches: **Hyperscale and Lightweight AVS** [(Section 3.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper).

                **Hyperscale AVS** involves distributing the computational workload across many nodes, allowing for high overall throughput and reducing incentives for centralized validation. This horizontal scaling minimizes validation costs and amortization gains for any central operator. 

                On the other hand, the **Lightweight** approach focuses on tasks that are redundantly performed by all operators but are inexpensive and require minimal computing infrastructure.

                While it does depend on the needs of an AVS, the Hyperscale-type is more robust and secure due to its decentralized nature, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our simulator.                    
                        """)
    


        st.write("  \n")
        st.write("  \n")
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

        st.markdown('<p class="header-style">AVS Restaking Modality</p>', unsafe_allow_html=True)

        restaking_mods = st.selectbox("", ["LST LP Restaking", "ETH LP Restaking", "LST Restaking", "Native Restaking"])

        with st.expander("Logic"):
            st.markdown("""
                Setting aside Liquid Staking and Superfluid Staking for now, EigenLayer introduces a few **Restaking Modalities** for yield stacking on its platform [(Section 2.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper). 

                - ***LST LP Restaking***, involving staking LP tokens of pairs with liquid staking ETH tokens. High complexity and exposure to DeFi market risks pose **potentially large risks**;
                - ***ETH LP Restaking***, where validators stake LP tokens including ETH which tie rewards to DeFi market performance, introducing considerable risk due to market volatility;
                - ***LST Restaking***, involving staking of ETH already restaked via protocols like Lido or Rocket Pool. Adds a layer of complexity and dependence on third-party staking services, presenting moderate risk;
                - ***Native Restaking***, where validators restake staked ETH directly to EigenLayer. This is the simplest and most direct form of restaking, offering the **lowest risk profile**.
                        """)


        st.write("  \n")
        st.write("  \n")
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

        st.markdown('<p class="header-style">AVS Average Operators\' Reputation</p>', unsafe_allow_html=True)

        avs_avg_operator_reputation = st.selectbox("", ["Unknown", "Established", "Renowned"])

        with st.expander("Logic"):
            st.markdown("""
                Although being a purely qualitative metric, the **Average Reputation of Operators** that the AVS chose to be opted in to validate its modules offers a useful glimpse into the AVS’s security profile. The user should consider operators’ historical slashing record and the overall validation and uptime performance, which are crucial in assessing overall operator-related risk for an AVS, including potential malicious collusions.                        
                        """)

        

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    def calculate_operator_attack_risk(total_restaked, tvl):
        if tvl < 100000 or total_restaked < 100000:
            return 10
        
        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, moderate risk
        elif ratio > 0.5:
            return 7  # Less than TVL but not by a wide margin, increased risk
        else:
            return 9

    operator_attack_risk = calculate_operator_attack_risk(total_restaked, tvl)

        
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
        <h2 style="color: black; margin:0; font-size: 1.4em;">AVS Risk Score: <span style="font-size: 1.5em; color: {color};">{risk_score:.0f}</span></h2>
    </div>
    """, 
    unsafe_allow_html=True
    )

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    st.markdown("""
                <style>
                .big-font {
                    font-size: 18px;  /* Adjust font size as needed */
                }
                </style>
                <div class="big-font">
                The <strong>AVS Risk Score</strong> is normalized to range from 0 to 10 (for easy reading), where 0 indicates the lowest level of risk and 10 represents the highest possible risk.
                </div>
                <br>

                <div class="big-font">
                The Risk Score is calculated based on the risk level of each input parameter as well as their weighting, which is determined by the <strong>Likelihood</strong> and <strong>Impact</strong> of that risk to the AVS. 
                For example, the Likelihood of a Security Audit posing a risk and its Impact on the integrity of the AVS are both greater than the Likelihood and Impact to an AVS of, say, its <em>Average Operator Reputation</em> and the <em>AVS Type</em> chosen. The Simulator takes these nuances into account.            
                </div>
                <br>

                <div class="big-font">
                <em>It's important to bear in mind that this Simulator was built from an AVS perspective alone.</em>
                </div>
                """, unsafe_allow_html=True)



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

