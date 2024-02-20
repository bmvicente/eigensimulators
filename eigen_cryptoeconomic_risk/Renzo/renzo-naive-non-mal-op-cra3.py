
# Naive & Non-Mal Op

# CoC = Stake / 3
# PfC = TVL



import pandas as pd
import streamlit as st


def avs_compounded_risk(operator_stake, op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3):

    def calculate_op_max_loss_avss(op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3):
        return op_max_loss_avs1 + op_max_loss_avs2 + op_max_loss_avs3

    op_max_loss_avss = calculate_op_max_loss_avss(op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3)

    return(op_max_loss_avss, op_max_loss_avs1, op_max_loss_avs2, op_max_loss_avs3,
            operator_stake)



def create_total_restaked_input():
    if 'total_restaked' not in st.session_state:
        st.session_state.total_restaked = 0

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
        st.session_state[risk_score_key] = 0

    risk_score = st.number_input(
        label,
        min_value=0,
        max_value=100,
        value=st.session_state[risk_score_key],
        step=10
    )

    return risk_score


def calculate_slashing(total_restaked, risk_score):
    if risk_score == 100:
        risk_factor = (90 + 10)  # This will give the same value as when risk_score is 9
    else:
        risk_factor = (risk_score + 10)

    slashing_amount = total_restaked * (risk_factor / 1000)
    return slashing_amount




def main():

    st.set_page_config(layout="wide")

    st.image("images/renzo1.png", width=450)

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
    

    st.write("  \n")

    st.title("Cryptoeconomic Risk Analysis III")
    st.subheader("**AVS ↔ Non-Malicious Operator Stake-Loss Event Simulator:** *Naïve Approach*")
    
    st.write("  \n")

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""
                    An AVS may be created with an unintentional slashing vulnerability (like a programming bug) which gets triggered and causes loss of funds to honest users. The main goal of the Simulator is to demonstrate how the Underlying Risk Profile of AVSs may influence the potential slashing an Operator may face, and how such a slash would, in turn, affect the AVSs individually. (Compounding effects of slashing were not taken into account.) 

                    **Cryptoeconomic Security** quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property, which is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security.
                    A core idea of EigenLayer is to provision cryptoeconomic security through various slashing mechanisms which levy a high cost of corruption.

                    Some of these slashing mechanisms concern the *Naive approach*, *Reorgs within Reversion Periods*, and *STAKESURE*. We start with the Naive one in this Simulator and STAKESURE on a later one. For more detailed information about these, check out [*STAKESURE: Proof of Stake Mechanisms with Strong Cryptoeconomic Safety*](https://arxiv.org/abs/2401.05797).
                    Very simply, the Naive approach takes the **CoC to be 1/3 of Total Stake** because that's usually the amount of node operators' stake needed to be corrupt and gain control of the network, takes **PfC to be the total amount of TVL that can be extracted by an adversary**. It was coined as Naive because the profit from an attack is usually not this straightforward, in that there are new and improved mechanisms in place to increase the bound on PfC. We consider it to be a important topic of research and analysis, to take the worst-case scenario in a situation like this, nevertheless.
                        """)
        
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")



    st.markdown('<p class="header-style" style="font-size: 19px;">Total Amount Restaked on AVS Ecosystem (T)</p>', unsafe_allow_html=True)

    st.session_state.total_restaked = create_total_restaked_input()
    formatted_value = "${:,.0f}".format(st.session_state.total_restaked)
        
    st.write(f"""&#8226; Total Restaked: {formatted_value}""")
    
    if st.session_state.total_restaked >= 10000000000:  # 10 billion
        st.markdown(f'<span style="color: red; font-weight: bold">Even though the conditions for cryptoeconomic security may not be satisfied, a large enough amount of stake is a strong determinant of the security and liveness of a PoS blockchain, to the point where no adversarial attack is warranted.</span>', unsafe_allow_html=True)

    st.write("\n")

    if 'tvl1' not in st.session_state:
            st.session_state.tvl1 = 0  # Default value
    if 'tvl2' not in st.session_state:
            st.session_state.tvl2 = 0  # Default value
    if 'tvl3' not in st.session_state:
            st.session_state.tvl3 = 0  # Default value

    if 'pfc' not in st.session_state:
            st.session_state.pfc = 0  # Default value

    if 'coc' not in st.session_state:
        st.session_state.coc = 0  # Default value

    max_slash_allowed = st.session_state.coc - st.session_state.pfc
    st.session_state.coc = total_restaked / 3


    col20,col21 = st.columns([7,8])

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
                    Cost of Corruption<span style="font-size: 0.9em; font-weight: normal;"> (T / 3)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.coc:,.0f}</span>
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
                    Profit from Corruption<span style="font-size: 0.9em; font-weight: normal;"> (&Sigma; TVL<sub>j</sub>)</span><span style="font-weight: bold;">:</span> <span style="font-size: 1.1em;">${st.session_state.pfc:,.0f}</span>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


    with col21:

        if max_slash_allowed >= 0:
            background_color = "#90EE90"  # light green for positive allowed loss
            max_slash_allowed_text = "Max Total Stake-Loss \"Allowed\" To Still Maintain Cryptoeconomic Security"
        else:
            background_color = "#ff9999"  # red for a negative allowed loss, indicating an insecure condition
            max_slash_allowed_text = "Ecosystem Already in an Insecure and Compromisable Cryptoeconomic Position of"

        

        st.markdown(
                    f"""
                    <div style="
                        border: 2px solid;
                        border-radius: 2px;
                        padding: 19px;
                        text-align: center;
                        margin: 5px 0;
                        background-color: {background_color};">
                        <h2 style="color: black; margin: 0; font-size: 1.1em;">
                            <div style="display: block;">
                                <span style="font-size: 1.2em;">α<sub style="font-size: 0.8em;">j</sub></span>
                            </div>
                            <div style="display: block;">
                                <br> <!-- Extra space -->
                            </div>
                            <div style="display: block;">
                                {max_slash_allowed_text}: <span style="font-size: 1.1em;">${max_slash_allowed:,.0f}</span>
                            </div>
                        </h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            
        st.write("\n")

    with st.expander("Logic"):
            st.markdown(f"""
                As laid out in the first dropdown, *CoC = T / 3* and *PfC = &Sigma; TVLj* (*j* corresponding to the set of AVSs at hand).
                
                The variable **Max Stake-Loss Allowed to Still Maintain Cryptoeconomic Security** (αj) represents the difference between CoC and PfC. We've quoted "Allowed" because the loss is not to be permissioned or validated by any entity; it simply represents the buffer (or the abscence of the buffer) that the AVS network can be slashed further and still keep the network secure.
                        If CoC > PfC, there is some amount "allowed" that can be slashed, and if CoC < PfC, the system is already in compromisable cryptoeconomic position and the slash "allowed" equals 0.
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")





    ##########################################
    ################ OPERATOR ################
    ##########################################


    col1, col2 = st.columns([1, 1], gap="large")

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

        # Format the operator_stake value as currency with a dollar sign and commas
        formatted_operator_stake = "${:,.0f}".format(operator_stake)

        st.write(f"""&#8226; Operator Stake: {formatted_operator_stake}""")


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
        st.markdown('<p class="header-style">Fraction of Total Stake Operator is Securing</p>', unsafe_allow_html=True)

        st.write("  \n")


        if total_restaked > 0:
            fraction_op_securing = operator_stake / total_restaked
        else:
            fraction_op_securing = 0  # Set to 0 or another appropriate default value

        op_max_loss_avs1 = potential_total_slashing1 * fraction_op_securing
        op_max_loss_avs2 = potential_total_slashing2 * fraction_op_securing
        op_max_loss_avs3 = potential_total_slashing3 * fraction_op_securing


        (
            op_max_loss_avss, 
            op_max_loss_avs1, 
            op_max_loss_avs2, 
            op_max_loss_avs3, 
            operator_stake
        ) = avs_compounded_risk(
            operator_stake,
            op_max_loss_avs1,
            op_max_loss_avs2,
            op_max_loss_avs3
        )



        st.session_state.operator_stake = operator_stake

        st.markdown(
            f"""
            <div style="
                border: 1px solid;
                border-radius: 2px;
                padding: 5px;
                text-align: center;
                margin: 5px 0;
                background-color: white;">
                <h2 style="color: black; margin: 0;">
                    <span style="font-size: 0.7em;"> <!-- Increase font size for gamma -->
                        γ<sub style="font-size: 0.8em;">ij</sub> = <!-- Increase font size for subscript -->
                        <div style="display: inline-block; vertical-align: middle;">
                            <span style="border-bottom: 1px solid; display: block;">
                                <span style="font-size: 0.9em;">s<sub style="font-size: 0.8em;">i</sub></span> <!-- Increase font size for s and its subscript -->
                            </span>
                            <span style="font-size: 0.9em;">T</span> <!-- Increase font size for T -->
                        </div>
                        = <span style="font-size: 0.9em;">{fraction_op_securing * 100:,.2f}%</span> <!-- Increase font size for the result -->
                    </span>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )



        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")

        
        st.markdown('<p class="header-style">Operator Potential Stake Losses Per AVS</p>', unsafe_allow_html=True)

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
                        <span style="font-size: 1.3em;">&gamma;<sub style="font-size: 0.9em;">ij</sub></span>
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
                <h2 style="color: black; margin: 0; font-size: 1em;">
                    <span style="font-size: 1.2em;">&Theta;<sub style="font-size: 0.8em;">i AVS1</sub></span> &nbsp; | &nbsp;
                    Max Potential Stake-Loss on <i>AVS 1</i>: <span style="font-size: 1.2em;">${op_max_loss_avs1:,.0f}</span>
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
                <h2 style="color: black; margin: 0; font-size: 1em;">
                    <span style="font-size: 1.2em;">&Theta;<sub style="font-size: 0.8em;">i AVS2</sub></span> &nbsp; | &nbsp;
                    Max Potential Stake-Loss on <i>AVS 2</i>: <span style="font-size: 1.2em;">${op_max_loss_avs2:,.0f}</span>
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
                <h2 style="color: black; margin: 0; font-size: 1em;">
                    <span style="font-size: 1.2em;">&Theta;<sub style="font-size: 0.8em;">i AVS3</sub></span> &nbsp; | &nbsp;
                    Max Potential Stake-Loss on <i>AVS 3</i>: <span style="font-size: 1.2em;">${op_max_loss_avs3:,.0f}</span>
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
                    margin: 5px 0;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <span style="font-size: 1.3em;">&Theta;<sub style="font-size: 0.9em;">ij</sub></span> &nbsp; | &nbsp;
                        Total Max Potential Stake-Loss Across AVSs: <span style="font-size: 1.2em;">${op_max_loss_avss:,.0f}</span>
                    </h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("\n")

        with st.expander("Logic"):
            st.markdown("""
                    We take the **Operator's amount of Stake** (Si, where *i* represents a given Operator), either delegated by themselves or on behalf of Restakers by proxy, and calculate the **Fraction of Total Stake this Operator is securing** (γij) which is simply calculated by their Stake divided by the Total Stake. For reference, each Restaker can only delegate to one Operator at a time.
                    
                    The **Total Maximum Potential Stake-Loss** (Θij) this Operator may be subject to by validating each of the AVSs is given by the formula just above: it is composed by the **sum of all the Potential Stake Losses given by the Risk Exposures per AVS** (Σ Ωj), calculated on the left side, times the **fraction of Total Stake the Operator is securing**.
                        
                    Of course, to do this calculation, it is assumed that each AVS de facto had some sort of vulnerability that was triggered that caused the Operator to lose Stake. Note that this Stake Loss was also maximized, based on AVS Risk Profile, to illustrate the worst-case possible.
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
                        <span style="font-size: 1.1em;">Ω<sub style="font-size: 0.8em;">AVS1</sub></span>
                    </div>
                    <div style="display: block; margin-top: 5px;">
                        Potential Max Stake-Loss Exposure to Operator based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing1:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("\n")


        with st.expander("Logic"):
            st.markdown("""
                **Ωj returns the Potential Stake-Loss Exposure an Operator is subjecting themselves to by validating a set of AVSs with their own Risk Profiles**. It is computed by the Total Staked Amount times the Risk Factor of the AVS (as calculated below). 
                
                Since AVSs access pooled security in EigenLayer, it only makes sense for the same amount of Total Stake to be equally considered in the calculation for each AVS. For consistency, the AVS Risk Score input should be based on the Normalized Risk Score calculated in our AVS Underlying Risk Simulator.
                    
                **ΩAVS1**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                    if risk_score == 100:
                        risk_factor = (90 + 10)
                    else:
                        risk_factor = (risk_score + 10)

                    slashing_amount = total_restaked * (risk_factor / 1000)

                potential_total_slashing1 = calculate_slashing(total_restaked, risk_score1)
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
                        <span style="font-size: 1.1em;">Ω<sub style="font-size: 0.8em;">AVS2</sub></span>
                    </div>
                    <div style="display: block; margin-top: 5px;">
                        Potential Max Stake-Loss Exposure to Operator based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing2:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


        st.write("\n")

    
        with st.expander("Logic"):
            st.markdown("""
                **Ωj returns the Potential Stake-Loss Exposure an Operator is subjecting themselves to by validating a set of AVSs with their own Risk Profiles**. It is computed by the Total Staked Amount times the Risk Factor of the AVS (as calculated below). 
                
                Since AVSs access pooled security in EigenLayer, it only makes sense for the same amount of Total Stake to be equally considered in the calculation for each AVS. For consistency, the AVS Risk Score input should be based on the Normalized Risk Score calculated in our AVS Underlying Risk Simulator.
                                
                **ΩAVS2**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                    if risk_score == 100:
                        risk_factor = (90 + 10)
                    else:
                        risk_factor = (risk_score + 10)

                    slashing_amount = total_restaked * (risk_factor / 1000)

                potential_total_slashing2 = calculate_slashing(total_restaked, risk_score2)
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
                        <span style="font-size: 1.1em;">Ω<sub style="font-size: 0.8em;">AVS3</sub></span>
                    </div>
                    <div style="display: block; margin-top: 5px;">
                        Potential Max Stake-Loss Exposure to Operator based on AVS Risk Profile: <span style="font-size: 1.1em;">${potential_total_slashing3:,.0f}</span>
                    </div>
                </h2>
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.write("\n")
    

        with st.expander("Logic"):
            st.markdown("""
                **Ωj returns the Potential Stake-Loss Exposure an Operator is subjecting themselves to by validating a set of AVSs with their own Risk Profiles**. It is computed by the Total Staked Amount times the Risk Factor of the AVS (as calculated below). 
                
                Since AVSs access pooled security in EigenLayer, it only makes sense for the same amount of Total Stake to be equally considered in the calculation for each AVS. For consistency, the AVS Risk Score input should be based on the Normalized Risk Score calculated in our AVS Underlying Risk Simulator.
                
                **ΩAVS3**
                ```python
                def calculate_slashing(total_restaked, risk_score):
                    if risk_score == 100:
                        risk_factor = (90 + 10)
                    else:
                        risk_factor = (risk_score + 10)

                    slashing_amount = total_restaked * (risk_factor / 1000)
                
                potential_total_slashing3 = calculate_slashing(total_restaked, risk_score3)
                ```
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")


    st.session_state.pfc = tvl1 + tvl2 + tvl3







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


    bst = max_slash_allowed - op_max_loss_avss

    if bst < 0:
            color = "#d32f2f"  # Red color for negative value
            background_color = "#fde0dc"  # Light red background
    elif 0 < bst <= 20000000:  # Condition for values between 0 and 20 million
            color = "#FB8C00"  # Orange color
            background_color = "#FFE0B2"  # Light orange background
    elif bst > 20000000:
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
                        ${max_slash_allowed:,.0f} - ${op_max_loss_avss:,.0f} = <span style="font-size: 1.3em; color: {color};">${bst:,.0f}</span>
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
            The <b>Byzantine <i>Slashing</i> Tolerance test</b> assesses the Cryptoeconomic Security of the AVS ecosystem, post Operator Stake-Loss event.
            <br>
            <br>
            The formula takes the <b>Max Allowed Stake-Loss</b> and subtracts it to the <b>Operator Max Stake-Loss suffered across all AVSs</b>. We say that the pool of AVSs has failed the BST test if β < 0, and passed if β > 0. 
            <br>            
            Under the Naive Analysis and without access to staking insurance, the set of AVSs may end up in an insecure cryptoeconomic position and potentially compromisable state, which may induce an intermediate- or max-loss risk to the whole network (scenario where either some or all AVSs fail).
            <br>
            <br>
            In the above box, the green background represents a comfortable AVS tolerance state post-slashing event, the orange background represents a warning signal for an uncomfortable but still secure system, and the red background represents a danger signal where the AVSs are in a cryptoeconomically insecure position, ripe for adversarial corruption.
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
    st.markdown('<p style="font-weight: bold;">&#8226; <s>Compounded Risk Propagation in AVS Ecosystem</s> & Visualization</p>', unsafe_allow_html=True)
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

