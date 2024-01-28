import random
import scipy.integrate as spi

memo = {}


def monte_carlo_integration(f, a, b, num_samples, memo=memo):
    total = 0
    # use random only once for each num_samples
    if not num_samples in memo:
        for _ in range(num_samples):
            x = random.uniform(a, b)
            total += f(x)
        memo[num_samples] = (b - a) * total / num_samples
    return memo[num_samples]


def f(x):
    return x**2


def monte_carlo_error_estimate(f, a, b, num_samples):
    return (b - a) / (num_samples**0.5) * (spi.quad(f, a, b)[1])


a = 0  # lower bound of integration
b = 2  # upper bound of integration
num_samples = 100000
num_samples_2 = 100000000  # number of random samples

spi_result, spi_error = spi.quad(f, a, b)


print(
    f"Approximate integral: {monte_carlo_integration(f, a, b, num_samples)}, \n \
error estimate: {monte_carlo_error_estimate(f, a, b, num_samples)}, \n \
Samples: {num_samples} \n"
)

print(
    f"Approximate integral: {monte_carlo_integration(f, a, b, num_samples_2)}, \n \
error estimate: {monte_carlo_error_estimate(f, a, b, num_samples_2)}, \n \
Samples: {num_samples_2} \n"
)

print(f"SciPy result: {spi_result}, SciPy error: {spi_error} \n")

print(
    f"Methods results difference for {num_samples} samples: \n \
{abs(spi_result - monte_carlo_integration(f, a, b, num_samples)) / spi_result} or \
{100 * abs(spi_result - monte_carlo_integration(f, a, b, num_samples)) / spi_result:.2}%"
)

print(
    f"Methods results difference for {num_samples_2} samples: \n \
{abs(spi_result - monte_carlo_integration(f, a, b, num_samples_2)) / spi_result} or \
{100 * abs(spi_result - monte_carlo_integration(f, a, b, num_samples_2)) / spi_result:.2}%"
)
