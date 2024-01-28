
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
    if risk_score == 10:
        risk_factor = (9 + 1) * 10  # This will give the same value as when risk_score is 9
    else:
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
    

    st.image("images/eigenimage.png")

    st.title("Cryptoeconomic Risk Analysis II")
    st.subheader("**Staker Potential Slashing Event Simulator**")
    
    st.write("  \n")

    with st.expander("How this Simulator Works"):
        st.markdown("""
                    We assume that the 3 AVSs are equally secured by the Total Amount Restaked, therefore each has 33% distribution.

                    Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property. 
                    This is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security.
                     A core idea of EigenLayer is to provision cryptoeconomic security through various slashing mechanisms which levy a high cost of corruption.
                    
                    We begin by assuming that the 3 AVS in this Simulator have an equal Total Restaked Amount distributed between them, therefore 33%.
                        """)
        

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
                background-color: #007bff;"> <!-- Blue background color -->
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
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1em;">γ<sub style="font-size: 0.9em;">i AVS1</sub></span>
                        </div>
                        <div style="display: block;">
                            <br> <!-- Extra space -->
                        </div>
                        <div style="display: block;">
                            Own Amount Staked on <i>AVS 1</i>: <span style="font-size: 1.1em;">${stake_avs_1:,.0f}</span>
                        </div>
                    </h2>
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
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1em;">γ<sub style="font-size: 0.9em;">i AVS2</sub></span>
                        </div>
                        <div style="display: block;">
                            <br> <!-- Extra space -->
                        </div>
                        <div style="display: block;">
                            Own Amount Staked on <i>AVS 2</i>: <span style="font-size: 1.1em;">${stake_avs_2:,.0f}</span>
                        </div>
                    </h2>
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
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1em;">γ<sub style="font-size: 0.9em;">i AVS3</sub></span>
                        </div>
                        <div style="display: block;">
                            <br> <!-- Extra space -->
                        </div>
                        <div style="display: block;">
                            Own Amount Staked on <i>AVS 3</i>: <span style="font-size: 1.1em;">${stake_avs_3:,.0f}</span>
                        </div>
                    </h2>
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
        st.write("\n")

        
        st.markdown('<p class="header-style">Operator Potential Slashes Across AVSs</p>', unsafe_allow_html=True)

        col30, col31 = st.columns([7, 8])

        with col30:

            st.markdown(
                f"""
                <div style="
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.2em;">
                        <div style="display: block;">
                            <span style="font-size: 1.3em;">&Theta;<sub style="font-size: 0.9em;">ij</sub></span> &nbsp; = &nbsp;
                            <span style="font-size: 1.7em;">&Sigma;</span> &nbsp;
                            <span style="font-size: 1.3em;">&Omega;<sub style="font-size: 0.9em;">j</sub></span> &nbsp;
                            <span style="display: inline-block; vertical-align: middle; font-size: 1.3em;">
                                <span style="border-bottom: 1px solid; display: block;">&gamma;<sub style="font-size: 0.9em;">ij</sub></span>
                                <span style="display: block;">s<sub style="font-size: 0.9em;">i</sub></span>
                            </span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 1</i>: <span style="font-size: 1.1em;">${op_max_loss_avs1:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 2</i>: <span style="font-size: 1.1em;">${op_max_loss_avs2:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Slash on <i>AVS 3</i>: <span style="font-size: 1.1em;">${op_max_loss_avs3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with col31:
            
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")
            
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Slash on <i>AVS 1</i>: <span style="font-size: 1.1em;">${op_int_loss_avs1:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Slash on <i>AVS 2</i>: <span style="font-size: 1.1em;">${op_int_loss_avs2:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Slash on <i>AVS 3</i>: <span style="font-size: 1.1em;">${op_int_loss_avs3:,.0f}</span></h2>
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
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <span style="font-size: 1.2em;">&Theta;<sub style="font-size: 0.8em;">ij</sub></span> &nbsp; | &nbsp;
                        Total Max Potential Slash Across AVSs: <span style="font-size: 1.1em;">${op_max_loss_avss:,.0f}</span>
                    </h2>
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
                    <h2 style="color: black; margin:0; font-size: 1.1em;">Total Int Potential Slash Across AVSs: ${op_int_loss_avss:,.0f}</h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


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
        
        st.write(f"""&#8226; Total Restaked: {formatted_value}""")

        with st.expander("Logic"):
            st.markdown(f"""
                """)
            
        st.write("\n")
        st.write("\n")
        st.write("\n")
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
                tvl1 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=0, step=10000000,
                                              help=f"""TVL was included to establish the CoC vs PfC threshold and calculate the "allowed" slashes to maintain AVS security.""")

                formatted_tvl1 = "${:,.0f}".format(tvl1)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl1}""")


        max_slash_allowed1 = total_restaked - 2 * tvl1
        int_slash_allowed1 = max_slash_allowed1 * 2/3


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
                            <span style="font-weight: bold; font-size: 1em;">Ω<sub style="font-size: 0.9em;">AVS1</sub></span> &nbsp; | &nbsp; Potential Max Slash Exposure to a Set of Operators based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing1:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with st.expander("Logic"):
                st.markdown(f"""
                    """)
            
        
        st.write("\n")
        st.write(f"""&#8226; **"Byzantine Slashing Tolerance" Test**: AVS 1 Max "Allowed" Slashes vs Max Potential Operator Slashes""")
            
        col6, col7 = st.columns([10, 9])

        with col6: 

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
                            <span style="font-weight: bold; font-size: 1em;">α<sub style="font-size: 0.9em;">AVS1</sub></span>
                        </div>
                        <div style="display: block;">
                            <br> <!-- Extra space -->
                        </div>
                        <div style="display: block;">
                            <span style="font-size: 1em;">Max Slash "Allowed" To Still Maintain Security:</span> <span style="font-size: 1.1em;">${max_slash_allowed1:,.0f}</span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Slash "Allowed" to Maintain Robust Security: <span style="font-size: 1.1em;">${int_slash_allowed1:,.0f}</span></h2>
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
                    <h2 style="color: black; margin: 0; font-size: 1em;">
                        <span style="font-weight: bold; font-size: 1.2em;">
                            &Omega;<sub style="font-size: 0.8em;">AVS1</sub> &nbsp;
                            <span style="display: inline-block; vertical-align: middle;">
                                <span style="border-bottom: 1px solid; display: block;">&gamma;<sub style="font-size: 0.8em;">iAVS1</sub></span>
                                <span style="display: block;">s<sub style="font-size: 0.8em;">i</sub></span>
                            </span>
                        </span>
                        <br><br>
                        <span style="font-size: 1.1em;">Max Potential Operator Slash:</span> <span style="font-size: 1.2em;">${op_max_loss_avs1:,.0f}</span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Operator Slash: <span style="font-size: 1.1em;">${op_int_loss_avs1:,.0f}</span></h2>
                </div>
                """,
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
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
                tvl2 = st.number_input("**AVS TVL** ", min_value=0, max_value=10000000000000, value=0, step=10000000)

                formatted_tvl2 = "${:,.0f}".format(tvl2)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl2}""")

        max_slash_allowed2 = total_restaked - 2*tvl2
        int_slash_allowed2 = total_restaked - 3*tvl2
        
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
                            <span style="font-weight: bold; font-size: 1em;">Ω<sub style="font-size: 0.8em;">AVS2</sub></span> &nbsp; | &nbsp; Potential Max Slash Exposure to a Set of Operators based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing2:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )


        with st.expander("Logic"):
                st.markdown(f"""
                   """)

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
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1em;">α<sub style="font-size: 0.9em;">AVS2</sub></span> &nbsp; | &nbsp; Max Slash "Allowed" To Still Maintain Security: <span style="font-size: 1.1em;">${max_slash_allowed2:,.0f}</span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Slash "Allowed" to Maintain Robust Security: <span style="font-size: 1.1em;">${int_slash_allowed2:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Operator Slash: <span style="font-size: 1.1em;">${op_max_loss_avs2:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Operator Slash: <span style="font-size: 1.1em;">${op_int_loss_avs2:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
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
                tvl3 = st.number_input("**AVS TVL**", min_value=0, max_value=1000000000000, value=0, step=10000000)
                formatted_tvl3 = "${:,.0f}".format(tvl3)
                st.write(f"""&#8226; AVS TVL: {formatted_tvl3}""")

        max_slash_allowed3 = total_restaked - 2*tvl3
        int_slash_allowed3 = total_restaked - 3*tvl3

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
                            <span style="font-weight: bold; font-size: 1em;">Ω<sub style="font-size: 0.8em;">AVS3</sub></span> &nbsp; | &nbsp; Potential Max Slash Exposure to a Set of Operators based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing3:,.0f}</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        with st.expander("Logic"):
                st.markdown(f"""
                    """)
            

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
                    margin: 5px 0;
                    background-color: white;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1em;">α<sub style="font-size: 0.9em;">AVS3</sub></span> &nbsp; | &nbsp; Max Slash "Allowed" To Still Maintain Security: <span style="font-size: 1.1em;">${max_slash_allowed3:,.0f}</span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Slash "Allowed" to Maintain Robust Security: <span style="font-size: 1.1em;">${int_slash_allowed3:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Max Potential Operator Slash: <span style="font-size: 1.1em;">${op_max_loss_avs3:,.0f}</span></h2>
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
                    <h2 style="color: black; margin:0; font-size: 1em;">Int Potential Operator Slash: <span style="font-size: 1.1em;">${op_int_loss_avs3:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )
    
        with st.expander("Logic"):
            st.markdown("""
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    ###################
    ####### BST #######
    ###################


    st.markdown(
        """
        <div style="text-align: center; font-size: 22px; font-weight: bold;">
            BYZANTINE <i>SLASHING</i> TOLERANCE TEST
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
                        &beta;<sub style="font-size: 0.8em;">ij</sub> = 
                        <span style="font-size: 1.3em;">&Sigma;</span>
                        &alpha;<sub style="font-size: 0.8em;">j</sub> - 
                        &theta;<sub style="font-size: 0.8em;">ij</sub>
                    </span>
                </div>
            </h2>
        </div>
        """, 
        unsafe_allow_html=True
    )

    st.write("\n")
    st.write("\n")
    st.write("\n")


    col50,col51,col52 = st.columns(3)

    with col50:
        bst_avs1 = max_slash_allowed1 - op_max_loss_avs1

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="color: black; margin:0; font-size: 1.2em;">
                    AVS 1
                <div style="color: black; font-size: 1em; margin-top: 10px;">
                    <span style="font-weight: bold;">${max_slash_allowed1:,.0f}</span> - <span style="font-weight: bold;">${op_max_loss_avs1:,.0f}</span> = <span style="font-weight: bold;">${bst_avs1:,.0f}</span>
                </div>
                </h2>
            </div>
            """, unsafe_allow_html=True
        )
         
    with col51:
        bst_avs2 = max_slash_allowed2 - op_max_loss_avs2

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="font-weight: bold; color: black; margin:0; font-size: 1.3em;">
                    AVS 2
                <div style="color: black; font-size: 1em; margin-top: 10px;">
                    <span style=">${max_slash_allowed2:,.0f}</span> - <span style=">${op_max_loss_avs2:,.0f}</span> = <span style="font-weight: bold;">${bst_avs2:,.0f}</span>
                </div>
                </h2>
            </div>
            """, unsafe_allow_html=True
        )
    with col52:
        bst_avs3 = max_slash_allowed3 - op_max_loss_avs3

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;">
                <h2 style="color: black; margin:0; font-size: 1.3em;">
                    AVS 3
                <div style="color: black; font-size: 1em; margin-top: 10px;">
                    <span style="font-weight: bold;">${max_slash_allowed3:,.0f}</span> - <span style="font-weight: bold;">${op_max_loss_avs3:,.0f}</span> = <span style="font-weight: bold;">${bst_avs3:,.0f}</span>
                </div>
                </h2>
            </div>
            """, unsafe_allow_html=True
        )

    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.write(f"""
             The Byzantine *Slashing* Tolerance test helps identify the ecosystem elements that are in a compromisable state due to a previous-executed Operator slashing event.
             
             We say that an element has failed the BST test if B < 0, and passed if B > 0.
            
              """)






#########################################
#########################################
#########################################

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.write("-----------------------")

    st.write("\n")

    st.markdown('<p style="font-weight: bold;">NEXT...</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Performance Reputation</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Centralization Risk Level</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Operator Collateralization Risk Level</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Multiple Operators Restaked Into Multiple AVSs</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Entrenchment Level Risk of a Set of Operators on Multiple AVSs Simultaneously</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; display: inline;">&#8226; Slashing Risks Based on AVS Nature</p><span style="font-weight: normal; display: inline;"> (data availability, keeper networks, oracles, bridges, etc.)</span>', unsafe_allow_html=True)


            # Displaying the custom styled header
            #st.markdown('<p class="header-style">Operator Reputation [Soon]</p>', unsafe_allow_html=True)

            # Select slider for average operator reputation
            #operator_reputation = st.selectbox("", ["Unknown", "Established", "Renowned"])

            # The expander with more information (optional)
            #with st.expander("Logic"):
            #    st.markdown("""
            #        Not accounted for in the calculations, as of now.
            #                """)

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

