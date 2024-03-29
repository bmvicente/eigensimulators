
import streamlit as st 



def renzo_avs_risk(avs_code_comp, avs_op_rep, avs_op_geo):

    avs_code_comp_risk = {"High": 10, "Medium": 5, "Low": 1}
    avs_op_rep_risk = {"High": 10, "Medium": 5, "Low": 1}
    avs_op_geo = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}

    avs_code_comp_score = avs_code_comp_risk[avs_code_comp]
    avs_op_rep_score = avs_op_rep_risk[avs_op_rep]
    avs_op_geo_score = avs_op_geo[avs_op_geo]

    normalized_risk_score = avs_code_comp_score + avs_op_rep_score + avs_op_geo_score
    normalized_risk_score = round(normalized_risk_score, 2)

    return normalized_risk_score



def main():

    st.title("Renzo: AVS Portfolio Risk")

    st.write("\n" * 4)


    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        avs_code_comp = st.selectbox("**AVS Code Complexity**", ["Low", "Medium", "High"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avs1_category_key")

        if avs_code_comp == "High":
            background_color = "red"
        elif avs_code_comp == "Medium":
            background_color = "yellow"
        else:  # "Low"
            background_color = "green"

        st.markdown(
            f"""
            <div style="
                border: 2px solid;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                margin: 10px 0;
                background-color: {background_color};">
                <h2 margin:0; font-size: 1.4em;">**AVS Code Complexity**: <span style="font-size: 1.5em;">{avs_code_comp}</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


    with col2:
        avs_op_rep = st.selectbox("**AVS Operator Reputation**", ["High", "Medium", "Low"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avs1_category_key")

        # Assign color based on selection
        if avs_op_rep == "High":
            background_color = "green"
        elif avs_op_rep == "Medium":
            background_color = "yellow"
        else:  # "Low"
            background_color = "red"

        st.markdown(
        f"""
        <div style="
            border: 2px solid;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            margin: 10px 0;
            background-color: {background_color};">
            <h2 style="color: black; margin:0; font-size: 1.4em;">**AVS Operator Reputation**: <span style="font-size: 1.5em;">{avs_op_rep:.0f}</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
        )

    with col3:
        avs_op_geo = st.selectbox("**AVS Operator Geographical Distribution**", ["Decentralized", "Semi-Decentralized", "Centralized"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avs1_category_key")

        # Assign color based on selection
        if avs_op_geo == "Decentralized":
            background_color = "green"
        elif avs_op_geo == "Semi-Decentralized":
            background_color = "yellow"
        else:  # "Low"
            background_color = "red"

        st.markdown(
        f"""
        <div style="
            border: 2px solid;
            border-radius: 5px;
            padding: 10px;
            text-align: center;
            margin: 10px 0;
            background-color: {background_color};">
            <h2 style="color: black; margin:0; font-size: 1.4em;">**AVS Operator Geographical Distribution**: <span style="font-size: 1.5em;">{avs_op_geo:.0f}</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
        )




    renzo_avs_risk = renzo_avs_risk(avs_code_comp, avs_op_rep, avs_op_geo)

    # Determine the color and background color based on the risk score
    if renzo_avs_risk >= 7.5:
        renzo_color = "#d32f2f"  # Red color for high risk
        renzo_background_color = "#fde0dc"  # Light red background
    elif renzo_avs_risk <= 2.5:
        renzo_color = "#388e3c"  # Green color for low risk
        renzo_background_color = "#ebf5eb"  # Light green background
    else:
        renzo_color = "black"  # Black color for medium risk
        renzo_background_color = "#ffffff"  # White background




    st.markdown(
    f"""
    <div style="
        border: 2px solid {renzo_color};
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        margin: 10px 0;
        background-color: {renzo_background_color};">
        <h2 style="color: black; margin:0; font-size: 1.4em;">AVS Risk Score: <span style="font-size: 1.5em; color: {renzo_color};">{renzo_avs_risk:.0f}</span></h2>
    </div>
    """, 
    unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()