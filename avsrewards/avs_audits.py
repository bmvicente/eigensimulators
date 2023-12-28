
import streamlit as st

### SECURITY AUDITS 

def avs_sec_audits():

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

        st.markdown('<p class="header-style">AVS Number of Security Audits</p>', unsafe_allow_html=True)

        security_audits = st.number_input("", min_value=0, max_value=5, step=1)

        with st.expander("Logic"):
                st.markdown("""
                        Registering the number of security audits performed onto an AVS provides a good insight into the reliability and robustness of their code structure.
                        While this input is purely quantitative, in terms of the number of audits performed, a strong correlation exists with its underlying smart contract risks, and thus rewards an AVS is confident to emit and restakers and operators to opt into it.
                """)