

import streamlit as st


#def calculate_operator_attack_risk(total_restaked, tvl):
#
#        if tvl < 100000 or total_restaked < 100000:
#            return 10
#        
#        ratio = (total_restaked / 2) / tvl
#
#        if ratio > 1.5:
#            return 1  # Significantly greater than TVL, lowest risk
#        elif ratio > 1:
#            return 3  # Greater than TVL, moderate risk
#        elif ratio > 0.5:
#            return 5  # Less than TVL but not by a wide margin, increased risk
#        else:
#            return 7

def main():
    st.set_page_config(layout="wide")
    st.image("images/eigenimage.png")

    st.title("Cryptoeconomic Risk Analysis II")
    st.subheader("**Operator Collateralization Level Simulator**")

    st.write("\n") 

    with st.expander("How this Simulator Works & Basic Assumptions"):
        st.markdown(f"""
                    The collateralization status of an Operator is crucial to assess, since it affects every agent in the ecosystem:

                    - Restakers, in knowing if it is an Operator they should delegate stake to.
                    - Operators themselves, in the case they arrive to an uncollateralized state involuntarily.
                    - AVS, in spotting undercollateralized Operators, that may be actively searching to extract Profit from the AVS value locked or involuntary Operators that should be warned to correct course and increase their stake to an overcollateralized status.

                    The Simulator was built based on the theory on Appendix B1 of EigenLayer's whitepaper, particularly.
                        """, unsafe_allow_html=True)
    
    st.write("\n") 
    st.write("\n") 


    col1, col2 = st.columns([1, 1], gap="large")

    with col1:

        st.markdown('<p style="font-weight: bold;">AVS</p>', unsafe_allow_html=True)
        total_restaked = st.number_input(
            "Total Restaked on AVSs ($)", 
            min_value=0,
            max_value=int(1e10),
            value=0,
            step=int(1e8)
        )
        st.write(f"&#8226; Total Restaked: ${total_restaked:,.0f}")

        st.write("\n")

        tvl = st.number_input("AVS *A* TVL ($)", min_value=0, max_value=100000000000, value=0, step=int(1e8))
        st.write(f"&#8226; AVS *A* TVL: ${tvl:,.0f}")


    with col2:

        st.markdown('<p style="font-weight: bold;">Operator</p>', unsafe_allow_html=True)
        operator_stake = st.number_input(
            "Operator Total Stake ($)",
            min_value=0,
            max_value=int(1e10),
            value=0,
            step=int(1e8),
        )
        st.write(f"&#8226; Operator Total Stake: ${operator_stake:,.0f}")

        st.write("\n")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    try:
        op_fraction_vs_total_restaked = operator_stake / total_restaked if total_restaked > 0 else 0
    except ZeroDivisionError:
        op_fraction_vs_total_restaked = 0  # This should catch any ZeroDivisionError
        print("Caught ZeroDivisionError")

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: grey;">
                    <h2 style="color: black; margin:0; font-size: 1.1em;">
                        <div style="height: 10px;"></div> <!-- Empty div for spacing -->
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1.2em;">s<sub style="font-size: 0.8em;">i</sub></span> &nbsp; | &nbsp; Operator Total Stake: <span style="font-size: 1.2em;">${operator_stake:,.0f}</span>
                        </div>
                        <div style="display: block;">
                        <div style="height: 10px;"></div> <!-- Empty div for spacing -->
                            <span style="font-size: 0.9m;">   </span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )

        stake_required_to_corrupt_avs = total_restaked / 2

        profit_from_corruption = max(tvl - stake_required_to_corrupt_avs, 0)

        
        st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: lightgreen;">
                    <h2 style="color: black; margin:0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1.2em;">p<sub style="font-size: 0.8em;">j</span> &nbsp; | &nbsp; Profit from Corrupting AVS <i>A</i>: <span style="font-size: 1.2em;">${profit_from_corruption:,.0f}</span>
                        </div>
                        <div style="height: 10px;"></div> <!-- Empty div for spacing -->
                        <div style="display: block;">
                            <span style="font-size: 0.8m;">TVL - α<sub style="font-size: 1em;">j</sub></span></span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
    with col4:
            
            st.markdown(
                f"""
                <div style="
                    border: 1px solid;
                    border-radius: 2px;
                    padding: 5px;
                    text-align: center;
                    margin: 5px 0;
                    background-color: lightblue;">
                    <h2 style="color: black; margin:0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1.2em;">&gamma;<sub style="font-size: 0.8em;">ij</sub></span> &nbsp; | &nbsp; Fraction of Total Restaked Amount the Operator is Securing: <span style="font-size: 1.2em;">{op_fraction_vs_total_restaked * 100:,.2f}%</span>
                        </div>
                        <div style="height: 10px;"></div> <!-- Empty div for spacing -->
                        <div style="display: block;">
                            <span style="font-size: 0.9m;">(Operator Total Stake / Total Restaked)</span>
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
                    background-color: green;">
                    <h2 style="color: black; margin: 0; font-size: 1.1em;">
                        <div style="display: block;">
                            <span style="font-weight: bold; font-size: 1.2em;">α<sub style="font-size: 1em;">j</sub></span> &nbsp; | &nbsp; Stake Required to Corrupt AVS <i>A</i>: <span style="font-size: 1.2em;">${stake_required_to_corrupt_avs:,.0f}</span>
                        </div>
                        <div style="height: 10px;"></div> <!-- Empty div for spacing -->
                        <div style="display: block;">
                            <span style="font-size: 0.9em;">(Total Restaked on AVSs / 2)</span>
                        </div>
                    </h2>
                </div>
                """, 
                unsafe_allow_html=True
            )



    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    # Inside your main function, after retrieving total_restaked and tvl values
    #calculation_result = calculate_operator_attack_risk(total_restaked, tvl)

    if stake_required_to_corrupt_avs > 0:
        operator_collateralization_level = operator_stake - (op_fraction_vs_total_restaked * (profit_from_corruption / stake_required_to_corrupt_avs))
    else:
        # Set operator_collateralization_level to a default numeric value to avoid TypeError when comparing
        operator_collateralization_level = 0  # or some other default value that makes sense for your application



    # Continue with your HTML formatting and Streamlit markdown as before
    formatted_profit_from_corruption = f"{profit_from_corruption:,.0f}"
    formatted_stake_required_to_corrupt_avs = f"{stake_required_to_corrupt_avs:,.0f}"
    formatted_operator_stake = f"{operator_stake:,.0f}"
    formatted_op_fraction_vs_total_restaked = f"{op_fraction_vs_total_restaked:,.4f}"
    if operator_collateralization_level is not None:
        formatted_result = f"{operator_collateralization_level:,.2f}"
    else:
        # Handle the case where operator_collateralization_level is None or not a number
        # For example, set formatted_result to a placeholder string or display a warning
        formatted_result = "N/A"  # Or any other placeholder indicating the calculation could not be performed


    # Determine collateralization status and result color based on the value of calculation_result
    # Ensure operator_collateralization_level is not None before comparing
    if operator_collateralization_level is not None:
        if operator_collateralization_level < 0:
            collat_status = "Overcollateralized"
            result_color = "green"
        elif operator_collateralization_level > 0:
            collat_status = "Undercollateralized"
            result_color = "red"
        else:
            collat_status = "The Operator Collateralization equals $0."
            result_color = "black"
    else:
        # Handle the case where operator_collateralization_level couldn't be calculated
        collat_status = "Calculation not possible"
        result_color = "grey"
        # You may want to set formatted_result to "N/A" or similar here


    st.write("  \n")
    st.write("  \n")


    col8,col9 = st.columns(2)

    with col8:
        desired_width = 650
        desired_width1 = 800
        st.image("images/collat_formula1.png", width=desired_width)
        st.image("images/collat_formula.png", width=desired_width1)
        st.write("**Note**: detailed explanation of variables and formula rationale can be found at Appendix B.1 of EigenLayer's whitepaper.")



    with col9:
        fraction_html = f"""
            <div style="text-align: center;">
                <span style="font-size: 20px; font-weight: bold;">Operator Collateralization Level:</span><br><br>
                <span style="font-size: 24px; font-weight: bold; background-color:grey; border-radius: 10px; padding: 5px; margin: 2px;">{formatted_operator_stake}</span> 
                <span style="font-size: 28px; font-weight: bold;">-</span>
                <span style="font-size: 24px; font-weight: bold; background-color:lightblue; border-radius: 10px; padding: 5px; margin: 2px;">{formatted_op_fraction_vs_total_restaked}</span> 
                <span style="font-size: 28px; font-weight: bold;">*</span>
                <div style="display: inline-block; vertical-align: middle;">
                    <div style="font-size: 24px; font-weight: bold; text-align: center;">
                        <span style="background-color:lightgreen; border-radius: 10px; padding: 5px; margin: 2px;">{formatted_profit_from_corruption}</span><br>
                        <hr style="margin: 2px 0; width: 100%; border-top: 2px solid black;">
                        <span style="background-color:green; border-radius: 10px; padding: 5px; margin: 2px;">{formatted_stake_required_to_corrupt_avs}</span>
                    </div>
                </div>
                <span style="font-size: 24px; font-weight: bold;"> = </span>
                <span style="font-size: 24px; font-weight: bold; color: {result_color}; border-radius: 10px; padding: 5px; margin: 2px;">{formatted_result}</span>
            </div>
        """

        st.markdown(fraction_html, unsafe_allow_html=True)


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    # Format the calculation result with a dollar sign, commas, and no decimals
    formatted_result = f"${abs(operator_collateralization_level):,.0f}"

    if operator_collateralization_level == 0:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'><span style='color: {result_color};'>{collat_status}</span></div>", unsafe_allow_html=True)
    elif operator_collateralization_level < 0:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'>The Operator is <strong>{collat_status}</strong> by <span style='color: {result_color};'><strong>{formatted_result}</strong></span>, therefore <em>has met</em> the sufficient conditions for Cryptoeconomic Security.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: center; font-size: 18px;'>The Operator is <strong>{collat_status}</strong> by <span style='color: {result_color};'><strong>{formatted_result}</strong></span>, therefore <em>has not met</em> the sufficient conditions for Cryptoeconomic Security.</div>", unsafe_allow_html=True)


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.markdown("""
        An Operator may be voluntarily or involuntarily undercollateralized. They may have positioned themselves that way to extract Profit from tasks they're validating or other ecosystem dependencies may have put them in that position and their collateralization status has a non-malicious intent.

        <br>
                
        **Suggestions on how to fix *Undercollateralization*:**

        1. The Undercollateralized Operator can increase their amount of stake;
        2. The Undercollateralized Operator can deregister or be deregistered from some set of modules;
        3. Other Operators can adjust their own registrations.
        """, unsafe_allow_html = True)
            
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.write("-----------------------")

    st.write("\n")

    st.markdown('<p style="font-weight: bold; font-size: 1.2em;">NEXT...</p>', unsafe_allow_html=True)

    st.markdown('<p style="font-weight: bold;">&#8226; Single Operator Restaked in Multiple AVSs</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold;">&#8226; Multiple Operators Restaked in Multiple AVSs</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-weight: bold; display: inline;">&#8226; Continuous Relaxation</p><span style="font-weight: normal; display: inline;"> (A more flexible method to ensure Operators tasks\' security, considering the varying risk profiles and preferences of Operators)</span>', unsafe_allow_html=True)

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

    col11, col12, col13 = st.columns([4,2,4])

    with col11:
        st.write("")

    with col12:
        st.image("images/tokensight.png", width=270)

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