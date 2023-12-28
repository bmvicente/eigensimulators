
import streamlit as st


# AVS TVL & Total Restaked
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

st.write("  \n")

col3, col4 = st.columns([3, 3])

with col3:
    tvl = st.number_input("**AVS TVL ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

with col4:
    total_restaked = st.number_input("**Total Restaked on AVS ($)**", min_value=0, max_value=10000000000, value=0, step=1000000)

tvl = float(tvl) if tvl else 0
total_restaked = float(total_restaked) if total_restaked else 0

with st.expander("Logic"):
    st.markdown("""
            CVS (Cost to Violate Safety) and CVL (Cost to Violate Liveliness) based and 51% operator attack dependant...
                """)