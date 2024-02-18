

import streamlit as st


def create_total_restaked_input():
    if 'pre_slash_total_restaked' not in st.session_state:
        st.session_state.pre_slash_total_restaked = 0

    pre_slash_total_restaked = st.number_input(
        "",
        min_value=0,
        max_value=10000000000000,
        value=st.session_state.pre_slash_total_restaked,
        step=100000000
    )

    return pre_slash_total_restaked


def create_risk_score_input(risk_score_key, label):
    if risk_score_key not in st.session_state:
        st.session_state[risk_score_key] = 0

    risk_score = st.number_input(
        label,
        min_value=0,
        max_value=100,
        value=st.session_state[risk_score_key],
        step=10
    )

    return risk_score


def calculate_slashing(pre_slash_total_restaked, risk_score):
    if risk_score == 100:
        risk_factor = (90 + 10)  
    else:
        risk_factor = (risk_score + 10)

    slashing_amount = (pre_slash_total_restaked / 3) * (risk_factor / 100)
    return slashing_amount


#################################


def main():

    st.set_page_config(layout="wide")

    st.image("images/renzo1.png", width=450)

    if 'operator_stake' not in st.session_state:
        st.session_state.operator_stake = 0

    if 'pre_slash_total_restaked' not in st.session_state:
        st.session_state.pre_slash_total_restaked = 0

    if 'risk_score1' not in st.session_state:
        st.session_state.risk_score1 = 0  
    if 'risk_score2' not in st.session_state:
        st.session_state.risk_score2 = 0  
    if 'risk_score3' not in st.session_state:
        st.session_state.risk_score3 = 0 


    pre_slash_total_restaked = st.session_state.pre_slash_total_restaked
    

    st.write("  \n")

    st.title("Cryptoeconomic Risk Analysis III")
    st.subheader("**Malicious Operator → AVS Slashing Event Simulator:** *Naïve & STAKESURE Approaches*")
    
    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
                    Explain Strong cryptoeconomic security vs cryptoeconomic security:
                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property. This is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security. A core idea of EigenLayer is to provision cryptoeconomic security
                    through various slashing mechanisms which levy a high cost of corruption.

                    Eigenlayer is going to manage situations where a few AVSs simultaneously take out insurances, and then a cascading effect is induced by some unexpected event, like a security breach. This could significantly reduce the shared security pool all at once

                    The main goal of the Simulator is to demonstrate how the Risk Profile of AVSs may influence the potential slashing an Operator may face, and how such a slash to the Operator would, in turn, affect the AVSs individually.

                    This Simulator deep dives on both these topics:

                    - **Cryptoeconomic Safety**: CoC > PfC

                    - **Strong Cryptoeconomic Safety**: No honest user of the system suffers any loss of funds.

                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property. 
                    This is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security.
                    A core idea of EigenLayer is to provision cryptoeconomic security through various slashing mechanisms which levy a high cost of corruption.
                    
                    We begin by assuming that the 3 AVS herein are equally secured by the Total Amount Restaked, therefore each has 33.33% "distribution".

                    **Context of EigenLayer**: EigenLayer is a blockchain protocol that allows for the re-staking of Ethereum (ETH) to secure multiple protocols. This re-staking introduces a layer of complexity when it comes to quantifying risks, as the security and value of the re-staked ETH are interdependent with the performance and security of the protocols it is securing.
                    
                    **Max-Loss Risk in Slashing**:
                    - The max-loss risk refers to the worst-case scenario of loss due to slashing. In the context of EigenLayer, this could mean evaluating the potential total loss a validator might face if their entire staked ETH is slashed due to violations or breaches of protocol rules.
                    - The article discusses how slashing increases the cost-of-corruption for attackers, indicating that the risk of max-loss is a significant deterrent against malicious behavior. However, it doesn't provide a formula or method to directly quantify this max-loss risk in a multi-protocol staking environment like EigenLayer.
                    
                    3. **Intermediate-Loss Risk in Slashing**:
                    - Intermediate-loss risk refers to partial losses that might occur due to less severe violations or smaller scale breaches of protocol rules.
                    - The article implies that slashing can be variable based on the severity of the offense, which is pertinent to understanding intermediate-loss risks. However, it doesn't delve into specific mechanisms or quantifications for these types of risks, especially not in the complex setting of a protocol like EigenLayer where staked assets are used across multiple protocols.
                    """)
    


    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    if 'tvl1' not in st.session_state:
            st.session_state.tvl1 = 0
    if 'tvl2' not in st.session_state:
            st.session_state.tvl2 = 0
    if 'tvl3' not in st.session_state:
            st.session_state.tvl3 = 0

    if 'pre_slash_pfc' not in st.session_state:
            st.session_state.pre_slash_pfc = 0
    if 'post_slash_pfc' not in st.session_state:
            st.session_state.post_slash_pfc = 0

    if 'pre_slash_coc' not in st.session_state:
        st.session_state.pre_slash_coc = 0
    if 'post_slash_coc' not in st.session_state:
        st.session_state.post_slash_coc = 0

    if 'op_stake_slashable' not in st.session_state:
        st.session_state.op_stake_slashable = 0
    
    if 'post_slash_total_restaked' not in st.session_state:
        st.session_state.post_slash_total_restaked = 0
    
    if 'avs1_category' not in st.session_state:
        st.session_state.avs1_category = "Data Availability Layer"  
    if 'avs2_category' not in st.session_state:
        st.session_state.avs2_category = "Data Availability Layer"  
    if 'avs3_category' not in st.session_state:
        st.session_state.avs3_category = "Data Availability Layer"
        
    if 'pre_slash_max_slash_allowed' not in st.session_state:
        st.session_state.pre_slash_max_slash_allowed = 0
    

    st.session_state.pre_slash_coc = st.session_state.pre_slash_total_restaked / 3

    pre_slash_max_slash_allowed = st.session_state.pre_slash_coc - st.session_state.pre_slash_pfc

    actual_slash_on_cs = max(0, st.session_state.pre_slash_coc - st.session_state.post_slash_coc)

    st.session_state.pos_neg_actual_slash_on_c = st.session_state.pre_slash_coc - st.session_state.post_slash_coc



##########################################


    col20,col21 = st.columns(2, gap="medium")

    # For Actual Slash on Cryptoeconomic Security
    if pre_slash_max_slash_allowed >= 0:
        if actual_slash_on_cs < pre_slash_max_slash_allowed:
            actual_slash_on_cs_color = "#90EE90"  # light green
        elif actual_slash_on_cs == 0:
            actual_slash_on_cs_color = "#FFFFFF"
        else:
            actual_slash_on_cs_color = "#FFC0CB"  # pink
    else:
        if actual_slash_on_cs > pre_slash_max_slash_allowed:
            actual_slash_on_cs_color = "#ff6666"  # red
        else:
            actual_slash_on_cs_color = "#FFC0CB"  # pink






    ###############################
    ########## PRE-SLASH ##########
    ###############################

    with col20:
        st.markdown('<p class="header-style" style="font-size: 20px;">PRE-SLASH (t)</p>', unsafe_allow_html=True)

        st.write("\n")

        st.markdown('<p class="header-style" style="font-size: 18px;">Total Amount Restaked on AVS Ecosystem (Tt)</p>', unsafe_allow_html=True)

        st.session_state.pre_slash_total_restaked = create_total_restaked_input()
        formatted_value = "${:,.0f}".format(st.session_state.pre_slash_total_restaked)
        
        st.write(f"""&#8226; Total Restaked: {formatted_value}""")
        
        if st.session_state.pre_slash_total_restaked >= 10000000000:  # 10 billion
            st.markdown(f'<span style="color: red; font-weight: bold">Even though the conditions for cryptoeconomic security may not be satisfied, a large enough amount of stake is a strong determinant of the security and liveness of a PoS blockchain, to the point where no adversarial attack is warranted.</span>', unsafe_allow_html=True)
        
        col24,col25 = st.columns(2)
        with col24:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        Cost of Corruption<span style="font-size: 0.9em; font-weight: normal;"> (Tt / 3)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.pre_slash_coc:,.0f}</span>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
        with col25:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        Profit from Corruption<span style="font-size: 0.9em; font-weight: normal;"> (&Sigma; TVL<sub>j</sub>)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.pre_slash_pfc:,.0f}</span>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )



        if pre_slash_max_slash_allowed >= 0:
            background_color = "#90EE90"  # light green for positive allowed loss
            max_slash_allowed_text = "Max Total Stake-Loss \"Allowed\" To Still Maintain Cryptoeconomic Security"
        else:
            background_color = "#ff9999"  # red for a negative allowed loss, indicating an insecure condition
            max_slash_allowed_text = "Ecosystem Already in an Insecure and Compromisable Cryptoeconomic Position of"

        
        display_text = f"""
                        <div style="
                            border: 2px solid;
                            border-radius: 2px;
                            padding: 5px;
                            text-align: center;
                            margin: 5px 0;
                            background-color: {background_color};">
                            <h2 style="color: black; margin: 0; font-size: 1.1em;">
                                <div style="display: block;">
                                    <span style="font-size: 1.3em;">α<sub style="font-size: 0.8em;">jt</sub></span> &nbsp; | &nbsp;
                                    {max_slash_allowed_text}: <span style="font-size: 1.1em;">${abs(pre_slash_max_slash_allowed):,.0f}</span>
                                    <br>
                                    <span style="font-size: 16px; font-weight: normal;">(CoC t - PfC t)</span>
                                </div>
                            </h2>
                        </div>
                        """

        st.markdown(display_text, unsafe_allow_html=True)






    ################################
    ########## POST-SLASH ##########
    ###############################

    with col21:
        st.markdown('<p class="header-style" style="font-size: 20px;">POST-SLASH (t+1)</p>', unsafe_allow_html=True)

        st.session_state.post_slash_total_restaked = max(0, pre_slash_total_restaked - st.session_state.op_stake_slashable)

        st.session_state.post_slash_coc = st.session_state.post_slash_total_restaked / 3

        st.write("\n")

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 44px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0; font-size: 1.1em;">
                    Total Amount Restaked on AVS Ecosystem <span style="font-weight: normal;">(T t+1)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.post_slash_total_restaked:,.0f}</span>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


        col27,col28 = st.columns(2)
        with col27:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        Cost of Corruption<span style="font-size: 0.9em; font-weight: normal;"> (Tt+1 / 3)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.post_slash_coc:,.0f}</span>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col28:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        Profit from Corruption<span style="font-size: 0.9em; font-weight: normal;"> (&Sigma; TVL<sub>j</sub>)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.pre_slash_pfc:,.0f}</span>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: {actual_slash_on_cs_color};">
                <h2 style="color: black; margin: 0; font-size: 1.1em;">
                    <div style="display: block;">
                        <span style="font-size: 1.3em;">δ<sub style="font-size: 0.8em;">ijt+1</sub></span> &nbsp; | &nbsp;
                        Actual Slash on Cryptoeconomic Security: <span style="font-size: 1.1em;">${actual_slash_on_cs:,.0f}</span>
                        <br>
                        <span style="font-size: 16px; font-weight: normal;">(Since PfC remains unchanged post-slash, the de facto cryptoeconomic slash = CoC t - CoC t+1. More on Logic below.)</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

            
    st.write("\n")
    st.write("\n")








    ###################
    ####### BST #######
    ###################

    def evaluate_allowed_vs_actual(actual_slash_on_cs_color):
        if actual_slash_on_cs_color == "#90EE90":  # light green or white
            return 1.00
        elif actual_slash_on_cs_color == "#FFFFFF":
             return 1.10
        elif actual_slash_on_cs_color == "#FFC0CB" or actual_slash_on_cs_color == "#ff6666":  # pink or light red
            return 1.50
        
        
    evaluation_result = evaluate_allowed_vs_actual(actual_slash_on_cs_color)

    bst = pre_slash_max_slash_allowed - actual_slash_on_cs

    formula_end = ""

    if evaluation_result == 1.00:
        formula_end = "> 0"  # For conditions leading to a 1.00 evaluation result
        if bst >= 0:
            color = "#388e3c"  # Green color for positive or zero value
            background_color = "#ebf5eb"  # Light green background
        else:
            color = "#d32f2f"  # Red color for negative value
            background_color = "#fde0dc"  # Light red background
    elif evaluation_result == 1.10:
        formula_end = "= 0"  # For conditions leading to a 1.50 evaluation result
        color = "#000000"  # Light red, considering it a more critical condition
        background_color = "#FFFFFF"  # white background
    elif evaluation_result == 1.50:
        formula_end = "< 0"  # For conditions leading to a 1.50 evaluation result
        color = "#ff6666"  # Light red, considering it a more critical condition
        background_color = "#FFC0CB"  # Pinkish light red background


    st.markdown(
        f"""
            <div style="padding: 5px 10px 15px; text-align: center; margin: 5px 0; background-color: {background_color}; border: 2px solid {color}; border-radius: 5px; display: flex; flex-direction: column; align-items: center;">
                <h2 style="color: black; margin: 0; padding-bottom: 3px; font-size: 20px; font-weight: bold; line-height: 1.1;">
                    POST-SLASH Aftermath: BYZANTINE <i>SLASHING</i> TOLERANCE (BST) TEST
                </h2>
                <span style="font-weight: bold; font-size: 26px; margin-top: 3px;">
                    &beta;<sub style="font-size: 16px;">ijt</sub> = 
                    &alpha;<sub style="font-size: 16px;">jt</sub> - 
                    δ<sub style="font-size: 16px;">ijt+1</sub>
                    {formula_end}
                </span>
            </div>
        """, 
        unsafe_allow_html=True
    )

    st.write("\n")

    with st.expander("Logic"):
                st.markdown(f"""
                        - **Pre-Slash** (t): In the same way the calculation for the *AVS <> Non-Malicious Operator: Naive Approach* Simulator was done, the Naive Analysis here was applied to CoC = Stake / 3 and PfC = Σ TVL.

                        - **Post-Slash** (t+1): What changes post-slashing event is the amount of the Operator's Stake that has been slashed, how it affects the Total Stake Amount and everything that comes after it: the slash in CoC, the status of cryptoeconomic security, the impact on AVS, etc.. 
                            Naturally, the Total Amount Staked Post-Slash (Tt+1) is given by *Tt - Slashed Operator Stake*. PfC post-slash should stay the same as the slash should have no impact on the AVSs' TVL. As a result, **Actual Slash on Cryptoeconomic Security** (δ) is given by the CoC amount pre-slash subtracted by the CoC post-slash.

                        - **BST test** (β): As introduced in the previous Simulator, the Byzantine Slashing Tolerance test assesses the Cryptoeconomic Security of the AVS ecosystem, post Operator Slash or Stake-Loss event. The network is in a secure cryptoeconomic position if the **Max Total Stake-Loss "Allowed" To Still Maintain Cryptoeconomic Security** is bigger than the **Actual Slash Effected on Cryptoeconomic Security**, and in an insecure position if the opposite is true. Therefore, the ecosystem has failed this test if β < 0, and passed if β > 0
                        
                        At the end of the simulator, we introduce the **STAKESURE staking insurance mechanism** to illustrate how this situation might be reverted.
                            """)




    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    def evaluate_service_categories(avs1_category, avs2_category, avs3_category):
        categories = [avs1_category, avs2_category, avs3_category]
        unique_categories = len(set(categories))

        if unique_categories == 1:
            return 1.50
        elif unique_categories == 2:
            return 1.25
        elif unique_categories == 3:
            return 1.10
        else:
            return 1.00

    categories_evaluation_result = evaluate_service_categories(
        st.session_state.avs1_category,
        st.session_state.avs2_category,
        st.session_state.avs3_category
    

    )
    allowed_vs_actual_evaluation_result = evaluate_allowed_vs_actual(
        actual_slash_on_cs_color
    )


    def categorize_risk(risk_score):
        if risk_score < 33:
            return 'low_risk'
        elif 33 <= risk_score <= 66:
            return 'medium_risk'
        else:
            return 'high_risk'
    
    risk_numeric = {
        'low_risk': 1.00,
        'medium_risk': 1.05,
        'high_risk': 1.10}

    def individual_risk_evaluation(risk_score):
        category = categorize_risk(risk_score)
        return risk_numeric[category]
    
    def collective_risk_adjustment(risk_category1, risk_category2, risk_category3):
        categories = [risk_category1, risk_category2, risk_category3]
        high_risk_count = categories.count('high_risk')
        medium_risk_count = categories.count('medium_risk')
        low_risk_count = categories.count('low_risk')

        if high_risk_count == 3:
            adjustment = 1.50
        elif high_risk_count == 2 and medium_risk_count == 1:
            adjustment = 0.90
        elif high_risk_count == 2 and low_risk_count == 1:
            adjustment = 0.75
        elif high_risk_count == 1 and medium_risk_count == 1 and low_risk_count == 1:
            adjustment = 0.60
        elif medium_risk_count == 3:
            adjustment = 0.45
        elif medium_risk_count == 2 and low_risk_count == 1:
            adjustment = 0.35
        elif high_risk_count == 1 and low_risk_count == 2:
            adjustment = 0.325
        elif medium_risk_count == 1 and low_risk_count == 2:
            adjustment = 0.25
        elif low_risk_count == 3:
            adjustment = 0.20
        else:
            adjustment = 0

        return adjustment

    risk_category1 = categorize_risk(st.session_state.risk_score1)
    risk_category2 = categorize_risk(st.session_state.risk_score2)
    risk_category3 = categorize_risk(st.session_state.risk_score3)

    collective_adjustment = collective_risk_adjustment(risk_category1, risk_category2, risk_category3)

    risk_evaluation1 = risk_numeric[risk_category1] + collective_adjustment
    risk_evaluation2 = risk_numeric[risk_category2] + collective_adjustment
    risk_evaluation3 = risk_numeric[risk_category3] + collective_adjustment

    avs1_compounded_loss = actual_slash_on_cs * risk_evaluation1 * categories_evaluation_result * allowed_vs_actual_evaluation_result
    avs2_compounded_loss = actual_slash_on_cs * risk_evaluation2 * categories_evaluation_result * allowed_vs_actual_evaluation_result
    avs3_compounded_loss = actual_slash_on_cs * risk_evaluation3 * categories_evaluation_result * allowed_vs_actual_evaluation_result

    col1, col2 = st.columns([1, 1], gap="large")







    ##########################################
    ################ OPERATOR ################
    ##########################################

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
                background-color: #28a745;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">OPERATOR</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")


        st.markdown('<p class="header-style">Operator Amount Staked (Si)</p>', unsafe_allow_html=True)

        if isinstance(st.session_state.operator_stake, tuple):
                operator_stake = st.number_input("", min_value=0, max_value=1000000000000, value=int(st.session_state.operator_stake[0]), step=10000000)
        else:
                operator_stake = st.number_input("", min_value=0, max_value=1000000000000, value=int(st.session_state.operator_stake), step=10000000)

        formatted_operator_stake = "${:,.0f}".format(operator_stake)

        st.write(f"""&#8226; Operator Stake: {formatted_operator_stake}""")


        st.write("\n")
        st.write("\n")
        st.write("\n")

        st.session_state.operator_stake = operator_stake

        st.write("\n")
        st.write("\n")

        
        st.markdown('<p class="header-style">Operator Stake % To Be Slashed</p>', unsafe_allow_html=True)

        op_stake_perc_slashable = st.slider('', min_value=0, max_value=100, value=100, format='%d%%')

        st.session_state.op_stake_slashable = operator_stake * op_stake_perc_slashable * 0.01
        
        st.write(f"""• Slashed Operator Stake Amount: **${st.session_state.op_stake_slashable:,.0f}**""")

        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
                        The default slash for a malicious Operator attack is usually 100% of the Operator's Stake (and proxied Restakers). Naturally, this slash directly affects the Total Amount Staked.
                        """)
        
        st.write("\n")
        st.write("\n")









    #############################################
    ################### AVSs ####################
    #############################################


    with col1:

        custom_css = """
            <style>
            .header-style {
                font-size: 18px; /* Existing font size */
                font-weight: bold;
            }

            .large-header-style {
                font-size: 24px; /* Larger font size */
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
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: #28a745;"> <!-- Green background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">AVS ECOSYSTEM</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("\n")




        #############################################
        ################### AVS 1 ###################
        #############################################
        

        st.markdown('<p class="header-style">AVS 1</p>', unsafe_allow_html=True)

        st.write("  \n")

        st.session_state.avs1_category = st.selectbox("**AVS Category**", ["Data Availability Layer", "Decentralized Sequencer", "Oracle"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avs1_category_key")
        
        st.write("  \n")

        col3, col4 = st.columns([3, 3])

        with col3:
                st.session_state.risk_score1 = create_risk_score_input('risk_score1', "**AVS Risk Score**")
                
                st.write("  \n")
                st.write("  \n")
                st.write("\n")

                def get_display_text(pre_slash_max_slash_allowed):
                    max_slash_allowed_text = "Max Total Stake-Loss \"Allowed\" To Still Maintain Cryptoeconomic Security" if pre_slash_max_slash_allowed >= 0 else "AVS Ecosystem Already in an Insecure and Compromisable Cryptoeconomic Position of"
                    return f"""
                        <div style="
                            border: 1px solid;
                            border-radius: 2px;
                            padding: 5px;
                            text-align: center;
                            margin: 5px 0;
                            background-color: white;">
                            <h2 style="color: black; margin: 0; font-size: 1.1em;">
                                <div style="display: block; margin-bottom: 10px;">
                                    <span style="font-size: 1.2em;">α<sub style="font-size: 0.8em;">AVS1 t</sub></span>
                                </div>
                                <div style="display: block;">
                                    {max_slash_allowed_text}: <span style="font-size: 1.1em;">${abs(pre_slash_max_slash_allowed):,.0f}</span>
                                </div>
                            </h2>
                        </div>
                        """


                display_text = get_display_text(pre_slash_max_slash_allowed)
                st.markdown(display_text, unsafe_allow_html=True)




        with col4:
                tvl1 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=st.session_state.tvl1, step=10000000,
                                              help=f"""TVL was included to establish the CoC vs PfC threshold and calculate the "allowed" slashing amount to still maintain AVS security.""")

                formatted_tvl1 = "${:,.0f}".format(tvl1)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl1}""")
                
                st.write("\n")

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 11px;
                        text-align: center;
                        margin: 5px 0;
                        background-color: white;">
                        <h2 style="color: black; margin: 0; font-size: 1.1em;">
                            <div style="display: block;">
                                <span style="font-size: 1.2em;">δ<sub style="font-size: 0.8em;">iAVS1 t+1</sub></span>
                            </div>
                            <div style="display: block; margin-top: 10px;"> <!-- Increased margin-top for more space -->
                                Actual Slash on Cryptoeconomic Security AVS1: <span style="font-size: 1.1em;">${actual_slash_on_cs:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        
        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0; font-size: 1.1em;">
                    <div style="display: block;">
                        <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS1</sub></span>
                    </div>
                    <div style="display: block; margin-top: 10px;">
                    AVS1 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.2em;">${avs1_compounded_loss:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("\n")

        avs1_compounded_loss_calc = f"""
        <div style="text-align: center;">
            <span style="font-size: 22px; font-weight: bold; background-color: orange; border-radius: 10px; padding: 5px; margin: 2px;">${actual_slash_on_cs:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation1:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs1_compounded_loss:,.0f}</span>
            <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 16px; font-weight: bold;">(Actual Slash on C.S. * Category * Risk Score * BST Status (β) = AVS1 Total Compounded Stake-Loss)</span>
        </div>
        """

        st.markdown(avs1_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")


        with st.expander("Logic"):
            st.markdown("""
                        AVSs are more prone to compounded risks if their Risk Profiles are equally high, if they are being secured by a common operator, if they belong to the same category of AVS, and the status of the overall BST test. Those were the 3 main metrics taken into account right now.

                        ```python
                        # Individual Risk Profiles
                        def categorize_risk(risk_score):
                            if risk_score < 33:
                                return 'low_risk'
                            elif 33 <= risk_score <= 66:
                                return 'medium_risk'
                            else:
                                return 'high_risk'

                        def collective_risk_adjustment(risk_category1, risk_category2, risk_category3):
                            ...

                            if high_risk_count == 3: # All 3 AVSs have Risk Scores higher than 66
                                adjustment = 1.50
                            elif high_risk_count == 2 and medium_risk_count == 1:
                                adjustment = 0.90
                            elif high_risk_count == 2 and low_risk_count == 1:
                                adjustment = 0.75
                            elif high_risk_count == 1 and medium_risk_count == 1 and low_risk_count == 1:
                                adjustment = 0.60
                            elif medium_risk_count == 3:
                                adjustment = 0.45
                            elif medium_risk_count == 2 and low_risk_count == 1:
                                adjustment = 0.35
                            elif high_risk_count == 1 and low_risk_count == 2:
                                adjustment = 0.325
                            elif medium_risk_count == 1 and low_risk_count == 2:
                                adjustment = 0.25
                            elif low_risk_count == 3: # All 3 AVSs have Risk Scores lower than 33
                                adjustment = 0.20
                            else:
                                adjustment = 0

                        # Category
                        def evaluate_service_categories(avs1_category, avs2_category, avs3_category):
                            categories = [avs1_category, avs2_category, avs3_category]
                            unique_categories = len(set(categories))

                            if unique_categories == 1: # Same category for all AVs
                                return 1.50
                            elif unique_categories == 2:
                                return 1.25
                            elif unique_categories == 3: # Different categories for all AVSs
                                return 1.10
                            else:
                                return 1.00
                        
                        # BST test
                        def evaluate_allowed_vs_actual(actual_slash_on_cs_color):
                            if actual_slash_on_cs_color == "#90EE90":  # Light Green or White
                                return 1.00
                            elif actual_slash_on_cs_color == "#FFFFFF":
                                return 1.10
                            elif actual_slash_on_cs_color == "#FFC0CB" or actual_slash_on_cs_color == "#ff6666":  # Pink or Light Red
                                return 1.50
                        ```
                        """)


        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")








        ##############################################
        ################### AVS 2 ####################
        ##############################################

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

        st.markdown('<p class="header-style">AVS 2</p>', unsafe_allow_html=True)
        
        st.write("  \n")

        st.session_state.avs2_category = st.selectbox("**AVS Category** ", ["Data Availability Layer", "Decentralized Sequencer", "Oracle"], key="avs2_category_key")

        st.write("  \n")

        col8, col9 = st.columns([3, 3])

        with col8:
                st.session_state.risk_score2 = create_risk_score_input('risk_score2', "**AVS Risk Score** ")

                st.write("  \n")
                st.write("  \n")
                st.write("  \n")

                def get_display_text(pre_slash_max_slash_allowed):
                    max_slash_allowed_text = "Max Total Stake-Loss \"Allowed\" To Still Maintain Cryptoeconomic Security" if pre_slash_max_slash_allowed >= 0 else "AVS Ecosystem Already in an Insecure and Compromisable Cryptoeconomic Position of"
                    return f"""
                        <div style="
                            border: 1px solid;
                            border-radius: 2px;
                            padding: 5px;
                            text-align: center;
                            margin: 5px 0;
                            background-color: white;">
                            <h2 style="color: black; margin: 0; font-size: 1.1em;">
                                <div style="display: block; margin-bottom: 10px;">
                                    <span style="font-size: 1.2em;">α<sub style="font-size: 0.8em;">AVS2 t</sub></span>
                                </div>
                                <div style="display: block;">
                                    {max_slash_allowed_text}: <span style="font-size: 1.1em;">${abs(pre_slash_max_slash_allowed):,.0f}</span>
                                </div>
                            </h2>
                        </div>
                        """


                display_text = get_display_text(pre_slash_max_slash_allowed)
                st.markdown(display_text, unsafe_allow_html=True)

        with col9:
                tvl2 = st.number_input("**AVS TVL** ", min_value=0, max_value=10000000000000, value=st.session_state.tvl2, step=10000000)

                formatted_tvl2 = "${:,.0f}".format(tvl2)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl2}""")
                
                st.write("  \n")

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 11px;
                        text-align: center;
                        margin: 5px 0;
                        background-color: white;">
                        <h2 style="color: black; margin: 0; font-size: 1.1em;">
                            <div style="display: block;">
                                <span style="font-size: 1.2em;">δ<sub style="font-size: 0.8em;">iAVS2 t+1</sub></span>
                            </div>
                            <div style="display: block; margin-top: 10px;"> <!-- Increased margin-top for more space -->
                                Actual Slash on Cryptoeconomic Security AVS2: <span style="font-size: 1.1em;">${actual_slash_on_cs:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        
        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0; font-size: 1.1em;">
                    <div style="display: block;">
                        <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS2</sub></span>
                    </div>
                    <div style="display: block; margin-top: 5px;">
                        AVS2 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs2_compounded_loss:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")

        avs2_compounded_loss_calc = f"""
        <div style="text-align: center;">
            <span style="font-size: 22px; font-weight: bold; background-color: orange; border-radius: 10px; padding: 5px; margin: 2px;">${actual_slash_on_cs:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation2:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs2_compounded_loss:,.0f}</span>
        </div>
        """

        # Displaying the markdown in Streamlit
        st.markdown(avs2_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")

    
        with st.expander("Logic"):
            st.markdown("""
                AVSs are more prone to compounded risks if their risk profiles are equally high, if they are being secured by a common operator, and if they belong to the same category of AVS.
                """)
        
        
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")
        st.write("  \n")








        #############################################
        ################### AVS 3 ###################
        #############################################

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

        st.markdown('<p class="header-style">AVS 3</p>', unsafe_allow_html=True)
        
        st.write("  \n")

        st.session_state.avs3_category = st.selectbox("**AVS Category**  ", ["Data Availability Layer", "Decentralized Sequencer", "Oracle"], key="avs3_category_key")

        st.write("  \n")

        col13, col14 = st.columns([3, 3])

        with col13:
                st.session_state.risk_score3 = create_risk_score_input('risk_score3', "**AVS Risk Score**  ")
                
                st.write("  \n")
                st.write("  \n")
                st.write("  \n")

                def get_display_text(pre_slash_max_slash_allowed):
                    max_slash_allowed_text = "Max Total Stake-Loss \"Allowed\" To Still Maintain Cryptoeconomic Security" if pre_slash_max_slash_allowed >= 0 else "AVS Ecosystem Already in an Insecure and Compromisable Cryptoeconomic Position of"
                    return f"""
                        <div style="
                            border: 1px solid;
                            border-radius: 2px;
                            padding: 5px;
                            text-align: center;
                            margin: 5px 0;
                            background-color: white;">
                            <h2 style="color: black; margin: 0; font-size: 1.1em;">
                                <div style="display: block; margin-bottom: 10px;">
                                    <span style="font-size: 1.2em;">α<sub style="font-size: 0.8em;">AVS3 t</sub></span>
                                </div>
                                <div style="display: block;">
                                    {max_slash_allowed_text}: <span style="font-size: 1.1em;">${abs(pre_slash_max_slash_allowed):,.0f}</span>
                                </div>
                            </h2>
                        </div>
                        """


                display_text = get_display_text(pre_slash_max_slash_allowed)
                st.markdown(display_text, unsafe_allow_html=True)

        with col14:
                tvl3 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=st.session_state.tvl3, step=10000000)
                formatted_tvl3 = "${:,.0f}".format(tvl3)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl3}""")

                st.write("  \n")

                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 11px;
                        text-align: center;
                        margin: 5px 0;
                        background-color: white;">
                        <h2 style="color: black; margin: 0; font-size: 1.1em;">
                            <div style="display: block;">
                                <span style="font-size: 1.2em;">δ<sub style="font-size: 0.8em;">iAVS3 t+1</sub></span>
                            </div>
                            <div style="display: block; margin-top: 10px;"> <!-- Increased margin-top for more space -->
                                Actual Slash on Cryptoeconomic Security AVS3: <span style="font-size: 1.1em;">${actual_slash_on_cs:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        
        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0; font-size: 1.1em;">
                    <div style="display: block;">
                        <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS3</sub></span>
                    </div>
                    <div style="display: block; margin-top: 5px;">
                        AVS3 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs3_compounded_loss:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")

        avs3_compounded_loss_calc = f"""
            <div style="text-align: center;">
                <span style="font-size: 22px; font-weight: bold; background-color: orange; border-radius: 10px; padding: 5px; margin: 2px;">${actual_slash_on_cs:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation3:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;"> = </span>
                <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs3_compounded_loss:,.0f}</span>
            </div>
            """

        st.markdown(avs3_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")
    

        with st.expander("Logic"):
            st.markdown("""
                AVSs are more prone to compounded risks if their risk profiles are equally high, if they are being secured by a common operator, and if they belong to the same category of AVS.
                """)


    st.session_state.pre_slash_pfc = tvl1 + tvl2 + tvl3

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








    ###########################
    ######## STAKESURE ########
    ###########################


    st.subheader("**Malicious Operator → AVS Slashing Event Simulator:** *STAKESURE Approach* (Attributable Security)")
    
    st.write("  \n")

    if 'existing_reserve' not in st.session_state:
        st.session_state['existing_reserve'] = 0

    if 'op_stake_slashable' not in st.session_state:
        st.session_state['op_stake_slashable'] = 0


    existing_reserve = st.number_input("**STAKESURE Insurance Amount Already in Reserve**", min_value=0,
                                        max_value=100000000000, value=0, step=10000000,
                                        key='existing_reserve_key')
    

    st.write(f"""• STAKESURE Amount in Reserve: ${existing_reserve:,.0f}""")

    st.write("  \n")
    st.write("  \n")


    total_stake_losses = avs1_compounded_loss + avs2_compounded_loss + avs3_compounded_loss

    stakesure_insurance_reserve = existing_reserve + st.session_state.op_stake_slashable / 2

    stake_losses_coverage = stakesure_insurance_reserve - total_stake_losses
        

    background_color = "#3CB371" if stake_losses_coverage >= 0 else "#ff6666"  # green for enough, red for not enough
    message = "(Enough to Cover Stake Losses)" if stake_losses_coverage >= 0 else "(Not Enough to Cover Stake Losses)"

    st.markdown(
            f"""
            <div style="
                border: 3px solid;
                border-radius: 5px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: {background_color};">
                <h2 style="color: black; margin: 0; font-size: 1.4em;">
                    <div style="display: block; margin-top: 5px;">
                    <span style="font-size: 1.1em;"><i>STAKESURE</i></span>: Existing Insurance Reserve + Amount from Operator Slashed Funds <span style="font-size: 0.8em;">(Operator Slashed Amount / 2)</span> = $<span style="font-size: 1.1em;">{stakesure_insurance_reserve:,.0f}</span>
                        <br><span style="font-size: 18px; font-weight: bold;">{message}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.write("  \n")

    stakesure_calc = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold; ">STAKESURE Insurance Available = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: orange; border-radius: 10px; padding: 5px; margin: 2px;">${existing_reserve:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">+</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.op_stake_slashable:,.0f}</span> 
        <span style="font-size: 22px; font-weight: bold;">/ 2</span> 
        <span style="font-size: 24px; font-weight: bold;"> = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">${(stakesure_insurance_reserve):,.0f}</span>
    </div>
    """
    st.markdown(stakesure_calc, unsafe_allow_html=True)



    st.write("  \n")
    st.write("  \n")


    if 'insurance_statuses' not in st.session_state:
            st.session_state.insurance_statuses = {
                'avs1_insurance_status': None,
                'avs2_insurance_status': None,
                'avs3_insurance_status': None
            }

    col50, col51, col52 = st.columns(3)

    def create_insurance_status_selectbox(column, options, key):
            selected_status = column.selectbox("Insurance Status", options, key=key)
            return selected_status

    def display_insurance_status_selectbox(avs_insurance_status, options, key):
            selected_status = st.selectbox(
                "**Insurance Status**", 
                options, 
                index=options.index(avs_insurance_status) if avs_insurance_status in options else 0,
                key=key
            )
            return selected_status

    insurance_options = ["Bought Appropriate Amount of Insurance", "Bought Inappropriate Amount of Insurance", "Didn't Buy Insurance"]

    with col50: 
            background_color1 = "#90EE90" if st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[0] else "#FFFFE0" if st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[1] else "#FF9999"
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 3px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: {background_color1};">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-size: 1.2em;">Ψ<sub style="font-size: 0.9em;">AVS1</sub></span>
                        </div>
                        <div style="display: block; margin-top: 5px;">
                            AVS1 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs1_compounded_loss:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.write("  \n")

            avs1_insurance_status_temp = create_insurance_status_selectbox(col50, insurance_options, "avs1_insurance_status")


    with col51:
            background_color2 = "#90EE90" if st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[0] else "#FFFFE0" if st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[1] else "#FF9999"
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 3px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: {background_color2};">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-size: 1.2em;">Ψ<sub style="font-size: 0.9em;">AVS2</sub></span>
                        </div>
                        <div style="display: block; margin-top: 5px;">
                            AVS2 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs2_compounded_loss:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            st.write("  \n")

            avs2_insurance_status_temp = create_insurance_status_selectbox(col51, insurance_options, "avs2_insurance_status")


    with col52:
            background_color3 = "#90EE90" if st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[0] else "#FFFFE0" if st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[1] else "#FF9999"
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 3px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: {background_color3};">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-size: 1.2em;">Ψ<sub style="font-size: 0.9em;">AVS3</sub></span>
                        </div>
                        <div style="display: block; margin-top: 5px;">
                            AVS3 Total Compounded Stake-Loss based on Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs3_compounded_loss:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

            st.write("  \n")

            avs3_insurance_status_temp = create_insurance_status_selectbox(col52, insurance_options, "avs3_insurance_status")


    st.session_state.insurance_statuses['avs1_insurance_status'] = avs1_insurance_status_temp
    st.session_state.insurance_statuses['avs2_insurance_status'] = avs2_insurance_status_temp
    st.session_state.insurance_statuses['avs3_insurance_status'] = avs3_insurance_status_temp


    st.write("  \n")
    st.write("  \n")


    def evaluate_cryptoeconomic_security(avs1_coverage_status, avs2_coverage_status, avs3_coverage_status):
            high = "Bought Appropriate Amount of Insurance"
            medium = "Bought Inappropriate Amount of Insurance"
            low = "Didn't Buy Insurance"

            coverage_status = [avs1_coverage_status, avs2_coverage_status, avs3_coverage_status]
            high_security_count = coverage_status.count(high)
            medium_security_count = coverage_status.count(medium)
            low_security_count = coverage_status.count(low)

            if high_security_count == 3:
                security_level = "Strong Cryptoeconomic Security"
            elif high_security_count == 2 and medium_security_count == 1:
                security_level = "Medium Cryptoeconomic Security"
            elif high_security_count == 2 and low_security_count == 1:
                security_level = "Medium Cryptoeconomic Security"
            elif high_security_count == 1 and medium_security_count == 2:
                security_level = "Medium Cryptoeconomic Security"
            elif high_security_count == 1 and low_security_count == 2:
                security_level = "Weak Cryptoeconomic Security"
            elif high_security_count == 1 and medium_security_count == 1 and low_security_count == 1:
                security_level = "Weak Cryptoeconomic Security"
            elif medium_security_count == 3:
                security_level = "Medium Cryptoeconomic Security"
            elif medium_security_count == 2 and low_security_count == 1:
                security_level = "Weak Cryptoeconomic Security"
            elif medium_security_count == 1 and low_security_count == 2:
                security_level = "Weak Cryptoeconomic Security"
            elif low_security_count == 3:
                security_level = "Very Weak Cryptoeconomic Security"
            else:
                security_level = "Undefined Cryptoeconomic Security"

            return f"""
            <div style="font-size: 19px;"> <!-- Adjust the font size as needed -->
                <b>Cryptoeconomic Security Level:</b> {security_level}
            </div>
            """
            
    cryptoeconomic_security_level = evaluate_cryptoeconomic_security(
            st.session_state.insurance_statuses['avs1_insurance_status'],
            st.session_state.insurance_statuses['avs2_insurance_status'],
            st.session_state.insurance_statuses['avs3_insurance_status']
        )

    st.markdown(cryptoeconomic_security_level, unsafe_allow_html=True)

    st.write("\n")

    st.markdown('<p style="">&#8226; Strong Cryptoeconomic Security is only met when all AVSs are properly insured against an adversarial attack and no honest users suffer losses.</p>', unsafe_allow_html=True)
    
    st.write("\n")
    st.write("\n")


    stake_losses_coverage_value = stake_losses_coverage if stake_losses_coverage >= 0 else abs(stake_losses_coverage)
    stake_losses_coverage_sign = '' if stake_losses_coverage >= 0 else '-'
    stake_losses_coverage_color = "green" if stake_losses_coverage >= 0 else "red"

    stakesure_coverage_level_calc = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold;">STAKESURE Insurance Coverage Level = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">${stakesure_insurance_reserve:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{stake_losses_coverage_sign}${avs1_compounded_loss:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">${avs2_compounded_loss:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">${avs3_compounded_loss:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;"> = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: #FFCCCC; border-radius: 10px; padding: 5px; margin: 2px; color: {stake_losses_coverage_color};">{stake_losses_coverage_sign}${stake_losses_coverage_value:,.0f}</span>
    </div>
    """

    st.markdown(stakesure_coverage_level_calc, unsafe_allow_html=True)










    ####################
    ###### BUFFER ######
    ####################
            
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    if 'buffer_reserve_amount' not in st.session_state:
            st.session_state.buffer_reserve_amount = 0  # or any default value

    st.markdown(f"""
            <div style="font-size: 22px;">
                <b>Cryptoeconomic Buffer Available for Poorly Insured or Uninsured Users
            </div>
            """, unsafe_allow_html=True)
    
    st.write("  \n")
    st.write("  \n")


    buffer_available_calc = f"""
        <div style="text-align: center;">
            <span style="font-size: 20px; font-weight: bold; ">Buffer Insurance Amount Available = </span>
            <span style="font-size: 22px; font-weight: bold; background-color: #FFCCCC; border-radius: 10px; padding: 5px; margin: 2px;">${stake_losses_coverage:,.0f}</span> 
            <span style="font-size: 24px; font-weight: bold;">+</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.op_stake_slashable:,.0f}</span> 
            <span style="font-size: 22px; font-weight: bold;">/ 2</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.buffer_reserve_amount:,.0f}</span>
        </div>
    """        
    
    st.markdown(buffer_available_calc, unsafe_allow_html=True)

    
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    st.session_state.buffer_reserve_amount = stake_losses_coverage + st.session_state.op_stake_slashable / 2


    buffer1, buffer2, buffer3 = 0, 0, 0 

    with col50:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message1 = "No Extra Insurance Needed from Buffer"
            buffer1 = 0
        elif st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_uninsured_1 = st.slider("% Amount Uninsured for AVS1", 0, 100, 50, key='percentage_uninsured_1') / 100
            buffer1 = avs1_compounded_loss * percentage_uninsured_1
            message1 = f"Buffer Insurance Amount Needed: ${buffer1:,.0f}"
        else:  # Didn't buy insurance
            buffer1 = avs1_compounded_loss
            message1 = f"Buffer Insurance Amount Needed: ${buffer1:,.0f}"

    with col51:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message2 = "No Extra Insurance Needed from Buffer"
            buffer2 = 0
        elif st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_uninsured_2 = st.slider("% Amount Uninsured for AVS2", 0, 100, 50, key='percentage_uninsured_2') / 100
            buffer2 = avs2_compounded_loss * percentage_uninsured_2
            message2 = f"Buffer Insurance Amount Needed: ${buffer2:,.0f}"
        else:  # Didn't buy insurance
            buffer2 = avs2_compounded_loss
            message2 = f"Buffer Insurance Amount Needed: ${buffer2:,.0f}"

    with col52:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message3 = "No Extra Insurance Needed from Buffer"
            buffer3 = 0
        elif st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_uninsured_3 = st.slider("% Amount Uninsured for AVS3", 0, 100, 50, key='percentage_uninsured_3') / 100
            buffer3 = avs3_compounded_loss * percentage_uninsured_3
            message3 = f"Buffer Insurance Amount Needed: ${buffer3:,.0f}"
        else:  # Didn't buy insurance
            buffer3 = avs3_compounded_loss
            message3 = f"Buffer Insurance Amount Needed: ${buffer3:,.0f}"


    total_buffer_needed = buffer1 + buffer2 + buffer3

    col54, col55, col56 = st.columns(3)

    with col54: 
            st.markdown(f"""
                <div style="border: 1px solid; border-radius: 2px; padding: 5px; text-align: center; margin: 5px 0;">
                    <h2 style="color: black; margin: 0; font-size: 1.2em;">
                        AVS1 - <span style="font-size: 1em;">{message1}</span>
                    </h2>
                </div>
                """, unsafe_allow_html=True)

    with col55:
            st.markdown(f"""
                <div style="border: 1px solid; border-radius: 2px; padding: 5px; text-align: center; margin: 5px 0;">
                    <h2 style="color: black; margin: 0; font-size: 1.2em;">
                        AVS2 - <span style="font-size: 1em;">{message2}</span>
                    </h2>
                </div>
                """, unsafe_allow_html=True)

    with col56:
            st.markdown(f"""
                <div style="border: 1px solid; border-radius: 2px; padding: 5px; text-align: center; margin: 5px 0;">
                    <h2 style="color: black; margin: 0; font-size: 1.2em;">
                        AVS3 - <span style="font-size: 1em;">{message3}</span>
                    </h2>
                </div>
                """, unsafe_allow_html=True)



    st.write("\n")

    buffer_coverage_level = st.session_state.buffer_reserve_amount - buffer1 - buffer2 - buffer3

    buffer_coverage_level_value = buffer_coverage_level if buffer_coverage_level >= 0 else abs(buffer_coverage_level)
    buffer_coverage_level_sign = '' if buffer_coverage_level >= 0 else '-'
    buffer_coverage_level_color = "green" if buffer_coverage_level >= 0 else "red"

    buffer_coverage_level_calc = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold;">Buffer Coverage Level = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.buffer_reserve_amount:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${buffer1:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${buffer2:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${buffer3:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;"> = </span>
        <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px; color: {buffer_coverage_level_color};">{buffer_coverage_level_sign}${buffer_coverage_level_value:,.0f}</span>
    </div>
    """

    st.markdown(buffer_coverage_level_calc, unsafe_allow_html = True)



    st.write("\n")
    st.write("\n")


    total_buffer_needed = buffer1 + buffer2 + buffer3
    if st.session_state.buffer_reserve_amount > total_buffer_needed:
            st.success("Enough attributable security can be safeguarded from the Buffer.")
    else:
            st.error("Not enough attributable security can be safeguarded from the Buffer due to a shortage of funds. We may be in the presence of an **Intermediate- or Max-Loss Risk of some or all the 3 AVSs failing**.")


    def recalculate_and_update():

        existing_reserve = st.session_state.get('existing_reserve', 0)
        op_stake_slashable = st.session_state.get('op_stake_slashable', 0) / 2

        existing_reserve = st.session_state['existing_reserve']
        op_stake_slashable = st.session_state.op_stake_slashable / 2
        
        total_stake_losses = avs1_compounded_loss + avs2_compounded_loss + avs3_compounded_loss
        stakesure_insurance_reserve = existing_reserve + op_stake_slashable
        stake_losses_coverage = stakesure_insurance_reserve - total_stake_losses

        st.session_state['stakesure_insurance_reserve'] = stakesure_insurance_reserve
        st.session_state['stake_losses_coverage'] = stake_losses_coverage


    with st.expander("Logic"):
                st.markdown(f"""
                    How much insurance should honest AVSs buy?
                    
                    We observe that the definition of cryptoeconomic safety does not really guarantee that a transaction user enjoys unconditional safety, rather it only says that an attacker does not derive profit from the attack. However, in complex scenarios, it is possible that an attacker may attack out of pure malice or other reasons, and a honest transactor is affected. We therefore define a stronger notion of cryptoeconomic safety as follows:
                    Strong cryptoeconomic safety is a much stronger definition than the definition of cryptoeconomic safety. While cryptoeconomic safety ensures that there is no incentive for an adversary to attack, a malicious adversary may still go ahead and attack the system which will lead to honest users in the system suffering without recourse. In contrast, in a system with strong cryptoeconomic safety, this can never happen.
                    In this section, we design and show a mechanism, called as STAKESURE, which achieves this stringent property while also solving for the information signalling problem from the previous section.      
                            
                    Since rational transactors only transact if they have enough coverage, automatically the total cryptoconomic load on the system will be smaller than the total insurance coverage available, which is Stot . Thus even if only 3 a smaller amount of stake is in the system, the system remains completely unconditionally safe. It is only the liveness of the honest transactors that get affected, i.e., they may have to wait to obtain insurance in order to transact. But this increases the insurance rate that such transactors may be willing to pay, in turn, increasing the total amount staked (as there is now enough return available for more stake). Thus staking in the system sets itself automatically to the right level of security rather than being controlled by an arbitrary preallocated rewards curve.        
                            
                    It is possible that smaller transactors may not have the foresight to buy insurance or may simply risk their funds (trying to freeride on the assumed safety of the system). We need to make sure that there is enough cryptoeconomic buffer in the system for these transactors to exist. We need to make sure that there is enough cost-of-corruption to protect against these small trans- actors, even though they do not have any insurance.       
                            
                    Half the Operator slashed amount is not accounted for the Insurance Reserve to either be burnt or allocated to a cryptoeconomic buffer to safeguard against irrational users that have not bought enough insurance or bought no insurance at all.
                    
                    In a nutshell, STAKESURE ensures that the system can automatically find out how much cryptoeconomic security is needed by looking at how much insurance is needed and allocate it. If the total amount staked is not sufficient to satisfy the insurance demand, then automatically the price of insurance increases, increases the staking returns, which incentivizes new stake to enter the system        
                            """)
                

    st.write("\n")
    st.write("\n")



    col1, col2, col3 = st.columns([9,10,1])

    with col2:
        button_text = '<p style="text-align: center; font-weight: bold; font-size: 20px;"><b>Update State</b></p>'
        if st.button('Update State'):
            recalculate_and_update()







#########################################
#########################################
#########################################

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

    st.write("-----------------------")

    st.write("\n")

    st.markdown('<p style="font-weight: bold; font-size: 1.2em;">NEXT...</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Performance Reputation</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Collateralization & Node Centralization Risk Levels</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; <s>Compounded Risk Propagation in AVS Ecosystem</s> & Visualization</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Multiple Operators Restaked Into Multiple AVSs + Entrenchment Risk Level</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; display: inline;"><s>&#8226; Slashing Risks Based on AVS Nature</s></p><span style="font-weight: normal; display: inline;"><s>(DA, keeper networks, oracles, bridges, etc.)</s></span><br><br>', unsafe_allow_html=True)
    st.markdown('<p><s style="font-weight: bold;">&#8226; STAKESURE&#39;s Parameters <span style="font-weight: normal;">(Post-Slashing Insurance & Reserves)</span></s></p>', unsafe_allow_html=True)


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




    col30, col31, col32 = st.columns([4,2,4])

    with col30:
        st.write("")

    with col31:
        st.image("images/tokensight.png", width=270)

    with col32:
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