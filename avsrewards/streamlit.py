import streamlit as st

# Importing the functions from other files
from avs_audits import avs_sec_audits
from avs_dual_staking import dual_staking
from avs_reward_calculation_logic import avs_rewards
from avs_revenue import revenue
from avs_tokenomics import tokenomics
from avs_tvl_totalstaked import tvl_total_staked
from avs_type import type
from avs_reward_result import calculate_rewards


def st_main():
    st.set_page_config(layout="wide")

    st.image("eigensimulators/images/eigenimage.png")
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
        revenue()  # Assuming this function renders content directly to the app

        st.write("\n")  # Adding a space or line break

        tvl_total_staked()  # Assuming this function renders content directly to the app

        st.write("\n")  # Adding a space or line break

        dual_staking()

    with col2:
        type()  # Assuming this function renders content directly to the app

        st.write("\n")  # Adding multiple spaces or line breaks

        avs_sec_audits()  # Assuming this function renders content directly to the app

        st.write("\n")  # Adding multiple spaces or line breaks

        tokenomics()  # Assuming this function renders content directly to the app


if __name__ == "__main__":
    st_main()
