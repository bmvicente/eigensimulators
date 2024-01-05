
# EigenLayer AVS Rewards


import streamlit as st


# Reward Calculation
def avs_rewards(avs_revenue, avs_tvl, avs_total_staked, avs_token_percentage, xeth_percentage, avs_type, security_audits):
    
    reward_percentage = 0.20  # Base reward percentage

    # Adjusting the base reward based on the AVS token and xETH balance
    #dual_staking_balance_adjustment = (avs_token_percentage - xeth_percentage) / 100.0

    def dual_staking_balance_adjustment(avs_token_percentage, xeth_percentage):
        ratio = avs_token_percentage / xeth_percentage

        if ratio > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
            return 0.020
        elif ratio > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
            return 0.015
        elif ratio > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.010
        elif ratio > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
            return 0.005
        elif ratio == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
            return 0  # Neutral adjustment for balanced scenario
        elif ratio > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
            return -0.010
        elif ratio > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
            return -0.015
        else:  # Very low AVS compared to ETH
            return -0.020


    dual_staking_adjustment = dual_staking_balance_adjustment(avs_token_percentage, xeth_percentage)

    # AVS type adjustment
    avs_type_adjustment = 0.02 if avs_type == "Lightweight" else -0.02

    # Check the ratio of Total Staked to TVL
    def ratio_tvl_totalstaked(avs_total_restaked, avs_tvl):
        
        if avs_tvl == 0:
            return 0
        
        ratio = (avs_total_restaked / 2) / avs_tvl

        if ratio > 2:
            return -0.03
        elif ratio > 1.5:
            return -0.02
        elif ratio > 1:
            return -0.01
        elif ratio == 1:
            return 0
        elif ratio < 1:
            return 0.01
        elif ratio < 0.5:
            return 0.02
        elif ratio < 0.25:
            return 0.03
        else:
             return 0

    ratio_tvl_totalstaked_adjustment = ratio_tvl_totalstaked(avs_total_staked, avs_tvl)


    # Revenue-based adjustment
    if avs_revenue > 100000000:  # Greater than $100M
        avs_revenue_adjustment = 0.01
    elif avs_revenue > 50000000:  # Greater than $50M
        avs_revenue_adjustment = 0.02
    elif avs_revenue > 20000000:  # Greater than $20M
        avs_revenue_adjustment = 0.03
    elif avs_revenue > 5000000:   # Greater than $5M
        avs_revenue_adjustment = 0.04
    elif avs_revenue > 1000000:   # Greater than $1M
        avs_revenue_adjustment = 0.05
    else:
        avs_revenue_adjustment = 0

    # Security audit adjustment
    def security_audit_adjustment(number_of_audits):
        if number_of_audits == 5:
            return -0.025  # Lower reward for more audits
        elif number_of_audits == 4:
            return -0.01
        elif number_of_audits == 3:
             return 0
        elif number_of_audits == 2:
            return 0.01
        elif number_of_audits == 1:
            return 0.025  # Higher reward for fewer audits
        else:
            return 0  # Neutral adjustment for moderate number of audits

    # Applying the adjustment
    audit_adjustment = security_audit_adjustment(security_audits)



    # Combine all adjustments
    reward_percentage_sum = reward_percentage + dual_staking_adjustment + avs_type_adjustment + avs_revenue_adjustment + audit_adjustment + ratio_tvl_totalstaked_adjustment

    # Ensure the reward percentage is within reasonable bounds
    reward_percentage_adj = max(min(reward_percentage_sum, 0.30), 0.10)

    # Calculate rewards for stakers and operators
    profit_percentage = 0.20
    staker_percentage = 0.40
    operator_percentage = 0.60

    staker_reward = avs_revenue * profit_percentage * reward_percentage_adj * staker_percentage
    operator_reward = avs_revenue * profit_percentage * reward_percentage_adj * operator_percentage

    return staker_reward, operator_reward


#####################################################
#####################################################
#####################################################


# Streamlit app setup
def main():
    st.set_page_config(layout="wide")

    st.image("images/eigenimage.png")

    st.title("AVS Reward Emission Simulator")

    st.write("   \n")

    with st.expander("Assumptions Made in Building our Simulator"):
        st.markdown("""
                A couple of assumptions were made in our Simulator to simplify and more easily illustrate the potential reward emission of an AVS in a ***Dual Staking*** and ***LST Restaking*** context:

                - **Dual Staking** was chosen as the business model, preferred over other models, due to the utility and security they confer to an AVS, and **Veto Dual Staking**, as the Dual Staking method, preferred over other methods, due to the low implementation cost and reliability in terms of liveness. [Learn more](https://www.blog.eigenlayer.xyz/dual-staking/)

                - **LST Restaking** was chosen as the Restaking Modality because the Dual Staking model requires a staked ETH of some kind, and also because it was simpler and more intuitive, compared to other modalities. [Learn more](https://docs.eigenlayer.xyz/overview/readme/whitepaper)

                Generally speaking, these three assumptions were made due to the safety they confer AVSs, especially new-born ones, and for simplicity's sake in a first version of the Simulator.
                    
                We recommend checking out the AVS Risk Simulator as an important introduction to understanding the AVS Reward Emission Simulator.
            """)
    
    st.write("  \n")

    # Creating two major columns
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:


        ### AVS REVENUE

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
        st.markdown('<p class="header-style">AVS Revenue ($)</p>', unsafe_allow_html=True)

        # Manual input for AVS TVL
        avs_revenue = st.number_input("", min_value=0, max_value=1000000000000, value=0, step=1000000)
        
        dist_rewards_10 = round(avs_revenue * 0.2 * 0.1)
        dist_rewards_30 = round(avs_revenue * 0.2 * 0.3)
        
            # The expander without a visible outline
        with st.expander("Logic"):
                st.markdown(f"""
                    An **AVS's Revenue**, at any given time, is a useful indicator to help assess the level of rewards an AVS might be able to emit. From the revenue inputted by the user, we assume a 20% profit for the AVS, and [10-30]% of that profit to be distributable as rewards (specific value of this range dependent on weighting of all the chosen inputs in our Simulator).

                    - Current AVS Revenue: **\${avs_revenue:,}**

                    - Total Distributable Reward Amount, if rewards = *10%* of profit: **\${dist_rewards_10:,}**

                    - Total Distributable Reward Amount, if rewards = *30%* of profit: **\${dist_rewards_30:,}**

                    Such a reward range is necessary to be calculated to account for the underlying riskiness/security of an AVS and subsequent reward emission values. 
                    We find these percentages reasonable, although would highly appreciate feedback from EigenLayer.
                """)


        #########################
        #########################
        st.write("  \n")
        st.write("  \n")


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

            # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS TVL & Total Staked</p>', unsafe_allow_html=True)

        st.write("  \n")

            # Creating two columns for input
        col3, col4 = st.columns([3, 3])

        with col3:
                # Manual input for AVS TVL
                avs_tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

        with col4:
                # Manual input for Total Restaked on AVS
                avs_total_staked = st.number_input("**AVS Total Staked - \$AVS & xETH ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

                min_tvl = avs_total_staked // 2

            # The expander without a visible outline
        with st.expander("Logic"):
                st.markdown(f"""
                    The **TVL/Total Restaked** reward logic herein is set so that the greater the *(AVS Total Staked/2) : AVS TVL* ratio, the safer the AVS is and the less rewards it should emit therefore, and vice-versa.

                    To take the simplest scenario of the single-AVS restaking by operators [(Section 3.4.1 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/readme/whitepaper) to begin with: an AVS where the amount of restaked ETH is at least double the total locked value (TVL) and a 50% quorum is required for a collusion attack to capture the TVL, the system appears secure, as any successful attack would result in at least half of the attacker's stake being slashed. If *AVS Total Restaked* increases from there compared to the *AVS TVL*, the risk/reward gets reduced even further.

                    Based on the values inputted:

                    - The **Current TVL** equals **\${avs_tvl:,}**.
                    - The **Current Total Staked (\$AVS & xETH)** equals **\${avs_total_staked:,}**;

                    Accordingly, the main goal is to maintain the *CfC (Cost from Corruption) above the PfC (Profit from Corruption)* to desincentivize colluding operators to perform an attack.

                    In a Dual Staking Model and Veto Dual Staking context such as ours increasing the [CVS (Cost to Violate Safety) and the CVL (Cost to Violate Liveness)](https://www.blog.eigenlayer.xyz/dual-staking/), calculated as ⅔ \$AVS + ⅔ xETH and ⅓ \$AVS respectively, is important to maintain the health of the AVS dual token pool (or AVS TVL, in other words).
                """)


        #########################
        #########################
        st.write("  \n")
        st.write("  \n")


        ### DUAL STAKING MODEL

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
                Following and based on the restaking modality (**LST Restaking**), business model (**Dual Staking Utility**), and dual staking method (**Veto Dual Staking**) assumptions made for our Simulator, we found it useful to set an $AVS/xETH balance scale to assess AVS risks and potential reward emissions, as well as providing an improved insight into what their token configuration should be.

                **\$AVS** is the AVS native token. **xETH** is any ETH-backed LST, such as stETH, rETH or cbETH.

                **Dual Staking**, by allowing the staking of a more stable and widely-used token like an ETH-LST alongside the AVS's native token, simplifies the bootstrapping process and provides baseline economic security, thereby mitigating these challenges.

                A greater xETH balance assures greater security and stability for the dual-token pool, whereas the opposite exposes the volatilities and likely “death spiral” problem inherent in newly-issued native AVS tokens. Therefore, a *% \$AVS* **>** *% xETH* pool balance makes sense to be a higher-reward event.
            """)
            


    with col2:

        ### AVS TYPE

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

        # Dropdown menu
        avs_type = st.selectbox("", ["Lightweight", "Hyperscale"])

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                In designing modules for maximal security and minimal centralization risk, EigenLayer suggests two approaches: **Hyperscale and Lightweight AVS** [(Section 3.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/intro/whitepaper).

                **Hyperscale AVS** involves distributing the computational workload across many nodes, allowing for high overall throughput and reducing incentives for centralized validation. This horizontal scaling minimizes validation costs and amortization gains for any central operator. 

                On the other hand, the **Lightweight** approach focuses on tasks that are redundantly performed by all operators but are inexpensive and require minimal computing infrastructure.

                While it does depend on the needs of an AVS, the Hyperscale-type is more robust and secure due to its decentralized nature, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our simulator, and thus a lower reward level is sensible to assume when selecting this category.               
                        """)
            

        
        #############################
        #############################
        st.write("  \n")
        st.write("  \n")
        

        ### SECURITY AUDITS

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

        st.write("  \n")

        # Dropdown menu
        security_audits = st.number_input("", min_value=0, max_value=5, step=1)

        # The expander without a visible outline
        with st.expander("Logic"):
            st.markdown("""
                Registering the number of security audits performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks, and thus rewards an AVS is confident to emit and restakers and operators to opt into it.
            """)



        #############################
        #############################
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")


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

            # Displaying the custom styled header
        st.markdown('<p class="header-style">$AVS Tokenomics [Optional]</p>', unsafe_allow_html=True)

        st.write("  \n")

        avs_inf_def_rate = st.slider("**$AVS Inflation/Deflation Rate**", 
                                    min_value=-50, 
                                    max_value=50, 
                                    value=0,
                                    format="%d%%")
                                    #help="Slide to set the inflation or deflation rate for $AVS token. -50% indicates deflation, 50% indicates inflation.")

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
                    Understanding this rate helps gauge how quickly new tokens are entering circulation, which can impact the token's value and hence the value of rewards. The *Circulating vs Total Supply* ratio provides a snapshot of how much of the total supply is active in the market, influencing supply-demand dynamics too.
                    
                    For \$AVS tokenomics to be considered a valuable metric in this context, one must assume token demand remains constant through time.
                """)


#########################################
#########################################
#########################################

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    # Call the function and get the rewards
    staker_reward, operator_reward = avs_rewards(avs_revenue, avs_tvl, avs_total_staked, avs_token_percentage, xeth_percentage, avs_type, security_audits)

    # Creating two columns for displaying the rewards
    col1, col2 = st.columns(2)

    with col1:
        # Calculate the percentage and handle division by zero
        if avs_total_staked != 0:
            staker_reward_percentage = (staker_reward / avs_total_staked) * 100
        else:
            staker_reward_percentage = 0.00

        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 10px 0;
                background-color: white;">
                <h2 style="color: black; margin:0; font-size: 1.5em;">$AVS Staker / xETH Restaker Reward: <span style="font-size: 1.2em;">{staker_reward_percentage:.2f}%</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

    with col2:
        # Calculate the percentage and handle division by zero
        if avs_total_staked != 0:
            operator_reward_percentage = (operator_reward / avs_total_staked) * 100
        else:
            operator_reward_percentage = 0.00

        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 10px 0;
                background-color: white;">
                <h2 style="color: black; margin:0; font-size: 1.5em;">AVS Operator Reward: <span style="font-size: 1.2em;">{operator_reward_percentage:.2f}%</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


    st.write("  \n")
    st.write("  \n")

    st.write(f"""
                The **AVS Reward Emission** simulator percentage-results suggest how much should be distributed among $AVS Stakers, xETH Restakers and AVS Operators, given the risk and economic security profile of the AVS. To build on the *Assumptions* explanation on top, this calculation is based on the correlated reward-to-risk sensitivity per variable input -- the *Logic* in each variable help understand the rationale.
                
                ***Operator Reward*** is naturally being given greater weight than the ***Staker Reward*** due to their paramount role in validating modules crucial to the well-function of an AVS.

                The \$AVS’s Tokenomics (while not included in the reward calculation) were deemed useful to include since they provide a look-ahead perspective of how the native AVS token can influence future rewards. A potential for improved rewards to be emitted in the future exists if a relatively small delta between circulating and total supply and a deflationary token rate exist. Whereas a larger delta and an inflationary token rate indicate the potential for lower rewards to be emitted in the future. 
                An important factor that should help AVS developers determine the $AVS minting rate is that of rewarding operators for their capital costs.

                It's important to bear in mind that this Simulator was built from an AVS perspective *alone*. 
             
                For a deeper dive, please visit the [source code](https://github.com/bmvicente/eigensimulators/blob/master/avsrewards/eigenavsrewards.py).
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

    
    #st.image("images/tokensight.png", width=400)

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