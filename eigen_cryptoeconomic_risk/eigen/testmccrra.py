import numpy as np

# Example portfolio: 2 assets with their expected return and volatility
expected_returns = np.array([0.06, 0.12])  # Expected returns for Asset 1 and Asset 2
volatilities = np.array([0.1, 0.2])  # Volatility (std. dev. of returns) for Asset 1 and Asset 2
correlation_matrix = np.array([[1, 0.5], [0.5, 1]])  # Correlation matrix between the two assets
weights = np.array([0.5, 0.5])  # Portfolio weights for each asset

# Number of simulations
n_simulations = 10000
n_years = 1  # Simulate 1 year of returns

# Generate random returns for each asset
random_returns = np.random.normal(loc=expected_returns, scale=volatilities, size=(n_simulations, len(expected_returns)))

# Adjust for correlations
cholesky_matrix = np.linalg.cholesky(correlation_matrix)
random_returns = random_returns @ cholesky_matrix.T

# Calculate portfolio returns for each simulation
portfolio_returns = np.sum(random_returns * weights, axis=1)

# Analyze the results
expected_portfolio_return = np.mean(portfolio_returns)
portfolio_volatility = np.std(portfolio_returns)
value_at_risk = np.percentile(portfolio_returns, 5)  # 5% VaR

print(f"Expected Portfolio Return: {expected_portfolio_return}")
print(f"Portfolio Volatility: {portfolio_volatility}")
print(f"Value at Risk (5%): {value_at_risk}")
