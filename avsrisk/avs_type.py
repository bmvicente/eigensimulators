
import streamlit as st


### AVS TYPE

def avs_type():
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

    st.markdown('<p class="header-style">AVS Type</p>', unsafe_allow_html=True)

    avs_type_risk = {"Lightweight": 10, "Hyperscale": 1}
    avs_type_weight = 1 * 2     # Likelihood 2, Impact 2

    user_selection = st.selectbox("Select the average reputation of operators", ["Unknown", "Established", "Renowned"])

    avs_type_score = avs_type_risk[user_selection]
    avs_type_risk_score = avs_type_score * avs_type_weight

    with st.expander("Logic"):
        st.markdown("""
            While it does depend on the needs of an AVS and while a **Lightweight AVS** safeguards it from risks otherwise incurred from a centralized architecture, the **Hyperscale**-type is more robust and secure, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our Simulator, and thus a lower reward level is sensible to assume when selecting this category, relative to the Lightweight AVS type.
                    """)

    return avs_type_risk_score


# If you need to use this function in your Streamlit app
avs_type_risk_score_result = avs_type()  # This will also render the selection box and explanation
