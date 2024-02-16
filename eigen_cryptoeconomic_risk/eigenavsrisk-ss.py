
import streamlit as st

def avs_risk(security_audits, business_model, dual_staking_balance, avs_type, operator_attack_risk, restaking_mods, avs_avg_operator_reputation, mev_extraction, liveness_deg, censorship, validator_collusion):
    # Define the risk scores for each metric (0-10 scale, 10 being riskiest)

    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1}
    business_model_risk = {"Pay in the Native Token of the AVS": 10, "Dual Staking Utility": 7, "Tokenize the Fee": 4, "Pure Wallet": 1}
    avs_type_risk = {"Lightweight": 7, "Hyperscale": 3}
    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
    avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
    mev_extraction_risk = {"High": 10, "Medium": 5, "Low": 2}
    liveness_deg_risk = {"High": 10, "Medium": 5, "Low": 2}
    censorship_risk = {"High": 10, "Medium": 5, "Low": 2}
    validator_collusion_risk = {"High": 10, "Medium": 5, "Low": 2}



    security_audit_score = security_audits_risk[security_audits]
    business_model_score = business_model_risk[business_model]
    avs_type_score = avs_type_risk[avs_type]
    restaking_mod_score = restaking_mods_risk[restaking_mods]
    avs_avg_operator_reputation_score = avs_avg_operator_reputation_risk[avs_avg_operator_reputation]
    mev_extraction_score = mev_extraction_risk[mev_extraction]
    liveness_deg_score = liveness_deg_risk[liveness_deg]
    censorship_score = censorship_risk[censorship]
    validator_collusion_score = validator_collusion_risk[validator_collusion]


    return security_audit_score, business_model_score, dual_staking_balance, avs_type_score, restaking_mod_score, avs_avg_operator_reputation_score, operator_attack_risk, mev_extraction_score, liveness_deg_score, censorship_score, validator_collusion_score



def main():
    st.set_page_config(layout="wide")

    st.image("images/espresso1.png", width=450)

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Shared Sequencer AVS: Espresso Underlying Risk Simulator**")

    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
            The Simulator takes six of the parameters that can compose an AVS to simulate their Risk Score and four parameters that specifically compose a Shared Sequencer AVS like Espresso. The underlying calculations and theory behind each input can be found in the Logic dropdowns below each Parameter.
            A good deal of the logic behind the right side of the Simulator (ESPRESSO-SPECIFIC METRICS) was researched on Nethermind's recent whitepaper [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581).
        
            The most significant parameter is the first: Cost-of-Corruption/Profit-from-Corruption relationship, since it poses the greatest weight on an AVS being exposed to corruption or to being cryptoeconomically secured. The dropdown 
        """)

        
    st.write("**Note**: The dropdown input values and the Likelihood and Impact sliders are set as such by default to represent the exact or most approximate utility or scenario for a Shared-Sequencer AVS.")

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
    if 'avs_avg_operator_reputation_score' not in st.session_state:
        st.session_state.avs_avg_operator_reputation_score = 0
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
                background-color: #CC8E00;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">SHARED-SEQUENCER GENERIC METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")


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

        st.markdown('<p class="header-style">SS Cost of Corruption <> Profit from Corruption</p>', unsafe_allow_html=True)

        st.write("  \n")

        col3, col4 = st.columns([3, 3])

        with col3:
                total_restaked = st.number_input("**Total Amount Restaked on AVS Ecosystem ($)**", min_value=0, max_value=1000000000000, value=0, step=100000000)
                st.write(f"&#8226; Total Amount Restaked: ${total_restaked:,.0f}")

        with col4:
                tvl = st.number_input("**SS TVL ($)**", min_value=0, max_value=1000000000000, value=0, step=10000000)
                st.write(f"&#8226; SS TVL: ${tvl:,.0f}")
        
        st.write("  \n")

        st.write("**PARAMETERS WEIGHTING**")
        
        col20,col21 = st.columns([3, 3])
        with col20:
            tvl_total_restaked_likelihood = st.slider("**Likelihood**", min_value=1, max_value=10, value=3,
                                                          help=f"""
                                                          Accounts for the likelihood of the parameter imposing a risk to the security of the AVS.

                                                          1 == Unlikely | 10 == Very Likely""")
        with col21:
            tvl_total_restaked_impact = st.slider("**Impact**", min_value=1, max_value=10, value=10, 
                                                      help=f"""
                                                      Assesses the impact that risk would have on the security of the AVS.

                                                      1 == Unimpactful | 10 == Very Impactful""")


        tvl = float(tvl) if tvl else 0
        total_restaked = float(total_restaked) if total_restaked else 0

        operator_attack_risk = calculate_operator_attack_risk(total_restaked, tvl)
        st.session_state.operator_attack_risk = operator_attack_risk

        with st.expander("Logic"):
                st.markdown("""
                    It is assumed a Total Amount Restaked superior to $10 billion is nearly impossible to be 51%-attacked and therefore is assigned the minimal risk of PfC exceeding CoC, in the Simulator.
                                            
                    The **TVL/Total Restaked** risk logic herein is set so that the greater the *(AVS Total Restaked/2) : AVS TVL* ratio, the safer the AVS is, and vice-versa.
                    
                    To take the simplest scenario of the single-AVS restaking by operators [(Section 3.4.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper) to begin with: an AVS appears to be most secure when the amount of restaked ETH is at least double the total locked value (TVL) and a 50% quorum is required for a collusion attack to capture the TVL, as any successful attack would result in at least half of the attacker's stake being slashed. If *AVS Total Restaked* increases from there compared to the *AVS TVL*, the risk gets reduced even further. If both variables are under $100K, we consider it the maximum risk scenario.

                    Accordingly, the main goal is to maintain the *CoC (Cost of Corruption)* ***above*** *the PfC (Profit from Corruption)* to desincentivize colluding, malicious operators to perform an attack. Appropriate bridges and oracles could be built to restrict the transaction flow within the period of slashing or to have bonds on the transacted value to maximize CoC/minimize PfC.

                    Understanding what a reduced risk level should be is not useful for operator-collusion cases only, but also for increasing the [CVS (Cost to Violate Safety) and the CVL (Cost to Violate Liveness)](https://www.blog.eigenlayer.xyz/dual-staking/), i.e. in a Dual Staking Model and Veto Dual Staking context, for example, which are useful to maintain the health of the AVS dual token pool (or AVS TVL, in other words).
                    
                    ```python
                    def calculate_operator_attack_risk(total_restaked, tvl):
                        if tvl < 100000 or total_restaked < 100000:
                        return 10
        
                        ratio = (total_restaked / 2) / tvl

                        if ratio > 1.5:
                            return 1  # Significantly greater than TVL, lowest risk
                        elif ratio > 1:
                            return 3  # Greater than TVL, low risk
                        elif ratio > 0.5:
                            return 7  # Less than TVL, increased risk
                        else:
                            return 9 # < 0.5 Greatest risk
                            """)

        result1 = st.session_state.operator_attack_risk * tvl_total_restaked_likelihood * tvl_total_restaked_impact

        tvl_total_restaked_calc = f"""
            <div style="text-align: center;">
                <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.operator_attack_risk}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{tvl_total_restaked_likelihood}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{tvl_total_restaked_impact}</span> 
                <span style="font-size: 24px; font-weight: bold;"> = </span>
                <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result1}</span>
                <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 16px; font-weight: bold;">(Parameter Risk based on Input * Likelihood * Impact = Weighted Overall Risk for Parameter)</span>
        </div>
        """

        st.markdown(tvl_total_restaked_calc, unsafe_allow_html=True)


        ###################        
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")




        col24, col25 = st.columns(2, gap="medium")
        with col24:

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
            st.markdown('<p class="header-style">SS Business Model</p>', unsafe_allow_html=True)

            # Dropdown menu
            business_model = st.selectbox("", ["Pay in the Native Token of the AVS", "Dual Staking Utility", "Tokenize the Fee", "Pure Wallet"], index=1)

        

        with col25:
            
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
            st.markdown('<p class="header-style">SS Dual Staking Model: Native Dual Staking</p>', unsafe_allow_html=True)
            
            st.write("  \n")

            avs_token_percentage = st.slider("**% $SS**", min_value=10, max_value=90, value=50)

            xeth_percentage = 100 - avs_token_percentage
            
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth_percentage, disabled=True)

            st.write("&#8226; **Native Dual Staking Balance**: {}% $SS : {}% xETH".format(avs_token_percentage, xeth_percentage))

        st.write("\n")

        col44,col45 = st.columns(2)
        with col44:
            business_model_likelihood = st.slider("**Likelihood** ", min_value=1, max_value=10, value=3)
        with col45:
            business_model_impact = st.slider("**Impact** ", min_value=1, max_value=10, value=7)

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
                    Particularly in the beginning, too much weight on the $SS native token increases the likelihood of the tokens of the dual staking model being toxic. And thus negatively impact liveness, an essential condition for a Shared Sequencer.
                            
                    Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                    **\$AVS** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                    **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                    A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$AVS* **>** *% xETH* pool balance makes sense to be a higher-reward event.
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


        col33,col34 = st.columns(2)
        with col33:
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

            st.markdown('<p class="header-style">SS Restaking Modality</p>', unsafe_allow_html=True)

            restaking_mods = st.selectbox("", ["LST LP Restaking", "ETH LP Restaking", "LST Restaking", "Native Restaking"], index=2)

            st.write("  \n")

            restaking_mods_likelihood = st.slider("**Likelihood**    ", min_value=1, max_value=10, value=2)
            restaking_mods_impact = st.slider("**Impact**    ", min_value=1, max_value=10, value=2)

            with st.expander("Logic"):
                st.markdown("""
                    Setting aside Liquid Staking and Superfluid Staking for now, EigenLayer introduces a few **Restaking Modalities** for yield stacking on its platform [(Section 2.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper). 

                    - ***LST LP Restaking***, involving staking LP tokens of pairs with liquid staking ETH tokens. High complexity and exposure to DeFi market risks pose **potentially large risks**;
                    - ***ETH LP Restaking***, where validators stake LP tokens including ETH which tie rewards to DeFi market performance, introducing considerable risk due to market volatility;
                    - ***LST Restaking***, involving staking of ETH already restaked via protocols like Lido or Rocket Pool. Adds a layer of complexity and dependence on third-party staking services, presenting moderate risk;
                    - ***Native Restaking***, where validators restake staked ETH directly to EigenLayer. This is the simplest and most direct form of restaking, offering the **lowest risk profile**.
                    
                    ```python
                    restaking_mods_risk = {"LST LP Restaking": 10, "ETH LP Restaking": 7, "LST Restaking": 4, "Native Restaking": 1}
                    ```
                            """)
                
            result5 = st.session_state.restaking_mod_score * restaking_mods_likelihood * restaking_mods_impact

            restaking_mod_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.restaking_mod_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{restaking_mods_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{restaking_mods_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result5}</span>
                </div>
                """

            st.markdown(restaking_mod_calc, unsafe_allow_html=True)


        with col34:

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

                st.markdown('<p class="header-style">SS Type</p>', unsafe_allow_html=True)

                avs_type = st.selectbox("", ["Lightweight", "Hyperscale"], index=1)
                
                st.write("  \n")

                avs_type_likelihood = st.slider("**Likelihood**   ", min_value=1, max_value=10, value=2)
                
                avs_type_impact = st.slider("**Impact**   ", min_value=1, max_value=10, value=5)

                with st.expander("Logic"):
                    st.markdown("""
                        In designing modules for maximal security and minimal centralization risk, EigenLayer suggests two approaches: **Hyperscale and Lightweight AVS** [(Section 3.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper).

                        **Hyperscale AVS** involves distributing the computational workload across many nodes, allowing for high overall throughput and reducing incentives for centralized validation. This horizontal scaling minimizes validation costs and amortization gains for any central operator. 

                        On the other hand, the **Lightweight** approach focuses on tasks that are redundantly performed by all operators but are inexpensive and require minimal computing infrastructure.

                        While it does depend on the needs of an AVS, the Hyperscale-type is more robust and secure due to its decentralized nature, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our simulator.                    
                        
                        ```python
                        avs_type_risk = {"Lightweight": 7, "Hyperscale": 3}
                        ```
                                """)
                
                result4 = st.session_state.avs_type_score * avs_type_likelihood * avs_type_impact

                avs_type_calc = f"""
                    <div style="text-align: center;">
                        <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.avs_type_score}</span> 
                        <span style="font-size: 24px; font-weight: bold;">&times;</span>
                        <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{avs_type_likelihood}</span> 
                        <span style="font-size: 24px; font-weight: bold;">&times;</span>
                        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{avs_type_impact}</span> 
                        <span style="font-size: 24px; font-weight: bold;"> = </span>
                        <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result4}</span>
                    </div>
                """

                st.markdown(avs_type_calc, unsafe_allow_html=True)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


        col27,col28 = st.columns(2)
        with col27:

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
            st.markdown('<p class="header-style">SS Number of Security Audits</p>', unsafe_allow_html=True)

            # Dropdown menu
            security_audits = st.number_input("", min_value=0, max_value=5, step=1)

            st.write("  \n")

            security_audits_likelihood = st.slider("**Likelihood**  ", min_value=1, max_value=10, value=4)
            security_audits_impact = st.slider("**Impact**  ", min_value=1, max_value=10, value=8)

            # The expander without a visible outline
            with st.expander("Logic"):
                st.markdown("""
                    Accounting for the **number of Security Audits** performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                    
                    While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks (and the risk of honest nodes getting slashed), and, as a result, rewards an AVS is confident to emit and Restakers and Operators to opt into it. 
                    
                    ```python
                    security_audits_risk = {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 1} # 0 security audits poses the greatest risk, 5 the least
                    ```
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
        



        with col28:

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

            st.markdown('<p class="header-style">SS Average Operators\' Reputation</p>', unsafe_allow_html=True)

            avs_avg_operator_reputation = st.selectbox("", ["Unknown", "Established", "Renowned"])

            st.write("  \n")

            avs_avg_operator_reputation_likelihood = st.slider("**Likelihood**     ", min_value=1, max_value=10, value=2)
            avs_avg_operator_reputation_impact = st.slider("**Impact**     ", min_value=1, max_value=10, value=8)

            with st.expander("Logic"):
                st.markdown("""
                    Although being a purely qualitative metric, the **Average Reputation of Operators** that the AVS chose to be opted in to validate its modules offers a useful glimpse into the AVS’s security profile. The user should consider operators’ historical slashing record and the overall validation and uptime performance, which are crucial in assessing overall operator-related risk for an AVS, including potential malicious collusions.                        
                    
                    ```python
                    avs_avg_operator_reputation_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
                    ```
                            """)
                
            result6 = st.session_state.avs_avg_operator_reputation_score * avs_avg_operator_reputation_likelihood * avs_avg_operator_reputation_impact

            avs_avg_operator_reputation_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.avs_avg_operator_reputation_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{avs_avg_operator_reputation_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{avs_avg_operator_reputation_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result6}</span>
                </div>
                """

            st.markdown(avs_avg_operator_reputation_calc, unsafe_allow_html=True)


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
                background-color: #CC8E00;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">ESPRESSO-SPECIFIC METRICS</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")



        # MEV Extraction Risk
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">MEV Extraction Risk</p>', unsafe_allow_html=True)

        mev_extraction = st.selectbox(" ", ["High", "Medium", "Low"])

        st.write("  \n")

        col18,col19 = st.columns(2)
        with col18:
            mev_extraction_likelihood = st.slider("**Likelihood**      ", min_value=1, max_value=10, value=3)
        with col19:
            mev_extraction_impact = st.slider("**Impact**      ", min_value=1, max_value=10, value=6)

        with st.expander("Logic"):
                st.markdown("""
                    The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581).
                            """)
                
        result7 = st.session_state.mev_extraction_score * mev_extraction_likelihood * mev_extraction_impact

        mev_extraction_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.mev_extraction_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{mev_extraction_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{mev_extraction_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result7}</span>
                </div>
                """

        st.markdown(mev_extraction_calc, unsafe_allow_html=True)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")





        # Liveness Degradation Risk
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">Liveness Degradation Risk</p>', unsafe_allow_html=True)

        liveness_deg = st.selectbox("   ", ["High", "Medium", "Low"])

        st.write("  \n")

        col38,col39 = st.columns(2)
        with col38:
            liveness_deg_likelihood = st.slider("**Likelihood**        ", min_value=1, max_value=10, value=3)
        with col39:
            liveness_deg_impact = st.slider("**Impact**        ", min_value=1, max_value=10, value=9)

        with st.expander("Logic"):
                st.markdown("""
                    The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581).
                    
                    "*Notably, shared sequencers are primarily exposed to three potential types of attacks, namely, MEV extraction, censorship, and liveness attacks. Among these, **liveness attacks pose the greatest threat.***" 
                    "*The main advantage of attacking a sequencer lies more in sabotage and attacking the shared sequencer liveness. An attacker could gain from discrediting a chain, leading to a drop in its transaction, a decline in the value of its native token, and an increase in the market share of competing projects.*"
                            
                    Therefore, Liveness Degradation Risk was assigned the greatest impact level out of the 4 specific metrics.      
                            """)
                
        result8 = st.session_state.liveness_deg_score * liveness_deg_likelihood * liveness_deg_impact

        liveness_deg_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.liveness_deg_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{liveness_deg_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{liveness_deg_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result8}</span>
                </div>
                """

        st.markdown(liveness_deg_calc, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")





        # Censorship Risk
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">Transaction Censorship Risk</p>', unsafe_allow_html=True)

        censorship = st.selectbox("  ", ["High", "Medium", "Low"])

        st.write("  \n")

        col14,col15 = st.columns(2)
        with col14:
            censorship_likelihood = st.slider("**Likelihood**       ", min_value=1, max_value=10, value=3)
        with col15:
            censorship_impact = st.slider("**Impact**       ", min_value=1, max_value=10, value=6)

        with st.expander("Logic"):
                st.markdown("""
                    The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581).
                            """)
                
        result9 = st.session_state.censorship_score * censorship_likelihood * censorship_impact

        censorship_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.censorship_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{censorship_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{censorship_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result9}</span>
                </div>
                """

        st.markdown(censorship_calc, unsafe_allow_html=True)



        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")





        # Validator Collusion Risk
        st.markdown("""
                <style>
                .header-style {
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 0px;  /* Adjust the space below the header */
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="header-style">Validator Collusion Risk</p>', unsafe_allow_html=True)

        validator_collusion = st.selectbox("    ", ["High", "Medium", "Low"])

        st.write("  \n")

        col42,col43 = st.columns(2)
        with col42:
            validator_collusion_likelihood = st.slider("**Likelihood**         ", min_value=1, max_value=10, value=2)
        with col43:
            validator_collusion_impact = st.slider("**Impact**         ", min_value=1, max_value=10, value=6)

        with st.expander("Logic"):
                st.markdown("""
                    The rationale behind the Impact and Likelihood default values in the sliders of this metric was taken from Nethermind's whitepaper on [*Restaking in Shared Sequencers*](https://assets.adobe.com/public/8fca5797-3914-4966-4bbe-24c1d0e10581).
                            """)
                
        result10 = st.session_state.validator_collusion_score * validator_collusion_likelihood * validator_collusion_impact

        validator_collusion_calc = f"""
                <div style="text-align: center;">
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{st.session_state.validator_collusion_score}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{validator_collusion_likelihood}</span> 
                    <span style="font-size: 24px; font-weight: bold;">&times;</span>
                    <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{validator_collusion_impact}</span> 
                    <span style="font-size: 24px; font-weight: bold;"> = </span>
                    <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">{result10}</span>
                </div>
                """

        st.markdown(validator_collusion_calc, unsafe_allow_html=True)


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


    def normalize_score(original_score, min_original=17, max_original=17700):
        normalized_score = ((original_score - min_original) / (max_original - min_original)) * 100
        return normalized_score

    final_result = result1 + result2 + result3 + result4 + result5 + result6 + result7 + result8 + result9 + result10
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
    
    
    risk_score = avs_risk(security_audits, business_model, st.session_state.dual_staking_balance, avs_type, st.session_state.operator_attack_risk, restaking_mods, avs_avg_operator_reputation, mev_extraction, liveness_deg, censorship, validator_collusion)
    (st.session_state.security_audit_score, st.session_state.business_model_score, st.session_state.dual_staking_balance, st.session_state.avs_type_score, st.session_state.restaking_mod_score, st.session_state.avs_avg_operator_reputation_score, st.session_state.operator_attack_risk, st.session_state.mev_extraction_score, st.session_state.liveness_deg_score, st.session_state.censorship_score, st.session_state.validator_collusion_score) = risk_score


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
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Centralization Risk Level</p>', unsafe_allow_html=True)
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

