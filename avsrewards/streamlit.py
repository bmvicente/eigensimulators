import streamlit as st

from avs_audits import selected_avs_audits_adjustment
from avs_dual_staking import selected_avs_dual_staking_adjustment
from avs_revenue import selected_avs_revenue_adjustment
from avs_tokenomics import selected_avs_inf_def_rate, selected_avs_circ_supply, selected_avs_total_supply
from avs_tvl_totalstaked import selected_avs_tvl_total_staked_adjustment, selected_avs_total_staked
from avs_type import selected_avs_type_adjustment
from avs_reward_result import staker_reward_result, operator_reward_result


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

    with col1:

        #AVS Revenue
        st.write("Selected AVS Revenue Adjustment: ", selected_avs_revenue_adjustment)

        st.write("\n")
        
        col3, col4 = st.columns([1, 1], gap="small")

        # AVS TVL & Staked
        with col3:
            st.write("Selected AVS Revenue Adjustment: ", selected_avs_tvl_total_staked_adjustment)

        with col4:
            st.write("Selected AVS Revenue Adjustment: ", selected_avs_total_staked)


        st.write("\n")

        # AVS Dual Staking
        st.write("Selected AVS Revenue Adjustment: ", selected_avs_dual_staking_adjustment)

    with col2:

        # AVS Type
        st.write("Selected AVS Revenue Adjustment: ", selected_avs_type_adjustment)

        st.write("\n")

        # AVS Security Audits
        st.write("Selected AVS Revenue Adjustment: ", selected_avs_audits_adjustment)

        st.write("\n")

        # AVS Tokenomics
        st.write("Selected AVS Revenue Adjustment: ", selected_avs_inf_def_rate)

        col5, col6 = st.columns([1, 1], gap="small")

        with col5:
            st.write("Selected AVS Revenue Adjustment: ", selected_avs_circ_supply)
        
        with col6:
            st.write("Selected AVS Revenue Adjustment: ", selected_avs_total_supply)

    st.write("\n")
    st.write("\n")


    st.write("Staker Reward Result: ", staker_reward_result)
    st.write("Operator Reward Result: ", operator_reward_result)


if __name__ == "__main__":
    st_main()
