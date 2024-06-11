import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, gamma, norm, nbinom, binom, hypergeom, poisson, rv_discrete

# Método de transformación inversa para la distribución uniforme
def generate_uniform(a, b, size):
    return np.random.uniform(a, b, size)

# Método de transformación inversa para la distribución exponencial
def generate_exponential(lam, size):
    U = np.random.uniform(0, 1, size)
    return -np.log(1 - U) / lam

# Método de transformación inversa para la distribución normal (Box-Muller)
def generate_normal(size):
    U1 = np.random.uniform(0, 1, size//2)
    U2 = np.random.uniform(0, 1, size//2)
    R = np.sqrt(-2 * np.log(U1))
    theta = 2 * np.pi * U2
    Z1 = R * np.cos(theta)
    Z2 = R * np.sin(theta)
    return np.concatenate((Z1, Z2))

# Método del rechazo para la distribución gamma
def generate_gamma(shape, scale, size):
    max_pdf = gamma.pdf(shape, shape, scale=scale)  # Máximo de la PDF
    samples = []
    while len(samples) < size:
        x = np.random.gamma(shape, scale, size)
        y = np.random.uniform(0, max_pdf, size)
        samples.extend(x[y <= gamma.pdf(x, shape, scale=scale)])
    return np.array(samples[:size])

# Método del rechazo para la distribución Pascal (o binomial negativa)
def generate_pascal(r, p, size):
    max_pmf = nbinom.pmf(r, r, p)  # Máximo de la PMF
    samples = []
    while len(samples) < size:
        x = np.random.negative_binomial(r, p, size)
        y = np.random.uniform(0, max_pmf, size)
        samples.extend(x[y <= nbinom.pmf(x, r, p)])
    return np.array(samples[:size])

# Método del rechazo para la distribución binomial
def generate_binomial(n, p, size):
    max_pmf = binom.pmf(n, n, p)  # Máximo de la PMF
    samples = []
    while len(samples) < size:
        x = np.random.binomial(n, p, size)
        y = np.random.uniform(0, max_pmf, size)
        samples.extend(x[y <= binom.pmf(x, n, p)])
    return np.array(samples[:size])

# Método del rechazo para la distribución hipergeométrica
def generate_hypergeometric(N, K, n, size):
    max_pmf = hypergeom.pmf(min(n, K), N, K, n)  # Máximo de la PMF
    samples = []
    while len(samples) < size:
        x = np.random.hypergeometric(K, N - K, n, size)
        y = np.random.uniform(0, max_pmf, size)
        samples.extend(x[y <= hypergeom.pmf(x, N, K, n)])
    return np.array(samples[:size])

# Método del rechazo para la distribución de Poisson
def generate_poisson(lam, size):
    max_pmf = poisson.pmf(int(lam), lam)  # Máximo de la PMF
    samples = []
    while len(samples) < size:
        x = np.random.poisson(lam, size)
        y = np.random.uniform(0, max_pmf, size)
        samples.extend(x[y <= poisson.pmf(x, lam)])
    return np.array(samples[:size])

# Método del rechazo para la distribución empírica discreta
def generate_empirical_discrete(values, probabilities, size):
    max_prob = np.max(probabilities)  # Máximo de las probabilidades
    samples = []
    while len(samples) < size:
        x = np.random.choice(values, size, p=probabilities)
        y = np.random.uniform(0, max_prob, size)
        for i in range(size):
            if y[i] <= probabilities[x[i]]:
                samples.append(x[i])
    return np.array(samples)

# Configuración de los parámetros
size = 100000

# Uniforme
uniform_samples = generate_uniform(0, 10, size)
plt.hist(uniform_samples, bins=50, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.linspace(0, 10, 1000)
plt.plot(x, np.ones_like(x) * 0.1, 'r--', label='Distribución teórica')
plt.title('Distribución Uniforme')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Exponencial
exp_samples = generate_exponential(1.5, size)
plt.hist(exp_samples, bins=50, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.linspace(0, 15, 1000)
plt.plot(x, expon.pdf(x, scale=1/1.5), 'r--', label='Distribución teórica')
plt.title('Distribución Exponencial')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Normal
normal_samples = generate_normal(size)
plt.hist(normal_samples, bins=50, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.linspace(-4, 4, 1000)
plt.plot(x, norm.pdf(x), 'r--', label='Distribución teórica')
plt.title('Distribución Normal')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Gamma
gamma_samples = generate_gamma(2, 2, size)
plt.hist(gamma_samples, bins=50, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.linspace(0, 20, 1000)
plt.plot(x, gamma.pdf(x, 2, scale=2), 'r--', label='Distribución teórica')
plt.title('Distribución Gamma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Pascal
pascal_samples = generate_pascal(5, 0.5, size)
plt.hist(pascal_samples, bins=50, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.arange(0, 40)
plt.plot(x, nbinom.pmf(x, 5, 0.5), 'r--', label='Distribución teórica')
plt.title('Distribución Pascal')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Binomial
binomial_samples = generate_binomial(10, 0.5, size)
plt.hist(binomial_samples, bins=11, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.arange(0, 11)
plt.plot(x, binom.pmf(x, 10, 0.5), 'r--', label='Distribución teórica')
plt.title('Distribución Binomial')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Hipergeométrica
hypergeom_samples = generate_hypergeometric(20, 7, 12, size)
plt.hist(hypergeom_samples, bins=13, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.arange(0, 13)
plt.plot(x, hypergeom.pmf(x, 20, 7, 12), 'r--', label='Distribución teórica')
plt.title('Distribución Hipergeométrica')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Poisson
poisson_samples = generate_poisson(3, size)
plt.hist(poisson_samples, bins=15, density=True, alpha=0.6, color='g', label='Muestras generadas')
x = np.arange(0, 15)
plt.plot(x, poisson.pmf(x, 3), 'r--', label='Distribución teórica')
plt.title('Distribución Poisson')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

# Empírica Discreta
values = np.array([0, 1, 2, 3, 4])
probabilities = np.array([0.1, 0.2, 0.3, 0.25, 0.15])
empirical_samples = generate_empirical_discrete(values, probabilities, size)
plt.hist(empirical_samples, bins=len(values), density=True, alpha=0.6, color='g', label='Muestras generadas')
plt.plot(values, probabilities, 'ro', label='Distribución teórica')
plt.title('Distribución Empírica Discreta')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
