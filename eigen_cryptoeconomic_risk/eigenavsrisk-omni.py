
import streamlit as st

def avs_risk(security_audits, business_model, dual_staking_balance, avs_type, operator_attack_risk, restaking_mods, avs_operator_reputation, avs_operator_centralization, mev_extraction, liveness_deg, censorship, validator_collusion):
    # Define the risk scores for each metric (0-10 scale, 10 being riskiest)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
    business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
    avs_type_risk = {"Lightweight": 7, "Hyperscale": 3}
    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    avs_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
    avs_operator_centralization_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}
    mev_extraction_risk = {"High": 10, "Medium": 5, "Low": 2}
    liveness_deg_risk = {"High": 10, "Medium": 5, "Low": 2}
    censorship_risk = {"High": 10, "Medium": 5, "Low": 2}
    validator_collusion_risk = {"High": 10, "Medium": 5, "Low": 2}



    security_audit_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    avs_type_score = avs_type_risk[avs_type]
    restaking_mod_score = restaking_mods_risk[restaking_mods]
    avs_operator_reputation_score = avs_operator_reputation_risk[avs_operator_reputation]
    avs_operator_centralization_score = avs_operator_centralization_risk[avs_operator_centralization]
    mev_extraction_score = mev_extraction_risk[mev_extraction]
    liveness_deg_score = liveness_deg_risk[liveness_deg]
    censorship_score = censorship_risk[censorship]
    validator_collusion_score = validator_collusion_risk[validator_collusion]


    return security_audit_score, business_model_score, dual_staking_balance, avs_type_score, restaking_mod_score, avs_operator_reputation_score, avs_operator_centralization_score, operator_attack_risk, mev_extraction_score, liveness_deg_score, censorship_score, validator_collusion_score



def main():
    st.set_page_config(layout="wide")

    st.image("images/omni.jpeg", width=450)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Interoperability Network AVS: Omni Underlying Risk & Slashing Conditions Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
                    The consensus layer is implemented by the Omni consensus client, halo, and uses CometBFT for consensus on XMsgs and Omni EVM blocks.

            The Simulator takes six of the AVS-generic parameters to simulate their Risk Score and four parameters that specifically compose a Shared Sequencer AVS like Espresso. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            A good deal of the logic behind the right side of the Simulator (ESPRESSO-SPECIFIC METRICS) was researched on Nethermind's recent whitepaper [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581), specifically for Espresso.
                    
            The most significant parameter is the first: Cost-of-Corruption/Profit-from-Corruption relationship, since it poses the greatest weight on an AVS being corrupted or cryptoeconomically secure. 
        """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate utility or scenario for Espresso as a Shared-Sequencer AVS.")

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    def calculate_operator_attack_risk(total_restaked, tvl):
        if tvl < 100000 or total_restaked < 100000:
            return 10
        elif total_restaked >= 10000000000:
            return 1
        
        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, low risk
        elif ratio > 0.5:
            return 7  # Less than TVL, increased risk
        else:
            return 9 # < 0.5 Greatest risk
    

    def dual_staking_balance_calc(avs_token_percentage, xeth_percentage):
        ratio = avs_token_percentage / xeth_percentage

        if ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
            return 9
        elif ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
            return 8
        elif ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 7
        elif ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 6
        elif ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
            return 5 # Neutral adjustment for balanced scenario
        elif ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
            return 4
        elif ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
            return 3
        else:  # Very low AVS compared to ETH
            return 2

    if 'security_audit_score' not in st.session_state:
        st.session_state.security_audit_score = 0
    if 'business_model_score' not in st.session_state:
        st.session_state.business_model_score = 0
    if 'avs_type_score' not in st.session_state:
        st.session_state.avs_type_score = 0
    if 'restaking_mod_score' not in st.session_state:
        st.session_state.restaking_mod_score = 0
    if 'avs_operator_reputation_score' not in st.session_state:
        st.session_state.avs_operator_reputation_score = 0
    if 'avs_operator_centralization_score' not in st.session_state:
        st.session_state.avs_operator_centralization_score = 0
    if 'mev_extraction_score' not in st.session_state:
        st.session_state.mev_extraction_score = 0
    if 'liveness_deg_score' not in st.session_state:
        st.session_state.liveness_deg_score = 0
    if 'censorship_score' not in st.session_state:
        st.session_state.censorship_score = 0
    if 'validator_collusion_score' not in st.session_state:
        st.session_state.validator_collusion_score = 0
    if 'risk_score' not in st.session_state:
            st.session_state.risk_score = 0


    st.write("\n")
    

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

        custom_css = """
            <style>
            .header-style {
                font-size: 16px; /* Existing font size */
                font-weight: bold;
            }

            .large-header-style {
                font-size: 20px; /* Larger font size */
                font-weight: bold;
            }
            </style>
            """

        st.markdown(custom_css, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 10px;
                padding: 4px;
                text-align: center;
                margin: 5px 0;
                background-color: #4169E1;">
                <h2 class='large-header-style' style="color: white; margin:0;">AVS METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")



        col24, col25 = st.columns(2, gap="medium")
        with col24:

            # Restaked ETH Delegated
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
            st.markdown('<p class="header-style">Total Restaked ETH Delegated to Omni</p>', unsafe_allow_html=True)

            # Dropdown menu
            restaked_eth_del = st.number_input("", min_value=0, max_value=100000000000, step=100000000)
            st.write(f"&#8226; Total Restaked ETH to Omni: **${restaked_eth_del:,.0f}**")


            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")


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
            st.markdown('<p class="header-style">Business Model</p>', unsafe_allow_html=True)

            # Dropdown menu
            business_model = st.selectbox("", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"], index=1)

        

        with col25:

            # Restaked TVL
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
            st.markdown('<p class="header-style">Total Restaked TVL on Omni</p>', unsafe_allow_html=True)

            # Dropdown menu
            restaked_tvl = st.number_input("", min_value=0, max_value=10000000000, step=10000000, key="33")
            st.write(f"&#8226; Total Restaked TVL on Omni: **${restaked_tvl:,.0f}**")


            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")


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
            st.markdown('<p class="header-style">Dual Staking Model: Native Dual Staking</p>', unsafe_allow_html=True)
            
            st.write("  \n")

            avs_token_percentage = st.slider("**% $OMNI**", min_value=10, max_value=90, value=50, format='%d%%')

            xeth_percentage = 100 - avs_token_percentage
            
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True, format='%d%%')

            st.write("&#8226; **Native Dual Staking Balance**: {}% $OMNI : {}% xETH".format(avs_token_percentage, xeth_percentage))

        st.write("-------")

        col44,col45 = st.columns(2, gap="medium")
        with col44:
            business_model_likelihood = st.slider("*Likelihood* ", min_value=1, max_value=10, value=3)
        with col45:
            business_model_impact = st.slider("*Impact* ", min_value=1, max_value=10, value=7)

        dual_staking_balance = dual_staking_balance_calc(avs_token_percentage, xeth_percentage)
        st.session_state.dual_staking_balance = dual_staking_balance

        with st.expander("Logic"):
                st.markdown("""
                    Ordering the **Business Models** from EigenLayer [(Section 4.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) by risk: 
                    
                    - ***Pay in the Native Token of the AVS*** is the most risky, as the entire fee structure is dependent on the AVS's native token (\$AVS), tying closely to its market performance and the AVS's ongoing profitability;
                    - ***Dual Staking Utility***, with a high risk too because it depends on both ETH restakers and $AVS stakers, which introduces complexities in security and token value dynamics;
                    - ***Tokenize the Fee*** model comes with moderate risk involving payments in a neutral denomination (like ETH) and distributing a portion of fees to holders of the AVS's token, thus partly dependent on the AVS token's value;
                    - ***Pure Wallet*** represents the lowest risk, relying on straightforward service fees paid in a neutral denomination, like ETH.

                    Thus, the risk of each model is influenced by its reliance on the AVS's native token and the complexities of its fee and security structures.
                    
                    ```python
                    business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
                            
                    def dual_staking_balance_calc(avs_token_percentage, xeth_percentage):
                        ratio = avs_token_percentage / xeth_percentage

                        if ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
                            return 9
                        elif ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
                            return 8
                        elif ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                            return 7
                        elif ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                            return 6
                        elif ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
                            return 5 # Neutral adjustment for balanced scenario
                        elif ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
                            return 4
                        elif ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
                            return 3
                        else:  # Very low AVS compared to ETH
                            return 2
                    ```
                            

                    The Native Dual Staking model was chosen as the default one because it guarantees the highest Cost to Violate Liveness.
                    Particularly in the beginning, too much weight on the $OMNI native token increases the likelihood of the tokens of the dual staking model being toxic. And thus negatively impact liveness, an essential condition for a Shared Sequencer.
                            
                    Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                    **\$AVS** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$AVS* **>** *% xETH* pool balance makes sense to be a higher-reward event.
                        """)



        result1 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_model_likelihood * business_model_impact
        
        business_model_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result1}</span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Dual Staking Balance Risk * Likelihood * Impact)</span>
                </div>
            </div>"""

        st.markdown(business_model_calc, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")






        col27,col28 = st.columns(2, gap="medium")
        with col27:

            # Code Complexity
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


            st.markdown('<p class="header-style">AVS Protocol Architecture/Code Complexity</p>', unsafe_allow_html=True)

            code_complexity = st.selectbox("", ["High", "Medium", "Low"], index=1, key="ertr")



        with col28:
            
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
            st.markdown('<p class="header-style">Number of Security Audits</p>', unsafe_allow_html=True)

            # Dropdown menu
            security_audits = st.number_input("", min_value=0, max_value=5, step=1, value=2)

        st.write("-------")

        col35,col36 = st.columns(2, gap="medium")
        with col35:
            security_audits_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4)
        with col36:
            security_audits_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8)

            # The expander without a visible outline
        with st.expander("Logic"):
                st.markdown("""
                    Accounting for the **number of Security Audits** performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                    
                    While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks (and the risk of honest nodes getting slashed), and, as a result, rewards an AVS is confident to emit and Restakers and Operators to opt into it. 
                    
                    ```python
                    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1} # 0 security audits poses the greatest risk, 5 the least
                    ```
                            """)



        result2 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_model_likelihood * business_model_impact

        business_model_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result2}</span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Dual Staking Balance Risk * Likelihood * Impact)</span>
                </div>
            </div>"""

        st.markdown(business_model_calc, unsafe_allow_html=True)




        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


        # Operator Metrics
        st.markdown("""
                    <style>
                    .header-style {
                        font-size: 18px;
                        font-weight: bold;
                        margin-bottom: 0px;  /* Adjust the space below the header */
                    }
                    </style>
                    """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">Operator Metrics</p>', unsafe_allow_html=True)
 
        st.write("  \n")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
                
                operator_reputation = st.selectbox("**Operator Reputation**", ["Unknown", "Established", "Renowned"], index=1)

        with col101:            

                operator_centralization = st.selectbox("**Operators' Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"])
            

        operator_entrenchment_level = st.selectbox("**Operators' Entrenchment Level** (on other AVSs)", ["High Entrenchment", "Medium Entrenchment", "Low Entrenchment"])

        st.write("-------")

        col33, col34 = st.columns(2, gap="medium")
        with col33:
            operator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="o0")
        with col34:
            operator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="o1")

        st.write("  \n")

        with st.expander("Logic"):
                    st.markdown("""
                        The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581):
                        
                        "*Full MEV extraction and implementing censorship on shared sequencers pose a significant challenge for an attacker. To ensure the success of such an attack and to collect the entire MEV generated, an attacker would need control over 100% of the validators. In certain sequencer setups, where leader election is lottery-based, there might be an incentive for validators to collude to maximize the amount of MEV distributed to validators as opposed to the chains.*"
                        
                        Given the significant challenge MEV extraction poses to an attacker, it was assigned a somewhat low Likelihood, but still a considerable Impact were the attack to happen.
                                """)
                

        result3 = st.session_state.security_audit_score * security_audits_likelihood * security_audits_impact

        security_audits_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.security_audit_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{security_audits_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{security_audits_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result3}</span>
                </div>
            """

        st.markdown(security_audits_calc, unsafe_allow_html=True)



#############################
#############################
#############################




    with col2:


        custom_css = """
            <style>
            .header-style {
                font-size: 16px; /* Existing font size */
                font-weight: bold;
            }

            .large-header-style {
                font-size: 20px; /* Larger font size */
                font-weight: bold;
            }
            </style>
            """

        st.markdown(custom_css, unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 10px;
                padding: 4px;
                text-align: center;
                margin: 5px 0;
                background-color: #4169E1;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">OMNI-SPECIFIC METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")



        # Staked OMNI
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
        st.markdown('<p class="header-style">Total Staked $OMNI</p>', unsafe_allow_html=True)

            # Dropdown menu
        staked_omni = st.number_input("", min_value=0, max_value=10000000000, step=10000000)
        st.write(f"&#8226; Total Staked \$OMNI: **${staked_omni:,.0f}**")


        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")









        st.markdown('<p style="font-size: 22px; font-weight: bold; margin-bottom: 0px;">Consensus Mechanism Metrics through Halo Client</p>', unsafe_allow_html=True)

        # Validator Metrics
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">CometBFT: Validator Metrics</p>', unsafe_allow_html=True)

        st.write("  \n")

        col38,col39 = st.columns(2, gap="medium")
        with col38:
            engine_api = st.checkbox('Nodes use **Ethereum Engine API** to pair the Consensus Client (Halo) with the EVM Execution Client', value=True)
        with col39:
            validator_abci_usage = st.checkbox('**Engine API uses ABCI++** for seamless state transitions between Omni EVM and CometBFT', help="**HANDLING TRANSACTION REQUESTS**: Previous approaches relied on the CometBFT mempool to manage transaction requests, leading to network congestion and compromised consensus speed as activity increased. Omni addresses this challenge by utilizing the Engine API, alongside ABCI++, to move the transaction mempool to the execution layer. This strategic move ensures the CometBFT consensus process remains lightweight and efficient. **STATE TRANSLATION**: One of the major challenges in previous designs was translating the EVM state to a format compatible with CometBFT. Omni overcomes this hurdle by incorporating an ABCI++ wrapper around the CometBFT engine, enabling seamless state translation and ensuring that Omni EVM blocks are efficiently converted into CometBFT transactions.", value=True)

        col42,col43 = st.columns(2, gap="medium")
        with col42:
            tee_mec = st.checkbox('**TEE** Implementation for Effective Key Management', value=False)
        with col43:
            dvt_mec = st.checkbox('**DVT** Implementation to Reduce Risks of Single Points of Failure from a Subset of Validators', value=False)

        col50,col51 = st.columns(2, gap="medium")
        with col50:
            oracle_bridge_mec = st.checkbox('**Oracle/Bridge Solution** to Restrict Potential PfC', value=False)
        with col51:
            lockup_mec = st.checkbox('**Lock-Up Periods** Applied to Validators for Security Guarantees', value=False)

        col52,col53 = st.columns(2, gap="medium")
        with col52:
            da_sol_mec = st.checkbox('**DA Solution** for Horizontal Scaling of Nodes, Mitigating Potential State Explosions', value=False)
        with col53:
            fast_fin_ss_mec = st.checkbox('**Shared Sequencer Pre-Confirmation Solution** for *XMsg* Fast Finality', value=False)

        st.write("  \n")

        validator_performance_acc_rate = st.slider("**Validator XBlocks Attestation Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%')

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            validator_reputation = st.selectbox("**Validator Reputation**", ["Unknown", "Established", "Renowned"], index=1)
        with col101:           
            validator_centralization = st.selectbox("**Validators' Nodes Geographical Centralization**", ["Centralized", "Semi-Decentralized", "Decentralized"])
        
        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            validator_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="v0")
        with col34:
            validator_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="v1")

        with st.expander("Logic"):
                st.markdown("""
Using the Engine API, Omni nodes pair existing high performance Ethereum execution clients with a new consensus client, referred to as halo, that implements CometBFT consensus.The Engine API allows clients to be substituted or upgraded without breaking the system. This allows the protocol to maintain flexibility on Ethereum and Cosmos technology while promoting client diversity within its execution layer and consensus layer. We consider this new network framework to be a public good that future projects may leverage for their own network designs.
                            
                            ABCI++  while introducing benefits at the application layer particularly, also introduce complexity in application design, multi-faceted security vulnerabilities, and performance overhead to the whole process. It is paramount to consider the deterministic design and logic of integrated applications.

                            Application BlockChain Interface (ABCI++): Leveraging CometBFT's ABCI, Omni introduces enhancements (potentially hinted at by the name ABCI++) that allow for more complex and flexible application interactions. This includes processing state transitions for the Omni EVM and external VMs without interference.
                Validators compile XMsg into XBlocks, which include metadata for efficient verification and attestation, streamlining the relaying process.
                            
                Engine API Conversion: An ABCI++ adapter wraps around the CometBFT engine, translating Engine API messages for consensus processing, ensuring Omni's lightweight consensus and quick finality.
                    During the consensus, validators utilize ABCI++ to attest to the state of Rollup VMs, running state transition functions for accurate and secure external VM interactions.
                    The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581):
                    
                    "*Full MEV extraction and implementing censorship on shared sequencers pose a significant challenge for an attacker. To ensure the success of such an attack and to collect the entire MEV generated, an attacker would need control over 100% of the validators. In certain sequencer setups, where leader election is lottery-based, there might be an incentive for validators to collude to maximize the amount of MEV distributed to validators as opposed to the chains.*"
                    
                    Given the significant challenge MEV extraction poses to an attacker, it was assigned a somewhat low Likelihood, but still a considerable Impact were the attack to happen.
                            
                    Leveraging CometBFT's ABCI, Omni introduces enhancements (potentially hinted at by the name ABCI++) that allow for more complex and flexible application interactions. This includes processing state transitions for the Omni EVM and external VMs without interference.
                    
                            
                    Decoupled Consensus and Application Logic: The separation of the consensus engine and application logic via ABCI facilitates the creation of diverse applications, from cryptocurrencies to e-voting systems, without being limited to a specific blockchain's capabilities or language.
                            

                    **PERFORMANCE ACCURACY RATE**
                    - **Submission of Cross-Chain Messages**: Relayers wait for more than two-thirds of the validators to attest to a source chain block. They then submit the validated XMsgs to the destination chains, along with necessary validator signatures and multi-merkle-proof.
- **Attestation Monitoring and XBlock Cache Management**: Relayers monitor the Omni Consensus Chain for attested XBlocks, maintaining a cache of these blocks for efficient processing and submission readiness.
- **Decision Making for Message Submission**: Relayers decide on the number of XMsgs to submit, balancing transaction cost considerations like data size and gas limits.
                            """)


        result4 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_model_likelihood * business_model_impact

        
        business_model_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result4}</span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Dual Staking Balance Risk * Likelihood * Impact)</span>
                </div>
            </div>"""

        st.markdown(business_model_calc, unsafe_allow_html=True)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("\n")
        st.write("  \n")







        # EVM Metrics
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">EVM Metrics through Execution Client</p>', unsafe_allow_html=True)

        st.write("  \n")
        
        sybil_mec = st.checkbox('**Anti-Sybil Mechanism** for transactions submitted to the Omni EVM, deterring spam and malicious activities such as DoS attacks', value=True)
        encrypted_mempool_mec = st.checkbox('**Encrypted Mempool** for increased privacy and security in transactions', value=False)

        st.write("  \n")

        col100, col101 = st.columns(2, gap="medium")
        with col100:
            evm_equivalence = st.selectbox("**EVM Compatibility**", ["Incompatible", "Compatible", "Equivalent"], help="**As a product of...", index=2)
        with col101:
            evm_client_div = st.selectbox("**EVM Client Diversity**", ["Poorly Diverse", "Moderately Diverse", "Highly Diverse"], help="**As a product of...** Omni adheres to the Engine API, a standard that all EVM clients also comply with. This adherence ensures that any EVM client, such as Geth, Besu, Erigon, and others, can be seamlessly integrated into the Omni network without the need for specialized modifications. This approach allows the Omni ecosystem to leverage the unique features and optimizations that different clients provide.", index=2)
            

        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            evm_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="e0")
        with col34:
            evm_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="e1")

        with st.expander("Logic"):
                st.markdown("""
**Execution Consensus**
1. When it is a validator's turn to propose a block, its halo client requests the latest Omni EVM block from its execution client using the Engine API.
2. The execution client builds a block from the transactions in its mempool and returns the block header to the halo client through the Engine API.
3. The halo client packages the new block proposal as a single CometBFT transaction and includes it in the consensus layer block.
4. The block is proposed to the rest of the validator network through the consensus layer’s P2P network.
5. Non-proposing validators use the Engine API and their execution clients to run the state transition function on the proposed block header to verify the block’s validity.
                        
                    OMNI provides an anti-sybil mechanism for transactions submitted to the Omni EVM, deterring spam and malicious activities such as denial-of-service attacks.        
                    
                    Developer Accessibility and EVM Equivalence: By ensuring EVM equivalence, Omni offers a seamless transition for Ethereum developers, making it a more accessible platform for deploying decentralized applications (DApps) without modifications.
                    
                    **Engine API**

                    - **Scalability and Efficiency:** By offloading the transaction mempool and facilitating efficient state translation, the Engine API contributes to Omni's scalability and sub-second transaction finality.
                    - **Flexibility:** Supports the interchangeability and upgrading of execution clients without system disruption, ensuring compatibility with various Ethereum execution clients.
                            
                    This fidelity guarantees that opcode compatibility issues are non-existent, and all developer tooling designed for Ethereum seamlessly works with the Omni EVM.

### Advantages of Omni’s EVM Equivalence

- **Seamless Migration:** Developers can port their DApps to Omni without any modifications, significantly reducing the effort and complexity involved in accessing a new blockchain ecosystem.
- **Developer Tooling Compatibility:** All the tools, libraries, and frameworks designed for Ethereum development are fully compatible with the Omni EVM, streamlining the development process.
- **Future-Proof:** Omni's alignment with Ethereum's upgrade path ensures that developers can leverage the latest features and improvements without delay.
                            
                    Client Diversity and EVM Equivalence: Omni emphasizes running an unmodified version of the Ethereum Virtual Machine (EVM), which guarantees that Ethereum smart contracts and developer tooling work seamlessly. This focus on EVM equivalence and support for diverse client implementations enhances developer accessibility and network resilience.
                            """)


        result5 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_model_likelihood * business_model_impact

        
        business_model_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result5}</span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Dual Staking Balance Risk * Likelihood * Impact)</span>
                </div>
            </div>"""

        st.markdown(business_model_calc, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("\n")
        st.write("  \n")





        # Relayer Metrics
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">Relayer Metrics</p>', unsafe_allow_html=True)

        st.write("  \n")

        relayer_merkle = st.checkbox('Use of **Merkle Multi-Proofs** for efficient XBlock Submission', value=True)
        relayer_da_solution = st.checkbox('**DA Solution** for Complex Verification of Validator Signatures and Merkle Multi-Proofs At Scale', value=False)

        st.write("  \n")


        col100, col101 = st.columns(2, gap="medium")
        with col100:
            relayer_reputation = st.selectbox("**Relayer Reputation**", ["Unknown", "Established", "Renowned"], index=1)
        with col101:
            relayer_performance_acc_rate = st.slider("**Relayer Performance Accuracy Rate**", min_value=0, max_value=100, value=50, format='%d%%')

        st.write("-------")
        
        col33, col34 = st.columns(2, gap="medium")
        with col33:
            relayer_metrics_likelihood = st.slider("*Likelihood*  ", min_value=1, max_value=10, value=4, key="r0")
        with col34:
            relayer_metrics_impact = st.slider("*Impact*  ", min_value=1, max_value=10, value=8, key="r1")

        with st.expander("Logic"):
                st.markdown("""
                            
                            Decision Making for Message Submission
A key decision that Relayers face is determining the number of XMsgs to submit to each destination chain. This decision directly influences the cost of transactions due to factors like data size, gas limits, and the computational overhead required for portal contract verification and message processing.
                            Relayer responsible for delivering attested cross-network messages from the Omni network to destination rollup VMs. Monitors the Omni Consensus Layer until ⅔ (>66%) of the validator set attested to the “next” block on each source chain, then proceeds to forwarding the respective XMsg list included in the block.
Relayers are responsible for delivering confirmed cross-network messages from Omni to destination rollups. When 2/3 (>66%) of Omni validators attest to a given XBlock, relayers forward the XBlock’s corresponding XMsg list to destination rollup networks.
                            
                            While Merkle multi-proofs provide a powerful tool for efficient data verification across blockchain networks, careful consideration of these risks and appropriate mitigations are essential to maintaining the security, efficiency, and robustness of blockchain protocols that utilize them.
        
                            - **Decision Making for Message Submission**: A key decision that Relayers face is determining the number of **`XMsg`**s to submit to each destination chain. This decision directly influences the cost of transactions due to factors like data size, gas limits, and the computational overhead required for portal contract verification and message processing. (**PERFORMANCE ACCURACY RATE**)
- **Submission** **Transaction**: For the actual submission to a destination chain, Relayers generate a merkle-multi-proof for the **`XMsg`**s that are to be included, based on the **`XBlock`** attestations root that has reached a quorum. They then craft an EVM transaction containing this data, aiming to ensure its swift inclusion on the destination chain.        
                    At scale, Merkle multi-proofs introduce data availability concerns, complexity in verification, and increased computational cost.
                            
                            Resource Intensiveness: The need for signature and merkle proof verification for each message can be resource-intensive, especially on high-traffic networks.
        Permissionless third-party Relayer (Permissionless — reduces single point of failure likelihood | decentralized): The Relayer plays a pivotal role in the Omni protocol as a permissionless entity that bridges cross-chain messages between source and destination chains. It performs critical functions that ensure the smooth and secure transmission of messages across the network.

        Relayer Submits XBlocks: Relayers construct submissions for each finalized XBlock hash, including validator signatures and merkle proofs of each XMsg's inclusion. (DA CONSTRAINTS AT SCALE)
                Relayer Role Security: While the permissionless relayer mechanism is a strength for interoperability, it also introduces a potential vector for attacks if relayers behave maliciously or if the reputation system is not robust enough to incentivize honest participation.
                            
                To submit XMsgs to a destination chain, Relayers generate a merkle-multi-proof for the XMsgs tied to an attested XBlock. They package this information into an EVM transaction aimed at the destination chain, encapsulating the core of their role in cross-chain communication.
                
                After validators' attestation, relayers submit XBlocks and their messages to destination chains, employing merkle-multi-proofs for verification.
                    Relayer Role Security: While the permissionless relayer mechanism is a strength for interoperability, it also introduces a potential vector for attacks if relayers behave maliciously or if the reputation system is not robust enough to incentivize honest participation.
                            """)


        result6 = st.session_state.business_model_score * st.session_state.dual_staking_balance * business_model_likelihood * business_model_impact

        
        business_model_calc = f"""
            <div style="text-align: center;">
                <div>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.business_model_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.dual_staking_balance}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{business_model_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result6}</span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Dual Staking Balance Risk * Likelihood * Impact)</span>
                </div>
            </div>"""

        st.markdown(business_model_calc, unsafe_allow_html=True)




    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    col1, col2, col3 = st.columns([1, 5, 1])

    # Placing the image in the middle column effectively centers it
    with col2:
        st.image("images/omni-diagram.jpeg", width=1200)

    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image("images/omni-diagram1.jpg", width=1200)

    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image("images/omni-diagram2.jpg", width=1200)

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

    st.subheader("**Profit from Corruption Scenario Analysis**")

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

    def normalize_score(original_score, min_original=17, max_original=17700):
        normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
        return normalized_score

    final_result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9 + result10 + result11
    normalized_risk_score = normalize_score(final_result)

    st.session_state.risk_score = normalized_risk_score

    st.markdown(f"<div style='text-align: center; font-size: 21px; font-weight: bold;'>Non-Normalized <i>Espresso</i> Risk Score</div>", unsafe_allow_html=True)
    final_result_html = f"""
            <div style="text-align: center;">
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result1}</span> 
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result2}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result3}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result4}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result5}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result6}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result7}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result8}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result9}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result10}</span>
                <span style="font-size: 22px; font-weight: bold;"> + </span>
                <span style="font-size: 22px; font-weight: bold; padding: 5px; margin: 2px;">{result11}</span>
                <span style="font-size: 22px; font-weight: bold;"> = </span>
                <span style="font-size: 24px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{final_result}</span>
            </div>
        """

    st.markdown(final_result_html, unsafe_allow_html=True)



#########################################
#########################################
#########################################


    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    
    
    risk_score = avs_risk(security_audits, business_model, st.session_state.dual_staking_balance, avs_type, st.session_state.operator_attack_risk, restaking_mods, avs_operator_reputation, avs_operator_centralization, mev_extraction, liveness_deg, censorship, validator_collusion)
    (st.session_state.security_audit_score, st.session_state.business_model_score, st.session_state.dual_staking_balance, st.session_state.avs_type_score, st.session_state.restaking_mod_score, st.session_state.avs_operator_reputation_score, st.session_state.avs_operator_centralization_score, st.session_state.operator_attack_risk, st.session_state.mev_extraction_score, st.session_state.liveness_deg_score, st.session_state.censorship_score, st.session_state.validator_collusion_score) = risk_score


    # Determine the color and background color based on the risk score
    if st.session_state.risk_score >= 75:
        color = "#d32f2f"  # Red color for high risk
        background_color = "#fde0dc"  # Light red background
    elif st.session_state.risk_score <= 25:
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
        <h2 style="color: black; margin:0; font-size: 1.4em;">Normalized <i>Espresso</i> Risk Score: <span style="font-size: 1.5em; color: {color};">{st.session_state.risk_score:.0f}</span></h2>
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
                The <strong>Espresso Risk Score</strong> is normalized to range from 0 to 100 (for easy reading), where 0 indicates the lowest level of risk and 100 represents the highest possible risk. The Risk Score is calculated based on the risk level of each input parameter as well as their weighting, which is determined by the <strong>Likelihood</strong> and <strong>Impact</strong> of that risk to the AVS. 
                </div>
                </div>
                """, unsafe_allow_html=True)



    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.write("-----------------------")

    st.write("\n")

    st.markdown('<p style="font-weight: bold; font-size: 1.2em;">NEXT...</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;"><s>&#8226; Operator Centralization Risk Level</s></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Proposed Minimum AVS TVL and TVL caps</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; display: inline;"><s>&#8226; Risks Based on AVS Nature</s></p><span style="font-weight: normal; display: inline;"><s> (data availability, keeper networks, oracles, bridges, etc.)</s></span>', unsafe_allow_html=True)

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

