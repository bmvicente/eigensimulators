

import streamlit as st



def calculate_operator_attack_risk(total_restaked, tvl):

        if tvl < 100000 or total_restaked < 100000:
            return 10
        
        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, moderate risk
        elif ratio > 0.5:
            return 5  # Less than TVL but not by a wide margin, increased risk
        else:
            return 7


def main():
    st.set_page_config(layout="wide")
    #st.image("images/eigenimage.png")

    st.title("Cryptoeconomic Risk Analysis I")
    st.subheader("**Staker Collateralization Level Simulator**")

    st.write("\n") 

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown("""We begin by assuming that the 3 AVS in this Simulator have an equal Total Restaked Amount distributed between them, therefore 33%.
                        """)
    
    st.write("\n") 
    st.write("\n") 


    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

        st.markdown('<p style="font-weight: bold;">AVS Total Restaked & AVS TVL</p>', unsafe_allow_html=True)
        total_restaked = st.number_input(
            "AVS Total Restaked ($)", 
            min_value=0,
            max_value=int(1e10),
            value=0,
            step=int(1e8)
        )
        st.write(f"&#8226; AVL Total Restaked: ${total_restaked:,.0f}")

        st.write("\n")

        tvl = st.number_input("AVS TVL ($)", min_value=0, max_value=1000000000, value=0, step=int(1e8))
        st.write(f"&#8226; AVS TVL: ${tvl:,.0f}")

        with st.expander("Logic"):
                st.write("CoC > PfC in order to maintain security. Get more from whitepaper.")

    with col2:

        st.markdown('<p style="font-weight: bold;">Operator Amount Restaked</p>', unsafe_allow_html=True)
        operator_stake = st.number_input(
            "Operator Stake ($)",
            min_value=0,
            max_value=int(1e10),
            value=0,
            step=int(1e8),
        )
        st.write(f"&#8226; Operator Stake: ${operator_stake:,.0f}")

        st.write("\n")

        perc_stake_avs = st.slider("% Staked on AVS", 0, 100, 10, help="The percentage of the operator's stake that is allocated to the AVS")
        
        st.write("\n")

        with st.expander("Logic"):
                st.write("CoC > PfC in order to maintain security. Get more from whitepaper.")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    op_stake_on_avs = total_restaked * perc_stake_avs

    st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;">
                    <h2 style="color: black; margin:0; font-size: 1em;">Fraction of AVS Restaked Amount the Operator is Securing: <span style="font-size: 1.1em;">{op_stake_on_avs:,.0f}</span></h2>
                </div>
                """, 
                unsafe_allow_html=True
                )

    col3, col4, col5 = st.columns(3)

        # Add in image of formula, meaning of variables, and section of whitepaper

    with col3:
        
            cost_of_corruption = total_restaked - 2 * tvl

            st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 5px;
                        text-align: center;
                        margin: 5px 0;">
                        <h2 style="color: black; margin:0; font-size: 1em;">Cost of Corruption (CoC): <span style="font-size: 1.1em;">{cost_of_corruption:,.0f}</span></h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                    )
        
    with col4:

            profit_from_corruption = 2 * tvl - total_restaked

            st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 5px;
                        text-align: center;
                        margin: 5px 0;">
                        <h2 style="color: black; margin:0; font-size: 1em;">Profit from Corruption (pj): <span style="font-size: 1.1em;">{profit_from_corruption:,.0f}</span></h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                    )
        
    with col5:

            stake_required_to_corrupt_avs = profit_from_corruption

            st.markdown(
                    f"""
                    <div style="
                        border: 1px solid;
                        border-radius: 2px;
                        padding: 5px;
                        text-align: center;
                        margin: 5px 0;">
                        <h2 style="color: black; margin:0; font-size: 1em;">Stake Required to Corrupt AVS (alphaj): <span style="font-size: 1.1em;">{stake_required_to_corrupt_avs:,.0f}</span></h2>
                    </div>
                    """, 
                    unsafe_allow_html=True
                    )

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    # Initialize calculation_result at the start
    calculation_result = 0

    # Check if stake_required_to_corrupt_avs is zero to avoid ZeroDivisionError
    if stake_required_to_corrupt_avs != 0:
        fraction_result = profit_from_corruption / stake_required_to_corrupt_avs
        calculation_result = operator_stake - op_stake_on_avs * fraction_result

    # Now, you can format calculation_result without error
    formatted_calculation_result = f"{calculation_result:,.0f}"

    # Continue with your HTML formatting and Streamlit markdown as before
    formatted_profit_from_corruption = f"{profit_from_corruption:,.0f}"
    formatted_stake_required_to_corrupt_avs = f"{stake_required_to_corrupt_avs:,.0f}"
    formatted_operator_stake = f"{operator_stake:,.0f}"
    formatted_op_stake_on_avs = f"{op_stake_on_avs:,.0f}"
    formatted_calculation_result = f"{calculation_result:,.0f}"

    # Check if stake_required_to_corrupt_avs is zero to avoid ZeroDivisionError
    if stake_required_to_corrupt_avs != 0:
        fraction_result = profit_from_corruption / stake_required_to_corrupt_avs
        calculation_result = operator_stake - op_stake_on_avs * fraction_result
    else:
        fraction_result = 0  # Set fraction_result to 0 if dividing by zero
        calculation_result = 0  # Set calculation_result to 0 in this case


    # Determine collateralization status and result color based on the value of calculation_result
    if calculation_result < 0:
        collat_status = "Overcollateralized"
        result_color = "green"
    elif calculation_result > 0:
        collat_status = "Undercollateralized"
        result_color = "red"
    else:
        collat_status = "The Staker Collateralization equals $0."
        result_color = "black"


    fraction_html = f"""
    <div style="text-align: center;">
        <span style="font-size: 20px; font-weight: bold;">Staker Collateralization Level:</span><br><br>
        <span style="font-size: 24px; font-weight: bold;">{formatted_operator_stake} - {formatted_op_stake_on_avs} * </span>
        <div style="display: inline-block; vertical-align: middle;">
            <div style="font-size: 24px; font-weight: bold; text-align: center;">
                <span>{formatted_profit_from_corruption}</span><br>
                <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                <span>{formatted_stake_required_to_corrupt_avs}</span>
            </div>
        </div>
        <span style="font-size: 24px; font-weight: bold;"> = </span><span style="font-size: 24px; font-weight: bold; color: {result_color};">{formatted_calculation_result}</span>
    </div>
    """

    st.markdown(fraction_html, unsafe_allow_html=True)

    st.write("\n")
    st.write("\n")

    # Format the calculation result with a dollar sign, commas, and no decimals
    formatted_calculation_result = f"${abs(calculation_result):,.0f}"

    if calculation_result == 0:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'><span style='color: {result_color};'>{collat_status}</span></div>", unsafe_allow_html=True)
    elif calculation_result < 0:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'>The Staker is <strong>{collat_status}</strong> by <span style='color: {result_color};'><strong>{formatted_calculation_result}</strong></span>, therefore <em>has met</em> the sufficient conditions for Cryptoeconomic Security.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'>The Staker is <strong>{collat_status}</strong> by <span style='color: {result_color};'><strong>{formatted_calculation_result}</strong></span>, therefore <em>has not met</em> the sufficient conditions for Cryptoeconomic Security.</div>", unsafe_allow_html=True)


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.write(f"""
            **Suggestions on How to Fix *Undercollateralization*:**

            1. The Undercollateralized Staker can increase their amount of stake;
            2. The Undercollateralized Staker can deregister or be deregistered from some set of modules;
            3. Other Stakers can adjust their own registrations.
            """)
            
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.write("-----------------------")

    st.write("\n")

    st.markdown('<p style="font-weight: bold;">NEXT...</p>', unsafe_allow_html=True)

    st.markdown('<p style="font-weight: bold;">&#8226; Single Operator Restaked in Multiple AVSs</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Multiple Operators Restaked in Multiple AVSs</p>', unsafe_allow_html=True)

    st.markdown('<p style="font-weight: bold; display: inline;">&#8226; Continuous Relaxation</p><span style="font-weight: normal; display: inline;">, a more flexible method to ensure Stakers tasks\' security, considering the varying risk profiles and preferences of Stakers.</span>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()