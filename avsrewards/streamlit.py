
import streamlit as st

from avs_reward_calculation_logic import calc_revenue,calc_tvl_total_staked,calc_avs_type,calc_dual_staking,calc_avs_sec_audits
from avs_revenue import avs_revenue_main
from avs_dual_staking import dual_staking
from avs_audits import avs_sec_audits
from avs_type import avs_type_function
from avs_tvl_totalstaked import tvl_total_staked
from avs_tokenomics import tokenomics


# Streamlit App

def st_main():
    st.set_page_config(layout="wide")

    st.image("images/eigenimage.png")
    st.title("AVS Reward Emission Simulator")

    with st.expander("Assumptions Made in Building our Simulator"):
        st.markdown("""
            A couple of assumptions were made in our Simulator to simplify and more easily illustrate the potential reward emission of an AVS in a Dual Staking and LST Restaking context:

            **Dual Staking** was chosen as the business model, preferred over other models, due to the utility and security they confer to an AVS, and **Veto Dual Staking**, as the Dual Staking method, preferred over other methods, due to the low implementation cost and reliability in terms of liveness. [Learn more](https://www.blog.eigenlayer.xyz/dual-staking/)

            **LST Restaking** was chosen as the Restaking Modality because the Dual Staking model requires a staked ETH of some kind, and also because it was simpler and more intuitive, compared to other modalities. [Learn more](https://docs.eigenlayer.xyz/overview/readme/whitepaper)

            Generally speaking, these three assumptions were made due to the safety they confer AVSs, especially recent ones, and for simplicity's sake in a first version of the Simulator.
                    
            We recommend the AVS Risk Simulator as an important introduction to understanding the AVS Reward Emission Simulator.
        """)
    

    col1, col2 = st.columns([1, 1], gap="large")
    
    avs_total_staked = tvl_total_staked()






    with col1:

        #AVS Revenue
        selected_avs_revenue_main = avs_revenue_main()  # Confirmed: it is capturing the value inputted by the user
        avs_revenue_final = calc_revenue(selected_avs_revenue_main)

        st.write("\n")
        
        # AVS TVL & Staked
        selected_avs_total_staked, selected_avs_tvl = tvl_total_staked()
        tvl_total_staked_final = calc_tvl_total_staked(selected_avs_total_staked, selected_avs_tvl)


        st.write("\n")
        st.write("\n")

        # AVS Dual Staking
        selected_avs_token_percentage_n, selected_xeth_percentage_n = dual_staking()
        dual_staking_final = calc_dual_staking(selected_avs_token_percentage_n, selected_xeth_percentage_n)  


    with col2:

        # AVS Type
        selected_avs_type = avs_type_function()
        avs_type_final = calc_avs_type(selected_avs_type)

        st.write("\n")

        # AVS Security Audits
        selected_number_audits = avs_sec_audits()
        avs_audits_final = calc_avs_sec_audits(selected_number_audits)

        st.write("\n")

        # AVS Tokenomics
        tokenomics()


    st.write("\n")
    st.write("\n")
    st.write("\n")







    col9, col10 = st.columns([1,1], gap="small")


    selected_avs_revenue = avs_revenue_main()
    avs_revenue_final = calc_revenue(selected_avs_revenue)


    with col9:

        reward_percentage = 0.20  # Base reward percentage
        profit_percentage = 0.20
        staker_percentage = 0.40
        operator_percentage = 0.60

        reward_percentage_adj = reward_percentage + avs_revenue_final + tvl_total_staked_final + avs_audits_final + dual_staking_final + avs_type_final

        #reward_percentage_adj = max(min(reward_percentage, 0.30), 0.10)


        # Reward Value Sum
        def reward_portion(reward_percentage_adj, profit_percentage, avs_revenue_final):
                return avs_revenue_final * profit_percentage * reward_percentage_adj

        reward_portion_result = reward_portion(reward_percentage_adj, profit_percentage, avs_revenue_final)



        # Staker Reward

        def staker_reward(reward_portion_result, staker_percentage):
                return reward_portion_result * staker_percentage

        def calculate_staker_reward_perc(reward_portion_result, staker_percentage, avs_total_staked):
            # Directly calculate the staker_reward_result inside this function
            staker_reward_result = staker_reward(reward_portion_result, staker_percentage)

            if avs_total_staked != 0:
                return staker_reward_result / avs_total_staked  # Calculate the percentage
            else:
                return 0.00  # Avoid division by zero


        staker_reward_result_perc = calculate_staker_reward_perc(reward_portion_result,staker_percentage,avs_total_staked)


        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 10px 0;
                background-color: white;">
                <h2 style="color: black; margin:0; font-size: 1.5em;">Staker Reward: <span style="font-size: 1.2em;">{staker_reward_result_perc:.12f}%</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
        




    with col10:
        

        # Operator Reward

        def operator_reward(reward_portion_result, operator_percentage):
                return reward_portion_result * operator_percentage


        def calculate_operator_reward_perc(reward_portion_result, operator_percentage, avs_total_staked):
            operator_reward_result = operator_reward(reward_portion_result, operator_percentage)

            if avs_total_staked != 0:
                return operator_reward_result / avs_total_staked
            else:
                return 0.00
        
        operator_reward_result_perc = calculate_operator_reward_perc(reward_portion_result, operator_percentage, avs_total_staked)


        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 10px 0;
                background-color: white;">
                <h2 style="color: black; margin:0; font-size: 1.5em;">Operator Reward: <span style="font-size: 1.2em;">{operator_reward_result_perc:.12f}%</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )



    st.write("  \n")
    st.write("  \n")

    st.write("""
                The AVS Reward Emission percentage from the AVS Revenue input range fell in the XX% value.

                Operator Reward is naturally being given greater weight than the Staker Reward due to their more important role.

                The \$AVS’s Tokenomics (while not included in the reward calculation) suggest a look-ahead perspective of how the native AVS token can influence future rewards. A potential for improved rewards to be emitted in the future exists if a relatively small delta between circulating and total supply and a deflationary token rate exist. Whereas a larger delta and an inflationary token rate indicate the potential for lower rewards to be emitted in the future.             
            """)


if __name__ == "__main__":
    st_main()
