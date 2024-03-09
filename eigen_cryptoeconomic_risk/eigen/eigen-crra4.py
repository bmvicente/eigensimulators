

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

    st.image("images/eigen.png", width=350)

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

    st.title("Cryptoeconomic Risk/Reward Analysis IV")

    st.header("**Malicious Operator → AVS Slashing Event Simulator:** *Naïve & STAKESURE Approaches*")
    st.write("  \n")

    with st.expander("Index"):
        st.markdown("""
    1. **RISK**
        - 1.1 **Malicious Operator → AVS Slashing Event Simulator:** *Naïve Approach*
        - 1.2 **Malicious Operator → AVS Slashing Event Simulator:** *STAKESURE Approach*

    <br>

    2. **REWARD**
        - 2.1 Staker/Operator Reward Distribution
        - 2.2 Sharpe Ratios
        """, unsafe_allow_html=True)



    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.header("**1. RISK**")
    st.subheader("**1.1 Malicious Operator → AVS Slashing Event Simulator:** *Naïve Approach*")

    
    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
                    The main goal of the Simulator is to demonstrate the effect a slashing event toward an adversarial Operator has on an ecosystem of 3 AVSs. This effect takes form in the **compounded risks** each AVS becomes exposed to, post-slashing event, and how the **STAKESURE** insurance mechanism may safeguard cryptoeconomic security against poorly-insured or uninsured AVSs.

                    We will cover and deep dive on two different kinds of Cryptoeconomic Security:

                    - **Cryptoeconomic Safety** (Naive Approach): *CoC > PfC*. 
                    We observe that the definition of cryptoeconomic safety does not really guarantee that a transactor enjoys unconditional safety, rather it only says that an attacker does not derive profit from the attack.
                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property (CoC). 
                    When CoC is greater than any potential PfC, we say that the system has robust security. The inverse suggests fleeble security.

                    - **Strong Cryptoeconomic Safety** (STAKESURE Approach): *No honest user of the system suffers any loss of funds*. This is the promise.
                    Strong cryptoeconomic safety is a much stronger definition than the definition of cryptoeconomic safety. While cryptoeconomic safety ensures that there is no incentive for an adversary to attack, a malicious adversary may still go ahead and attack the system which will lead to honest users in the system suffering without recourse. In contrast, in a system with strong cryptoeconomic safety, this can never happen.
                    It introduces staking insurance, through STAKESURE, to attest to such losses never happening. As per the paper [*STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety*](https://arxiv.org/html/2401.05797v1) by the EigenLayer founders: "***STAKESURE** ensures that the system can automatically find out how much cryptoeconomic security is needed by looking at how much insurance is needed and allocate it.*" 
                    Additionally, in the event of the insurance reserve being insufficient, the paper also advises: "*It is possible that smaller transactors may not have the foresight to buy insurance or may simply risk their funds. We need to make sure that there is enough **cryptoeconomic buffer** in the system for these transactors to exist.*" 
                    
                    This is exactly what we attempt to model and simulate at the end of this Simulator: the STAKESURE mechanism with the optional Insurance Buffer for negligent users.

                    Whilst in-between the Naive and STAKESURE approaches there exist mechanisms around Reversion Periods for Reorg attacks to further levy CoC and reduce chances at extracting PfC, we took the Naive case and then went straight to STAKESURE. This unorthodox bridging is helpful to understand how **Attributable Security** can work and stress-test STAKESURE against the least-cryptoeconomically-secure approach possible.
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
                                    {max_slash_allowed_text}: <span style="font-size: 1.1em;">${pre_slash_max_slash_allowed:,.0f}</span>
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
                        The 3 main ideas in this section are:
                            
                        - **Pre-Slash** (t): In the same way the calculation for the *AVS <> Non-Malicious Operator: Naive Approach* Simulator was performed, here again the Naive Analysis was applied as *CoC = T/3* and *PfC = ΣTVL*.

                        - **Post-Slash** (t+1): What changes post-slashing event is the amount of the Operator's Stake that has been slashed, how it affects the Total Stake Amount and everything that comes after it: the slash in CoC, the status of cryptoeconomic security, and the impact on the AVS ecosystem.
                            Naturally, the Total Amount Staked Post-Slash (Tt+1) is given by *Tt - Slashed Operator Stake*. PfC post-slash should stay the same as the slash should have no impact on the AVSs' TVL. As a result, **Actual Slash on Cryptoeconomic Security** (δ) is given by the CoC amount pre-slash subtracted by the CoC amount post-slash.

                        - **BST test** (β): As introduced in the previous Simulator, the Byzantine Slashing Tolerance test assesses the Cryptoeconomic Security of the AVS ecosystem, post Operator Slash or Stake-Loss event. The network is in a secure cryptoeconomic position if the **Max Total Stake-Loss "Allowed" To Still Maintain Cryptoeconomic Security** is greater than the **Actual Slash on Cryptoeconomic Security**, and in an insecure position if the opposite is true. Therefore, the ecosystem has failed this test if β < 0, and passed if β > 0.
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
                background-color: #3333FF;">
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
                background-color: #3333FF;"> 
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
                        The previously-calculated **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level) such as in this case, if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψj).
                        
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
                        The previously-calculated **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level) such as in this case, if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψj).
                        
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
                        The previously-calculated **α**jt and **δ**ijt+1 variables were displayed above per AVS to illustrate how cryptoeconomic security is in fact pooled and shared among AVSs, not fractionalized or customized. 

                        On a post-slash potential risk-cascading event, AVSs are more prone to compounded risks if they are being secured by a **common Operator** (Operator entrenchment level) such as in this case, if they belong to the **same category of AVSs** (if they do, it's likely they are being validated by the same set of Operators that likely use similar EigenLayer modules to perform their validations), if their **Individual Risk Profiles are equally high** (note that the outputted values by the function *collective_risk_adjustment* are non-linear, they have a compounding effect as the collective risk increases), and if they have **collectively failed (and to what degree) the BST test**. These were the 4 main metrics taken into account to assess each **AVS Total Compounded Stake-Loss** (Ψj).
                        
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


    st.subheader("**1.2 Malicious Operator → AVS Slashing Event Simulator:** *STAKESURE Approach*")

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

    st.markdown('<p style="font-size: 18px;">&#8226; <i>Strong Cryptoeconomic Security</i> is only met when all AVSs are properly insured against an adversarial attack and no honest users suffer losses. If we are presented only with a Medium or Weak Level of Cryptoeconomic Security -- which signals poorly-insured AVSs --, we should revert to the <b>STAKESURE Reserve</b>.</p>', unsafe_allow_html=True)
    


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
            st.error("Not enough **Attributable Security** can be safeguarded from the **STAKESURE Reserve** due to a shortage of funds. We should revert to the **Buffer**.")








    ####################
    ###### BUFFER ######
    ####################
            
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
                    This is what it means to have Attributable Security in a Restaking cryptoeconomic context.      
                            
                    From the paper [*STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety*](https://arxiv.org/abs/2401.05797) (recommended reading for a deeper dive on this topic):

                    "*Since rational transactors only transact if they have enough coverage, automatically the total cryptoconomic load on the system will be smaller than the total insurance coverage available. Thus even if only a smaller amount of stake is in the system, the system remains completely unconditionally safe. It is only the liveness of the honest transactors that get affected, i.e., they may have to wait to obtain insurance in order to transact. 
                    It is possible, nevertheless, that smaller transactors may not have the foresight to buy insurance or may simply risk their funds (trying to freeride on the assumed safety of the system). We need to make sure that there is enough cryptoeconomic buffer in the system for these transactors to exist. We need to make sure that there is enough cost-of-corruption to protect against these small transactors, even though they do not have any insurance.*"
                    
                    Logic behind the STAKESURE Approach Simulator:
                    - **Post-Slash STAKESURE Insurance Reserve Available**: Pre-Slash Reserve Available - Σ(Insured Ψj) + Operator Slashed Stake Amount/2 (other half of Operator Slashed Stake is to be allocated to a cryptoeconomic buffer or burnt to safeguard against irrational users that have not bought enough insurance or bought no insurance at all);
                    - If **Post-Slash STAKESURE Insurance Reserve Available > 0** and all AVSs bought an appropriate amount of insurance, the system is cryptoeconomically secure, there is no need to revert to the **Buffer**. The system is always cryptoeconomically insecure to some degree if NOT all AVSs bought an appropriate amount of Insurance, and we should revert to the **Buffer**, as a result;
                    - If an AVS "Didn't Buy Insurance", all the Ψ amount for that AVS will be passed on to the **Buffer**, and if an AVS "Bought Inappropriate Amount of Insurance" a slider pops up that enables the user to set the *percentage of Ψ that was Insured and covered by the STAKESURE Reserve*, while the remaining *percentage of Ψ, that was Uninsured, will be covered by the Buffer*;
                    - The **Buffer** takes the leftover from the Reserve (if it exists) that hasn't been allocated and, if needed, the other half of Operator's slashed stake to adequately accommodate for Uninsured or Poorly-Insured users;
                    - Finally, the **Buffer Coverage Level** assesses if the Buffer, in turn, is able to cover for the Uninsured portions of stake per AVS that were not covered by the initial STAKESURE Reserve. If that's the case, we may be in the presence of an **Intermediate- or Max-Loss cascading risk scenario**, as the pop-up message displays.
                                        
                    By offering such an hindsight view, this simulation model also helps answer the question: *How much insurance should honest AVSs buy?*  The potential compounding risks of AVSs and how much insurance is in Reserve should be good pointers as to how much insurance an honest AVS should secure for a future slashing event.          
                            """)
                

    st.write("\n")
    st.write("\n")



    col1, col2, col3 = st.columns([9,10,1])

    with col2:
        button_text = '<p style="text-align: center; font-weight: bold; font-size: 20px;"><b>Update State</b></p>'
        if st.button('Update State'):
            recalculate_and_update()




    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n") 
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n") 
    st.write("\n")
    st.write("\n")



















    ###################################
    ###################################
    ############# REWARD ##############
    ###################################
    ###################################




    st.header("**2. REWARD**")
    st.subheader("**2.1 Staker/Operator Revenue Distributions**")
    
    st.write("\n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
                    An **AVS's Revenue**, at any given time, is a useful indicator to help assess the level of rewards an AVS might be able to emit. From the revenue inputted by the user, we assume a 20% profit for the AVS, and [10-30]% of that profit to be distributable as rewards (specific value of this range dependent on weighting of all the chosen inputs in our Simulator).

                    - Current AVS Revenue: **\${avs_revenue:,}**

                    - Total Distributable Reward Amount, if rewards = *10%* of profit: **\${dist_rewards_10:,}**

                    - Total Distributable Reward Amount, if rewards = *30%* of profit: **\${dist_rewards_30:,}**

                    Such a reward range is necessary to be calculated to account for the underlying riskiness/security of an AVS and subsequent reward emission values. 
                    We find these percentages reasonable, although would highly appreciate feedback from EigenLayer.
                    """)


  
    st.write("\n")        
    st.write("\n")
    st.write("\n")


    st.markdown("""
    <style>
    .big-font {
        font-size:23px !important;
        font-weight:bold;
    }
    </style>
    <div class='big-font'>AVSs METRICS</div>
    """, unsafe_allow_html=True)


    col63, col64, col65 = st.columns(3, gap="large")







    #####################
    ####### AVS 1 #######
    #####################


    def avs1_rewards(avs1_revenue, tvl1, pre_slash_total_restaked, avs1_token_percentage, xeth1_percentage):
        
        reward_percentage = 0.20  # Base reward percentage

        # Adjusting the base reward based on the AVS token and xETH balance
        #dual_staking_balance_adjustment = (avs_token_percentage - xeth_percentage) / 100.0

        def dual_staking_balance_adjustment1(avs1_token_percentage, xeth1_percentage):
            ratio1 = avs1_token_percentage / xeth1_percentage

            if ratio1 > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
                return 0.020
            elif ratio1 > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
                return 0.015
            elif ratio1 > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.010
            elif ratio1 > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.005
            elif ratio1 == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
                return 0  # Neutral adjustment for balanced scenario
            elif ratio1 > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
                return -0.010
            elif ratio1 > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
                return -0.015
            else:  # Very low AVS compared to ETH
                return -0.020

        dual_staking_adjustment1 = dual_staking_balance_adjustment1(avs1_token_percentage, xeth1_percentage)


        # Check the ratio of Total Staked to TVL
        def ratio_tvl_totalstaked1(avs1_compounded_loss, tvl1):
            
            if tvl1 == 0:
                return 0
            
            ratio1 = (pre_slash_total_restaked / 2) / tvl1

            if ratio1 > 2:
                return -0.03
            elif ratio1 > 1.5:
                return -0.02
            elif ratio1 > 1:
                return -0.01
            elif ratio1 == 1:
                return 0
            elif ratio1 < 1:
                return 0.01
            elif ratio1 < 0.5:
                return 0.02
            elif ratio1 < 0.25:
                return 0.03
            else:
                return 0

        ratio_tvl_totalstaked_adjustment = ratio_tvl_totalstaked1(pre_slash_total_restaked, tvl1)


        # Revenue-based adjustment
        if avs1_revenue > 100000000:  # Greater than $100M
            avs1_revenue_adjustment = 0.01
        elif avs1_revenue > 50000000:  # Greater than $50M
            avs1_revenue_adjustment = 0.02
        elif avs1_revenue > 20000000:  # Greater than $20M
            avs1_revenue_adjustment = 0.03
        elif avs1_revenue > 5000000:   # Greater than $5M
            avs1_revenue_adjustment = 0.04
        elif avs1_revenue > 1000000:   # Greater than $1M
            avs1_revenue_adjustment = 0.05
        else:
            avs1_revenue_adjustment = 0


        # Combine all adjustments
        reward_percentage_sum1 = reward_percentage + dual_staking_adjustment1 + avs1_revenue_adjustment + ratio_tvl_totalstaked_adjustment

        # Ensure the reward percentage is within reasonable bounds
        reward_percentage_adj1 = max(min(reward_percentage_sum1, 0.30), 0.10)

        # Calculate rewards for stakers and operators
        profit_percentage = 0.20
        staker_percentage = 0.40
        operator_percentage = 0.60

        staker_reward1 = avs1_revenue * profit_percentage * reward_percentage_adj1 * staker_percentage
        operator_reward1 = avs1_revenue * profit_percentage * reward_percentage_adj1 * operator_percentage

        return staker_reward1, operator_reward1



    with col63:
         
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
        st.markdown('<p class="header-style">AVS1</p>', unsafe_allow_html=True)

        st.write("\n")

        avs1_revenue = st.number_input("Revenue", min_value=0, max_value=1000000000000, value=0, step=10000000, key="avs1_revenue")
        
        st.write(f"""&#8226; AVS1 Revenue: **${avs1_revenue:,.0f}**""")

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
        st.markdown('<p class="header-style">AVS1 Dual Staking Model</p>', unsafe_allow_html=True)
        
        st.write("  \n")

        col5, col6 = st.columns(2)
        with col5:
            avs1_token_percentage = st.slider("**% $AVS**", min_value=10, max_value=90, value=50, key="avs1_dual")
        with col6:
            xeth1_percentage = 100 - avs1_token_percentage
        
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth1_percentage, disabled=True, key="avs1_dualx")

        st.write("&#8226; **Dual Staking Balance**: {}% $AVS : {}% xETH".format(avs1_token_percentage, xeth1_percentage))

        st.write("\n")
        st.write("\n")
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
        st.markdown('<p class="header-style">$AVS1 Tokenomics [Optional]</p>', unsafe_allow_html=True)

        st.write("  \n")

        avs1_inf_def_rate = st.slider("**$AVS1 Inflation/Deflation Rate**", 
                                    min_value=-50, 
                                    max_value=50, 
                                    value=0,
                                    format="%d%%",
                                    key="avs1_tok")
                                    #help="Slide to set the inflation or deflation rate for $AVS token. -50% indicates deflation, 50% indicates inflation.")

        if avs1_inf_def_rate > 0:
            st.write(f"&#8226; $AVS1 Inflation Rate: {avs1_inf_def_rate}%")
        elif avs1_inf_def_rate < 0:
            st.write(f"&#8226; $AVS1 Deflation Rate: {(avs1_inf_def_rate)}%")

        col3, col4 = st.columns([3, 3])

        with col3:
                avs1_circ_supply = st.number_input("**$AVS1 Circulating Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, help="Circulating Supply should never exceed Total Supply", key="avs1_circ")
                st.write(f"&#8226; Circulating Supply: {avs1_circ_supply:,}")

        with col4:
                avs1_total_supply = st.number_input("**$AVS1 Total Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, key="avs1_total")
                st.write(f"&#8226; Total Supply: {avs1_total_supply:,}")



        st.write("\n")
        st.write("  \n")
        st.write("  \n")

        staker_reward1, operator_reward1 = avs1_rewards(avs1_revenue, tvl1, pre_slash_total_restaked, avs1_token_percentage, xeth1_percentage)

        col66, col67 = st.columns(2)

        with col66:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs1_revenue != 0:
                staker_reward1_percentage = (staker_reward1 / avs1_revenue) * 100
            else:
                staker_reward1_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS1 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{staker_reward1_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        with col67:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs1_revenue != 0:
                operator_reward1_percentage = (operator_reward1 / avs1_revenue) * 100
            else:
                operator_reward1_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS1 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{operator_reward1_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
            """)











    #####################
    ####### AVS 2 #######
    #####################
            


    def avs2_rewards(avs2_revenue, tvl2, pre_slash_total_restaked, avs2_token_percentage, xeth2_percentage):
        
        reward_percentage = 0.20  # Base reward percentage

        # Adjusting the base reward based on the AVS token and xETH balance
        dual_staking_balance_adjustment2 = (avs2_token_percentage - xeth2_percentage) / 100.0

        def dual_staking_balance_adjustment2(avs2_token_percentage, xeth2_percentage):
            ratio2 = avs2_token_percentage / xeth2_percentage

            if ratio2 > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
                return 0.020
            elif ratio2 > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
                return 0.015
            elif ratio2 > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.010
            elif ratio2 > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.005
            elif ratio2 == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
                return 0  # Neutral adjustment for balanced scenario
            elif ratio2 > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
                return -0.010
            elif ratio2 > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
                return -0.015
            else:  # Very low AVS compared to ETH
                return -0.020

        dual_staking_adjustment2 = dual_staking_balance_adjustment2(avs2_token_percentage, xeth2_percentage)


        # Check the ratio of Total Staked to TVL
        def ratio_tvl_totalstaked2(pre_slash_total_restaked, tvl2):
            
            if tvl2 == 0:
                return 0
            
            ratio2 = (pre_slash_total_restaked / 2) / tvl2

            if ratio2 > 2:
                return -0.03
            elif ratio2 > 1.5:
                return -0.02
            elif ratio2 > 1:
                return -0.01
            elif ratio2 == 1:
                return 0
            elif ratio2 < 1:
                return 0.01
            elif ratio2 < 0.5:
                return 0.02
            elif ratio2 < 0.25:
                return 0.03
            else:
                return 0

        ratio_tvl_totalstaked_adjustment2 = ratio_tvl_totalstaked2(pre_slash_total_restaked, tvl2)


        # Revenue-based adjustment
        if avs2_revenue > 100000000:  # Greater than $100M
            avs2_revenue_adjustment = 0.01
        elif avs2_revenue > 50000000:  # Greater than $50M
            avs2_revenue_adjustment = 0.02
        elif avs2_revenue > 20000000:  # Greater than $20M
            avs2_revenue_adjustment = 0.03
        elif avs2_revenue > 5000000:   # Greater than $5M
            avs2_revenue_adjustment = 0.04
        elif avs2_revenue > 1000000:   # Greater than $1M
            avs2_revenue_adjustment = 0.05
        else:
            avs2_revenue_adjustment = 0


        # Combine all adjustments
        reward_percentage_sum2 = reward_percentage + dual_staking_adjustment2 + avs2_revenue_adjustment + ratio_tvl_totalstaked_adjustment2

        # Ensure the reward percentage is within reasonable bounds
        reward_percentage_adj2 = max(min(reward_percentage_sum2, 0.30), 0.10)

        # Calculate rewards for stakers and operators
        profit_percentage = 0.20
        staker_percentage = 0.40
        operator_percentage = 0.60

        staker_reward2 = avs2_revenue * profit_percentage * reward_percentage_adj2 * staker_percentage
        operator_reward2 = avs2_revenue * profit_percentage * reward_percentage_adj2 * operator_percentage

        return staker_reward2, operator_reward2

    with col64:
         
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
        st.markdown('<p class="header-style">AVS2</p>', unsafe_allow_html=True)

        st.write("\n")

        avs2_revenue = st.number_input("Revenue", min_value=0, max_value=1000000000000, value=0, step=10000000, key="avs2_revenue")

        st.write(f"""&#8226; AVS2 Revenue: **${avs2_revenue:,.0f}**""")

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
        st.markdown('<p class="header-style">AVS2 Dual Staking Model</p>', unsafe_allow_html=True)
        
        st.write("  \n")

        col5, col6 = st.columns(2)
        with col5:
            avs2_token_percentage = st.slider("**% $AVS2**", min_value=10, max_value=90, value=50, key="avs2_dual")
        with col6:
            xeth2_percentage = 100 - avs2_token_percentage
        
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth2_percentage, disabled=True, key="avs2_dualx")

        st.write("&#8226; **Dual Staking Balance**: {}% $AVS2 : {}% xETH".format(avs2_token_percentage, xeth2_percentage))



        st.write("\n")
        st.write("  \n")
        st.write("\n")



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
        st.markdown('<p class="header-style">$AVS2 Tokenomics [Optional]</p>', unsafe_allow_html=True)

        st.write("  \n")

        avs2_inf_def_rate = st.slider("**$AVS2 Inflation/Deflation Rate**", 
                                    min_value=-50, 
                                    max_value=50, 
                                    value=0,
                                    format="%d%%",
                                    key="avs2_tok")
                                    #help="Slide to set the inflation or deflation rate for $AVS token. -50% indicates deflation, 50% indicates inflation.")

        if avs2_inf_def_rate > 0:
            st.write(f"&#8226; $AVS2 Inflation Rate: {avs2_inf_def_rate}%")
        elif avs2_inf_def_rate < 0:
            st.write(f"&#8226; $AVS2 Deflation Rate: {(avs2_inf_def_rate)}%")


        col3, col4 = st.columns([3, 3])

        with col3:
                avs2_circ_supply = st.number_input("**$AVS2 Circulating Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, help="Circulating Supply should never exceed Total Supply", key="avs2_circ")
                st.write(f"&#8226; Circulating Supply: {avs2_circ_supply:,}")

        with col4:
                avs2_total_supply = st.number_input("**$AVS2 Total Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, key="avs2_total")
                st.write(f"&#8226; Total Supply: {avs2_total_supply:,}")




        st.write("\n")
        st.write("  \n")
        st.write("\n")

        staker_reward2, operator_reward2 = avs2_rewards(avs2_revenue, tvl2, pre_slash_total_restaked, avs2_token_percentage, xeth2_percentage)

        col68, col69 = st.columns(2)

        with col68:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs2_revenue != 0:
                staker_reward2_percentage = (staker_reward2 / avs2_revenue) * 100
            else:
                staker_reward2_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS2 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{staker_reward2_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col69:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs2_revenue != 0:
                operator_reward2_percentage = (operator_reward2 / avs2_revenue) * 100
            else:
                operator_reward2_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS2 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{operator_reward2_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
            """)









    #####################
    ####### AVS 3 #######
    #####################


    def avs3_rewards(avs3_revenue, tvl3, pre_slash_total_restaked, avs3_token_percentage, xeth3_percentage):
        
        reward_percentage = 0.20  # Base reward percentage

        # Adjusting the base reward based on the AVS token and xETH balance
        dual_staking_balance_adjustment3 = (avs3_token_percentage - xeth3_percentage) / 100.0

        def dual_staking_balance_adjustment3(avs3_token_percentage, xeth3_percentage):
            ratio3 = avs3_token_percentage / xeth3_percentage

            if ratio3 > 4:  # Very high AVS compared to ETH e.g., 80% AVS:20% ETH
                return 0.020
            elif ratio3 > 7/3:  # High AVS, e.g., 70% AVS:30% ETH
                return 0.015
            elif ratio3 > 1.5:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.010
            elif ratio3 > 1:  # Moderately high AVS, e.g., 60% AVS:40% ETH
                return 0.005
            elif ratio3 == 1:  # Perfect balance, e.g., 50% AVS:50% ETH
                return 0  # Neutral adjustment for balanced scenario
            elif ratio3 > 2/3:  # More ETH, e.g., 40% AVS:60% ETH
                return -0.010
            elif ratio3 > 0.25:  # Low AVS, e.g., 20% AVS:80% ETH
                return -0.015
            else:  # Very low AVS compared to ETH
                return -0.020

        dual_staking_adjustment3 = dual_staking_balance_adjustment3(avs3_token_percentage, xeth3_percentage)


        # Check the ratio of Total Staked to TVL
        def ratio_tvl_totalstaked3(pre_slash_total_restaked, tvl3):
            
            if tvl3 == 0:
                return 0
            
            ratio3 = (pre_slash_total_restaked / 2) / tvl3

            if ratio3 > 2:
                return -0.03
            elif ratio3 > 1.5:
                return -0.02
            elif ratio3 > 1:
                return -0.01
            elif ratio3 == 1:
                return 0
            elif ratio3 < 1:
                return 0.01
            elif ratio3 < 0.5:
                return 0.02
            elif ratio3 < 0.25:
                return 0.03
            else:
                return 0

        ratio_tvl_totalstaked_adjustment3 = ratio_tvl_totalstaked3(pre_slash_total_restaked, tvl3)


        # Revenue-based adjustment
        if avs3_revenue > 100000000:  # Greater than $100M
            avs3_revenue_adjustment = 0.01
        elif avs3_revenue > 50000000:  # Greater than $50M
            avs3_revenue_adjustment = 0.02
        elif avs3_revenue > 20000000:  # Greater than $20M
            avs3_revenue_adjustment = 0.03
        elif avs3_revenue > 5000000:   # Greater than $5M
            avs3_revenue_adjustment = 0.04
        elif avs3_revenue > 1000000:   # Greater than $1M
            avs3_revenue_adjustment = 0.05
        else:
            avs3_revenue_adjustment = 0


        # Combine all adjustments
        reward_percentage_sum3 = reward_percentage + dual_staking_adjustment3 + avs3_revenue_adjustment + ratio_tvl_totalstaked_adjustment3

        # Ensure the reward percentage is within reasonable bounds
        reward_percentage_adj3 = max(min(reward_percentage_sum3, 0.30), 0.10)

        # Calculate rewards for stakers and operators
        profit_percentage = 0.20
        staker_percentage = 0.40
        operator_percentage = 0.60

        staker_reward3 = avs3_revenue * profit_percentage * reward_percentage_adj3 * staker_percentage
        operator_reward3 = avs3_revenue * profit_percentage * reward_percentage_adj3 * operator_percentage

        return staker_reward3, operator_reward3



    with col65:

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
        st.markdown('<p class="header-style">AVS3</p>', unsafe_allow_html=True)

        st.write("\n")

        avs3_revenue = st.number_input("Revenue", min_value=0, max_value=1000000000000, value=0, step=10000000, key="avs3_revenue")

        st.write(f"""&#8226; AVS3 Revenue: **${avs3_revenue:,.0f}**""")


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
        st.markdown('<p class="header-style">AVS3 Dual Staking Model</p>', unsafe_allow_html=True)
        
        st.write("  \n")

        col5, col6 = st.columns(2)
        with col5:
            avs3_token_percentage = st.slider("**% $AVS3**", min_value=10, max_value=90, value=50, key="avs3_dual")
        with col6:
            xeth3_percentage = 100 - avs3_token_percentage
        
            st.slider("**% xETH**", min_value=10, max_value=90, value=xeth3_percentage, disabled=True, key="avs3_dualx")

        st.write("&#8226; **Dual Staking Balance**: {}% $AVS3 : {}% xETH".format(avs3_token_percentage, xeth3_percentage))


        st.write("\n")
        st.write("  \n")
        st.write("\n")



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
        st.markdown('<p class="header-style">$AVS3 Tokenomics [Optional]</p>', unsafe_allow_html=True)

        st.write("  \n")

        avs3_inf_def_rate = st.slider("**$AVS3 Inflation/Deflation Rate**", 
                                    min_value=-50, 
                                    max_value=50, 
                                    value=0,
                                    format="%d%%",
                                    key="avs3_tok")
                                    #help="Slide to set the inflation or deflation rate for $AVS token. -50% indicates deflation, 50% indicates inflation.")

        if avs3_inf_def_rate > 0:
            st.write(f"&#8226; $AVS3 Inflation Rate: {avs3_inf_def_rate}%")
        elif avs3_inf_def_rate < 0:
            st.write(f"&#8226; $AVS3 Deflation Rate: {(avs3_inf_def_rate)}%")

        col3, col4 = st.columns([3, 3])

        with col3:
                avs3_circ_supply = st.number_input("**$AVS3 Circulating Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, help="Circulating Supply should never exceed Total Supply", key="avs3_circ")
                st.write(f"&#8226; Circulating Supply: {avs3_circ_supply:,}")

        with col4:
                avs3_total_supply = st.number_input("**$AVS3 Total Supply**", min_value=0, max_value=1000000000000, value=0, step=1000000, key="avs3_total")
                st.write(f"&#8226; Total Supply: {avs3_total_supply:,}")



        st.write("\n")
        st.write("  \n")
        st.write("\n")

        staker_reward3, operator_reward3 = avs3_rewards(avs3_revenue, tvl3, pre_slash_total_restaked, avs3_token_percentage, xeth3_percentage)

        col70, col71 = st.columns(2)

        with col70:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs3_revenue != 0:
                staker_reward3_percentage = (staker_reward3 / avs3_revenue) * 100
            else:
                staker_reward3_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS3 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{staker_reward3_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col71:
            # Calculate the percentage and handle division by zero
            if pre_slash_total_restaked != 0 and avs3_revenue != 0:
                operator_reward3_percentage = (operator_reward3 / avs3_revenue) * 100
            else:
                operator_reward3_percentage = 0.00

            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">$AVS3 Staker / xETH Restaker Reward: <span style="font-size: 1.3em;">{operator_reward3_percentage:.2f}%</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        st.write("  \n")

        with st.expander("Logic"):
            st.markdown("""
            """)




    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")












































    st.subheader("**2.2 Sharpe Ratios**")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    col95, col96 = st.columns([3,4], gap="large")
    with col95:
        fraction_html = """
            <div style="text-align: center;">
                <span style="font-size: 24px; font-weight: bold;">In-Isolation AVS Sharpe Ratio =  </span>
                <div style="display: inline-block; vertical-align: middle; font-size: 22px; font-weight: bold; text-align: center;">
                    <span>AVS Net Yield  <span style="font-size: 28px;">-</span>  AVS Expected Slash</span><br>
                    <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                    <span>Standard Deviation of Excess Return</span>
                </div>
            </div> """

        st.markdown(fraction_html, unsafe_allow_html=True)

    with col96:
        fractiona_html = """
            <div style="text-align: center;">
                <span style="font-size: 24px; font-weight: bold;">Ecosystem-Aware AVS Sharpe Ratio =  </span>
                <div style="display: inline-block; vertical-align: middle; font-size: 22px; font-weight: bold; text-align: center;">
                    <span>In-Isolation AVS Sharpe Ratio <span style="font-size: 28px;">-</span> Compounded Loss(Ψj)/Actual Slash(δj) Ratio Factor <span style="font-size: 28px;">-</span> AVS Insurance Status Factor</span>
                </div>
            </div> """

        st.markdown(fractiona_html, unsafe_allow_html=True)



    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    def avs_sr_eco(avs1_compounded_loss, avs2_compounded_loss, avs3_compounded_loss, actual_slash_on_cs):
        
        def avs1_comp_vs_actual_slash(avs1_compounded_loss, actual_slash_on_cs):
            if actual_slash_on_cs == 0:
                return 0
            else:
                ratio1 = avs1_compounded_loss / actual_slash_on_cs
            
            if ratio1 > 3:
                return 1
            elif ratio1 > 2:
                return 0.50
            elif ratio1 <= 2:
                return 0.20
            else:
                return 1
            
        def avs2_comp_vs_actual_slash(avs2_compounded_loss, actual_slash_on_cs):
            if actual_slash_on_cs == 0:
                return 0
            else:
                ratio2 = avs2_compounded_loss / actual_slash_on_cs
            
            if ratio2 > 3:
                return 1
            elif ratio2 > 2:
                return 0.50
            elif ratio2 <= 2:
                return 0.20
            else:
                return 1
        
        def avs3_comp_vs_actual_slash(avs3_compounded_loss, actual_slash_on_cs):
            if actual_slash_on_cs == 0:
                return 0
            else:
                ratio3 = avs3_compounded_loss / actual_slash_on_cs
            
            if ratio3 > 3:
                return 1
            elif ratio3 > 2:
                return 0.50
            elif ratio3 <= 2:
                return 0.20
            else:
                return 1

        avs_comp_vs_actual_slash_adj1 = avs1_comp_vs_actual_slash(avs1_compounded_loss, actual_slash_on_cs)
        avs_comp_vs_actual_slash_adj2 = avs2_comp_vs_actual_slash(avs2_compounded_loss, actual_slash_on_cs)
        avs_comp_vs_actual_slash_adj3 = avs3_comp_vs_actual_slash(avs3_compounded_loss, actual_slash_on_cs)

        avs_insurance_adjustment1 = 0 if st.session_state.insurance_statuses['avs1_insurance_status'] == insurance_options[0] else 1
        avs_insurance_adjustment2 = 0 if st.session_state.insurance_statuses['avs2_insurance_status'] == insurance_options[0] else 1
        avs_insurance_adjustment3 = 0 if st.session_state.insurance_statuses['avs3_insurance_status'] == insurance_options[0] else 1

        return avs_comp_vs_actual_slash_adj1, avs_comp_vs_actual_slash_adj2, avs_comp_vs_actual_slash_adj3, avs_insurance_adjustment1, avs_insurance_adjustment2, avs_insurance_adjustment3





    col80, col81, col82 = st.columns(3, gap="large")
    
    avs_comp_vs_actual_slash_adj1, avs_comp_vs_actual_slash_adj2, avs_comp_vs_actual_slash_adj3, avs_insurance_adjustment1, avs_insurance_adjustment2, avs_insurance_adjustment3 = avs_sr_eco(avs1_compounded_loss, avs2_compounded_loss, avs3_compounded_loss, actual_slash_on_cs)

    profit_percentage = 0.20

    with col80:

        avs1_net_yield = avs1_revenue * profit_percentage - staker_reward1 - operator_reward1

        fraction_html1 = f"""
        <div style="text-align: center;">
        <span style="font-size: 22px; font-weight: bold;"> <span style="font-size: 24px;">AVS1</span> Sharpe Ratios</span><br>
        </div>"""

        st.markdown(fraction_html1, unsafe_allow_html=True)
        
        st.write("\n")

        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 15px;
                text-align: center;
                margin: 10px 0;
                background-color: white;">
                <h2 style="color: black; margin:0; padding:0; font-size: 1.2em;">AVS1 Net Yield: <span style="font-size: 1.3em;">${avs1_net_yield:,.0f}</span></h2>
                <p style="color: black; margin:5px 0 0 0; padding:0; font-size: 1em;">
                    (AVS Revenue * Profit Percentage - Staker Reward - Operator Reward)
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")

        col85, col86 = st.columns(2, gap="medium")

        with col85:
            avs1_expected_slash = st.number_input("**AVS1 Expected Slash**", min_value=0, max_value=1000000000000, value=0, step=1000000, key='avs1_es')
            st.write(f"""&#8226; AVS1 Expected Slash: **${avs1_expected_slash:,.0f}**""")

        with col86:
            avs1_st_dev = st.slider("**Standard Deviation of Excess Return**", min_value=5, max_value=10, step=1, format='%d%%', key='avs1_sd', help="AVSs have been benchmarked against bonds, which historically exhibit standard deviations ranging from 5% to 10%. Given the lack of historical data on AVSs, that same logic was applied here. The standard deviations, in absolute terms, were calculated as the product of an AVS net yield by the standard deviation % chosen.")
            avs1_st_dev_abs = avs1_net_yield * (avs1_st_dev/100)
            st.write(f"""&#8226; AVS1 Standard Deviation: **${avs1_st_dev_abs:,.0f}**""")

        st.write("--------")
        st.write("\n")

        st.write("**IN-ISOLATION WEIGHTINGS**")

        col91, col92 = st.columns(2, gap="medium")

        with col91:
            avs1_net_yield_weight = st.slider("**Net Yield Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs1_ny_w")

        with col92:
            avs1_expected_slash_weight = 100 - avs1_net_yield_weight
            st.slider("**Expected Slash Weight**", min_value=10, max_value=90, value=avs1_expected_slash_weight, format='%d%%', disabled=True, key="avs1_es_w")
        
        st.write("\n")
        st.write("\n")

        if avs1_st_dev_abs != 0:
            sharpe_ratio1 = ((avs1_net_yield_weight*0.01 * avs1_net_yield) - (avs1_expected_slash_weight*0.01 * avs1_expected_slash)) / avs1_st_dev_abs
        else:
            sharpe_ratio1 = 0

        fraction_html11 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">In-Isolation AVS1 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">({avs1_net_yield_weight}% * ${avs1_net_yield:,.0f}) - ({avs1_expected_slash_weight}% * ${avs1_expected_slash:,.0f})</span><br>
                    <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                    <span style="font-size: 21px; font-weight: bold;">${avs1_st_dev_abs:,.0f}</span>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {sharpe_ratio1:.2f}</span>
            </div>
        """

        st.markdown(fraction_html11, unsafe_allow_html=True)

        st.write("\n")
        st.write("------")
        st.write("\n")

        st.write("**ECOSYSTEM-AWARE WEIGHTINGS**")
        col93, col94 = st.columns(2, gap="medium")

        with col93:
            avs1_comp_loss_weight = st.slider("**Compounded Loss(Ψ AVS1)/Actual Slash(δj) Ratio Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs1_clac_w")

        with col94:
            avs1_insurance_status_weight = 100 - avs1_comp_loss_weight
            st.slider("**Insurance Status Weight**", min_value=10, max_value=90, value=avs1_insurance_status_weight, format='%d%%', disabled=True, key="avs1_is_w")
        
        st.write("\n")
        st.write("\n")

        eco_sharpe_ratio1 = sharpe_ratio1 - (avs1_comp_loss_weight*0.01 * avs_comp_vs_actual_slash_adj1) - (avs1_insurance_status_weight*0.01 * avs_insurance_adjustment1)

        fraction_html111 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">Ecosystem-Aware AVS1 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">{sharpe_ratio1:.2f} - ({avs1_comp_loss_weight}% * {avs_comp_vs_actual_slash_adj1:.2f}) - ({avs1_insurance_status_weight}% * {avs_insurance_adjustment1:.2f})</span><br>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {eco_sharpe_ratio1:.2f}</span> <!-- replace with actual resulting value -->
            </div>
        """

        st.markdown(fraction_html111, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
                        """)




    with col81:
        
        avs2_net_yield = avs2_revenue * profit_percentage - staker_reward2 - operator_reward2

        fraction_html2 = f"""
        <div style="text-align: center;">
        <span style="font-size: 22px; font-weight: bold;"> <span style="font-size: 24px;">AVS2</span> Sharpe Ratio</span><br>
        </div>"""

        st.markdown(fraction_html2, unsafe_allow_html=True)
        
        st.write("\n")

        st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">AVS2 Net Yield: <span style="font-size: 1.3em;">${avs2_net_yield:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        st.write("\n")

        col87, col88 = st.columns(2, gap="medium")

        with col87:
            avs2_expected_slash = st.number_input("**AVS2 Expected Slash**", min_value=0, max_value=1000000000000, value=0, step=1000000, key='avs2_es')
            st.write(f"""&#8226; AVS2 Expected Slash: **${avs2_expected_slash:,.0f}**""")

        with col88:
            avs2_st_dev = st.slider("**Standard Deviation of Excess Return**", min_value=5, max_value=10, step=1, format='%d%%', key='avs2_sd')
            avs2_st_dev_abs = avs2_net_yield * (avs2_st_dev/100)
            st.write(f"""&#8226; AVS2 Standard Deviation: **${avs2_st_dev_abs:,.0f}**""")


        st.write("--------")
        st.write("\n")

        st.write("**IN-ISOLATION WEIGHTINGS**")

        col91, col92 = st.columns(2, gap="medium")

        with col91:
            avs2_net_yield_weight = st.slider("**Net Yield Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs2_ny_w")

        with col92:
            avs2_expected_slash_weight = 100 - avs2_net_yield_weight
            st.slider("**Expected Slash Weight**", min_value=10, max_value=90, value=avs2_expected_slash_weight, format='%d%%', disabled=True, key="avs2_es_w")
        
        st.write("\n")
        st.write("\n")

        if avs2_st_dev_abs != 0:
            sharpe_ratio2 = ((avs2_net_yield_weight*0.01 * avs2_net_yield) - (avs2_expected_slash_weight*0.01 * avs2_expected_slash)) / avs2_st_dev_abs
        else:
            sharpe_ratio2 = 0

        fraction_html22 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">In-Isolation AVS2 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">({avs2_net_yield_weight}% * ${avs2_net_yield:,.0f}) - ({avs2_expected_slash_weight}% * ${avs2_expected_slash:,.0f})</span><br>
                    <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                    <span style="font-size: 21px; font-weight: bold;">${avs2_st_dev_abs:,.0f}</span>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {sharpe_ratio2:.2f}</span>
            </div>
        """

        st.markdown(fraction_html22, unsafe_allow_html=True)

        st.write("\n")
        st.write("------")
        st.write("\n")

        st.write("**ECOSYSTEM-AWARE WEIGHTINGS**")
        col93, col94 = st.columns(2, gap="medium")

        with col93:
            avs2_comp_loss_weight = st.slider("**Compounded Loss(Ψ AVS2)/Actual Slash(δj) Ratio Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs2_clac_w")

        with col94:
            avs2_insurance_status_weight = 100 - avs2_comp_loss_weight
            st.slider("**Insurance Status Weight**", min_value=10, max_value=90, value=avs2_insurance_status_weight, format='%d%%', disabled=True, key="avs2_is_w")
        
        st.write("\n")
        st.write("\n")

        eco_sharpe_ratio2 = sharpe_ratio2 - (avs2_comp_loss_weight*0.01 * avs_comp_vs_actual_slash_adj2) - (avs2_insurance_status_weight*0.01 * avs_insurance_adjustment2)

        fraction_html222 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">Ecosystem-Aware AVS2 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">{sharpe_ratio2:.2f} - ({avs2_comp_loss_weight}% * {avs_comp_vs_actual_slash_adj2:.2f}) - ({avs2_insurance_status_weight}% * {avs_insurance_adjustment2:.2f})</span><br>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {eco_sharpe_ratio2:.2f}</span> <!-- replace with actual resulting value -->
            </div>
        """

        st.markdown(fraction_html222, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
                        """)



    with col82:

        avs3_net_yield = avs3_revenue * profit_percentage - staker_reward3 - operator_reward3

        fraction_html3 = f"""
        <div style="text-align: center;">
        <span style="font-size: 22px; font-weight: bold;"> <span style="font-size: 24px;">AVS3</span> Sharpe Ratio</span><br>
        </div>"""

        st.markdown(fraction_html3, unsafe_allow_html=True)
        
        st.write("\n")

        st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 5px;
                    padding: 10px;
                    text-align: center;
                    margin: 10px 0;
                    background-color: white;">
                    <h2 style="color: black; margin:0; font-size: 1.2em;">AVS3 Net Yield: <span style="font-size: 1.3em;">${avs3_net_yield:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        st.write("\n")

        col89, col90 = st.columns(2, gap="medium")

        with col89:
            avs3_expected_slash = st.number_input("**AVS3 Expected Slash**", min_value=0, max_value=1000000000000, value=0, step=1000000, key='avs3_es')
            st.write(f"""&#8226; AVS3 Expected Slash: **${avs3_expected_slash:,.0f}**""")

        with col90:
            avs3_st_dev = st.slider("**Standard Deviation of Excess Return**", min_value=5, max_value=10, step=1, format='%d%%', key='avs3_sd')
            avs3_st_dev_abs = avs3_net_yield * (avs3_st_dev/100)
            st.write(f"""&#8226; AVS3 Standard Deviation: **${avs3_st_dev_abs:,.0f}**""")

        st.write("--------")
        st.write("\n")

        st.write("**IN-ISOLATION WEIGHTINGS**")

        col91, col92 = st.columns(2, gap="medium")

        with col91:
            avs3_net_yield_weight = st.slider("**Net Yield Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs3_ny_w")

        with col92:
            avs3_expected_slash_weight = 100 - avs3_net_yield_weight
            st.slider("**Expected Slash Weight**", min_value=10, max_value=90, value=avs3_expected_slash_weight, format='%d%%', disabled=True, key="avs3_es_w")
        
        st.write("\n")
        st.write("\n")

        if avs3_st_dev_abs != 0:
            sharpe_ratio3 = ((avs3_net_yield_weight*0.01 * avs3_net_yield) - (avs3_expected_slash_weight*0.01 * avs3_expected_slash)) / avs3_st_dev_abs
        else:
            sharpe_ratio3 = 0

        fraction_html33 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">In-Isolation AVS3 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">({avs3_net_yield_weight}% * ${avs3_net_yield:,.0f}) - ({avs3_expected_slash_weight}% * ${avs3_expected_slash:,.0f})</span><br>
                    <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                    <span style="font-size: 21px; font-weight: bold;">${avs3_st_dev_abs:,.0f}</span>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {sharpe_ratio3:.2f}</span>
            </div>
        """

        st.markdown(fraction_html33, unsafe_allow_html=True)

        st.write("\n")
        st.write("------")
        st.write("\n")

        st.write("**ECOSYSTEM-AWARE WEIGHTINGS**")
        col93, col94 = st.columns(2, gap="medium")

        with col93:
            avs3_comp_loss_weight = st.slider("**Compounded Loss(Ψ AVS3)/Actual Slash(δj) Ratio Weight**", min_value=10, max_value=90, value=50, format='%d%%', key="avs3_clac_w")

        with col94:
            avs3_insurance_status_weight = 100 - avs3_comp_loss_weight
            st.slider("**Insurance Status Weight**", min_value=10, max_value=90, value=avs3_insurance_status_weight, format='%d%%', disabled=True, key="avs3_is_w")
        
        st.write("\n")
        st.write("\n")

        eco_sharpe_ratio3 = sharpe_ratio3 - (avs3_comp_loss_weight*0.01 * avs_comp_vs_actual_slash_adj3) - (avs3_insurance_status_weight*0.01 * avs_insurance_adjustment3)

        fraction_html333 = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">Ecosystem-Aware AVS3 Ratio:</span><br>
                <div style="display: inline-block; vertical-align: middle; text-align: center;">
                    <span style="font-size: 21px; font-weight: bold;">{sharpe_ratio3:.2f} - ({avs3_comp_loss_weight}% * {avs_comp_vs_actual_slash_adj3:.2f}) - ({avs3_insurance_status_weight}% * {avs_insurance_adjustment3:.2f})</span><br>
                </div>
                <span style="font-size: 24px; font-weight: bold;">= {eco_sharpe_ratio3:.2f}</span> <!-- replace with actual resulting value -->
            </div>
        """

        st.markdown(fraction_html333, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
                        """)
            


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    # Assuming the updated scenario with possible equal values among formatted_result1, formatted_result2, and formatted_result3.

    # Re-organize the results in a dictionary for easier handling
    results = {"AVS1": sharpe_ratio1, "AVS2": sharpe_ratio2, "AVS3": sharpe_ratio3}

    # Check if all values are the same
    if len(set(results.values())) == 1:
        recommendation = "The LRT protocol should expect the <b>same risk-adjusted return on AVS1, AVS2, and AVS3</b>."
    else:
        # Sort the results based on their values
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
        # Group by value to handle equals
        grouped_results = {}
        for avs, value in sorted_results:
            grouped_results.setdefault(value, []).append(avs)
        
        if len(grouped_results) == 2:  # If two groups, one has the greater, other two are equal
            greater_value_group = max(grouped_results.keys())
            smaller_value_group = min(grouped_results.keys())
            
            greater_avs = ', '.join(grouped_results[greater_value_group])
            smaller_avs = ', '.join(grouped_results[smaller_value_group])
            
            if len(grouped_results[greater_value_group]) > 1:  # If the greater group has more than one AVS
                recommendation = f"""
                    <div>
                        <p style="font-size: 18px !important;">The LRT protocol should expect:</p>
                        <p style="font-size: 19px !important;">
                            <b>&#8226; Greater risk-adjusted return by selecting {greater_avs}</b><br>
                            <b>&#8226; Smaller risk-adjusted return by selecting {smaller_avs}</b>
                        </p>
                    </div>
                """
            else:  # If the smaller group has more than one AVS
                recommendation = f"""
                    <div>
                        <p style="font-size: 18px;">The LRT protocol should expect:</p>
                        <p style="font-size: 19px;">
                            <b>&#8226; Greater risk-adjusted return by selecting {greater_avs}</b><br>
                            <b>&#8226; Smaller risk-adjusted return by selecting {smaller_avs}</b>
                        </p>
                    </div>
                """
        else:  # If all values are distinct
                recommendation = f"""
                    <div>
                        <p style="font-size: 18px;">The LRT protocol should expect:</p>
                        <p style="font-size: 19px;">
                            <b>&#8226; Greater risk-adjusted return by selecting {sorted_results[0][0]}</b><br>
                            <b>&#8226; Milder risk-adjusted return by selecting {sorted_results[1][0]}</b><br>
                            <b>&#8226; Smaller risk-adjusted return by selecting {sorted_results[2][0]}</b>
                        </p>
                    </div>
                """

    recommendation_html = f'<div style="font-size: 20px;">{recommendation}</div>'

    st.markdown(recommendation_html, unsafe_allow_html=True)

    st.write("\n")
    st.write("\n")

    st.markdown("""
    **In-Isolation AVS3 Ratio:**

    The Sharpe Ratio results represent the amount of net yield (after accounting for expected slashes) AVSs may earn going forward for each unit of risk, as measured by the standard deviation of those net yields over a previous time period.

    The result of 20 represents the amount of net profit (after accounting for expected losses) earned for each unit of risk, as measured by the standard deviation of returns or profit.

    The denominator of the Sharpe Ratio represents the standard deviation of the portfolio's excess returns, which is a measure of the investment's volatility or risk. Specifically, it quantifies how much the returns of the investment deviate from their average over a certain period. This measure is crucial in the context of the Sharpe Ratio because it provides a way to adjust for risk: by dividing the excess return (the return of the investment minus the risk-free rate) by the standard deviation of these excess returns, the Sharpe Ratio essentially tells you how much excess return you are getting for each unit of risk taken.

    In essence, the denominator of the Sharpe Ratio allows investors to understand the risk-adjusted return of an investment. A higher standard deviation indicates a higher level of risk (since the investment's returns are more spread out from the average), which in turn would require a higher excess return to achieve the same Sharpe Ratio. This helps investors compare investments on a risk-adjusted basis, making it easier to identify which investments are truly outperforming on a risk-adjusted basis rather than simply due to taking on more risk.

    **AVS Reward Emission:**

    The AVS Reward Emission simulator percentage-results suggest how much should be distributed among $AVS Stakers, xETH Restakers, and AVS Operators, given the risk and economic security profile of the AVS. To build on the Assumptions explanation on top, this calculation is based on the correlated reward-to-risk sensitivity per variable input -- the Logic below each input parameter helps understand the underlying rationale.

    Operator Reward is naturally being given greater weight than the Staker Reward due to their paramount role in validating modules crucial to the well-function of an AVS. We've assigned 60% of distributable rewards to Operators and 40% to Stakers and Restakers.

    The $AVS’s Tokenomics (while not included in the reward calculation) were deemed useful to include since they provide a look-ahead perspective of how the native AVS token can influence future rewards. A potential for improved rewards to be emitted in the future exists if a relatively small delta between circulating and total supply and a deflationary token rate exist. Whereas a larger delta and an inflationary token rate indicate the potential for lower rewards to be emitted in the future. An important factor that should help AVS developers determine the $AVS minting rate is that of rewarding operators for their capital costs.

    It's important to bear in mind that this Simulator was built from an AVS perspective alone.
    """, unsafe_allow_html=False)






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
    st.markdown('<p style="font-weight: bold;"><s>&#8226; Operator Performance Reputation</s></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Collateralization & <s>Node Centralization Risk Levels</s></p>', unsafe_allow_html=True)
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