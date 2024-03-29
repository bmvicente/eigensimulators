
# Naive & Mal Op

# CoC = Stake / 3
# PfC = TVL



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
        risk_factor = (90 + 10)  # This will give the same value as when risk_score is 9
    else:
        risk_factor = (risk_score + 10)

    slashing_amount = (pre_slash_total_restaked / 3) * (risk_factor / 100)
    return slashing_amount




def main():

    st.set_page_config(layout="wide")


    if 'operator_stake' not in st.session_state:
        st.session_state.operator_stake = 0


    # Initialize session state variables
    if 'pre_slash_total_restaked' not in st.session_state:
        st.session_state.pre_slash_total_restaked = 0


    if 'risk_score1' not in st.session_state:
        st.session_state.risk_score1 = 0  # or any default value
    if 'risk_score2' not in st.session_state:
        st.session_state.risk_score2 = 0  # or any default value
    if 'risk_score3' not in st.session_state:
        st.session_state.risk_score3 = 0  # or any default value


    pre_slash_total_restaked = st.session_state.pre_slash_total_restaked


    potential_total_slashing1 = calculate_slashing(st.session_state.pre_slash_total_restaked, st.session_state.risk_score1)
    potential_total_slashing2 = calculate_slashing(st.session_state.pre_slash_total_restaked, st.session_state.risk_score2)
    potential_total_slashing3 = calculate_slashing(st.session_state.pre_slash_total_restaked, st.session_state.risk_score3)
    

    #st.image("images/renzo1.png", width=400)
    st.write("  \n")

    st.title("Cryptoeconomic Risk Analysis III")
    st.subheader("**AVS <> Operator Potential Slashing Event Simulator:** *Naïve Approach* & *Malicious Operator*")
    
    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
                    The main goal of the Simulator is to demonstrate how the Risk Profile of AVSs may influence the potential slashing an Operator may face, and how such a slash to the Operator would, in turn, affect the AVSs individually.

                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property. 
                    This is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security.
                    A core idea of EigenLayer is to provision cryptoeconomic security through various slashing mechanisms which levy a high cost of corruption.
                    
                    We begin by assuming that the 3 AVS herein are equally secured by the Total Amount Restaked, therefore each has 33.33% "distribution".
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
    

    st.session_state.pre_slash_coc = st.session_state.pre_slash_total_restaked / 3

    pre_slash_max_slash_allowed_calc = max(0, st.session_state.pre_slash_coc - st.session_state.pre_slash_pfc)
    pre_slash_max_slash_allowed = pre_slash_max_slash_allowed_calc * 3

    actual_stake_loss = max(0, st.session_state.pre_slash_total_restaked - st.session_state.post_slash_total_restaked)

    col20,col21 = st.columns(2, gap="medium")





    ########## PRE-SLASH ##########
    with col20:
        st.markdown('<p class="header-style" style="font-size: 20px;">PRE-SLASH (t)</p>', unsafe_allow_html=True)

        st.write("\n")

        st.markdown('<p class="header-style" style="font-size: 18px;">Total Amount Restaked on AVS Ecosystem (Tt)</p>', unsafe_allow_html=True)

        st.session_state.pre_slash_total_restaked = create_total_restaked_input()
        formatted_value = "${:,.0f}".format(st.session_state.pre_slash_total_restaked)
        
        st.write(f"""&#8226; Total Restaked: {formatted_value}""")
        
        if st.session_state.pre_slash_total_restaked >= 10000000000:  # 10 billion
            st.markdown(f'<span style="color: red; font-weight: bold">Even though the conditions for cryptoeconomic security may not be satisfied, a large enough amount of stake is a strong determinant of the security and liveness of a PoS blockchain, to the point where no attack is warranted.</span>', unsafe_allow_html=True)
        
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
                                <span style="font-size: 1.2em;">α<sub style="font-size: 0.8em;">jt</sub></span> &nbsp; | &nbsp;
                                Max Total Stake Loss "Allowed" To Maintain Cryptoeconomic Security: <span style="font-size: 1.1em;">${pre_slash_max_slash_allowed:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )


    ########## POST-SLASH ##########
    with col21:
        st.markdown('<p class="header-style" style="font-size: 20px;">POST-SLASH (t+1)</p>', unsafe_allow_html=True)

        st.session_state.post_slash_total_restaked = pre_slash_total_restaked - st.session_state.op_stake_slashable
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
                    Total Amount Restaked on AVS Ecosystem (T t+1)<span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.post_slash_total_restaked:,.0f}</span>
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
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 5px;
                        text-align: center;
                        margin: 5px 0;
                        background-color: white;">
                        <h2 style="color: black; margin: 0; font-size: 1.1em;">
                            <div style="display: block;">
                                <span style="font-size: 1.2em;">&Theta;<sub style="font-size: 0.8em;">ijt+1</sub></span> &nbsp; | &nbsp;
                                Actual Stake Loss: <span style="font-size: 1.1em;">${actual_stake_loss:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            
    st.write("\n")

    with st.expander("Logic"):
            st.markdown(f"""
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


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
                border-radius: 1px;
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

        # Format the operator_stake value as currency with a dollar sign and commas
        formatted_operator_stake = "${:,.0f}".format(operator_stake)

        st.write(f"""&#8226; Operator Stake: {formatted_operator_stake}""")

        with st.expander("Logic"):
            st.markdown(f"""
                    """)


        st.write("\n")
        st.write("\n")
        st.write("\n")


        st.session_state.operator_stake = operator_stake

        st.write("\n")
        st.write("\n")

        
        st.markdown('<p class="header-style">Operator Stake % To Be Slashed</p>', unsafe_allow_html=True)

        op_stake_perc_slashable = st.slider('', min_value=0, max_value=100, value=100, format='%d%%')

        st.session_state.op_stake_slashable = operator_stake * op_stake_perc_slashable * 0.01
        
        st.write(f"""• Slashable Operator Stake Amount: ${st.session_state.op_stake_slashable:,.0f}""")

        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
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
                border-radius: 2px;
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

        # Dropdown menu
        col3, col4 = st.columns([3, 3])

        with col3:
                st.session_state.risk_score1 = create_risk_score_input('risk_score1', "**AVS Risk Score**")

        with col4:
                tvl1 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=st.session_state.tvl1, step=10000000,
                                              help=f"""TVL was included to establish the CoC vs PfC threshold and calculate the "allowed" slashing amount to still maintain AVS security.""")

                formatted_tvl1 = "${:,.0f}".format(tvl1)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl1}""")


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
                    <div style="display: block; margin-top: 5px;">
                        Potential Max Stake Loss from Operator Attack based on Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing1:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("\n")


        with st.expander("Logic"):
            st.markdown("""
                **ΩAVS1**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                if risk_score == 10:
                    risk_factor = (9 + 1) * 10
                else:
                    risk_factor = (risk_score + 1) * 10
                
                slashing_amount = (total_restaked / 3) * (risk_factor / 100)
                return slashing_amount
                ```
                ```python
                potential_total_slashing1 = calculate_slashing(total_restaked, risk_score1)
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

        col8, col9 = st.columns([3, 3])

        with col8:
                st.session_state.risk_score2 = create_risk_score_input('risk_score2', "**AVS Risk Score** ")

        with col9:
                tvl2 = st.number_input("**AVS TVL** ", min_value=0, max_value=10000000000000, value=st.session_state.tvl2, step=10000000)

                formatted_tvl2 = "${:,.0f}".format(tvl2)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl2}""")
        
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
                        Potential Max Stake Loss from Operator Attack based on Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing2:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


        st.write("\n")

    
        with st.expander("Logic"):
            st.markdown("""
                **ΩAVS2**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                if risk_score == 10:
                    risk_factor = (9 + 1) * 10
                else:
                    risk_factor = (risk_score + 1) * 10
                
                slashing_amount = (total_restaked / 3) * (risk_factor / 100)
                return slashing_amount
                ```
                ```python
                potential_total_slashing2 = calculate_slashing(total_restaked, risk_score2)
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

        col13, col14 = st.columns([3, 3])

        with col13:
                st.session_state.risk_score3 = create_risk_score_input('risk_score3', "**AVS Risk Score**  ")

        with col14:
                tvl3 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=st.session_state.tvl3, step=10000000)
                formatted_tvl3 = "${:,.0f}".format(tvl3)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl3}""")
        
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
                        Potential Max Stake Loss from Operator Attack based on Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing3:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")
    

        with st.expander("Logic"):
            st.markdown("""
                **ΩAVS3**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                if risk_score == 10:
                    risk_factor = (9 + 1) * 10
                else:
                    risk_factor = (risk_score + 1) * 10
                
                slashing_amount = (total_restaked / 3) * (risk_factor / 100)
                return slashing_amount
                ```
                ```python
                potential_total_slashing3 = calculate_slashing(total_restaked, risk_score3)
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    st.session_state.pre_slash_pfc = tvl1 + tvl2 + tvl3



    ###################
    ####### BST #######
    ###################

    st.markdown(
        """
        <div style="text-align: center; font-size: 22px; font-weight: bold">
            <span>POST-SLASH Aftermath:</span> BYZANTINE <i>SLASHING</i> TOLERANCE TEST
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
            f"""
            <div style="
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0; font-size: 1.5em;">
                    <div style="display: block;">
                        <span style="font-weight: bold; font-size: 1.5em;">
                            &beta;<sub style="font-size: 0.8em;">ijt</sub> = 
                            &alpha;<sub style="font-size: 0.8em;">jt</sub> - 
                            &theta;<sub style="font-size: 0.8em;">ijt+1</sub>
                        </span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.write("\n")
    st.write("\n")


    bst_avs1 = pre_slash_max_slash_allowed - actual_stake_loss

    if bst_avs1 < 0:
                color = "#d32f2f"  # Red color for negative value
                background_color = "#fde0dc"  # Light red background
    elif 0 < bst_avs1 <= 20000000:  # Condition for values between 0 and 20 million
                color = "#FB8C00"  # Orange color
                background_color = "#FFE0B2"  # Light orange background
    elif bst_avs1 > 20000000:
                color = "#388e3c"  # Green color for positive value
                background_color = "#ebf5eb"  # Light green background
    else:  # This will be for bst_avs3 exactly equal to 0
                color = "black"  # Black color for zero
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
                        <div style="color: black; margin:0; font-size: 1.6em; font-weight: bold;">
                            AVS Ecosystem
                        </div>
                        <div style="color: black; font-size: 1.3em; margin-top: 1px; font-weight: bold;">
                            ${pre_slash_max_slash_allowed:,.0f} - ${actual_stake_loss:,.0f} = <span style="font-size: 1.3em; color: {color};">${bst_avs1:,.0f}</span>
                        </div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )

    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.markdown(f"""
        <div style="font-size: 1.1em;"> <!-- Adjust the font size as needed -->
            The Byzantine <i>Slashing</i> Tolerance test helps identify the AVSs that are in a compromisable state due to a previously-executed Operator slashing event, which may induce an intermediate- or max-loss risk to the ecosystem.
            <br>
            We say that an AVS has failed the BST test if β < 0, and passed if β > 0.
            <br>
            <br>
            In the above boxes, the green background represents a comfortable AVS tolerance in the case of a slashing event, the orange background represents a warning signal for a potential AVS failure, and the red background represents a danger signal where the AVS is in a very compromisable position, ripe for corruption.
        </div>
    """, unsafe_allow_html=True)



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
    st.markdown('<p style="font-weight: bold;">&#8226; Visualization of Compounded Risk Propagation in AVS Ecosystem</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Multiple Operators Restaked Into Multiple AVSs + Entrenchment Risk Level</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; display: inline;">&#8226; Slashing Risks Based on AVS Nature</p><span style="font-weight: normal; display: inline;"> (DA, keeper networks, oracles, bridges, etc.)</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Stakesure&#39;s Parameters <span style="font-weight: normal;">(Post-Slashing Insurance & Reserves)</span>', unsafe_allow_html=True)


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

