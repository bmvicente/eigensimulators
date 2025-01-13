

####### DONE # what does ebUSD interest rate change overall or incentivize? what about for the other tokens?
    ###### DONE # risk multiplier not working for LBTC
    ###### DONE # wrong probably: Effective Liquidation Threshold (USD)=Liquidation Threshold⋅(1−Token Utilization)
    ###### DONE # 🚨 Critical Utilization: 21.00% exceeds safe levels! --- appearing 21% all the time
    ###### DONE # not correct: "⚠️ High Minting Rate: ebUSD minting rate exceeds 30%, indicating potential over-minting risks." --- say 30% more than collateral
##### DONE # improve insights section
##### DONE # ask GPT about Liquity paper
##### DONE # even when DCR < 1, the message "🚨 Over-Leveraged: Debt exceeds collateral value. High risk of liquidation." shows up. whats going on?
##### DONE # check carefully how formulas are built
##### DONE # ebUSD formula is wrong
##### DONE # how's depegging probability calculated?
##### DONE # correct the positioning of the token sections
##### DONE # go through it formula by formula

# ASK THIS ONCE AGAIN ---- what constitutes debt, liquidation, collateral, liquidity--ask GPT for summary
# go through each per token
# check if variables are correct
# review Ethan message and what was asked

### need to figure out how much liquidity do we need relative to collateral deposited & 
### ebUSD minted (probs taking into consideration how much leverage is in the system too so we can proccess liquidations)









import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

def calculate_interest_rate(base_rate, utilization):
    return base_rate * utilization

def calculate_max_leverage_loop(mcr):
    return mcr / (mcr - 100)

def calculate_ebusd_minted(deposits, mcr_dec, ebusd_minting_rate_vs_mcr_dec):
    return deposits * (mcr_dec + ebusd_minting_rate_vs_mcr_dec)

def calculate_stablecoin_debt_ratio(stablecoin_debt, total_collateral):
    return stablecoin_debt / total_collateral

def simulate_price_var(collateral, price_var_dec):
    return collateral * (1 + price_var_dec / 100)


def simulate_leverage_loops(collateral_after_price_var, mcr_dec, iterations, token_utilization):
    debt = 0
    utilized_collateral = collateral_after_price_var * token_utilization  # Adjusted for utilization
    full_iterations = int(iterations)  # Integer part of iterations
    fractional_iteration = iterations - full_iterations  # Fractional part of iterations

    # Full iterations
    for _ in range(full_iterations):
        additional_debt = utilized_collateral / mcr_dec
        debt += additional_debt
        utilized_collateral += additional_debt  # Only the utilized portion is leveraged

    # Fractional iteration
    if fractional_iteration > 0:
        additional_debt = (utilized_collateral / mcr_dec) * fractional_iteration
        debt += additional_debt

    return debt


def calculate_liquidation_threshold(collateral_after_price_var, mcr_dec):
    return collateral_after_price_var * mcr_dec

def simulate_unwind(total_debt_after_leverage, mcr_dec, liquidation_threshold, liquidation_rate):
    """
    Calculate the amount of debt or collateral to be liquidated, adjusted by liquidation rate.
    Debt to Unwind should be positive only if total debt exceeds the liquidation threshold.
    """
    if total_debt_after_leverage > liquidation_threshold:
        # Calculate the amount of debt to repay
        debt_to_repay = total_debt_after_leverage - liquidation_threshold
        # Calculate the collateral to liquidate for the repayment
        collateral_to_liquidate = debt_to_repay / mcr_dec  # Adjusted by MCR to find equivalent collateral
        return {
            "debt_to_repay": float(max(0, debt_to_repay)),
            "collateral_to_liquidate": float(max(0, collateral_to_liquidate))
        }

    # No liquidation needed
    return {"debt_to_repay": 0, "collateral_to_liquidate": 0}



def calculate_slippage(total_minted, dex_liquidity):
    if dex_liquidity <= 0:
        # Handle zero or negative liquidity gracefully
        return 1  # Set maximum slippage to 100% (1.0 in decimal) or another threshold
    slippage = (total_minted - dex_liquidity) / dex_liquidity
    return max(0, slippage)  # Ensure non-negative slippage


def calculate_interest_rate(base_rate, utilization, risk_multiplier=1):
    """
    Dynamically calculates interest rates based on utilization and risk level.
    Includes a risk multiplier for high-risk tokens.

    :param base_rate: The base interest rate as a percentage (e.g., 10 for 10%).
    :param utilization: Utilization ratio as a decimal (e.g., 0.8 for 80%).
    :param risk_multiplier: Multiplier to adjust rates for high-risk tokens (default is 1).
    :return: The adjusted interest rate as a percentage.
    """
    return base_rate * utilization * risk_multiplier


def model_token_specific_interest_rates(token_data):
    """
    Models token-specific interest rates by adjusting for utilization and token-specific risks.

    :param tokens: A dictionary of token data, each containing utilization and risk level.
    :param base_rate: The system-wide base interest rate.
    :return: A dictionary of calculated interest rates per token.
    """
    interest_rates = {}
    for token, data in token_data.items():
        utilization = data.get("token_utilization", 0.0)
        base_rate = data.get("token_base_interest_rate", 10.0)
        risk_multiplier = data.get("token_risk_multiplier", 1.0)
        interest_rate = calculate_interest_rate(base_rate, utilization, risk_multiplier)
        interest_rates[token] = interest_rate
    return interest_rates

def model_system_interest_rate(base_rate, utilization, risk_multiplier=1.0):
    """
    Calculates a system-wide interest rate based on average utilization.

    :param base_rate: The base interest rate as a percentage (e.g., 10 for 10%).
    :param system_utilization: Average utilization ratio across all tokens as a decimal (e.g., 0.6 for 60%).
    :return: The system-wide interest rate as a percentage.
    """
    return base_rate * utilization * risk_multiplier



def calculate_depegging_risk(slippage, system_utilization, dex_liquidity, system_total_ebusd_minted):
    """
    Determines the probability of ebUSD depegging based on slippage, utilization, and liquidity metrics.

    :param slippage: The calculated slippage in the system as a decimal (e.g., 0.05 for 5%).
    :param system_utilization: The average utilization ratio across all tokens.
    :param dex_liquidity: The total DEX liquidity available for ebUSD pairs.
    :param system_total_ebusd_minted: The total amount of ebUSD minted in the system.
    :return: A tuple (depegging_probability, explanation).
    """
    if slippage > 2 or system_utilization > 90:
        return "High", (
            f"Slippage is significant ({slippage:.2f}%) and/or system utilization is very high "
            f"({system_utilization * 100:.2f}%), indicating a strong risk of ebUSD depegging."
        )
    elif slippage > 1 or system_utilization > 70:
        return "Medium", (
            f"Moderate slippage ({slippage:.2f}%) and/or system utilization ({system_utilization * 100:.2f}%) "
            "indicates a potential for ebUSD depegging under stress conditions."
        )
    elif dex_liquidity < system_total_ebusd_minted * 0.5:
        return "Medium", (
            f"DEX liquidity ({dex_liquidity:,.2f}) is less than 50% of the total ebUSD minted "
            f"({system_total_ebusd_minted:,.2f}), indicating potential stress on the peg."
        )
    else:
        return "Low", (
            f"Slippage is low ({slippage:.2f}%), system utilization is within safe bounds "
            f"({system_utilization * 100:.2f}%), and DEX liquidity is sufficient to cover ebUSD trades."
        )



def calculate_ebusd_debt(dex_liquidity, system_utilization, leverage):
    """
    Calculates the debt for ebUSD using leverage looping.

    :param dex_liquidity: Total liquidity in the DEX.
    :param system_utilization: System-wide utilization ratio.
    :param leverage: The leverage multiplier applied to ebUSD.
    :return: The total ebUSD debt.
    """
    debt = 0
    full_iterations = int(leverage)  # Integer part of leverage
    fractional_iteration = leverage - full_iterations  # Fractional part of leverage

    # Full leverage loops
    for _ in range(full_iterations):
        additional_debt = dex_liquidity * system_utilization  # Available liquidity per loop
        debt += additional_debt
        dex_liquidity += additional_debt

    # Fractional iteration
    if fractional_iteration > 0:
        additional_debt = (dex_liquidity * system_utilization) * fractional_iteration
        debt += additional_debt

    return debt


# Formula for Total System Debt
def calculate_total_system_debt(total_debt_after_leverage_list):
    """
    Calculate the total system debt by summing all token debts after leverage and ebUSD minted.
    
    :param total_debt_after_leverage_list: List of total debts after leverage for each token.
    :param total_ebusd_minted: Total ebUSD minted across the system.
    :return: Total system debt.
    """
    return sum(total_debt_after_leverage_list) 
        #+ total_ebusd_minted


# Formula for Debt-to-Collateral Ratio
def calculate_debt_to_collateral_ratio(total_system_debt, total_collateral_after_price_variation):
    """
    Calculate the debt-to-collateral ratio for the entire system.
    
    :param total_system_debt: Total system debt.
    :param total_collateral_after_price_variation: Total collateral after price variation across all tokens.
    :return: Debt-to-collateral ratio.
    """
    if total_collateral_after_price_variation > 0:
        return total_system_debt / total_collateral_after_price_variation
    else:
        return float('inf')  # Handle division by zero












# Default values for tokens
default_values = {
    "weETH": {"deposits": 5000000.0, "mcr": 120.0, "price_var": 0, "iterations": 1.5, "token_utilization": 0.5, "token_risk_multiplier": 2.0},
    "sUSDe": {"deposits": 10000000.0, "mcr": 110.0, "price_var": 0, "iterations": 1.5, "token_utilization": 0.5, "token_risk_multiplier": 1.0},
    "LBTC": {"deposits": 50000000.0, "mcr": 130.0, "price_var": 0, "iterations": 1.5, "token_utilization": 0.5, "token_risk_multiplier": 1.5},
}



def main():
    st.title("Ebisu Tokenomics: Parameterization & Simulation")
    st.write("\n")
    st.write("\n")

    # Create two main columns
    col_input, col_results = st.columns([1, 3], gap="large")

    # Input parameters for each token type
    with col_input:
        st.header("Input Parameters (IP)")
        token_data = {}

        for token, defaults in default_values.items():
            st.subheader(f"{token}")
            deposits = st.number_input(f"Deposits (USD)", min_value=0.0, value=defaults["deposits"], 
                                       step=10000000.0, key=f"{token}_deposits", help="The total USD value of collateral deposited for this token. Higher deposits improve the system's collateral base and stability.")
            mcr = st.number_input(f"MCR (%)", min_value=50.0, max_value=250.0, value=defaults["mcr"], step=10.0, key=f"{token}_mcr",
                                  help="The minimum ratio of collateral to debt required to avoid liquidation for a given token. A higher MCR ensures greater safety at the cost of lower capital efficiency.")
            leverage_iterations = st.number_input(f"Leverage (x)", min_value=0.0, value=defaults["iterations"], 
                                                  step=0.25, key=f"{token}_iterations", help="The maximum number of leverage loops achievable with the current MCR. Indicates the theoretical upper limit for leveraging.")
            col8, col9 = st.columns(2)
            with col8:
                token_base_interest_rate = st.slider(f"{token} Base Interest Rate (%)", min_value=0.0, max_value = 20.0, value=10.0, format="%d%%",
                                                    step=0.5, key=f"{token}_token_interest_rate", help="Base interest rate for borrowing.")
            with col9:
                token_risk_multiplier = st.number_input(f"{token} IR Risk Multiplier", min_value=0.0, max_value=10.0, value=defaults["token_risk_multiplier"], 
                                                    step=0.5, key=f"{token}_risk_multiplier", help="Adjusts the interest rate for this token based on its specific risk factors, such as infra and architecture specs, price volatility, and utilization.")
            price_var = st.slider(f"Collateral Price Variation (%)", min_value=-50, max_value=50, 
                format="%d%%", value=defaults["price_var"], key=f"{token}_price_var", help="The adjusted value of collateral after applying a simulated price variation. Useful for stress-testing the system against collateral price volatility.")
            
            ebusd_minting_rate_vs_mcr = st.slider(f"ebUSD Minting Rate Against MCR (%)", min_value=-100, max_value=100, format="%d%%", value=20, 
                                                  key=f"{token}_ebusd_minting_rate_vs_mcr", help="The percentage of ebUSD minted relative to the collateral. Reflects the efficiency of converting collateral into stablecoin liquidity.")

            token_util_ratio = st.slider(
                    "Token Utilization Ratio (%)",
                    min_value=0,
                    max_value=100,
                    value=50,
                    key=f"{token}_util_ratio",  # Unique key using token name
                    help="The percentage of total liquidity currently utilized by borrowed funds for this token. Higher utilization ratios indicate less available liquidity and increased borrowing activity."
                ) / 100



            token_data[token] = {
                "deposits": deposits,
                "mcr": mcr,
                "price_var": price_var,
                "iterations": leverage_iterations,
                "token_utilization": token_util_ratio,
                "ebusd_minting_rate_vs_mcr": ebusd_minting_rate_vs_mcr,
                "token_risk_multiplier": token_risk_multiplier,
                "token_base_interest_rate": token_base_interest_rate
            }


            if token == "weETH":
                num_spaces = 30
            elif token == "sUSDe":
                num_spaces = 18
            elif token == "LBTC":
                num_spaces = 22
            else:
                num_spaces = 10  # Default number of spaces

            for _ in range(num_spaces):
                st.write("\n")





        # System-wide parameters
        st.subheader("System-Wide Parameters")
        dex_liquidity = st.number_input("DEX Liquidity (USD)", min_value=0.0, value=200_000_000.0, step=25_000_000.0, help="Total liquidity available for all ebUSD pairs. This is a critical measure of the system's ability to handle ebUSD trading and support minting without excessive slippage.")

        liquidation_rate = st.slider(
                "ebUSD Liquidation Rate (%)",
                min_value=0,
                max_value=100,
                value=50,  # Default to 50%
                step=5,
                help="Percentage of debt or collateral liquidated when liquidation thresholds are breached for ebUSD. Factored into Bad Debt calculations."
            ) / 100  # Convert to decimal
        
        col10,col11 = st.columns(2)
        with col10:
            system_base_interest_rate = st.slider(
                "ebUSD Base Interest Rate (%)",
                min_value=0.0,
                max_value=20.0,
                step=0.5,
                value=10.0,
                format="%d%%",  
                help="Baseline borrowing rate for ebUSD.")
        with col11:
            system_risk_multiplier = st.number_input(
                    f"ebUSD IR Risk Multiplier", 
                    min_value=0.0, 
                    max_value=10.0, 
                    value=1.0,  # Change to float
                    step=0.5, 
                    key=f"system_risk_multiplier", 
                    help="Affects the ebUSD interest rate to account for aggregate risk, including collateral health, overall liquidity, and utilization."
                )


    system_total_collateral = 0
    system_total_ebusd_minted = 0
    system_total_debt = 0
    weighted_mcr_sum = 0
    weighted_collateral = 0
    system_utilization = 0
    total_token_utilization = 0
    total_mcr = 0
    system_total_debt_to_unwind = 0
    token_interest_rates = model_token_specific_interest_rates(token_data)
    system_interest_rate = model_system_interest_rate(
        system_base_interest_rate, system_utilization, system_risk_multiplier
    )



    results = {}

    for token, data in token_data.items():
        deposits = data["deposits"]
        mcr = data["mcr"]
        mcr_dec = mcr / 100  # Convert MCR to decimal form
        price_var = data["price_var"]
        price_var_dec = price_var/100
        iterations = data["iterations"]
        token_utilization = data["token_utilization"]
        ebusd_minting_rate_vs_mcr = data["ebusd_minting_rate_vs_mcr"]
        ebusd_minting_rate_vs_mcr_dec = ebusd_minting_rate_vs_mcr / 100
        ebusd_minting_rate = mcr + ebusd_minting_rate_vs_mcr

        max_leverage_loop = calculate_max_leverage_loop(mcr)
        ebusd_minted = calculate_ebusd_minted(deposits, mcr_dec, ebusd_minting_rate_vs_mcr_dec)
        collateral_after_price_var = simulate_price_var(deposits, price_var_dec)
        total_debt_after_leverage = simulate_leverage_loops(collateral_after_price_var, mcr_dec, iterations, token_utilization)
        liquidation_threshold = calculate_liquidation_threshold(total_debt_after_leverage, mcr_dec)
        debt_to_unwind = simulate_unwind(
            total_debt_after_leverage=total_debt_after_leverage,
            mcr_dec=mcr_dec,
            #collateral_after_price_var=collateral_after_price_var,
            liquidation_threshold=liquidation_threshold,
            liquidation_rate=liquidation_rate
        )

        debt_to_repay = debt_to_unwind["debt_to_repay"]
        collateral_to_liquidate = debt_to_unwind["collateral_to_liquidate"]

        debt_to_collateral_ratio = total_debt_after_leverage / collateral_after_price_var if collateral_after_price_var > 0 else float('inf')
        
        collateral_coverage_ratio = collateral_after_price_var / total_debt_after_leverage if total_debt_after_leverage > 0 else 0
        #system_collateral_coverage_ratio = total_collateral_after_price_variation / system_total_debt if system_total_debt > 0 else 0

        system_liquidity_to_debt_ratio = dex_liquidity / (system_total_debt or 1)  # Avoid division by zero
        liquidity_buffer = dex_liquidity * (1 - system_utilization)
        total_token_utilization += token_utilization

        total_mcr += mcr
        system_mcr = total_mcr / len(token_data)

        # Aggregate calculations for system-wide metrics
        system_total_collateral += deposits
        system_total_ebusd_minted += ebusd_minted
        weighted_mcr_sum += mcr * collateral_after_price_var
        weighted_collateral += collateral_after_price_var
        system_utilization = total_token_utilization / len(token_data)
        system_collateral_value_after_liquidation = system_total_collateral * (1 - liquidation_rate)



        # Calculate system-wide interest rate
        system_interest_rate = model_system_interest_rate(
                    system_base_interest_rate, 
                    system_utilization, 
                    system_risk_multiplier)

        # Calculate token-specific interest rates
        token_interest_rates = model_token_specific_interest_rates(token_data)

        slippage = calculate_slippage(system_total_ebusd_minted, dex_liquidity)

        # Example usage in the system-wide results
        depegging_probability, explanation = calculate_depegging_risk(
            slippage=slippage,
            system_utilization=system_utilization,
            dex_liquidity=dex_liquidity,
            system_total_ebusd_minted=system_total_ebusd_minted)

        # Store token-specific results
        results[token] = {
            "Warnings": [],
            "Deposits (USD)": deposits,
            "MCR (%)": mcr,
            "MCR Dec": mcr_dec,
            "Max Leverage Loops (x)": max_leverage_loop,
            "ebUSD Minted (USD)": ebusd_minted,
            "ebUSD Minting Rate Against MCR (%)": ebusd_minting_rate_vs_mcr,
            "ebUSD Minting Rate (%)": ebusd_minting_rate,
            "Collateral Price Variation (%)": price_var,
            "Collateral Price Variation Dec": price_var_dec,
            "Collateral Value After Price Variation (USD)": collateral_after_price_var,
            "Liquidation Threshold (USD)": liquidation_threshold,
            "Debt to Unwind (USD)": debt_to_unwind,
            "Total Debt After Leverage (USD)": total_debt_after_leverage,
            "Leverage (x))": iterations,
            "Debt-to-Collateral Ratio": debt_to_collateral_ratio,
            "Collateral Coverage Ratio": collateral_coverage_ratio,
            "Liquidity Buffer (USD)": liquidity_buffer,
            "token_utilization": token_utilization,
            "token_base_interest_rate": token_data[token]["token_base_interest_rate"],
            "token_interest_rates": token_interest_rates[token],  # Include calculated interest rates here
            "token_risk_multiplier": token_data[token]["token_risk_multiplier"],
            "Debt to Repay (USD)": debt_to_repay,
            "Collateral to Liquidate (USD)": collateral_to_liquidate
        }

    results[token]["Liquidation Rate (%)"] = liquidation_rate * 100
    results[token]["Collateral to Liquidate (USD)"] = debt_to_unwind["collateral_to_liquidate"]
    #results[token]["Debt to Unwind (USD)"] = debt_to_unwind
    #results[token]["Debt to Repay (USD)"] = debt_to_repay


    # Corrected Implementation of Total Debt After Leverage Calculation
    total_debt_after_leverage_list = [
        simulate_leverage_loops(
            results[token]["Collateral Value After Price Variation (USD)"],
            results[token]["MCR Dec"],
            results[token]["Leverage (x))"],
            results[token]["token_utilization"]
        )
        for token in results
    ]

    total_debt_after_leverage_list = [results[token]["Total Debt After Leverage (USD)"] for token in results]
    
    total_collateral_after_price_variation = sum(
        results[token]["Collateral Value After Price Variation (USD)"] for token in results
    )

    # Calculate Total System Debt
    system_total_debt = calculate_total_system_debt(total_debt_after_leverage_list)

    # Calculate Debt-to-Collateral Ratio
    system_debt_to_collateral_ratio = calculate_debt_to_collateral_ratio(system_total_debt, total_collateral_after_price_variation)


    # System-wide metrics
    system_leverage = system_total_ebusd_minted / system_total_collateral
    system_liquidity_to_debt_ratio = dex_liquidity / system_total_debt
    system_interest_rate = calculate_interest_rate(system_base_interest_rate, system_utilization, system_risk_multiplier)
    system_total_debt_to_unwind += debt_to_unwind["debt_to_repay"]
    system_bad_debt = max(0, system_total_debt_to_unwind - system_collateral_value_after_liquidation)

    average_utilization = sum(data["token_utilization"] for data in token_data.values()) / len(token_data)
    liquidity_buffer = dex_liquidity * (1 - system_utilization)

    # Valuable Ratios
    system_collateral_coverage_ratio = total_collateral_after_price_variation / system_total_debt if system_total_debt > 0 else 0

    # Display results in the right column
    with col_results:
        st.header("Results")
        for token, token_results in results.items():
            for warning in token_results.get("Warnings", []):
                st.warning(warning)

            st.subheader(f"{token} Metrics")

            cols = st.columns(5)

            # Deposits
            cols[0].metric(
                "**IP**: Deposits (USD)",
                f"{token_results['Deposits (USD)']:,.2f}",
                help="The total USD value of collateral deposited for this token. Higher deposits improve the system's collateral base and stability.")

            # MCR
            cols[1].metric(
                "**IP**: MCR (%)",
                f"{token_results['MCR (%)']:.2f}%",
                help="The minimum ratio of collateral to debt required to avoid liquidation for a given token. A higher MCR ensures greater safety at the cost of lower capital efficiency.")

            # Max Leverage Loops
            cols[2].metric(
                "**IP**: Max Leverage Loops (x)",
                f"{token_results['Max Leverage Loops (x)']:.2f}x",
                help="The maximum number of leverage loops achievable with the current MCR. Indicates the theoretical upper limit for leveraging.")

            # ebUSD Minting Rate
            cols[3].metric(
                "**IP**: ebUSD Minting Rate (%)",
                f"{token_results['ebUSD Minting Rate (%)']:.2f}%",
                help="The percentage of ebUSD minted relative to the collateral. Reflects the efficiency of converting collateral into stablecoin liquidity.")

            cols[4].metric(
                f"**IP**: {token} Base Interest Rate (%)",
                f"{results[token]['token_base_interest_rate']:.2f}%",
                help="The base interest rate for this token.")


            cols = st.columns(4)

            # Collateral Value After Price Variation
            cols[0].metric(
                "Collateral Value After Price Variation (USD)",
                f"{token_results['Collateral Value After Price Variation (USD)']:,.2f}",
                help="The adjusted value of collateral after applying a simulated price variation. Useful for stress-testing the system against collateral price volatility.")

            # ebUSD Minted
            cols[1].metric(
                "ebUSD Minted (USD)",
                f"{token_results['ebUSD Minted (USD)']:,.2f}",
                help="The total amount of ebUSD stablecoin minted using the deposited collateral. A measure of the system’s capital efficiency.")
            
            cols[2].metric(
                f"{token} Interest Rate (%)",  # Replace placeholder with the token name
                f"{token_interest_rates[token]:.2f}%",
                help=f"The borrowing interest rate for {token}, adjusted for utilization and token-specific risk factors. Higher rates discourage excessive borrowing and compensate for increased risks.")

            # Liquidation Threshold
            cols[3].metric(
                "Liquidation Threshold (USD)",
                f"{token_results['Liquidation Threshold (USD)']:,.2f}",
                help="The total debt value below which liquidation is triggered. Higher thresholds indicate stricter collateral requirements.")

            

            cols = st.columns(4)

            # Total Debt After Leverage
            cols[0].metric(
                "Total Debt After Leverage (USD)",
                f"{token_results['Total Debt After Leverage (USD)']:,.2f}",
                help="The cumulative debt incurred through iterative leveraging for this token. A higher value indicates greater exposure to liquidation risk.")

            cols[1].metric(
                "Debt to Unwind (USD)",
                f"{results[token]['Debt to Unwind (USD)']['debt_to_repay']:,.2f}",
                help="The amount of debt that must be repaid to restore the position above the liquidation threshold. Critical for managing risk during stress events.")

            cols[2].metric(
                "Debt-to-Collateral Ratio", 
                f"{token_results['Debt-to-Collateral Ratio']:.2f}", 
                help="This metric represents the ratio of total debt to the collateral value after price variation. A higher ratio indicates higher leverage and risk.")


            cols[3].metric(
                "Collateral Coverage Ratio",
                f"{token_results['Collateral Coverage Ratio']:.2f}",
                help="The ratio of total collateral after price variation to total system debt. Values below 1 signal under-collateralization risks, while values above 1 indicate sufficient collateral coverage.")

            


            cols_warnings = st.columns(2)

            # Token Utilization
            if token_results["token_utilization"] >= 0.9:
                cols_warnings[1].error(
                    f"🚨 **Critical Utilization**: {token_results['token_utilization'] * 100:.2f}% utilization exceeds safe levels, leaving minimal liquidity buffer and increasing systemic strain."
                )
            elif 0.9 > token_results["token_utilization"] > 0.7:
                cols_warnings[1].warning(
                    f"⚠️ **High Utilization**: {token_results['token_utilization'] * 100:.2f}% utilization reduces available liquidity and increases systemic stress."
                )
            else:
                cols_warnings[1].success(
                    f"✅ **Safe Utilization Level**: {token} utilization is at {token_results['token_utilization'] * 100:.2f}%, well within safe bounds, leaving ample liquidity buffer."
                )

            # ebUSD Minting Rate Against MCR
            if 50 >= token_results["ebUSD Minting Rate Against MCR (%)"] >= 25:
                cols_warnings[0].warning(
                    f"⚠️ **High Minting Rate**: ebUSD minting rate is {token_results['ebUSD Minting Rate Against MCR (%)']}% against MCR, increasing risks of over-minting and liquidity strain."
                )
            elif token_results["ebUSD Minting Rate Against MCR (%)"] > 50:
                cols_warnings[0].error(
                    f"🚨 **Critical Minting Rate**: ebUSD minting rate is {token_results['ebUSD Minting Rate Against MCR (%)']}% against MCR, posing severe risks of collateral insufficiency and system instability."
                )
            else:
                cols_warnings[0].success(
                    f"✅ **Safe ebUSD Minting Rate**: Minting rate is {token_results['ebUSD Minting Rate Against MCR (%)']}% against MCR, well below critical levels, ensuring sufficient collateral backing."
                )



            cols_warnings = st.columns(2)

            # Interest Rates
            interest_rate = results[token]["token_interest_rates"]
            if interest_rate < 2.5:
                cols_warnings[0].warning(
                    f"⚠️ **Low Interest Rate for {token}**: {interest_rate:.2f}% is below the safe threshold of 2.50%, potentially incentivizing excessive borrowing and increasing systemic risk."
                )
            elif 2.5 <= interest_rate <= 15:
                cols_warnings[0].success(
                    f"✅ **Safe Interest Level**: Interest rate for {token} is {interest_rate:.2f}%, within the optimal range of 2.5% to 15.0%, balancing borrowing costs and systemic stability."
                )
            else:
                cols_warnings[0].error(
                    f"🚨 **High Interest Rate for {token}**: {interest_rate:.2f}% exceeds the critical threshold of 15.00%, which may discourage borrowing and reduce system liquidity."
                )


            # Check liquidation threshold relative to total debt
            threshold_margin = token_results["Total Debt After Leverage (USD)"] * 1.05  # 5% buffer above total debt

            if token_results["Liquidation Threshold (USD)"] < token_results["Total Debt After Leverage (USD)"]:
                # Liquidation threshold is below total debt
                cols_warnings[1].error(
                    f"🚨 **Critical Liquidation Risk**: Liquidation threshold (\${token_results['Liquidation Threshold (USD)']:,.2f}) "
                    f"is below total debt (\${token_results['Total Debt After Leverage (USD)']:,.2f}), indicating severe under-collateralization and high risk of liquidation."
                )
            elif token_results["Total Debt After Leverage (USD)"] <= token_results["Liquidation Threshold (USD)"] < threshold_margin:
                # Liquidation threshold is close to total debt (within 5%)
                cols_warnings[1].warning(
                    f"⚠️ **Moderate Liquidation Risk**: Liquidation threshold (\${token_results['Liquidation Threshold (USD)']:,.2f}) "
                    f"is within 5% of total debt (\${token_results['Total Debt After Leverage (USD)']:,.2f}), indicating potential under-collateralization risk."
                )
            elif token_results["Liquidation Threshold (USD)"] >= threshold_margin:
                # Liquidation threshold significantly exceeds total debt
                cols_warnings[1].success(
                    f"✅ **Low Liquidation Risk**: Liquidation threshold (\${token_results['Liquidation Threshold (USD)']:,.2f}) "
                    f"significantly exceeds total debt (\${token_results['Total Debt After Leverage (USD)']:,.2f}), providing strong collateral protection."
                )




            cols_warnings = st.columns(2)

            # Debt-to-Collateral Ratio
            if token_results["Debt-to-Collateral Ratio"] > 2:
                cols_warnings[0].error(
                    f"🚨 **Critical Debt-to-Collateral Level**: Debt exceeds collateral by {token_results['Debt-to-Collateral Ratio']:.2f}x, significantly increasing liquidation risk and systemic instability."
                )
            elif 2 >= token_results["Debt-to-Collateral Ratio"] > 1:
                cols_warnings[0].warning(
                    f"⚠️ **Moderate Debt-to-Collateral Level**: Debt exceeds collateral by {token_results['Debt-to-Collateral Ratio']:.2f}x, posing a moderate liquidation risk that requires monitoring."
                )
            else:
                cols_warnings[0].success(
                    f"✅ **Safe Debt-to-Collateral Level**: Debt is well-covered by collateral, with a ratio of {token_results['Debt-to-Collateral Ratio']:.2f}x, indicating stable leverage and minimal liquidation risk."
                )


            # Collateral Coverage Ratio
            if token_results['Collateral Coverage Ratio'] < 0.5:
                cols_warnings[1].error(
                    f"🚨 **Insufficient Collateral Coverage for {token}**: Coverage ratio is {token_results['Collateral Coverage Ratio']:.2f}, indicating under-collateralization and elevated liquidation risks."
                )
            elif 0.5 <= token_results['Collateral Coverage Ratio'] <= 1.5:
                cols_warnings[1].warning(
                    f"⚠️ **Low Collateral Coverage for {token}**: Coverage ratio is {token_results['Collateral Coverage Ratio']:.2f}, providing limited protection against price volatility and liquidation risks."
                )
            else:
                cols_warnings[1].success(
                    f"✅ **Strong Collateral Coverage for {token}**: Coverage ratio is {token_results['Collateral Coverage Ratio']:.2f}, indicating a robust buffer against liquidation risks."
                )







            st.write("\n")


            # EXPANDER
            with st.expander(f"Detailed Formulas and Calculations for {token}"):
                st.write(f"**Max Leverage Loops Formula:**")
                st.latex(r"""
                \text{Max Leverage Loops (x)} = \frac{\text{MCR (\%)}}{\text{MCR (\%)} - 100}
                """)
                st.write(f"Result: {token_results['MCR (%)']:.2f} / ({token_results['MCR (%)']:.2f} - 100) = {token_results['Max Leverage Loops (x)']:.2f}")

                st.write(f"**Collateral Value After Price Variation Formula:**")
                st.latex(r"""
                \text{Collateral Value After Price Variation (USD)} = \text{Deposits (USD)} \cdot \left(1 + \frac{\text{Price Variation (\%)}}{100}\right)
                """)
                st.write(f"Result: {token_results['Deposits (USD)']:,.2f} * (1 + {token_results['Collateral Price Variation Dec']:.2f}) = {token_results['Collateral Value After Price Variation (USD)']:,.2f}")

                st.write(f"**ebUSD Minted Formula:**")
                st.latex(r"""
                \text{ebUSD Minted (USD)} = \text{Deposits (USD)} \cdot \left(\frac{\text{MCR} + \text{ebUSD Minting Rate}}{100}\right)
                """)
                st.write(f"Result: {token_results['Deposits (USD)']:,.2f} * ({token_results['MCR Dec']:.2f} + {token_results['ebUSD Minting Rate Against MCR (%)'] / 100:.2f}) = {token_results['ebUSD Minted (USD)']:,.2f}")

                st.write(f"**Interest Rate Formula:**")
                st.latex(r"""
                \text{Interest Rate (\%)} = \text{Base Interest Rate (\%)} \cdot \text{Token Utilization} \cdot \text{Risk Multiplier}
                """)
                st.write(f"Result: {token_results['token_base_interest_rate']:.2f} * {token_results['token_utilization']:.2f} * {token_results['token_risk_multiplier']:.2f} = {token_interest_rates[token]:.2f}%")

                st.write(f"**Liquidation Threshold Formula:**")
                st.latex(r"""
                \text{Liquidation Threshold (USD)} = \text{Total Debt After Leverage (USD)} \cdot \text{MCR}
                """)
                st.write(f"Result: {token_results['Total Debt After Leverage (USD)']:,.2f} * {token_results['MCR Dec']:.2f} = {token_results['Liquidation Threshold (USD)']:,.2f}")

                st.write(f"**Total Debt After Leverage Formula:**")
                st.latex(r"""
                \text{Total Debt After Leverage (USD)} = \text{Iterative Summation} \left(\frac{\text{Collateral Value After Price Variation (USD)}}{\text{MCR Dec}}\right)
                """)
                st.write(f"Result: Simulated over {token_results['Leverage (x))']:.1f} leverage loops, resulting in total debt of {token_results['Total Debt After Leverage (USD)']:,.2f}")

                st.write(f"**Debt to Unwind Formula:**")
                st.latex(r"""
                \text{Debt to Unwind (USD)} = 
                \begin{cases} 
                \text{Total Debt After Leverage} - \text{Liquidation Threshold}, & \text{if Total Debt After Leverage > Liquidation Threshold} \\ 
                0, & \text{otherwise}
                \end{cases}
                """)
                st.write(f"Result: max(0, {token_results['Total Debt After Leverage (USD)']:,.2f} - {token_results['Liquidation Threshold (USD)']:,.2f}) = {token_results['Debt to Unwind (USD)'].get('debt_to_repay', 0):,.2f}")

                st.write(f"**Debt-to-Collateral Ratio Formula:**")
                st.latex(r"""
                \text{Debt-to-Collateral Ratio} = \frac{\text{Total Debt After Leverage (USD)}}{\text{Collateral Value After Price Variation (USD)}}
                """)
                st.write(f"Result: {token_results['Total Debt After Leverage (USD)']:,.2f} / {token_results['Collateral Value After Price Variation (USD)']:,.2f} = {token_results['Debt-to-Collateral Ratio']:.2f}")

                st.write(f"**Collateral Coverage Ratio Formula:**")
                st.latex(r"""
                \text{Collateral Coverage Ratio} = \frac{\text{Collateral Value After Price Variation (USD)}}{\text{Total Debt After Leverage (USD)}}
                """)
                st.write(f"Result: {token_results['Collateral Value After Price Variation (USD)']:,.2f} / {token_results['Total Debt After Leverage (USD)']:,.2f} = {token_results['Collateral Coverage Ratio']:.2f}")



            with st.expander(f"**Insights for {token}**"):
                st.subheader(f"**Insights for {token}**")

                st.write(f"""
                #### **Collateralization and Stability**
                - The Minimum Collateralization Ratio (MCR) for {token} is **{mcr:.2f}%**, acting as a critical safeguard against liquidation risks.
                - Total deposits: **{deposits:,.2f} USD**, with collateral value after price variation at **{collateral_after_price_var:,.2f} USD**.
                - System remains robust, but excessively high MCR values can reduce capital efficiency.

                #### **Leverage and Minting Dynamics**
                - Max Leverage Loop: **{max_leverage_loop:.2f}x**, balancing efficiency with risk.
                - Total ebUSD Minted: **{ebusd_minted:,.2f} USD**.
                - Total Debt After Leverage: **{total_debt_after_leverage:,.2f} USD** highlights exposure requiring monitoring.

                #### **Risk Assessment**
                - **Debt-to-Collateral Ratio:** {debt_to_collateral_ratio:.2f}. Values above 1.5 signal elevated liquidation risks.
                - **Collateral Coverage Ratio:** {collateral_coverage_ratio:.2f}. Values below 1 indicate under-collateralization.
                - **Utilization:** {token_utilization * 100:.2f}%. Levels above 80% pose liquidity strain.

                #### **Liquidation**
                - Debt to Unwind: **{debt_to_unwind["debt_to_repay"]:,.2f} USD**.
                - Liquidation Threshold: **{liquidation_threshold:,.2f} USD**, signaling collateral adequacy to avoid forced liquidations.

                #### **Recommendations for {token}**
                - Maintain collateral above the MCR to buffer against price fluctuations.
                - Monitor leverage and reduce exposure in volatile markets.
                - Keep Debt-to-Collateral Ratio below 1.5 and Coverage Ratio above 1.0.
                - Limit utilization below 80% to preserve liquidity.
                - Regularly rebalance positions to align with market dynamics.
                """)







            if token == "weETH":
                st.write("---")
                st.write("**Additional Ether.fi LRT (weETH) Metrics, based on Current AVS Portfolio Risk Assessment** ([model](https://ebisu-lrt-risk-dashboard.streamlit.app/)): ***Riskiest LRT***")
                
                # Add custom metrics for "weETH"
                cols = st.columns(2)
                cols[0].metric("Deposit Cap USD Share Relative to Other LRTs *(Total Pool = $100M)*", "$4.5M (Lowest Allowed)")
                cols[1].metric("MCR Relative to Other LRTs", "165% (Highest)") 



            if token == "weETH":
                num_spaces = 14
            elif token == "sUSDe":
                num_spaces = 15
            elif token == "LBTC":
                num_spaces = 13
            else:
                num_spaces = 10  # Default number of spaces

            for _ in range(num_spaces):
                st.write("\n")
            


        st.write("\n") 
        st.write("\n")
        st.write("\n") 
        st.write("\n") 
        









        with col_results:
            st.header("System-Wide Results")
            
        cols = st.columns(3)
        cols[0].metric(
            "**IP**: DEX Liquidity (USD)",
            f"{dex_liquidity:,.2f}",
            help="The total USD liquidity available in the DEX for ebUSD trading pairs. High liquidity ensures efficient trades and supports system stability during liquidations.")

        cols[1].metric(
                "**IP**: Liquidation Rate (%)",
                f"{liquidation_rate * 100:.2f}%",
                help="The percentage of debt or collateral liquidated during system-wide liquidation events. Determines how aggressively the system handles liquidation risks. Factored into Bad Debt calculations.")
        
        cols[2].metric(
            "**IP**: ebUSD Base Interest Rate (%)",
            f"{system_base_interest_rate:.2f}%",
            help="The borrowing interest rate dynamically adjusted for system-wide utilization. Higher rates reflect constrained liquidity and increase the cost of borrowing.")


        cols = st.columns(4)
        cols[0].metric(
            "Total Collateral (USD)",
            f"{system_total_collateral:,.2f}",
            help="The total value of collateral deposited across all tokens in the system. Serves as the security backing all minted ebUSD.")

        cols[1].metric(
            "Total ebUSD Minted (USD)",
            f"{system_total_ebusd_minted:,.2f}",
            help="The total amount of ebUSD stablecoin minted in the system. Reflects the system's capacity to create liquidity based on collateral.")

        cols[2].metric(
            "Average System-Wide MCR (%)",
            f"{system_mcr:.2f}%",
            help="The weighted average Minimum Collateralization Ratio (MCR) across all tokens in the system. Higher values indicate more conservative and secure collateral requirements.")

        cols[3].metric(
            "Average Token Utilization (%)",
            f"{average_utilization * 100:.2f}%",
            help="The average utilization ratio across all tokens. High utilization indicates constrained liquidity, increasing risks of slippage and stress.")
        


        cols = st.columns(4)
        cols[0].metric(
            "ebUSD Leverage (x)",
            f"{system_leverage:.2f}x",
            help="The ratio of total ebUSD minted to total collateral. Indicates the system’s overall exposure to leverage.")

        cols[1].metric(
            "Liquidity Buffer (USD)",
            f"{liquidity_buffer:,.2f}",
            help="The remaining liquidity in the DEX after accounting for current utilization. Provides a measure of how much liquidity is available to absorb shocks.")

        cols[2].metric(
                "Liquidity Stress Indicator",
                "High" if system_utilization > 0.9 else "Medium" if system_utilization > 0.7 else "Low",
                help="Categorizes liquidity stress based on system utilization. High stress (utilization > 80%) suggests immediate intervention is needed, while low stress (< 50%) indicates sufficient liquidity.")

        cols[3].metric(
                "ebUSD Interest Rate (%)",
                f"{system_interest_rate:,.2f}%",
                help="The effective borrowing interest rate adjusted for system-wide utilization. Reflects the cost of borrowing across the system.")


        cols = st.columns(4)

        cols[0].metric(
            "ebUSD Slippage (%)",
            f"{slippage:.2f}%",
            help="The percentage price impact caused by ebUSD trading or minting relative to DEX liquidity. High slippage indicates liquidity stress.")
        
        cols[1].metric(
                "Total Debt-to-Collateral Ratio",
                f"{system_debt_to_collateral_ratio:,.2f}",
                help="The total debt across all tokens in the system that must be unwound to restore positions above liquidation thresholds. Includes ebUSD and token-specific debt, providing an aggregate view of the system's debt at risk of liquidation.")

        cols[2].metric(
            "System-Wide Collateral Coverage Ratio",
            f"{system_collateral_coverage_ratio:.2f}",
            help="The ratio of total collateral after price variation to total system debt. Values below 1 signal under-collateralization risks, while values above 1 indicate sufficient collateral coverage.")

        cols[3].metric(
            "Total Liquidity-to-Debt Ratio",
            f"{system_liquidity_to_debt_ratio:.2f}",
            help="The ratio of DEX liquidity to total ebUSD minted. A higher ratio implies better liquidity to cover potential redemptions and liquidations.")



        cols = st.columns(4)

        cols[0].metric(
                "Total System Collateral Debt (USD)",
                f"{system_total_debt:,.2f}",
                help=(
                    "The aggregate debt across the system, including leveraged debt from weETH, sUSDe, and LBTC. "
                    "ebUSD minted is excluded as debt in the calculations, as it is presumed to be backed by over-collateralization and managed independently of liquidation thresholds, "
                    "though this interpretation lacks clear confirmation. "
                    "Higher values indicate greater exposure to leverage and systemic risk, requiring robust collateralization."
                ))

        cols[1].metric(
                "Total System Debt to Unwind (USD)",
                f"{system_total_debt_to_unwind:,.2f}",
                help=(
                    "The total leveraged debt across all tokens in the system that must be unwound to restore positions above liquidation thresholds. "
                    "ebUSD is excluded as debt from this calculation, due to the lack of clarity and ambiguity of interpretations regarding whether it is separately managed through over-collateralization."
                ))
    
        cols[2].metric(
            "System-Wide Bad Debt (USD)",
            f"{system_bad_debt:,.2f}",
            help="The aggregate unrecoverable debt across all tokens in the system. Reflects systemic collateral insufficiency.")
        
        cols[3].metric(
                "ebUSD Depegging Probability",
                f"{depegging_probability}",
                help="An indicator of the likelihood of ebUSD losing its peg under current conditions. Determined by metrics like slippage, utilization, and liquidity.")







        cols_warnings = st.columns(2)

        # Utilization
        if system_utilization >= 0.9:
            cols_warnings[0].error(
                f"🚨 **Critical Utilization Level**: Averafe utilization is at {system_utilization * 100:.2f}%, exceeding 90%, leaving almost no buffer for further borrowing."
            )
        elif 0.9 > system_utilization > 0.7:
            cols_warnings[0].warning(
                f"⚠️ **Moderate Utilization Level**: Average utilization is at {system_utilization * 100:.2f}%, between 70% and 90%, indicating reduced liquidity availability."
            )
        else:
            cols_warnings[0].success(
                f"✅ **Healthy Utilization Level**: Average utilization is at {system_utilization * 100:.2f}%, well below 70%, ensuring sufficient liquidity buffers."
            )

        # System Leverage
        if system_leverage > 3:
            cols_warnings[1].error(
                f"🚨 **Excessive System Leverage**: Leverage is {system_leverage:.2f}x, exceeding the critical threshold of 3x, exposing the system to unsustainable risks."
            )
        elif 3 >= system_leverage > 2:
            cols_warnings[1].warning(
                f"⚠️ **Moderate System Leverage**: Leverage is {system_leverage:.2f}x, between 2x and 3x, requiring closer monitoring."
            )
        else:
            cols_warnings[1].success(
                f"✅ **Healthy System Leverage**: Leverage is {system_leverage:.2f}x, well below 2x, indicating controlled risk exposure."
            )


        cols_warnings = st.columns(2)

        # Slippage
        if slippage > 5:
            cols_warnings[0].error(
                f"🚨 **Severe Slippage**: Slippage is {slippage:.2f}%, exceeding the critical threshold of 5%, potentially destabilizing the system."
            )
        elif 5 >= slippage > 3:
            cols_warnings[0].warning(
                f"⚠️ **Moderate Slippage**: Slippage is {slippage:.2f}%, above the safe range of 3%, indicating growing price impact."
            )
        else:
            cols_warnings[0].success(
                f"✅ **Minimal Slippage**: Slippage is {slippage:.2f}%, well within acceptable limits, ensuring efficient trading."
            )

        # Liquidity Buffer
        if liquidity_buffer < system_total_debt * 0.2:
            cols_warnings[1].error(
                f"🚨 **Insufficient Liquidity Buffer**: Liquidity buffer is \${liquidity_buffer:,.2f}, below 20% of total system debt (\${system_total_debt * 0.2:,.2f})."
            )
        elif system_total_debt * 0.2 <= liquidity_buffer < system_total_debt * 0.4:
            cols_warnings[1].warning(
                f"⚠️ **Moderate Liquidity Buffer**: Liquidity buffer is \${liquidity_buffer:,.2f}, between 20% and 40% of total system debt (\${system_total_debt * 0.4:,.2f})."
            )
        else:
            cols_warnings[1].success(
                f"✅ **Strong Liquidity Buffer**: Liquidity buffer is \${liquidity_buffer:,.2f}, exceeding 40% of total system debt (\${system_total_debt:,.2f})."
            )


        cols_warnings = st.columns(2)

        # Debt-to-Collateral Ratio
        if system_debt_to_collateral_ratio > 3:
            cols_warnings[0].error(
                f"🚨 **Critical Debt-to-Collateral Level**: Debt exceeds collateral by {system_debt_to_collateral_ratio:.2f}x, signaling a high leverage and liquidation risks."
            )
        elif 3 >= system_debt_to_collateral_ratio > 2:
            cols_warnings[0].warning(
                f"⚠️ **Moderate Debt-to-Collateral Level**: Debt exceeds collateral by {system_debt_to_collateral_ratio:.2f}x, requiring attention to reduce leverage risks."
            )
        else:
            cols_warnings[0].success(
                f"✅ **Safe Debt-to-Collateral Level**: Debt is well-covered by collateral with a ratio of {system_debt_to_collateral_ratio:.2f}x, indicating low leverage risk."
            )

        # Collateral Coverage Ratio
        if system_collateral_coverage_ratio < 1:
            cols_warnings[1].error(
                f"🚨 **Collateral Insufficiency**: Collateral covers only {system_collateral_coverage_ratio:.2f}x of debt, highlighting under-collateralization risks."
            )
        elif 1 <= system_collateral_coverage_ratio <= 1.5:
            cols_warnings[1].warning(
                f"⚠️ **Low Collateral Coverage**: Collateral covers {system_collateral_coverage_ratio:.2f}x of debt, providing limited room for price volatility."
            )
        else:
            cols_warnings[1].success(
                f"✅ **Strong Collateral Coverage**: Collateral comfortably covers {system_collateral_coverage_ratio:.2f}x of debt, ensuring high stability."
            )


        cols_warnings = st.columns(2)

        # System Debt and Bad Debt Warnings
        if system_total_debt_to_unwind == 0 and system_bad_debt == 0:
            cols_warnings[0].success(
                "✅ **Stable System Debt**: No debt to unwind or bad debt exists, indicating a healthy and stable system."
            )
        elif system_total_debt_to_unwind > 0 and system_bad_debt == 0:
            cols_warnings[0].warning(
                f"⚠️ **Moderate Insolvency Risk**: System Debt to Unwind is ${system_total_debt_to_unwind:,.2f}, but no bad debt is present. "
                "While manageable, the system is under some stress and requires monitoring."
            )
        else:
            cols_warnings[0].error(
                f"🚨 **Critical Insolvency Risk**: System Debt to Unwind is ${system_total_debt_to_unwind:,.2f}, and Bad Debt is ${system_bad_debt:,.2f}. "
                "This indicates systemic instability and inadequate collateral to cover debts, requiring urgent intervention."
            )

        # Depegging Risk
        if depegging_probability == "High":
            cols_warnings[1].error(
                f"🚨 **High Depegging Risk**: {explanation}"
            )
        elif depegging_probability == "Medium":
            cols_warnings[1].warning(
                f"⚠️ **Medium Depegging Risk**: {explanation}"
            )
        else:
            cols_warnings[1].success(
                f"✅ **Low Depegging Risk**: {explanation}"
            )










        st.write("\n")

        # Add an expander for system-wide formulas and calculations
        with st.expander("Detailed Formulas and Calculations for System-Wide Metrics"):

            # Total Collateral Formula
            st.write(f"**Total Collateral Formula:**")
            st.latex(r"""
            \text{Total Collateral (USD)} = \Sigma (\text{Token Deposits})
            """)
            st.write(f"Result: Sum of all token deposits = {system_total_collateral:,.2f}")

            # Total ebUSD Minted Formula
            st.write(f"**Total ebUSD Minted Formula:**")
            st.latex(r"""
            \text{Total ebUSD Minted (USD)} = \Sigma (\text{ebUSD Minted per Token})
            """)
            st.write(f"Result: Sum of all ebUSD minted across tokens = {system_total_ebusd_minted:,.2f}")
            
            # Safe MCR System-Wide Formula
            st.write(f"**Safe MCR System-Wide Formula:**")
            st.latex(r"""
            \text{Safe MCR (\%)} = \frac{\Sigma (\text{Token MCR} \times \text{Token Collateral})}{\Sigma (\text{Token Collateral})}
            """)
            st.write(f"Result: {weighted_mcr_sum:,.2f} / {weighted_collateral:,.2f} = {system_mcr:.2f}%")

            # Average Token Utilization Formula
            st.write(f"**Average Token Utilization Formula:**")
            st.latex(r"""
            \text{Average Token Utilization (\%)} = \frac{\Sigma (\text{Token Utilization Ratios})}{\text{Number of Tokens}}
            """)
            st.write(f"Result: {average_utilization * 100:.2f}%")

            # ebUSD Leverage Formula
            st.write(f"**ebUSD Leverage Formula:**")
            st.latex(r"""
            \text{ebUSD Leverage (x)} = \frac{\text{Total ebUSD Minted}}{\text{Total Collateral}}
            """)
            st.write(f"Result: {system_total_ebusd_minted:,.2f} / {system_total_collateral:,.2f} = {system_leverage:.2f}")

            # Liquidity Buffer Formula
            st.write(f"**Liquidity Buffer Formula:**")
            st.latex(r"""
            \text{Liquidity Buffer (USD)} = \text{DEX Liquidity} \times (1 - \text{System Utilization})
            """)
            st.write(f"Result: {dex_liquidity:,.2f} × (1 - {system_utilization:.2f}) = {liquidity_buffer:,.2f}")

            # Liquidity Stress Indicator Formula
            st.write(f"**Liquidity Stress Indicator Formula:**")
            st.write("Indicator is 'High' if Utilization > 80%, 'Medium' if Utilization > 50%, else 'Low'.")
            st.write(f"Result: System Utilization = {average_utilization * 100:.2f}% -> Indicator = {'High' if average_utilization > 0.8 else 'Medium' if average_utilization > 0.5 else 'Low'}")
            
            # ebUSD Interest Rate Formula
            st.write(f"**ebUSD Interest Rate Formula:**")
            st.latex(r"""
            \text{ebUSD Interest Rate (\%)} = \text{Base Interest Rate} \times \text{Average Utilization}
            """)
            st.write(f"Result: {system_base_interest_rate:.2f} * {average_utilization:.2f} = {system_interest_rate:.2f}%")

            # ebUSD Slippage Formula
            st.write(f"**ebUSD Slippage Formula:**")
            st.latex(r"""
            \text{ebUSD Slippage (\%)} = \frac{\text{Total ebUSD Minted} - \text{DEX Liquidity}}{\text{DEX Liquidity}}
            """)
            st.write(f"Result: ({system_total_ebusd_minted:,.2f} - {dex_liquidity:,.2f}) / {dex_liquidity:,.2f} = {slippage:.2f}%")

            # Debt-to-Collateral Ratio Formula
            st.write(f"**Debt-to-Collateral Ratio Formula:**")
            st.latex(r"""
            \text{Debt-to-Collateral Ratio} = \frac{\text{Total System Debt}}{\text{Total Collateral}}
            """)
            st.write(f"Result: {system_total_debt:,.2f} / {total_collateral_after_price_variation:,.2f} = {system_debt_to_collateral_ratio:.2f}")

            # Collateral Coverage Ratio Formula
            st.write(f"**Collateral Coverage Ratio Formula:**")
            st.latex(r"""
            \text{Collateral Coverage Ratio} = \frac{\text{Total Collateral}}{\text{Total System Debt}}
            """)
            st.write(f"Result: {total_collateral_after_price_variation:,.2f} / {system_total_debt:,.2f} = {system_collateral_coverage_ratio:.2f}")

            # Liquidity-to-Debt Ratio Formula
            st.write(f"**Liquidity-to-Debt Ratio Formula:**")
            st.latex(r"""
            \text{Liquidity-to-Debt Ratio} = \frac{\text{DEX Liquidity}}{\text{Total ebUSD Minted}}
            """)
            st.write(f"Result: {dex_liquidity:,.2f} / {system_total_debt:,.2f} = {system_liquidity_to_debt_ratio:.2f}")

            # Total System Debt Formula
            st.write(f"**Total System Debt After Leverage Formula:**")
            st.latex(r"""
            \text{Total System Debt (USD)} = \Sigma (\text{Token Debt After Leverage})
            """)
            st.write(f"Result: {system_total_debt:,.2f}")

            # Total System Debt to Unwind Formula
            st.write(f"**Total System Debt to Unwind Formula:**")
            st.latex(r"""
            \text{System Total Debt to Unwind (USD)} = \Sigma (\text{Debt to Repay for Each Token})
            """)
            st.write(f"Result: {system_total_debt_to_unwind:,.2f}")

            # System Bad Debt Formula
            st.write(f"**System Bad Debt Formula:**")
            st.latex(r"""
            \text{Collateral Value After Liquidation (USD)} = 
            \text{System Total Collateral (USD)} \cdot (1 - \text{Liquidation Rate})
            """)
            st.latex(r"""
            \text{System Bad Debt (USD)} = 
            \max(0, \text{System Total Debt to Unwind (USD)} - \text{Collateral Value After Liquidation (USD)})
            """)
            st.write(f"Result: {system_bad_debt:,.2f}")

            # Depegging Probability Formula (Insight-Based)
            st.write(f"**Depegging Probability Formula:**")
            st.write("Derived from system-wide slippage, utilization, and liquidity metrics.")
            st.write(f"Indicator: {depegging_probability}")

            st.code("""
            def calculate_depegging_risk(slippage, system_utilization, dex_liquidity, system_total_ebusd_minted):

                if slippage > 2 or system_utilization > 90:
                    return "High", (
                        f"Slippage is significant ({slippage:.2f}%) and/or system utilization is very high "
                        f"({system_utilization * 100:.2f}%), indicating a strong risk of ebUSD depegging."
                    )
                elif slippage > 1 or system_utilization > 70:
                    return "Medium", (
                        f"Moderate slippage ({slippage:.2f}%) and/or system utilization ({system_utilization * 100:.2f}%) "
                        "indicates a potential for ebUSD depegging under stress conditions."
                    )
                elif dex_liquidity < system_total_ebusd_minted * 0.5:
                    return "Medium", (
                        f"DEX liquidity ({dex_liquidity:,.2f}) is less than 50% of the total ebUSD minted "
                        f"({system_total_ebusd_minted:,.2f}), indicating potential stress on the peg."
                    )
                else:
                    return "Low", (
                        f"Slippage is low ({slippage:.2f}%), system utilization is within safe bounds "
                        f"({system_utilization * 100:.2f}%), and DEX liquidity is sufficient to cover ebUSD trades."
                    )
                """, language="python")







            #st.write(f"**Insights:** System-wide Safe MCR is {system_mcr:.2f}%, providing a holistic stability measure. The system-wide leverage of {system_leverage:.2f}x reflects the overall capital efficiency. A Liquidity-to-Debt Ratio of {system_liquidity_to_debt_ratio:.2f} indicates the sufficiency of liquidity to cover minted ebUSD. Interest Rate is dynamically set at {interest_rate:.2f}% based on utilization, ensuring borrowing remains sustainable.")
        with st.expander("**System-Wide Insights for ebUSD**"):
            st.subheader("**System-Wide ebUSD Insights**")

            st.write(f"""
            #### **Collateralization and Stability**
            - The system's Safe Minimum Collateralization Ratio (MCR) is **{system_mcr:.2f}%**, reflecting the average collateral safety across all tokens.
            - Total collateral of **{system_total_collateral:,.2f} USD** underpins the system's stability, ensuring robust support for ebUSD minting and trading.
            - However, increasing leverage, utilization, or slippage may erode this safety margin, necessitating proactive interventions.

            #### **Leverage, Liquidity, and Elasticity**
            - System leverage is **{system_leverage:.2f}x**, indicating the ratio of ebUSD minted to total collateral. This efficiency must be balanced against potential systemic risks during market volatility.
            - The Liquidity-to-Debt Ratio is **{system_liquidity_to_debt_ratio:.2f}**, signaling adequate liquidity to handle redemptions and liquidations.
            - A Liquidity Buffer of **{liquidity_buffer:,.2f} USD** provides a critical safeguard against sudden liquidity shocks.

            Elasticity metrics further underscore the system's adaptability:
            - **Borrower Demand Elasticity**: Higher interest rates reduce borrowing, mitigating systemic risk but potentially impacting liquidity.
            - **Stability Pool Elasticity**: Influences the system's resilience in handling liquidations under changing risk and yield conditions.

            #### **Risk Metrics and Depegging Risks**
            Current system-wide risk indicators:
            - **Slippage**: At **{slippage:.2f}%**, slippage poses a potential peg stability risk during high demand or constrained liquidity periods.
            - **Average Token Utilization**: At **{average_utilization * 100:.2f}%**, utilization indicates moderate liquidity constraints, requiring intervention if utilization exceeds **80%**.
            - **Total System Debt**: **{system_total_debt:,.2f} USD**, emphasizing the need for careful debt and leverage management.
            - **Debt-to-Collateral Ratio**: Currently at **{system_debt_to_collateral_ratio:.2f}**, signaling controlled leverage. Ratios exceeding **3x** may elevate systemic risks.

            The Depegging Probability is currently **{depegging_probability}**, highlighting a composite analysis of slippage, liquidity, and utilization metrics. Proactive measures, such as dynamic interest rates or redemption fees, can mitigate risks.

            #### **Redemption Fee Dynamics**
            Dynamic redemption fees can stabilize the system during stress:
            - A fee based on high Debt-to-Collateral Ratios (e.g., >0.9) or utilization levels (e.g., >85%) can discourage destabilizing redemptions.
            - Proposed formula:
            \[
            \text{{Redemption Fee (\%)}} = 3 \cdot \max(0, (\text{{Debt-to-Collateral Ratio}} - 0.9)) + 5 \cdot \max(0, (\text{{Utilization}} - 0.85)).
            \]

            #### **Conclusions and Recommendations**
            - **Maintain Robust Collateralization**: Ensure collateral remains above the Safe MCR to cushion against volatility.
            - **Monitor Risk Metrics**: Track slippage, utilization, and leverage; intervene if leverage exceeds **3x** or slippage surpasses **5%**.
            - **Adjust System Elasticity**: Dynamically modify interest rates and stability incentives to optimize liquidity and borrowing demand.
            - **Implement Dynamic Redemption Fees**: Prevent destabilizing behaviors under high stress by adjusting fees based on system-wide risk indicators.
            - **Strengthen Liquidity Buffers**: Maintain a Liquidity-to-Debt Ratio above **1.0** to support system resilience.

            Overall, the ebUSD system demonstrates robustness, with manageable risks under current conditions. Proactive monitoring and adjustments can ensure long-term stability.
            """)




if __name__ == "__main__":
    main()
