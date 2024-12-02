import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Parameters
n_samples = 1000  # Number of samples
rho = 0.8  # Correlation coefficient for Gaussian and t-Copulas (high correlation due to economic factors)
nu = 5  # Degrees of freedom for t-Copula

# Correlation matrix
corr_matrix = np.array([[1, rho], [rho, 1]])

# Real-world scenario description:
# - Risk 1 (R1): Probability of bankruptcy due to financial instability
# - Risk 2 (R2): Probability of a major lawsuit due to mismanagement

# Gaussian Copula
# Generate samples from a multivariate normal distribution
mean = [0, 0]  # Mean for the normal distribution
samples_gaussian = np.random.multivariate_normal(mean, corr_matrix, size=n_samples)

# Transform to uniform margins using the CDF
r1_gaussian = stats.norm.cdf(samples_gaussian[:, 0])  # Bankruptcy risk
r2_gaussian = stats.norm.cdf(samples_gaussian[:, 1])  # Lawsuit risk

# Helper function for multivariate t-distribution sampling
def multivariate_t_rvs(mean, cov, df, n_samples):
    """
    Generate random samples from a multivariate t-distribution.
    """
    g = np.random.gamma(df / 2.0, 2.0 / df, n_samples)
    z = np.random.multivariate_normal(np.zeros(len(mean)), cov, size=n_samples)
    return mean + z / np.sqrt(g)[:, None]

# t-Copula
# Generate samples from a multivariate t-distribution
samples_t = multivariate_t_rvs(mean=np.zeros(2), cov=corr_matrix, df=nu, n_samples=n_samples)

# Transform to uniform margins using the CDF of t-distribution
r1_t = stats.t.cdf(samples_t[:, 0], df=nu)  # Bankruptcy risk
r2_t = stats.t.cdf(samples_t[:, 1], df=nu)  # Lawsuit risk

# Visualize the results
plt.figure(figsize=(12, 6))

# Gaussian Copula
plt.subplot(1, 2, 1)
plt.scatter(r1_gaussian, r2_gaussian, alpha=0.5, label="Gaussian Copula")
plt.title("Gaussian Copula: Bankruptcy vs. Lawsuit Risk")
plt.xlabel("Risk of Bankruptcy (R1)")
plt.ylabel("Risk of Lawsuit (R2)")
plt.legend()

# t-Copula
plt.subplot(1, 2, 2)
plt.scatter(r1_t, r2_t, alpha=0.5, label="t-Copula")
plt.title(f"t-Copula: Bankruptcy vs. Lawsuit Risk (df={nu})")
plt.xlabel("Risk of Bankruptcy (R1)")
plt.ylabel("Risk of Lawsuit (R2)")
plt.legend()

plt.tight_layout()
plt.show()
