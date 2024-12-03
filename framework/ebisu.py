import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Ebisu Dashboard", layout="wide")
st.image("framework/images/ebisunoback.png", width=150)
st.title("Ebisu Dashboard")

# Function to fetch AVS data from the EigenExplorer API
@st.cache_data(ttl=60)
def fetch_ee_avs_data():
    url = "https://api.eigenexplorer.com/avs"
    params = {
        "withTVL": "true",
        "withCuratedMetadata": "true",
        "sortByTVL": "desc",
        "take": 100
    }
    headers = {"x-api-key": "your_api_key_here"}  # Replace with your actual API key
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch EigenExplorer AVS data: {response.status_code}")
        return None

# Function to fetch LRT balances from the u--1 API
@st.cache_data(ttl=60)
def fetch_u1_avs_balances():
    url = "https://api.u--1.com/v2/latest-avs-balances"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch LRT balances data: {response.status_code}")
        return None

# Function to fetch LRT balances from the u--1 API
@st.cache_data(ttl=60)
def fetch_u1_lrt_balances():
    url = "https://api.u--1.com/v2/latest-lrt-balances"
    params = {"api_key": "9e325ecaa2cb49e895595e0e446e1d64"}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch LRT balances data: {response.status_code}")
        return None



# IR values mapped to AVS addresses
ir_mapping = {
    "0x23221c5bb90c7c57ecc1e75513e2e4257673f0ef": 5.99,
    "0x870679e138bcdf293b7ff14dd44b70fc97e12fc0": 7.08,
    "0xed2f4d90b073128ae6769a9a8d51547b1df766c8": 14.72,
    "0x35f4f28a8d3ff20eed10e087e8f96ea2641e6aa2": 7.15,
    "0x22cac0e6a1465f043428e8aef737b3cb09d0eeda": 8.47,
    "0x9fc952bdcbb7daca7d420fa55b942405b073a89d": 28.42,
    "0x71a77037870169d47aad6c2c9360861a4c0df2bf": 9.46,
    "0x6026b61bdd2252160691cb3f6005b6b72e0ec044": 9.46,
    "0xd25c2c5802198cb8541987b73a8db4c9bcae5cc7": 17.57,
    "0xe544583c475a2980e6a88054ff1514230b83aeb": 12.74,
    "0x7f7cff55d5fdaf2c3bbeb140be5e62a2c7d26db3": 15.41,
    "0x1de75eaab2df55d467494a172652579e6fa4540e": 11.82,
    "0x1f2c296448f692af840843d993ffc0546619dcdb": 14.00,
    "0xe8e59c6c8b56f2c178f63bcfc4ce5e5e2359c8fc": 12.75,
}

# Fetch AVS data
st.header("EigenLayer: Current AVS Table")

eigen_avs_data = fetch_ee_avs_data()
avs_category_mapping = {}
if eigen_avs_data and "data" in eigen_avs_data:
    avs_records = eigen_avs_data["data"]
    processed_data = []
    for record in avs_records:
        address = record.get("address", "")
        metadata_name = record.get("metadataName", "")
        curated_metadata = record.get("curatedMetadata") or {}
        tags = curated_metadata.get("tags", [])
        tags_str = ", ".join(tags) if tags else "None"
        avs_category_mapping[address] = tags_str
        ir = ir_mapping.get(address, 25)  # Default to 25 if no IR value is found
        processed_data.append({
            "Address": address,
            "Name": metadata_name,
            "Category": tags_str,
            "IR": round(float(ir), 2)  # Ensure IR is a float before rounding
        })

    # Convert processed data into a DataFrame
    avs_df = pd.DataFrame(processed_data)

    # Apply styling to highlight rows where IR == 25
    def highlight_rows(row):
        return ['background-color: #FAF3E0'] * len(row) if row["IR"] == 25 else [''] * len(row)

    styled_avs_df = avs_df.style.apply(highlight_rows, axis=1)

    # Display the styled DataFrame
    st.dataframe(styled_avs_df)

else:
    st.write("No AVS data available to display.")


st.markdown("**<u>Note</u>:** AVSs without assigned risk scores are highlighted in yellow and defaulted to a risk score of 25 for calculation purposes.", unsafe_allow_html=True)




st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")





# Fetch LRT balances data
st.header("LRTs Full Analysis: Ether.fi, Renzo, Puffer, Kelp")

if not avs_category_mapping:
    avs_category_mapping = {}

# Fetch AVS balances data
avs_balances_data = fetch_u1_avs_balances()

# Safely map AVS balances
# Safely map AVS balances based on correct API structure
avs_balances_mapping = {
    avs_address: details.get("totalUsdValue", 0) 
    for avs_address, details in avs_balances_data.items()
} if avs_balances_data else {}

lrt_balances_data = fetch_u1_lrt_balances()

if lrt_balances_data:

    if "ether.fi" in lrt_balances_data:
        # Get Ether.fi data
        etherfi_data = lrt_balances_data["ether.fi"]["latest"]
        etherfi_avs_registrations = etherfi_data.get("avsRegistrations", [])

        # Calculate the LIR
        total_usd_restaked = sum(
            avs.get("totalUsdValueRestaked", 0) for avs in etherfi_avs_registrations
        )
        etherfi_lir = 0
        etherfi_lir_data = []

        for avs in etherfi_avs_registrations:
            avs_address = avs.get("address", "N/A")
            avs_name = avs.get("name", "N/A")
            avs_total_usd = avs.get("totalUsdValueRestaked", 0)
            avs_ir = ir_mapping.get(avs_address, 25)  # Default IR is 25
            avs_category = avs_category_mapping.get(avs_address, "Unknown")  # Map Category
            # Fetch AVS total USD value balances
            avs_total_usd_balances = avs_balances_mapping.get(avs_address, 0)  # Updated to use corrected mapping

            # Calculate eETH % of Total
            eeth_percentage_of_total = (
                (avs_total_usd / avs_total_usd_balances * 100) 
                if avs_total_usd_balances > 0 else 0
            )

            # Calculate weighted risk
            weighted_risk = (eeth_percentage_of_total / 100) * avs_ir  # Adjusting percentage to a decimal
            etherfi_lir += weighted_risk

            etherfi_lir_data.append({
                "Address": avs_address,
                "AVS Name": avs_name,
                "Category": avs_category,  # Add the Category column
                "Etherfi Total USD Value Restaked on AVS": f"${avs_total_usd:,.2f}",
                "AVS Total USD Value Restaked": f"${avs_total_usd_balances:,.2f}",  # New column
                "eETH % of Total": f"{eeth_percentage_of_total:.2f}%",  # New column for percentage
                "IR": round(avs_ir, 2),
                "LIR": round(weighted_risk, 4)
            })


        # Display LIR Table
        etherfi_lir_df = pd.DataFrame(etherfi_lir_data)

        # Convert percentage column to numeric for sorting or calculations
        etherfi_lir_df["eETH % of Total"] = etherfi_lir_df["eETH % of Total"].str.rstrip('%').astype(float)


        # Highlight rows where IR == 25
        def highlight_ir(row):
            return ['background-color: #FAF3E0'] * len(row) if row["IR"] == 25 else [''] * len(row)

        styled_etherfi_lir_df = etherfi_lir_df.style.apply(highlight_ir, axis=1)

        # Display LIR Table
        st.markdown('<span style="color: blue; font-size: 25px;"><b>Ether.fi</b></span><span style="font-size: 22px;">: AVS Registrations</span>', unsafe_allow_html=True)
        st.dataframe(styled_etherfi_lir_df)

        # --- Calculate LPR ---
        n_avs = len(etherfi_avs_registrations)
        n_t = 0.12 if n_avs >= 15 else 0.075 if n_avs >= 10 else 0.05 if n_avs >= 5 else 0

        category_counts = {}
        for avs in etherfi_avs_registrations:
            address = avs.get("address", "N/A")
            category = avs_category_mapping.get(address, "Unknown")
            category_counts[category] = category_counts.get(category, 0) + 1

        most_common_category_percentage = max(category_counts.values()) / n_avs if n_avs > 0 else 0
        c_t = 0.10 if most_common_category_percentage > 0.5 else 0.05 if most_common_category_percentage >= 0.2 else 0

        ir_scores = [ir_mapping.get(avs.get("address", "N/A"), 20) for avs in etherfi_avs_registrations]
        low_ir_percentage = sum(1 for ir in ir_scores if ir < 10) / n_avs
        medium_ir_percentage = sum(1 for ir in ir_scores if 10 <= ir <= 20) / n_avs
        high_ir_percentage = sum(1 for ir in ir_scores if ir > 20) / n_avs

        # Updated logic with default value
        if low_ir_percentage > 0.5:
            a_t = 0.05  # +5%
        elif medium_ir_percentage > 0.5:
            a_t = 0.10  # +10%
        elif high_ir_percentage > 0.5:
            a_t = 0.20  # +20%
        else:
            a_t = 0.075  # Default to +7.5%

        etherfi_lpr = etherfi_lir * (1 + n_t + c_t + a_t)

        # --- Calculate DC and CR ---
        total_ta = 100_000_000  # Example Total Allowable Amount (TA)
        lrt_lpr_values = [etherfi_lpr, 18.05, 10.0, 30.0]  # Replace with all available LPRs
        inv_lpr_sum = sum(1 / lpr for lpr in lrt_lpr_values if lpr > 0)

        etherfi_dc = total_ta * ((1 / etherfi_lpr) / inv_lpr_sum) if etherfi_lpr > 0 else 0
        etherfi_cr = 1 + (etherfi_lpr / sum(lrt_lpr_values)) if etherfi_lpr > 0 else 0

        # Display LIR, LPR, DC, and CR in a table
        etherfi_summary_data = [
            {"Metric": "LIR", "Value": round(etherfi_lir, 2)},
            {"Metric": "LPR", "Value": round(etherfi_lpr, 2)},
            {"Metric": "Deposit Cap (DC)", "Value": f"${etherfi_dc:,.2f}"},
            {"Metric": "Collateralization Ratio (CR)", "Value": f"{etherfi_cr * 100:.2f}%"}
        ]
        etherfi_summary_df = pd.DataFrame(etherfi_summary_data)

        st.write("\n")
        st.markdown("**Ether.fi Summary Metrics**")
        st.dataframe(etherfi_summary_df)

        # Include expanded breakdown
        with st.expander("Metrics Calc Method"):
            st.markdown(f"""
            ##### LPR Calculation Breakdown = LIR * (1 + N + C + A)
            - **N (Number of AVSs):** {n_t:.2%}
            - **C (Category Risk):** {c_t:.2%}
            - **A (Individual Risk Contribution):** {a_t:.2%}
            - **Ether.fi LPR:** {etherfi_lir:.2f} * (1 + {n_t:.2f} + {c_t:.2f} + {a_t:.2f}) = {etherfi_lpr:.2f}

            ##### DC Calculation Breakdown = TA * (1 / Ether.fi LPR) / Sum(1/LPR)
            - **TA (Total Allowable Amount):** ${total_ta:,.2f}
            - **Sum of 1/LPR:** {inv_lpr_sum:.4f}
            - **Ether.fi DC:** {total_ta:,.2f} * (1 / {etherfi_lpr:.2f}) / {inv_lpr_sum:.4f} = ${etherfi_dc:,.2f}

            ##### CR Calculation Breakdown = 1 + (Ether.fi LPR / Sum(LPRs))
            - **Sum of LPRs:** {sum(lrt_lpr_values):.2f}
            - **Ether.fi CR:** 1 + ({etherfi_lpr:.2f} / {sum(lrt_lpr_values):.2f}) = {etherfi_cr * 100:.2f}%
            <br>
            ***LIR*** represents the aggregate risk score for the LRT (***t***), accounting only for individual, isolated AVS risks on its portfolio selection, weighted according to relative delegation by the LRT.
            ***LPR*** provides a comprehensive underwriting of the interdependent risk exposure of the pooled ecosystem of AVSs selected by the LRT.
            ***DC*** calculates the deposit cap by taking the total allowable amount for LRT deposits (***TA***), as determined by Ebisu, and adjusts it based on the relative risk of each LRT (***LPR***), in the context of Ebisu’s basket of LRTs (**Σ *LPR***).
            ***CR*** relativizes the pooled risk of the LRT portfolio at hand (***LPR***), against the aggregate pooled risk of ALL the LRT portfolios (Ebisu’s LRT basket (**Σ *LPR***)) to arrive at a considerate, minimum collateralisation ratio for the LRT being considered.
            """)





    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("------------")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")






    if "renzo" in lrt_balances_data:
        # Get Renzo data
        renzo_data = lrt_balances_data["renzo"]["latest"]
        renzo_avs_registrations = renzo_data.get("avsRegistrations", [])

        # Calculate the LIR
        total_usd_restaked = sum(
            avs.get("totalUsdValueRestaked", 0) for avs in renzo_avs_registrations
        )
        renzo_lir = 0
        renzo_lir_data = []

        for avs in renzo_avs_registrations:
            avs_address = avs.get("address", "N/A")
            avs_name = avs.get("name", "N/A")
            avs_total_usd = avs.get("totalUsdValueRestaked", 0)
            avs_ir = ir_mapping.get(avs_address, 25)  # Default IR is 25
            avs_category = avs_category_mapping.get(avs_address, "Unknown")  # Map Category

            weight = avs_total_usd / total_usd_restaked if total_usd_restaked > 0 else 0
            weighted_risk = weight * avs_ir
            renzo_lir += weighted_risk

            renzo_lir_data.append({
                "Address": avs_address,
                "AVS Name": avs_name,
                "Category": avs_category,  # Add the Category column
                "Total USD Value Restaked": f"${avs_total_usd:,.2f}",
                "IR": round(avs_ir, 2),
                "AIR": round(weighted_risk, 4)
            })

        # Display LIR Table
        renzo_lir_df = pd.DataFrame(renzo_lir_data)

        # Highlight rows where IR == 25
        def highlight_ir(row):
            return ['background-color: #FAF3E0'] * len(row) if row["IR"] == 25 else [''] * len(row)

        styled_renzo_lir_df = renzo_lir_df.style.apply(highlight_ir, axis=1)

        # Display LIR Table
        st.markdown('<span style="color: green; font-size: 25px;"><b>Renzo</b></span><span style="font-size: 22px;">: AVS Registrations</span>', unsafe_allow_html=True)
        st.dataframe(styled_renzo_lir_df)

        # --- Calculate LPR ---
        n_avs = len(renzo_avs_registrations)
        n_t = 0.12 if n_avs >= 15 else 0.075 if n_avs >= 10 else 0.05 if n_avs >= 5 else 0

        category_counts = {}
        for avs in renzo_avs_registrations:
            address = avs.get("address", "N/A")
            category = avs_category_mapping.get(address, "Unknown")
            category_counts[category] = category_counts.get(category, 0) + 1

        most_common_category_percentage = max(category_counts.values()) / n_avs if n_avs > 0 else 0
        c_t = 0.10 if most_common_category_percentage > 0.5 else 0.05 if most_common_category_percentage >= 0.2 else 0

        ir_scores = [ir_mapping.get(avs.get("address", "N/A"), 20) for avs in renzo_avs_registrations]
        low_ir_percentage = sum(1 for ir in ir_scores if ir < 10) / n_avs
        medium_ir_percentage = sum(1 for ir in ir_scores if 10 <= ir <= 20) / n_avs
        high_ir_percentage = sum(1 for ir in ir_scores if ir > 20) / n_avs

        if low_ir_percentage > 0.5:
            a_t = 0.05
        elif medium_ir_percentage > 0.5:
            a_t = 0.10
        elif high_ir_percentage > 0.5:
            a_t = 0.20
        else:
            a_t = 0

        renzo_lpr = renzo_lir * (1 + n_t + c_t + a_t)

        # --- Calculate DC and CR ---
        total_ta = 100_000_000  # Example Total Allowable Amount (TA)
        lrt_lpr_values = [renzo_lpr, 18.05, 10.0, 30.0]  # Replace with all available LPRs
        inv_lpr_sum = sum(1 / lpr for lpr in lrt_lpr_values if lpr > 0)

        renzo_dc = total_ta * ((1 / renzo_lpr) / inv_lpr_sum) if renzo_lpr > 0 else 0
        renzo_cr = 1 + (renzo_lpr / sum(lrt_lpr_values)) if renzo_lpr > 0 else 0

        # Display LIR, LPR, DC, and CR in a table
        renzo_summary_data = [
            {"Metric": "LIR", "Value": round(renzo_lir, 2)},
            {"Metric": "LPR", "Value": round(renzo_lpr, 2)},
            {"Metric": "Deposit Cap (DC)", "Value": f"${renzo_dc:,.2f}"},
            {"Metric": "Collateralization Ratio (CR)", "Value": f"{renzo_cr * 100:.2f}%"}
        ]
        renzo_summary_df = pd.DataFrame(renzo_summary_data)

        st.write("\n")
        st.markdown("**Renzo Summary Metrics**")
        st.dataframe(renzo_summary_df)

        with st.expander("Metrics Calc Method"):
            st.markdown("""
            **LIR** represents the aggregate risk score for the LRT (*t*), accounting only for individual, isolated AVS risks on its portfolio selection, weighted according to relative delegation by the LRT.

            **LPR** provides a comprehensive underwriting of the interdependent risk exposure of the pooled ecosystem of AVSs selected by the LRT.

            **DC** calculates the deposit cap by taking the total allowable amount for LRT deposits (*TA*), as determined by Ebisu, and adjusts it based on the relative risk of each LRT (*LPR*), in the context of Ebisu’s basket of LRTs (\(Σ LPR\)).

            **CR** relativizes the pooled risk of the LRT portfolio at hand (*LPR*), against the aggregate pooled risk of ALL the LRT portfolios (Ebisu’s LRT basket \(Σ LPR\)) to arrive at a considerate, minimum collateralization ratio for the LRT being considered.
            """)






    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("------------")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")






    if "puffer" in lrt_balances_data:
        # Get Renzo data
        puffer_data = lrt_balances_data["puffer"]["latest"]
        puffer_avs_registrations = puffer_data.get("avsRegistrations", [])

        # Calculate the LIR
        total_usd_restaked = sum(
            avs.get("totalUsdValueRestaked", 0) for avs in puffer_avs_registrations
        )
        puffer_lir = 0
        puffer_lir_data = []

        for avs in puffer_avs_registrations:
            avs_address = avs.get("address", "N/A")
            avs_name = avs.get("name", "N/A")
            avs_total_usd = avs.get("totalUsdValueRestaked", 0)
            avs_ir = ir_mapping.get(avs_address, 25)  # Default IR is 25
            avs_category = avs_category_mapping.get(avs_address, "Unknown")  # Map Category

            weight = avs_total_usd / total_usd_restaked if total_usd_restaked > 0 else 0
            weighted_risk = weight * avs_ir
            puffer_lir += weighted_risk

            puffer_lir_data.append({
                "Address": avs_address,
                "AVS Name": avs_name,
                "Category": avs_category,  # Add the Category column
                "Total USD Value Restaked": f"${avs_total_usd:,.2f}",
                "IR": round(avs_ir, 2),
                "AIR": round(weighted_risk, 4)
            })

        # Display LIR Table
        puffer_lir_df = pd.DataFrame(puffer_lir_data)

        # Highlight rows where IR == 25
        def highlight_ir(row):
            return ['background-color: #FAF3E0'] * len(row) if row["IR"] == 25 else [''] * len(row)

        styled_puffer_lir_df = puffer_lir_df.style.apply(highlight_ir, axis=1)

        # Display LIR Table
        st.markdown('<span style="color: purple; font-size: 25px;"><b>Puffer</b></span><span style="font-size: 22px;">: AVS Registrations</span>', unsafe_allow_html=True)
        st.dataframe(styled_puffer_lir_df)

        # --- Calculate LPR ---
        n_avs = len(puffer_avs_registrations)
        n_t = 0.12 if n_avs >= 15 else 0.075 if n_avs >= 10 else 0.05 if n_avs >= 5 else 0

        category_counts = {}
        for avs in puffer_avs_registrations:
            address = avs.get("address", "N/A")
            category = avs_category_mapping.get(address, "Unknown")
            category_counts[category] = category_counts.get(category, 0) + 1

        most_common_category_percentage = max(category_counts.values()) / n_avs if n_avs > 0 else 0
        c_t = 0.10 if most_common_category_percentage > 0.5 else 0.05 if most_common_category_percentage >= 0.2 else 0

        ir_scores = [ir_mapping.get(avs.get("address", "N/A"), 20) for avs in puffer_avs_registrations]
        low_ir_percentage = sum(1 for ir in ir_scores if ir < 10) / n_avs
        medium_ir_percentage = sum(1 for ir in ir_scores if 10 <= ir <= 20) / n_avs
        high_ir_percentage = sum(1 for ir in ir_scores if ir > 20) / n_avs

        if low_ir_percentage > 0.5:
            a_t = 0.05
        elif medium_ir_percentage > 0.5:
            a_t = 0.10
        elif high_ir_percentage > 0.5:
            a_t = 0.20
        else:
            a_t = 0

        puffer_lpr = puffer_lir * (1 + n_t + c_t + a_t)

        # --- Calculate DC and CR ---
        total_ta = 100_000_000  # Example Total Allowable Amount (TA)
        lrt_lpr_values = [puffer_lpr, 18.05, 10.0, 30.0]  # Replace with all available LPRs
        inv_lpr_sum = sum(1 / lpr for lpr in lrt_lpr_values if lpr > 0)

        puffer_dc = total_ta * ((1 / puffer_lpr) / inv_lpr_sum) if puffer_lpr > 0 else 0
        puffer_cr = 1 + (puffer_lpr / sum(lrt_lpr_values)) if puffer_lpr > 0 else 0

        # Display LIR, LPR, DC, and CR in a table
        puffer_summary_data = [
            {"Metric": "LIR", "Value": round(puffer_lir, 2)},
            {"Metric": "LPR", "Value": round(puffer_lpr, 2)},
            {"Metric": "Deposit Cap (DC)", "Value": f"${puffer_dc:,.2f}"},
            {"Metric": "Collateralization Ratio (CR)", "Value": f"{puffer_cr * 100:.2f}%"}
        ]
        puffer_summary_df = pd.DataFrame(puffer_summary_data)

        st.write("\n")
        st.markdown("**Puffer Summary Metrics**")
        st.dataframe(puffer_summary_df)

        with st.expander("Metrics Calc Method"):
            st.markdown("""
            **LIR** represents the aggregate risk score for the LRT (*t*), accounting only for individual, isolated AVS risks on its portfolio selection, weighted according to relative delegation by the LRT.

            **LPR** provides a comprehensive underwriting of the interdependent risk exposure of the pooled ecosystem of AVSs selected by the LRT.

            **DC** calculates the deposit cap by taking the total allowable amount for LRT deposits (*TA*), as determined by Ebisu, and adjusts it based on the relative risk of each LRT (*LPR*), in the context of Ebisu’s basket of LRTs (\(Σ LPR\)).

            **CR** relativizes the pooled risk of the LRT portfolio at hand (*LPR*), against the aggregate pooled risk of ALL the LRT portfolios (Ebisu’s LRT basket \(Σ LPR\)) to arrive at a considerate, minimum collateralization ratio for the LRT being considered.
            """)





    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("------------")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")






    if "kelp" in lrt_balances_data:
        # Get Renzo data
        kelp_data = lrt_balances_data["kelp"]["latest"]
        kelp_avs_registrations = kelp_data.get("avsRegistrations", [])

        # Calculate the LIR
        total_usd_restaked = sum(
            avs.get("totalUsdValueRestaked", 0) for avs in kelp_avs_registrations
        )
        kelp_lir = 0
        kelp_lir_data = []

        for avs in kelp_avs_registrations:
            avs_address = avs.get("address", "N/A")
            avs_name = avs.get("name", "N/A")
            avs_total_usd = avs.get("totalUsdValueRestaked", 0)
            avs_ir = ir_mapping.get(avs_address, 25)  # Default IR is 25
            avs_category = avs_category_mapping.get(avs_address, "Unknown")  # Map Category

            weight = avs_total_usd / total_usd_restaked if total_usd_restaked > 0 else 0
            weighted_risk = weight * avs_ir
            kelp_lir += weighted_risk

            kelp_lir_data.append({
                "Address": avs_address,
                "AVS Name": avs_name,
                "Category": avs_category,  # Add the Category column
                "Kelp Total USD Value Restaked": f"${avs_total_usd:,.2f}",
                "IR": round(avs_ir, 2),
                "AIR": round(weighted_risk, 4)
            })

        # Display LIR Table
        kelp_lir_df = pd.DataFrame(kelp_lir_data)

        # Highlight rows where IR == 25
        def highlight_ir(row):
            return ['background-color: #FAF3E0'] * len(row) if row["IR"] == 25 else [''] * len(row)

        styled_kelp_lir_df = kelp_lir_df.style.apply(highlight_ir, axis=1)

        # Display LIR Table
        st.markdown('<span style="color: #006400; font-size: 25px;"><b>Kelp</b></span><span style="font-size: 22px;">: AVS Registrations</span>', unsafe_allow_html=True)
        st.dataframe(styled_kelp_lir_df)

        # --- Calculate LPR ---
        n_avs = len(kelp_avs_registrations)
        n_t = 0.12 if n_avs >= 15 else 0.075 if n_avs >= 10 else 0.05 if n_avs >= 5 else 0

        category_counts = {}
        for avs in kelp_avs_registrations:
            address = avs.get("address", "N/A")
            category = avs_category_mapping.get(address, "Unknown")
            category_counts[category] = category_counts.get(category, 0) + 1

        most_common_category_percentage = max(category_counts.values()) / n_avs if n_avs > 0 else 0
        c_t = 0.10 if most_common_category_percentage > 0.5 else 0.05 if most_common_category_percentage >= 0.2 else 0

        ir_scores = [ir_mapping.get(avs.get("address", "N/A"), 20) for avs in kelp_avs_registrations]
        low_ir_percentage = sum(1 for ir in ir_scores if ir < 10) / n_avs
        medium_ir_percentage = sum(1 for ir in ir_scores if 10 <= ir <= 20) / n_avs
        high_ir_percentage = sum(1 for ir in ir_scores if ir > 20) / n_avs

        if low_ir_percentage > 0.5:
            a_t = 0.05
        elif medium_ir_percentage > 0.5:
            a_t = 0.10
        elif high_ir_percentage > 0.5:
            a_t = 0.20
        else:
            a_t = 0

        kelp_lpr = kelp_lir * (1 + n_t + c_t + a_t)

        # --- Calculate DC and CR ---
        total_ta = 100_000_000  # Example Total Allowable Amount (TA)
        lrt_lpr_values = [kelp_lpr, 18.05, 10.0, 30.0]  # Replace with all available LPRs
        inv_lpr_sum = sum(1 / lpr for lpr in lrt_lpr_values if lpr > 0)

        kelp_dc = total_ta * ((1 / kelp_lpr) / inv_lpr_sum) if kelp_lpr > 0 else 0
        kelp_cr = 1 + (kelp_lpr / sum(lrt_lpr_values)) if kelp_lpr > 0 else 0

        # Display LIR, LPR, DC, and CR in a table
        kelp_summary_data = [
            {"Metric": "LIR", "Value": round(kelp_lir, 2)},
            {"Metric": "LPR", "Value": round(kelp_lpr, 2)},
            {"Metric": "Deposit Cap (DC)", "Value": f"${kelp_dc:,.2f}"},
            {"Metric": "Collateralization Ratio (CR)", "Value": f"{kelp_cr * 100:.2f}%"}
        ]
        kelp_summary_df = pd.DataFrame(kelp_summary_data)

        st.write("\n")
        st.markdown("**Kelp Summary Metrics**")
        st.dataframe(kelp_summary_df)

        with st.expander("Metrics Calc Method"):
            st.markdown("""
            **LIR** represents the aggregate risk score for the LRT (*t*), accounting only for individual, isolated AVS risks on its portfolio selection, weighted according to relative delegation by the LRT.

            **LPR** provides a comprehensive underwriting of the interdependent risk exposure of the pooled ecosystem of AVSs selected by the LRT.

            **DC** calculates the deposit cap by taking the total allowable amount for LRT deposits (*TA*), as determined by Ebisu, and adjusts it based on the relative risk of each LRT (*LPR*), in the context of Ebisu’s basket of LRTs (\(Σ LPR\)).

            **CR** relativizes the pooled risk of the LRT portfolio at hand (*LPR*), against the aggregate pooled risk of ALL the LRT portfolios (Ebisu’s LRT basket \(Σ LPR\)) to arrive at a considerate, minimum collateralization ratio for the LRT being considered.
            """)




else:
    st.write("No LRT balances data available to display.")




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


# Consolidate LRT Data
lrt_data = [
    {"Protocol": "Ether.fi", "LRT": "eETH", "LIR": etherfi_lir, "LPR": etherfi_lir},
    {"Protocol": "Renzo", "LRT": "ezETH", "LIR": renzo_lir, "LPR": renzo_lpr},
    {"Protocol": "Puffer", "LRT": "pufETH", "LIR": puffer_lir, "LPR": puffer_lir},
    {"Protocol": "Kelp", "LRT": "rsETH", "LIR": kelp_lir, "LPR": kelp_lir},
]

# Total Allowable Amount (TA)
total_ta = 100_000_000

# Calculate Deposit Cap (DC) and Minimum Collateralization Ratio (CR)
lrt_lpr_values = [data["LPR"] for data in lrt_data]
inv_lpr_sum = sum(1 / lpr for lpr in lrt_lpr_values if lpr > 0)

for data in lrt_data:
    lpr = data["LPR"]
    data["DC"] = total_ta * ((1 / lpr) / inv_lpr_sum) if lpr > 0 else 0
    data["CR"] = 1 + (lpr / sum(lrt_lpr_values)) if lpr > 0 else 0

# Convert to DataFrame
lrt_df = pd.DataFrame(lrt_data)

# Format Columns
lrt_df["DC"] = lrt_df["DC"].apply(lambda x: f"${x:,.2f}")
lrt_df["CR"] = lrt_df["CR"].apply(lambda x: f"{x:.2%}")



# --- Final Summary Table ---
st.header("Full LRT Deposit Cap & Minimum Collateral Ratio Breakdown")

# Collect data for the summary table
lrt_summary_data = [
    {
        "Protocol": "Ether.fi",
        "LRT": "eETH",
        "LIR": round(etherfi_lir, 4),  # Use dynamically calculated LIR
        "LPR": round(etherfi_lpr, 4),  # Use dynamically calculated LPR
        "Deposit Cap (DC)": f"${etherfi_dc:,.2f}",  # Use dynamically calculated DC
        "Min Collateralization Ratio (CR)": f"{etherfi_cr * 100:.2f}%"  # Use dynamically calculated CR
    },
    {
        "Protocol": "Renzo",
        "LRT": "ezETH",
        "LIR": round(renzo_lir, 4),  # Use dynamically calculated LIR
        "LPR": round(renzo_lpr, 4),  # Use dynamically calculated LPR
        "Deposit Cap (DC)": f"${renzo_dc:,.2f}",  # Use dynamically calculated DC
        "Min Collateralization Ratio (CR)": f"{renzo_cr * 100:.2f}%"  # Use dynamically calculated CR
    },
    {
        "Protocol": "Puffer",
        "LRT": "pufETH",
        "LIR": round(puffer_lir, 4),  # Use dynamically calculated LIR
        "LPR": round(puffer_lpr, 4),  # Use dynamically calculated LPR
        "Deposit Cap (DC)": f"${puffer_dc:,.2f}",  # Use dynamically calculated DC
        "Min Collateralization Ratio (CR)": f"{puffer_cr * 100:.2f}%"  # Use dynamically calculated CR
    },
    {
        "Protocol": "Kelp",
        "LRT": "rsETH",
        "LIR": round(kelp_lir, 4),  # Use dynamically calculated LIR
        "LPR": round(kelp_lpr, 4),  # Use dynamically calculated LPR
        "Deposit Cap (DC)": f"${kelp_dc:,.2f}",  # Use dynamically calculated DC
        "Min Collateralization Ratio (CR)": f"{kelp_cr * 100:.2f}%"  # Use dynamically calculated CR
    }
]

# Convert to DataFrame for rendering
lrt_summary_df = pd.DataFrame(lrt_summary_data)

# Identify the highest and lowest risk
highest_risk = max(lrt_summary_data, key=lambda x: x["LPR"])
lowest_risk = min(lrt_summary_data, key=lambda x: x["LPR"])

# Function to apply styles
def highlight_risk(row):
    if row["Protocol"] == highest_risk["Protocol"]:
        return ['background-color: orange'] * len(row)  # Riskiest
    elif row["Protocol"] == lowest_risk["Protocol"]:
        return ['background-color: lightgreen'] * len(row)  # Safest
    else:
        return [''] * len(row)

# Apply the style to the DataFrame
styled_lrt_summary_df = lrt_summary_df.style.apply(highlight_risk, axis=1)

# Display the styled DataFrame
st.dataframe(styled_lrt_summary_df, use_container_width=True)

# Generate Insights Dynamically
insights = []

insights.append(f"- **{highest_risk['Protocol']} ({highest_risk['LRT']})** is the riskiest LRT. "
                f"A relatively lower deposit cap and higher minimum collateralization ratio are "
                f"recommended to manage the increased risk and maintain the solvency of this collateral asset.")

insights.append(f"- **{lowest_risk['Protocol']} ({lowest_risk['LRT']})** is the least risky LRT. "
                f"A higher deposit cap and a more relaxed collateralization ratio are acceptable.")

moderate_risk_lrt = [lrt for lrt in lrt_summary_data if lrt != highest_risk and lrt != lowest_risk]
if moderate_risk_lrt:
    moderate_protocols = ", ".join([f"**{lrt['Protocol']} ({lrt['LRT']})**" for lrt in moderate_risk_lrt])
    insights.append(f"- {moderate_protocols} are moderately risky, in a relative sense, with a very similar risk profile.")

insights.append("- On top of the above insights, carefully considering financial market risks of each asset "
                "is important to gauge a full picture of what the final deposit caps and collateralization ratios should be.")

for insight in insights:
    st.write(insight)

