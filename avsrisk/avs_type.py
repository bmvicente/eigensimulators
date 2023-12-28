
import streamlit as st

# AVS Type

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

st.write("  \n")

avs_type = st.selectbox("", ["Lightweight", "Hyperscale"])

with st.expander("Logic"):
    st.markdown("""
                In designing modules for maximal security and minimal centralization risk, EigenLayer suggests two approaches: **Hyperscale** and **Lightweight AVS** [(Section 3.6 of EigenLayer's Whitepaper)](https://docs.eigenlayer.xyz/overview/readme/whitepaper). 
                        
                **Hyperscale AVS** involves distributing the computational workload across many nodes, allowing for high overall throughput and reducing incentives for centralized validation. This horizontal scaling minimizes validation costs and amortization gains for any central operator. 
                
                On the other hand, the **Lightweight** approach focuses on tasks that are redundantly performed by all operators but are inexpensive and require minimal computing infrastructure. By combining these hyperscale and lightweight approaches, EigenLayer aims to maximize yield while enabling even home validators on Ethereum to benefit economically, thus minimizing centralization pressures on Ethereum staking. This strategy ensures maximum security by leveraging the full potential of restaked ETH on EigenLayer and addressing operational and computational resource concerns.                        
                        """)