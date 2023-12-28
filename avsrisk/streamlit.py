
import streamlit as st


# Streamlit app setup
def main():
    st.set_page_config(layout="wide")

    st.image("eigenimage.png")

    st.title("AVS Risk Simulator")
    
    st.write("  \n")

    # Creating two major columns
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
    with col2:


    st.write("  \n")

    st.write("The AVS Risk Score ranges from 0 to 10, where 0 indicates the lowest level of risk and 10 represents the highest possible risk. The risk score of this AVS tells us...")


if __name__ == "__main__":
    main()