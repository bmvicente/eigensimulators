
import streamlit as st
import pandas as pd

def main():
    st.set_page_config(layout="wide")

    st.image("images/eigenimage.png")

    st.title("Cryptoeconomic Risk Analysis III")
    st.subheader("**AVS Ecosystem Risk Simulator**")
    
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.markdown('<p style="font-weight: bold; font-size: 1.2em;">NEXT...</p>', unsafe_allow_html=True)
    
    st.write(f"""Cryptoeconomic security quantifies the cost that an adversary must bear in order to cause a protocol to lose a desired security property. 
             This is referred to as the Cost-of-Corruption (CoC). When CoC is much greater than any potential Profit-from-Corruption (PfC), we say that the system has robust security. 
             A core idea of EigenLayer is to provision cryptoeconomic security through various slashing mechanisms which levy a high cost of corruption.
             """)
    
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    
    st.markdown('<p class="header-style"><strong>AVS ECOSYSTEM RISK</strong></p>', unsafe_allow_html=True)

    st.write(f"""
             Let us take the scenario of the Max Slash event:

             - Actual Total Loss?
             - Probability of all 3 AVSs failing? p(AVS1) * p(AVS2) * p(AVS3)
             - How to visualize compounded risks that may exist. How AVS1 could affect 2 and 3? Visual Tool? Detail scenarios (in writing too)
             
             Dependencies between AVSs
             - Diversity of the AVSs nature, systemic risk, same modules being used
             - Percentage of Overlaping Operators Between the AVSs
                """)

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    col40, col41 = st.columns(2)

    with col40:
         st.markdown('<p class="header-style"><strong>AVSs RISK PROFILES BEFORE & AFTER MAX SLASH EVENT</strong></p>', unsafe_allow_html=True)
    #     average_risk_score = (st.session_state.risk_score1 + st.session_state.risk_score2 + st.session_state.risk_score3) / 3

         st.write(f"""
                     **Risk Scores *Before* Max Slash Event**
                     - AVS 1 Risk Score: ...
                     - AVS 2 Risk Score: ...
                     - AVS 3 Risk Score: ...                  
                     - Average AVSs Risk Score: ***...***

                     **Risk Scores *After* Max Slash Event**
                     - AVS 1 Risk Score: ...
                     - AVS 2 Risk Score: ...
                     - AVS 3 Risk Score: ...
                     - Average AVSs Risk Score: ***...***
                     """)
        
    with col41:
             st.markdown('<p class="header-style"><strong>ECOSYSTEM SHARPE RATIOS</strong></p>', unsafe_allow_html=True)
             st.markdown('<p class="header-style">Three Risk-Adjusted Reward Scenarios: Operator to AVS, Restaker to Operator, Restaker to AVS</p>', unsafe_allow_html=True)
             st.write("  \n")
             st.write(f"""
                     - **Operator/AVS Sharpe Ratio**: ...
                     - **Restaker/Operator Sharpe Ratio**: ...
                     - **Restaker/AVS Sharpe Ratio**: ...
                     """)

             
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    st.markdown('<p class="header-style"><strong>GAME THEORY MATRIX</strong></p>', unsafe_allow_html=True)
    st.markdown('<p class="header-style"><strong>Operator Decision-Making on AVS Restaking Allocation Based on Slashing Likelihood</strong></p>', unsafe_allow_html=True)
    st.write("*NS: Non-Slashing Event | S: Slashing Event*")

    st.write("  \n")

    data = {
         'Strategies': ["1", "2", "3", "4", "5", "6", "7", "8"],
         'AVS 1': ["NS", "NS", "NS", "NS", "S", "S", "S", "S"],
         'AVS 2': ["NS", "NS", "S", "S", "NS", "NS", "S", "S"],
         'AVS 3': ["NS", "S", "NS", "S", "NS", "S", "NS", "S"],
         'Pay-Off': ["...", "...", "...", "...", "...", "...", "...", "..."]
     }

    df = pd.DataFrame(data)

    st.table(df)

    st.markdown("2<sup>3</sup> = 8 possible scenarios that can affect the Operator with a pool of 3 AVSs to validate.", unsafe_allow_html=True)

    st.write("  \n")

    with st.expander("Logic"):
            st.markdown("""Add in cooperative, non-zero-sum, etc game...
    #             """)
         
    #                 - AVS 1 Risk Score: {st.session_state.risk_score1} 
    #                 - AVS 2 Risk Score: {st.session_state.risk_score2} 
    #                 - AVS 3 Risk Score: {st.session_state.risk_score3} 
    #                 - Average AVSs Risk Score: ***{average_risk_score:.2f}***

    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")
    st.write("  \n")

    col50, col51, col52 = st.columns([4,2,4])

    with col50:
        st.write("")

    with col51:
        st.image("images/tokensight.png", width=250)

    with col52:
        st.write("")
    
    
    image_url = 'https://img.freepik.com/free-vector/twitter-new-2023-x-logo-white-background-vector_1017-45422.jpg'
    link = 'https://twitter.com/tokensightxyz'
    markdown = f"""
    <a href="{link}" target="_blank">
        <img src="{image_url}" alt="Alt Text" style="display:block; margin-left: auto; margin-right: auto; width: 4%;">
    </a>
    """    
    st.markdown(markdown, unsafe_allow_html=True)



if __name__ == "__main__":
    main()