
import streamlit as st
from avs_reward_calculation_logic import avs_revenue_adjustment


### AVS REVENUE

import streamlit as st

### AVS REVENUE
def revenue():

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

    st.markdown('<p class="header-style">AVS Revenue ($)</p>', unsafe_allow_html=True)

    def get_avs_revenue():
        return st.number_input("Revenue", min_value=0, max_value=1000000000000, value=0, step=1000000)

    avs_revenue = get_avs_revenue()

    dist_rewards_10 = round(avs_revenue * 0.2 * 0.1)
    dist_rewards_30 = round(avs_revenue * 0.2 * 0.3)

    adjustment = avs_revenue_adjustment(avs_revenue)
                
    with st.expander("Logic"):
        st.markdown(f"""
        An **AVS's Revenue**, at any given time, is an adequate indicator to help assess the level of rewards an AVS might be able to emit. From the revenue inputted by the user, we assume a 20% profit for the AVS, and [10-30]% of that profit to be distributable as rewards (specific value of this range dependent on weighting of all the chosen inputs in our Simulator).

        - Current AVS Revenue: **\${avs_revenue:,}**
        - Total Distributable Reward Amount, if rewards equal *10%* of profit: **\${dist_rewards_10:,}**
        - Total Distributable Reward Amount, if rewards equal *30%* of profit: **\${dist_rewards_30:,}**

        Such a reward range is necessary to be calculated to account for the underlying riskiness/security of an AVS and subsequent reward emission values. 
        We find these percentages reasonable, although would highly appreciate feedback from EigenLayer.
        """)
    
    return adjustment

#selected_avs_revenue_adjustment = revenue()  # This will also render the selection box and explanation