
import streamlit as st 



def renzo_avs_risk(avs_code_comp, avs_op_rep, avs_op_geo):

    avs_code_comp_risk = {"High": 10, "Medium": 5, "Low": 1}
    avs_op_rep_risk = {"Unknown": 10, "Established": 5, "Renowned": 1}
    avs_op_geo_risk = {"Centralized": 10, "Semi-Decentralized": 5, "Decentralized": 1}

    avs_code_comp_score = avs_code_comp_risk[avs_code_comp]
    avs_op_rep_score = avs_op_rep_risk[avs_op_rep]
    avs_op_geo_score = avs_op_geo_risk[avs_op_geo]

    total_score = avs_code_comp_score + avs_op_rep_score + avs_op_geo_score

    min_possible_score = 2  # Minimum possible score (all low)
    max_possible_score = 31  # Maximum possible score (all high)
    normalized_risk_score = (total_score - min_possible_score) / (max_possible_score - min_possible_score) * 10
    normalized_risk_score = round(normalized_risk_score, 2)

    return normalized_risk_score



def main():

    st.image("images/renzo1.png", width=350)

    st.write("\n")

    st.title("Renzo: AVS Risk")

    st.write("\n")
    st.write("\n")
    st.write("\n")


    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        avs_code_comp = st.selectbox("**AVS Code Complexity**", ["Low", "Medium", "High"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avskey1")

        if avs_code_comp == "High":
            color = "#FF0000"  # Standard red
            background_color = "#FFCCCC"  # Light red
        elif avs_code_comp == "Medium":
            color = "#FFFF00"  # Standard yellow
            background_color = "#FFFFE0"  # Light yellow
        else:  # "Low"
            color = "#008000"  # Standard green
            background_color = "#90EE90"  # Light green

        st.markdown(
            f"""
            <div style="
                border: 2px solid {color};
                border-radius: 5px;
                padding: 32px;
                text-align: center;
                margin: 10px 0;
                background-color: {background_color};">
                <h2 style="color: black; margin:0; font-size: 1.2em;">AVS Code Complexity: <span style="font-size: 1.28em;">  {avs_code_comp}</span></h2>
            </div>
            """, 
            unsafe_allow_html=True
        )


    with col2:
        avs_op_rep = st.selectbox("**AVS Operator Reputation**", ["Renowned", "Established", "Unknown"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avskey2")

        if avs_op_rep == "Unknown":
            color = "#FF0000"  # Standard red
            background_color = "#FFCCCC"  # Light red
        elif avs_op_rep == "Established":
            color = "#FFFF00"  # Standard yellow
            background_color = "#FFFFE0"  # Light yellow
        else:  # "Low"
            color = "#008000"  # Standard green
            background_color = "#90EE90"  # Light green

        st.markdown(
        f"""
        <div style="
            border: 2px solid {color};
            border-radius: 5px;
            padding: 30px;
            text-align: center;
            margin: 10px 0;
            background-color: {background_color};">
            <h2 style="color: black; margin:0; font-size: 1.2em;">AVS Operator Reputation: <span style="font-size: 1.25em;">{avs_op_rep}</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
        )


    with col3:
        avs_op_geo = st.selectbox("**AVS Op. Geo Distribution**", ["Decentralized", "Semi-Decentralized", "Centralized"], help="Important to evaluate systemic risk. AVSs in the same categories share a lot of commonalities, such as operating with the same underlying modules.", key="avskey3")

        if avs_op_geo == "Centralized":
            color = "#FF0000"  # Standard red
            background_color = "#FFCCCC"  # Light red
        elif avs_op_geo == "Semi-Decentralized":
            color = "#FFFF00"  # Standard yellow
            background_color = "#FFFFE0"  # Light yellow
        else:  # "Low"
            color = "#008000"  # Standard green
            background_color = "#90EE90"  # Light green

        st.markdown(
        f"""
        <div style="
            border: 2px solid  {color};
            border-radius: 5px;
            padding: 18px;
            text-align: center;
            margin: 10px 0;
            background-color: {background_color};">
            <h2 style="color: black; margin:0; font-size: 1.2em;">AVS Operator Geographical Distribution: <span style="font-size: 1.25em;">{avs_op_geo}</span></h2>
        </div>
        """, 
        unsafe_allow_html=True
        )


    st.write("\n")


    risk_score = renzo_avs_risk(avs_code_comp, avs_op_rep, avs_op_geo)

    # Determine the color and background color based on the risk score
    if risk_score >= 7.50:
        renzo_color = "#d32f2f"  # Red color for high risk
        renzo_background_color = "#fde0dc"  # Light red background
    elif risk_score <= 2.50:
        renzo_color = "#388e3c"  # Green color for low risk
        renzo_background_color = "#ebf5eb"  # Light green background
    else:
        renzo_color = "black"  # Black color for medium risk
        renzo_background_color = "#ffffff"  # White background


    st.markdown(
    f"""
    <div style="
        border: 3px solid {renzo_color};
        border-radius: 5px;
        padding: 10px;
        text-align: center;
        margin: 10px 0;
        background-color: {renzo_background_color};">
        <h2 style="color: black; margin:0; font-size: 1.4em;">AVS Risk Score: <span style="font-size: 1.5em; color: {renzo_color};">{risk_score:.2f}</span></h2>
    </div>
    """, 
    unsafe_allow_html=True
    )


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    col11, col12, col13 = st.columns([2,1,2])

    with col11:
        st.write("")

    with col12:
        st.image("images/tokensight.png", width=250)

    with col13:
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