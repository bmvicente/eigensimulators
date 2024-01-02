
import streamlit as st


### AVS TYPE

def get_avs_type():
    return st.selectbox("", ["Lightweight", "Hyperscale"])

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

    # Calling get_avs_type as a function to get the actual value
    avs_type_selected = get_avs_type()


    with st.expander("Logic"):
        st.markdown("""
            While it does depend on the needs of an AVS and while a **Lightweight AVS** safeguards it from risks otherwise incurred from a centralized architecture, the **Hyperscale**-type is more robust and secure, particularly for new-born AVSs. Therefore, it was categorized as the safest AVS type in our Simulator, and thus a lower reward level is sensible to assume when selecting this category, relative to the Lightweight AVS type.
                    """)

    return avs_type_selected


# If you need to use this function in your Streamlit app
selected_avs_type_adjustment = avs_type()  # This will also render the selection box and explanation
