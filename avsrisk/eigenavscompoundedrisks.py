
# EigenLayer AVS Compounded Risks

import pandas as pd
import streamlit as st


def avs_compounded_risk(operator_stake, perc_stake_avs_1, perc_stake_avs_2, perc_stake_avs_3, op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3, op_int_loss_avs1, op_int_loss_avs2, op_int_loss_avs3):

    stake_avs_1 = operator_stake * (perc_stake_avs_1 * 0.01)
    stake_avs_2 = operator_stake * (perc_stake_avs_2 * 0.01)
    stake_avs_3 = operator_stake * (perc_stake_avs_3 * 0.01)

    def calculate_op_max_loss_avss(op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3):
        return op_max_loss_avs1 + op_max_loss_avs2 + op_max_loss_avs3

    def calculate_op_int_loss_avss(op_int_loss_avs1, op_int_loss_avs2, op_int_loss_avs3):
        return (op_int_loss_avs1 + op_int_loss_avs2 + op_int_loss_avs3) * 2/3

    op_max_loss_avss = calculate_op_max_loss_avss(op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3)
    op_int_loss_avss = calculate_op_int_loss_avss(op_int_loss_avs1, op_int_loss_avs2, op_int_loss_avs3)

    return(op_max_loss_avss, op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3,op_int_loss_avss, op_int_loss_avs1, op_int_loss_avs2, op_int_loss_avs3,
            operator_stake, stake_avs_1, stake_avs_2, stake_avs_3)



def create_perc_stake_inputs(col_avs_1, col_avs_2, col_avs_3):

    perc_stake_avs_1 = st.session_state.perc_stake_avs_1
    perc_stake_avs_2 = st.session_state.perc_stake_avs_2
    perc_stake_avs_3 = st.session_state.perc_stake_avs_3

    with col_avs_1:
        perc_stake_avs_1 = st.number_input(
            "**% Staked on AVS 1**",
            min_value=0,
            max_value=100,
            step=10,
            help="Percentages must = 100%",
            key="perc_stake_avs_1"  # Unique key for AVS 1
        )
    
    with col_avs_2:
        perc_stake_avs_2 = st.number_input(
            "**% Staked on AVS 2**",
            min_value=0,
            max_value=100,
            step=10,
            key="perc_stake_avs_2"  # Unique key for AVS 1

        )
    
    with col_avs_3:
        perc_stake_avs_3 = st.number_input(
            "**% Staked on AVS 3**",
            min_value=0,
            max_value=100,
            step=10,
            key="perc_stake_avs_3"  # Unique key for AVS 1
        )
        
    return perc_stake_avs_1, perc_stake_avs_2, perc_stake_avs_3


def create_total_restaked_input():
    if 'total_restaked' not in st.session_state:
        st.session_state.total_restaked = 0  # Default value

    total_restaked = st.number_input(
        "",
        min_value=0,
        max_value=10000000000000,
        value=st.session_state.total_restaked,
        step=100000000
    )

    return total_restaked


def create_risk_score_input(risk_score_key, label):
    if risk_score_key not in st.session_state:
        st.session_state[risk_score_key] = 0  # Default value

    risk_score = st.number_input(
        label,
        min_value=0,
        max_value=10,
        value=st.session_state[risk_score_key],
        step=1
    )

    return risk_score


def calculate_slashing(total_restaked, risk_score):

    risk_factor = (risk_score + 1) * 10
    slashing_amount = (total_restaked / 3) * (risk_factor / 100)
    return slashing_amount


def main():
    st.set_page_config(layout="wide")

    if 'perc_stake_avs_1' not in st.session_state:
        st.session_state.perc_stake_avs_1 = 0  # or any default value
    if 'perc_stake_avs_2' not in st.session_state:
        st.session_state.perc_stake_avs_2 = 0  # or any default value
    if 'perc_stake_avs_3' not in st.session_state:
        st.session_state.perc_stake_avs_3 = 0  # or any default value


    if 'operator_stake' not in st.session_state:
        st.session_state.operator_stake = 0


    # Initialize session state variables
    if 'total_restaked' not in st.session_state:
        st.session_state.total_restaked = 0


    if 'risk_score1' not in st.session_state:
        st.session_state.risk_score1 = 0  # or any default value
    if 'risk_score2' not in st.session_state:
        st.session_state.risk_score2 = 0  # or any default value
    if 'risk_score3' not in st.session_state:
        st.session_state.risk_score3 = 0  # or any default value


    total_restaked = st.session_state.total_restaked


    potential_total_slashing1 = calculate_slashing(st.session_state.total_restaked, st.session_state.risk_score1)
    potential_total_slashing2 = calculate_slashing(st.session_state.total_restaked, st.session_state.risk_score2)
    potential_total_slashing3 = calculate_slashing(st.session_state.total_restaked, st.session_state.risk_score3)
    

    #st.image("images/eigenimage.png")

    st.title("Operator/Restaker Potential Slashing Event & AVS Ecosystem Risk Simulator")
    
    st.write("  \n")

    with st.expander("How this Simulator Works"):
        st.markdown("""
                        """)
    
    st.write("**Note**: Except where otherwise specified, all values displayed are in USD.")


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
                background-color: #007bff;"> <!-- Blue background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">OPERATOR</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")


        col35, col36 = st.columns(2)

        with col35:

            # Use the custom styled headers in your markdown
            st.markdown('<p class="header-style">Operator Amount Staked</p>', unsafe_allow_html=True)

            if isinstance(st.session_state.operator_stake, tuple):
                    operator_stake = st.number_input("", min_value=0, max_value=1000000000000, value=int(st.session_state.operator_stake[0]), step=10000000)
            else:
                    operator_stake = st.number_input("", min_value=0, max_value=1000000000000, value=int(st.session_state.operator_stake), step=10000000)

            # Format the operator_stake value as currency with a dollar sign and commas
            formatted_operator_stake = "${:,.0f}".format(operator_stake)


            with st.expander("Logic"):
                st.markdown(f"""
                    &#8226; Operator Stake: {formatted_operator_stake}""")

        with col36:

            # Displaying the custom styled header
            st.markdown('<p class="header-style">Operator Reputation [Soon]</p>', unsafe_allow_html=True)

            # Select slider for average operator reputation
            operator_reputation = st.selectbox("", ["Unknown", "Established", "Renowned"])

            # The expander with more information (optional)
            with st.expander("Logic"):
                st.markdown("""
                    Not accounted for in the calculations, as of now.
                            """)

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
        st.markdown('<p class="header-style">Operator % Staked Across AVSs</p>', unsafe_allow_html=True)

        st.write("  \n")

        col_avs_1, col_avs_2, col_avs_3 = st.columns(3)

        perc_stake_avs_1, perc_stake_avs_2, perc_stake_avs_3 = create_perc_stake_inputs(col_avs_1, col_avs_2, col_avs_3)

        op_max_loss_avs1 = potential_total_slashing1 * perc_stake_avs_1 * 0.01
        op_max_loss_avs2 = potential_total_slashing2 * perc_stake_avs_2 * 0.01
        op_max_loss_avs3 = potential_total_slashing3 * perc_stake_avs_3 * 0.01

        op_int_loss_avs1 = potential_total_slashing1 * perc_stake_avs_1 * 2/3 * 0.01
        op_int_loss_avs2 = potential_total_slashing2 * perc_stake_avs_2 * 2/3 * 0.01
        op_int_loss_avs3 = potential_total_slashing3 * perc_stake_avs_3 * 2/3 * 0.01


        (
            op_max_loss_avss, 
            op_max_loss_avs1, 
            op_max_loss_avs2, 
            op_max_loss_avs3, 
            op_int_loss_avss, 
            op_int_loss_avs1, 
            op_int_loss_avs2, 
            op_int_loss_avs3, 
            operator_stake, 
            stake_avs_1, 
            stake_avs_2, 
            stake_avs_3
        ) = avs_compounded_risk(
            operator_stake,
            perc_stake_avs_1,
            perc_stake_avs_2,
            perc_stake_avs_3,
            op_max_loss_avs1,
            op_max_loss_avs2,
            op_max_loss_avs3,
            op_int_loss_avs1,
            op_int_loss_avs2,
            op_int_loss_avs3
        )



        st.session_state.operator_stake = operator_stake



        col18, col19, col20 = st.columns([3, 3, 3])

        with col18:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Amount Staked on <i>AVS 1</i>: <span style="font-size: 1.1em;">{stake_avs_1:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        with col19:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Amount Staked on <i>AVS 2</i>: <span style="font-size: 1.1em;">{stake_avs_2:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col20:
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Amount Staked on <i>AVS 3</i>: <span style="font-size: 1.1em;">{stake_avs_3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        with st.expander("Logic"):
            st.markdown("""
                """)


        st.write("\n")
        st.write("\n")
        st.write("\n")

        
        st.markdown('<p class="header-style">Operator Potential Slashes Across AVSs</p>', unsafe_allow_html=True)

        st.write("\n")

        col30, col31 = st.columns([7, 8])

        with col30:


            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 1</i>: <span style="font-size: 1.1em;">{op_max_loss_avs1:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 2</i>: <span style="font-size: 1.1em;">{op_max_loss_avs2:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 3</i>: <span style="font-size: 1.1em;">{op_max_loss_avs3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col31:

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Potential Slash on <i>AVS 1</i>: <span style="font-size: 1.1em;">{op_int_loss_avs1:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Potential Slash on <i>AVS 2</i>: <span style="font-size: 1.1em;">{op_int_loss_avs2:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Potential Slash on <i>AVS 3</i>: <span style="font-size: 1.1em;">{op_int_loss_avs3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        col21, col22 = st.columns([7, 8])


        with col21:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1.1em;">Total Max Potential Slash Across AVSs: {op_max_loss_avss:,.0f}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col22:
            st.markdown(
                f"""
                <div style="
                    border: 2px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1.1em;">Total Intermediate Potential Slash Across AVSs: {op_int_loss_avss:,.0f}</h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        with st.expander("Logic"):
            st.markdown("""
                """)
        
        st.write("\n")
        st.write("\n")


        st.markdown('<p class="header-style">How collateralized is this Operator?</p>', unsafe_allow_html=True)


        # Over- & Undercollateralization

        if operator_stake != 0 and op_max_loss_avss != 0:
            fraction_result = operator_stake / op_max_loss_avss
            difference_result = operator_stake - op_max_loss_avss
            
            difference_result1 = stake_avs_1 - op_max_loss_avs1
            difference_result2 = stake_avs_2 - op_max_loss_avs2
            difference_result3 = stake_avs_3 - op_max_loss_avs3

            formatted_fraction = "{:.2f}".format(fraction_result)  # Format the result to 2 decimal places

            if difference_result > 0:
                collat_status = "overcollateralized"
                color = "green"
            elif difference_result < 0:
                collat_status = "undercollateralized"
                color = "red"
            else:
                collat_status = "properly collateralized"
                color = "black"  # Default color

            formatted_difference = '**${:,.0f} USD**'.format(abs(difference_result))
            
            formatted_difference1 = '**${:,.0f} USD**'.format(abs(difference_result1))
            formatted_difference2 = '**${:,.0f} USD**'.format(abs(difference_result2))
            formatted_difference3 = '**${:,.0f} USD**'.format(abs(difference_result3))

            formatted_difference_colored = f'<span style="color: {color};">{formatted_difference}</span>'
            
            formatted_difference_colored1 = f'<span style="color: {color};">{formatted_difference1}</span>'
            formatted_difference_colored2 = f'<span style="color: {color};">{formatted_difference2}</span>'
            formatted_difference_colored3 = f'<span style="color: {color};">{formatted_difference3}</span>'


            st.markdown(f"""
                        - The Operator is **{collat_status}** by {formatted_difference_colored1} on AVS 1.
                        - The Operator is **{collat_status}** by {formatted_difference_colored2} on AVS 2.
                        - The Operator is **{collat_status}** by {formatted_difference_colored3} on AVS 3.
                        
                        The Operator is overall **{collat_status}** by {formatted_difference_colored}. 
                        The *Operator Amount Staked / Max Potential Slash* ratio = **{formatted_fraction}** (a result above 1 suggests the Operator is overcollateralized, and below 1 undercollateralized).""", unsafe_allow_html=True)
        else:
            st.write("Operator Stake or Max Potential Slash are zero, cannot calculate collateralization.")












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
                background-color: #007bff;"> <!-- Blue background color -->
                <h2 class='large-header-style' style="color: white; margin:0;">AVSs</h2> <!-- Larger font for AVSs -->
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")

        # Use the custom styled headers in your markdown
        st.markdown('<p class="header-style">Total Amount Restaked Across AVSs 1, 2 & 3</p>', unsafe_allow_html=True)

        st.session_state.total_restaked = create_total_restaked_input()
        formatted_value = "${:,.0f}".format(st.session_state.total_restaked)

        with st.expander("Logic"):
            st.markdown(f"""
                &#8226; Total Restaked: {formatted_value}""")
            
        st.write("\n")



        #############################################
        ################### AVS 1 ###################
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

            # Displaying the custom styled header
        st.markdown('<p class="header-style">AVS 1</p>', unsafe_allow_html=True)

        st.write("  \n")

        # Dropdown menu
        col3, col4 = st.columns([3, 3])

        with col3:
                st.session_state.risk_score1 = create_risk_score_input('risk_score1', "**AVS Risk Score**")

        with col4:
                tvl1 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=0, step=10000000,
                                              help=f"""TVL was included to establish the CoC vs PfC threshold and calculate the "allowed" slashes to maintain AVS security.""")

                formatted_tvl1 = "${:,.0f}".format(tvl1)


        max_eth_loss_allowed1 = total_restaked - 2*tvl1
        int_eth_loss_allowed1 = total_restaked - 3*tvl1


        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="color: black; margin:0; font-size: 1em;">Potential Slashing based on Risk Profile: <span style="font-size: 1.1em;">{potential_total_slashing1:,.0f}</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
            )

        with st.expander("Logic"):
                st.markdown(f"""
                    &#8226; AVS 1 TVL: {formatted_tvl1}""")
            
        
        st.write("\n")
        st.write(f"""&#8226; **"Byzantine Slashing Tolerance" Test**: AVS 1 Max "Allowed" Slashes vs Max Potential Operator Slashes""")
            
        col6, col7 = st.columns([10, 6])

        with col6: 

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Slash "Allowed" To Still Maintain Security: <span style="font-size: 1.1em;">{max_eth_loss_allowed1:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Slash "Allowed" to Maintain Relaxed Security: <span style="font-size: 1.1em;">{int_eth_loss_allowed1:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
        
        with col7:

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Operator Slash: <span style="font-size: 1.1em;">{op_max_loss_avs1:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;"> Intermediate Potential Operator Slash: <span style="font-size: 1.1em;">{op_int_loss_avs1:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
                """)
            
        
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
                tvl2 = st.number_input("**AVS TVL** ", min_value=0, max_value=10000000000000, value=0, step=10000000)

                formatted_tvl2 = "${:,.0f}".format(tvl2)

        max_eth_loss_allowed2 = total_restaked - 2*tvl2
        int_eth_loss_allowed2 = total_restaked - 3*tvl2


        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="color: black; margin:0; font-size: 1em;">Potential Slashing based on Risk Profile: <span style="font-size: 1.1em;">{potential_total_slashing2:,.0f}</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
            )

        with st.expander("Logic"):
                st.markdown(f"""
                    &#8226; AVS 2 TVL: {formatted_tvl2}""")

        st.write("\n")
        st.write(f"""&#8226; **"Byzantine Slashing Tolerance" Test**: AVS 2 Max "Allowed" Slashes vs Max Potential Operator Slashes""")


        col11, col12 = st.columns([10, 6])

        with col11: 

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Slash "Allowed" To Still Maintain Security: <span style="font-size: 1.1.em;">{max_eth_loss_allowed2:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Slash "Allowed" to Maintain Relaxed Security: <span style="font-size: 1.1em;">{int_eth_loss_allowed2:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
        
        with col12: 

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Operator Slash: <span style="font-size: 1.1em;">{op_max_loss_avs2:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Potential Operator Slash: <span style="font-size: 1.1em;">{op_int_loss_avs2:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
                """)
        
        
        ###################
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
                tvl3 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=0, step=10000000)
                formatted_tvl3 = "${:,.0f}".format(tvl3)

        max_eth_loss_allowed3 = total_restaked - 2*tvl3
        int_eth_loss_allowed3 = total_restaked - 3*tvl3

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="color: black; margin:0; font-size: 1em;">Potential Slashing based on Risk Profile: <span style="font-size: 1.1em;">{potential_total_slashing3:,.0f}</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
            )

        with st.expander("Logic"):
                st.markdown(f"""
                    &#8226; AVS 3 TVL: {formatted_tvl3}""")
            

        st.write("\n")
        st.write(f"""&#8226; **"Byzantine Slashing Tolerance" Test**: AVS 3 Max "Allowed" Slashes vs Max Potential Operator Slashes""")


        col16, col17 = st.columns([10, 6])

        with col16: 

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Slash "Allowed" To Still Maintain Security: <span style="font-size: 1.1em;">{max_eth_loss_allowed3:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Slash "Allowed" to Maintain Relaxed Security: <span style="font-size: 1.1em;">{int_eth_loss_allowed3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
        
        with col17:

            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Operator Slash: <span style="font-size: 1.1em;">{op_max_loss_avs3:,.0f}</span></h2>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Intermediate Potential Operator Slash: <span style="font-size: 1.1em;">{op_int_loss_avs3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
                """)





#########################################
#########################################
#########################################

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    
    st.markdown('<p class="header-style">AVS ECOSYSTEM RISK</p>', unsafe_allow_html=True)
    st.write("  \n")

    st.write(f"""
             Let us take the scenario of the Max Slash event:

             - Actual Total Loss? What does this mean really?
             - Probability of all 3 AVSs failing? p(AVS1) * p(AVS2) * p(AVS3)
             - How to visualize compounded risks that may exist. How AVS1 could affect 2 and 3? Visual Tool? Detail scenarios (in writing too)
                """)
    

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    col40, col41 = st.columns(2)

    with col40:
        st.markdown('<p class="header-style">AVSs RISK PROFILES BEFORE & AFTER MAX SLASH EVENT</p>', unsafe_allow_html=True)
        st.write("  \n")
        average_risk_score = (st.session_state.risk_score1 + st.session_state.risk_score2 + st.session_state.risk_score3) / 3

        st.write(f"""
                    **Risk Scores *Before* Max Slash Event**
                    - AVS 1 Risk Score: {st.session_state.risk_score1} 
                    - AVS 2 Risk Score: {st.session_state.risk_score2} 
                    - AVS 3 Risk Score: {st.session_state.risk_score3} 
                    - Average AVSs Risk Score: ***{average_risk_score:.2f}***

                    **Risk Scores *After* Max Slash Event**
                    - AVS 1 Risk Score: ...
                    - AVS 2 Risk Score: ...
                    - AVS 3 Risk Score: ...
                    - Average AVSs Risk Score: ***...***
                    """)
        
    with col41:
            st.markdown('<p class="header-style">ECOSYSTEM SHARPE RATIOS</p>', unsafe_allow_html=True)
            st.markdown('<p class="header-style">Three Risk-Adjusted Reward Scenarios: Operator to AVS, Restaker to Operator, Restaker to AVS</p>', unsafe_allow_html=True)
            st.write("  \n")
            st.write(f"""
                    - **Operator/AVS Sharpe Ratio**: ...
                    - **Restaker/Operator Sharpe Ratio**: ...
                    - **Restaker/AVS Sharpe Ratio**: ...
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




    st.markdown('<p class="header-style">GAME THEORY MATRIX</p>', unsafe_allow_html=True)
    st.markdown('<p class="header-style">Operator Decision-Making on AVS Restaking Allocation Based on Slashing Likelihood</p>', unsafe_allow_html=True)
    st.write("*NS: Non-Slashing Event | S: Slashing Event*")

    st.write("  \n")


    # Create the DataFrame from the data
    data = {
        'Strategies': ["1", "2", "3", "4", "5", "6", "7", "8"],
        'AVS 1': ["NS", "NS", "NS", "NS", "S", "S", "S", "S"],
        'AVS 2': ["NS", "NS", "S", "S", "NS", "NS", "S", "S"],
        'AVS 3': ["NS", "S", "NS", "S", "NS", "S", "NS", "S"],
        'Pay-Off': ["...", "...", "...", "...", "...", "...", "...", "..."]
    }

    df = pd.DataFrame(data)
    st.table(df)

    st.markdown("2<sup>3</sup> = 8 possible scenarios that can affect the Operator with a pool of 3 AVSs to validate.", unsafe_allow_html=True)


    st.write("  \n")

    with st.expander("Logic"):
            st.markdown("""Add in cooperative, non-zero-sum, etc game...
                """)
    
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")





    #col11, col12, col13 = st.columns([2,1,2])

    #with col11:
    #    st.write("")

    #with col12:
    #    #st.image("images/tokensight.png", width=250)

    #with col13:
    #    st.write("")
    
    
    #image_url = 'https://img.freepik.com/free-vector/twitter-new-2023-x-logo-white-background-vector_1017-45422.jpg'
    #link = 'https://twitter.com/tokensightxyz'
    #markdown = f"""
    #<a href="{link}" target="_blank">
    #    <img src="{image_url}" alt="Alt Text" style="display:block; margin-left: auto; margin-right: auto; width: 4%;">
    #</a>
    #"""    
    #st.markdown(markdown, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

