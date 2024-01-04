
import streamlit as st


# AVS TVL & Total Restaked

def avs_tvl_total_staked_risk():

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

        st.markdown('<p class="header-style">AVS TVL & Total Restaked</p>', unsafe_allow_html=True)

        tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

        total_restaked = st.number_input("**Total Restaked on AVS ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)


        tvl = float(tvl) if tvl else 0
        total_restaked = float(total_restaked) if total_restaked else 0

        with st.expander("Logic"):
                st.markdown("""
                    CVS (Cost to Violate Safety) and CVL (Cost to Violate Liveliness) based and 51% operator attack dependant...
                """)

        return


avs_tvl_total_staked_risk_score = avs_tvl_total_staked_risk()




# Operator Risk


def operator_attack_risk():
        
        # High risk if either TVL or total restaked is below $50,000
        if tvl < 100000 or total_restaked < 100000:
            return 10
        
        default_minimum_risk = 9

        operator_attack_weight = 3 * 5                  # Likelihood 3, Impact 5
        operator_attack_risk * operator_attack_weight # Use the calculated risk score directly


        ratio = (total_restaked / 2) / tvl

        if ratio > 1.5:
            return 1  # Significantly greater than TVL, lowest risk
        elif ratio > 1:
            return 3  # Greater than TVL, moderate risk
        elif ratio > 0.5:
            return 5  # Less than TVL but not by a wide margin, increased risk
        else:
            return 7
        
        

    
operator_attack_risk_score = operator_attack_risk())