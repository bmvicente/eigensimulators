

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
                    The main goal of the Simulator is to demonstrate the effect a slashing event toward an adversarial Operator has on an ecosystem of 3 AVSs. This effect takes form in the compounded risks each AVS becomes exposed to, post-slashing event, and how the STAKESURE insurance mechanism may safeguard cryptoeconomic security against poorly insured or uninsured AVSs.

                    We will cover and deep dive on two different kinds of Cryptoeconomic Security:

                    - **Cryptoeconomic Safety** (Naive Approach): *CoC > PfC*. 
                    We observe that the definition of cryptoeconomic safety does not really guarantee that a transaction user enjoys unconditional safety, rather it only says that an attacker does not derive profit from the attack. However, in complex scenarios, it is possible that an attacker may attack out of pure malice or other reasons, and a honest transactor is affected.
                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property (CoC). 
                    When CoC is greater than any potential PfC, we say that the system has robust security. The inverse suggests fleeble security.

                    - **Strong Cryptoeconomic Safety** (STAKESURE Approach): *No honest user of the system suffers any loss of funds*. 
                    Strong cryptoeconomic safety is a much stronger definition than the definition of cryptoeconomic safety. While cryptoeconomic safety ensures that there is no incentive for an adversary to attack, a malicious adversary may still go ahead and attack the system which will lead to honest users in the system suffering without recourse. In contrast, in a system with strong cryptoeconomic safety, this can never happen.
                    STAKESURE, which achieves this stringent property while also solving for the information signalling problem from the previous section.  
                    Strong Cryptoeconomic Security introduces staking insurance, through STAKESURE, to attest to such losses never happening. As per the paper [*STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety*](https://arxiv.org/html/2401.05797v1) by the EigenLayer founders: "**STAKESURE** ensures that the system can automatically find out how much cryptoeconomic security is needed by looking at how much insurance is needed and allocate it." 
                    Additionally, in the event of the insurance reserve being insufficient, the paper also advises: "It is possible that smaller transactors may not have the foresight to buy insurance or may simply risk their funds. We need to make sure that there is enough **cryptoeconomic buffer** in the system for these transactors to exist." This is exactly what we attempt to model and simulate at the end of this Simulator: the STAKESURE mechanism with the optional Insurance Buffer for negligent users.

                    Whilst inbetween the Naive and STAKESURE approaches there exist mechanisms around Reversion Periods for Reorg attacks to further levy CoC and reduce chances at extracting PfC, we took the Naive case and then went straight to STAKESURE. This unorthodox bridging is helpful to stress-test STAKESURE against the least-secure approach possible.
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
                        
                        At the end of the Simulator, we introduce the **STAKESURE staking insurance mechanism** to illustrate how a β < 0 situation might be reverted.
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
    
    common_operator = 1.10

    avs1_compounded_loss = actual_slash_on_cs * common_operator * risk_evaluation1 * categories_evaluation_result * allowed_vs_actual_evaluation_result
    avs2_compounded_loss = actual_slash_on_cs * common_operator * risk_evaluation2 * categories_evaluation_result * allowed_vs_actual_evaluation_result
    avs3_compounded_loss = actual_slash_on_cs * common_operator * risk_evaluation3 * categories_evaluation_result * allowed_vs_actual_evaluation_result

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
                        The default slash for a malicious Operator attack is usually 100% of their Stake (and of the proxied Restakers). Naturally, this slash negatively affects the Total Amount Staked and the underlying cryptoeconomic security of the whole ecosystem.
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
                            padding: 16px;
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
                    AVS1 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.2em;">${avs1_compounded_loss:,.0f}</span>
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
            <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{common_operator:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation1:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs1_compounded_loss:,.0f}</span>
            <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 16px; font-weight: bold;">(Actual Slash on Cryptoeconomic Security * Operator Entrenchment Level * AVS Category * AVS Individual Risk Score * BST Status (β) = AVS1 Total Compounded Stake-Loss)</span>
        </div>
        """

        st.markdown(avs1_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")


        with st.expander("Logic"):
            st.markdown("""
                        The **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level), if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψ).
                        
                        The AVS Individual Risk Scores should be derived from the normalized result outputted in our *AVS Underlying Risk* Simulator, for consistency.

                        ```python
                        # Common Operator
                        common_operator = 1.10 # Flat value for now, could be adapted based on Operator reputation, node centralization, and entrenchment levels

                        # Individual AVS Risk Profiles
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

                        # AVS Category
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
                            if actual_slash_on_cs_color == "#90EE90":  # Light Green
                                return 1.00
                            elif actual_slash_on_cs_color == "#FFFFFF": #  White
                                return 1.10
                            elif actual_slash_on_cs_color == "#FFC0CB" or actual_slash_on_cs_color == "#ff6666":  # Light Red
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
                            padding: 16px;
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
                        AVS2 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs2_compounded_loss:,.0f}</span>
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
            <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{common_operator:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation2:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;">&times;</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs2_compounded_loss:,.0f}</span>
            <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 16px; font-weight: bold;">(Actual Slash on Cryptoeconomic Security * Operator Entrenchment Level * AVS Category * AVS Individual Risk Score * BST Status (β) = AVS2 Total Compounded Stake-Loss)</span>
        </div>
        """

        # Displaying the markdown in Streamlit
        st.markdown(avs2_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")

    
        with st.expander("Logic"):
            st.markdown("""
                        The **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level), if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψ).
                        
                        The AVS Individual Risk Scores should be derived from the normalized result outputted in our *AVS Underlying Risk* Simulator, for consistency.

                        ```python
                        # Common Operator
                        common_operator = 1.10 # Flat value for now, could be adapted based on Operator reputation, node centralization, and entrenchment levels

                        # Individual AVS Risk Profiles
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

                        # AVS Category
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
                            if actual_slash_on_cs_color == "#90EE90":  # Light Green
                                return 1.00
                            elif actual_slash_on_cs_color == "#FFFFFF": #  White
                                return 1.10
                            elif actual_slash_on_cs_color == "#FFC0CB" or actual_slash_on_cs_color == "#ff6666":  # Light Red
                                return 1.50
                        ```                
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
                            padding: 16px;
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
                        AVS3 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs3_compounded_loss:,.0f}</span>
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
                <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">{common_operator:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{categories_evaluation_result:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">{risk_evaluation3:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;">&times;</span>
                <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{allowed_vs_actual_evaluation_result:,.2f}</span> 
                <span style="font-size: 24px; font-weight: bold;"> = </span>
                <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px;">${avs3_compounded_loss:,.0f}</span>
            <div style="text-align: center; margin-top: 10px;">
            <span style="font-size: 16px; font-weight: bold;">(Actual Slash on Cryptoeconomic Security * Operator Entrenchment Level * AVS Category * AVS Individual Risk Score * BST Status (β) = AVS3 Total Compounded Stake-Loss)</span>
            </div>
            """

        st.markdown(avs3_compounded_loss_calc, unsafe_allow_html=True)

        st.write("\n")
    

        with st.expander("Logic"):
            st.markdown("""
                        The **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level), if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψ).
                        
                        The AVS Individual Risk Scores should be derived from the normalized result outputted in our *AVS Underlying Risk* Simulator, for consistency.

                        ```python
                        # Common Operator
                        common_operator = 1.10 # Flat value for now, could be adapted based on Operator reputation, node centralization, and entrenchment levels

                        # Individual AVS Risk Profiles
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

                        # AVS Category
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
                            if actual_slash_on_cs_color == "#90EE90":  # Light Green
                                return 1.00
                            elif actual_slash_on_cs_color == "#FFFFFF": #  White
                                return 1.10
                            elif actual_slash_on_cs_color == "#FFC0CB" or actual_slash_on_cs_color == "#ff6666":  # Light Red
                                return 1.50
                        ```                
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


    st.subheader("**Malicious Operator → AVS Slashing Event Simulator:** *STAKESURE Approach*")

    st.write("  \n")
    st.write("  \n")

    st.markdown('<p class="header-style" style="font-size: 21px;">PRE-SLASH (t)</p>', unsafe_allow_html=True)

    st.write("  \n")
    st.write("  \n")

    pre_slash_reserve = st.number_input("**Pre-Slash STAKESURE Insurance Amount Reserve (t):**", min_value=0,
                                        max_value=100000000000, value=0, step=10000000,
                                        key='pre_slash_reserve_key')

    st.write(f"• Pre-Slash STAKESURE Insurance Amount Reserve (t): **${pre_slash_reserve:,.0f}**")
    
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
                            AVS1 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs1_compounded_loss:,.0f}</span>
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
                            AVS2 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs2_compounded_loss:,.0f}</span>
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
                            AVS3 Total Compounded Stake-Loss based on Operator Entrenchment, AVS Category, Risk Profile & BST Status (β): <span style="font-size: 1.1em;">${avs3_compounded_loss:,.0f}</span>
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

    st.markdown('<p style="font-size: 18px;">&#8226; Strong Cryptoeconomic Security is only met when all AVSs are properly insured against an adversarial attack and no honest users suffer losses. If we are presented only with a Medium or Weak Level of Cryptoeconomic Security, we should pass on to STAKESURE Reserve.</p>', unsafe_allow_html=True)
    


    st.write("\n")
    st.write("\n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


###########################################################


    st.markdown('<p class="header-style" style="font-size: 21px;">POST-SLASH (t+1)</p>', unsafe_allow_html=True)


    if 'existing_reserve' not in st.session_state:
        st.session_state['existing_reserve'] = 0

    if 'op_stake_slashable' not in st.session_state:
        st.session_state['op_stake_slashable'] = 0

    if 'post_slash_reserve' not in st.session_state:
        st.session_state['post_slash_reserve'] = 0

    if 'buffer1' not in st.session_state:
        st.session_state.buffer1 = 0
    if 'buffer2' not in st.session_state:
        st.session_state.buffer2 = 0
    if 'buffer3' not in st.session_state:
        st.session_state.buffer3 = 0

    st.write("  \n")



    background_color = "#3CB371" if st.session_state.post_slash_reserve >= 0 else "#ff6666"  # green for enough, red for not enough

    avs1_insured_portion = avs1_compounded_loss - st.session_state.buffer1
    avs2_insured_portion = avs2_compounded_loss - st.session_state.buffer2
    avs3_insured_portion = avs3_compounded_loss - st.session_state.buffer3

    st.session_state.post_slash_reserve = pre_slash_reserve - avs1_insured_portion - avs2_insured_portion - avs3_insured_portion + st.session_state.op_stake_slashable / 2

    st.markdown(
            f"""
            <div style="
                border: 3px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 5px 0;
                background-color: {background_color};">
                <h2 style="color: black; margin: 0; font-size: 1.4em;">
                    <div style="display: block; margin-top: 5px;">
                    <span style="font-size: 1.1em;">Post-Slash <i>STAKESURE</i></span> Insurance Reserve (t+1) = $<span style="font-size: 1.1em;">{st.session_state.post_slash_reserve:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
    
    st.write("  \n")



    stakesure_calc = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold;">Post-Slash STAKESURE Insurance Available = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: orange; border-radius: 10px; padding: 5px; margin: 2px;">${pre_slash_reserve:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">${avs1_insured_portion:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">${avs2_insured_portion:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightblue; border-radius: 10px; padding: 5px; margin: 2px;">${avs3_insured_portion:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">+</span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.op_stake_slashable:,.0f}</span> 
        <span style="font-size: 22px; font-weight: bold;">/ 2</span> 
        <span style="font-size: 24px; font-weight: bold;"> = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">${(st.session_state.post_slash_reserve):,.0f}</span>
    </div>
    <div style="text-align: center; font-size: 18px; font-weight: normal;">
        (Pre-Slash Insurance Reserve - Insured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS1</sub></span> - Insured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS2</sub></span> - Insured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS3</sub></span> + Operator Slash Amount / 2)
    </div>
    """


    st.markdown(stakesure_calc, unsafe_allow_html=True)

    st.write("  \n")
    st.write("  \n")

    if st.session_state.post_slash_reserve > 0:
            st.success("Enough **Attributable Security** can be safeguarded from the **STAKESURE Reserve**.")
    else:
            st.error("Not enough **Attributable Security** can be safeguarded from the **STAKESURE Reserve** due to a shortage of funds. We should pass on to the **Buffer**.")








    ####################
    ###### BUFFER ######
    ####################
            
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    if 'buffer_reserve_amount' not in st.session_state:
            st.session_state.buffer_reserve_amount = 0  # or any default value
    
    st.write("  \n")

    buffer_reserve_amount = st.session_state.post_slash_reserve + st.session_state.op_stake_slashable / 2

    
    background_color_buffer = "#90EE90" if buffer_reserve_amount >= 0 else "#FFCCCC"  # green for enough, red for not enough

    st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 5px;
                padding: 2px;
                text-align: center;
                margin: 5px 0;
                background-color: {background_color_buffer};">
                <h2 style="color: black; margin: 0; font-size: 1.4em;">
                    <div style="display: block; margin-top: 5px;">
                    <span style="font-size: 0.95em;"><i>Buffer</i> Insurance Available for Poorly Insured or Uninsured Users (t+1) = $<span style="font-size: 1.1em;">{buffer_reserve_amount:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.write("  \n")

    buffer_available_calc = f"""
        <div style="text-align: center;">
            <span style="font-size: 20px; font-weight: bold; ">Buffer Available = </span>
            <span style="font-size: 22px; font-weight: bold; background-color: yellow; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.post_slash_reserve:,.0f}</span> 
            <span style="font-size: 24px; font-weight: bold;">+</span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.op_stake_slashable:,.0f}</span> 
            <span style="font-size: 22px; font-weight: bold;">/ 2</span> 
            <span style="font-size: 24px; font-weight: bold;"> = </span>
            <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">${buffer_reserve_amount:,.0f}</span>
        </div>
    """        
    
    st.markdown(buffer_available_calc, unsafe_allow_html=True)

    
    st.write("  \n")
    st.write("  \n")



    with col50:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message1 = "No Extra Insurance Needed from Buffer"
            st.session_state.buffer1 = 0
        elif st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_insured_1 = st.slider("% Amount Insured for AVS1", 0, 100, 50, key='percentage_insured_1') / 100
            st.session_state.buffer1 = avs1_compounded_loss * (1 - percentage_insured_1)
            message1 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer1:,.0f}"
        else:  # Didn't buy insurance
            st.session_state.buffer1 = avs1_compounded_loss
            message1 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer1:,.0f}"

    with col51:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message2 = "No Extra Insurance Needed from Buffer"
            st.session_state.buffer2 = 0
        elif st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_insured_2 = st.slider("% Amount Insured for AVS2", 0, 100, 50, key='percentage_insured_2') / 100
            st.session_state.buffer2 = avs2_compounded_loss * (1 - percentage_insured_2)
            message2 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer2:,.0f}"
        else:  # Didn't buy insurance
            st.session_state.buffer2 = avs2_compounded_loss
            message2 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer2:,.0f}"

    with col52:
        # Calculate buffer based on the selected insurance option
        if st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[0]:  # Bought appropriate amount
            message3 = "No Extra Insurance Needed from Buffer"
            st.session_state.buffer3 = 0
        elif st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[1]:  # Bought inappropriate amount
            percentage_insured_3 = st.slider("% Amount Insured for AVS3", 0, 100, 50, key='percentage_insured_3') / 100
            st.session_state.buffer3 = avs3_compounded_loss * (1 - percentage_insured_3)
            message3 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer3:,.0f}"
        else:  # Didn't buy insurance
            st.session_state.buffer3 = avs3_compounded_loss
            message3 = f"Buffer Insurance Amount Needed: ${st.session_state.buffer3:,.0f}"


    total_buffer_needed = st.session_state.buffer1 + st.session_state.buffer2 + st.session_state.buffer3

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

    buffer_coverage_level = buffer_reserve_amount - st.session_state.buffer1 - st.session_state.buffer2 - st.session_state.buffer3

    buffer_coverage_level_value = buffer_coverage_level if buffer_coverage_level >= 0 else abs(buffer_coverage_level)
    buffer_coverage_level_sign = '' if buffer_coverage_level >= 0 else '-'
    buffer_coverage_level_color = "green" if buffer_coverage_level >= 0 else "red"

    buffer_coverage_level_calc = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold;">Buffer Coverage Level = </span>
        <span style="font-size: 22px; font-weight: bold; background-color: lightgrey; border-radius: 10px; padding: 5px; margin: 2px;">${buffer_reserve_amount:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.buffer1:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.buffer2:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;">-</span>
        <span style="font-size: 22px; font-weight: bold; background-color: #D2B48C; border-radius: 10px; padding: 5px; margin: 2px;">${st.session_state.buffer3:,.0f}</span> 
        <span style="font-size: 24px; font-weight: bold;"> = </span>
        <span style="font-size: 22px; font-weight: bold; border-radius: 10px; padding: 5px; margin: 2px; color: {buffer_coverage_level_color};">{buffer_coverage_level_sign}${buffer_coverage_level_value:,.0f}</span>
    </div>
        <div style="text-align: center; font-size: 18px; font-weight: normal;">
            (Buffer Insurance Available - Uninsured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS1</sub></span> 
            - Uninsured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS2</sub></span> 
            - Uninsured <span style="font-size: 1.1em;">Ψ<sub style="font-size: 0.8em;">AVS3</sub></span>)
    </div>
    """

    st.markdown(buffer_coverage_level_calc, unsafe_allow_html = True)



    st.write("\n")
    st.write("\n")


    total_buffer_needed = st.session_state.buffer1 + st.session_state.buffer2 + st.session_state.buffer3
    if buffer_reserve_amount > total_buffer_needed:
            st.success("Enough extra **Attributable Security** can be safeguarded from the **Buffer**.")
    else:
            st.error("No extra **Attributable Security** can be safeguarded from the **Buffer** due to a shortage of funds. We may be in the presence of an **Intermediate- or Max-Loss Risk of some or all the 3 AVSs failing**.")


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
                    In a nutshell and as said in the beginning of the Simulator, **STAKESURE** ensures that the system can automatically find out how much cryptoeconomic security is needed by looking at how much insurance is needed and allocate it. 
                    This is what it means to have attributable in a Restaking cryptoeconomic context.
                    
                    "*Since rational transactors only transact if they have enough coverage, automatically the total cryptoconomic load on the system will be smaller than the total insurance coverage available. Thus even if only a smaller amount of stake is in the system, the system remains completely unconditionally safe. It is only the liveness of the honest transactors that get affected, i.e., they may have to wait to obtain insurance in order to transact. 
                    It is possible, nevertheless, that smaller transactors may not have the foresight to buy insurance or may simply risk their funds (trying to freeride on the assumed safety of the system). We need to make sure that there is enough cryptoeconomic buffer in the system for these transactors to exist. We need to make sure that there is enough cost-of-corruption to protect against these small transactors, even though they do not have any insurance.*"
                    
                    From the paper [*STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety*](https://arxiv.org/abs/2401.05797). Recommmended reading for a deeper dive on this topic.
                    
                    Logic behind the STAKESURE Approach Simulator:
                    - **Post-Slash STAKESURE Insurance Reserve Available**: Pre-Slash Reserve Available - Σ(Insured Ψj) + Operator Slashed Stake Amount/2 (other half of Operator Slashed Stake is to be allocated to a cryptoeconomic buffer or burnt to safeguard against irrational users that have not bought enough insurance or bought no insurance at all);
                    - If all AVSs bought an appropriate amount of insurance, the system is cryptoeconomically secure. There's no need to revert to the Reserve or Buffer;
                    - The system is always cryptoeconomically insecure to some degree if NOT all AVSs bought an appropriate amount of Insurance;
                    - If it so happens that **Post-Slash STAKESURE Insurance Available < 0** and if NOT all AVSs bought an appropriate amount of Insurance, we should revert to the **Buffer**;
                    - If an AVS "Didn't Buy Insurance", all the Ψ amount for that AVS will be passed on to the **Buffer**, and if an AVS "Bought Inappropriate Amount of Insurance" a slider pops up that enables the user to set the *percentage of Ψ that was Insured and covered by the STAKESURE Reserve*, while the remaining *percentage of Ψ that was Uninsured will be covered by the Buffer*;
                    - The **Buffer** takes the leftover from the Reserve (if it exists) that hasn't been allocated and, if needed, the other half of Operator's slashed stake to adequately accommodate for Uninsured or Poorly-Insured users;
                    - Finally, the **Buffer Coverage Level** assesses if the Buffer, in turn, is able to cover for the Uninsured portions of stake per AVS that were not covered by the initial STAKESURE Reserve. If that's the case, we may be in the presence of an intermediate- or max-loss cascading risk scenario, as the pop-up message displays.
                                        
                    By offering such hindsight view, this simulation model also helps answer the question: *How much insurance should honest AVSs buy?*  The potential compounding risks of AVSs and how much insurance is already in Reserve should be good pointers as to how much insurance an honest AVS should secure for a future slashing event.          
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