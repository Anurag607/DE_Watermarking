import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt

# Dummy function for embedding watermark, just returns a simulated quality metric
def embed_watermark(scale_factor):
    # Simulate a quality metric for watermarking (higher is better)
    return 1 - abs(scale_factor - 0.1)  # Pretend 0.1 is the best scale factor

# Dummy function for applying distortions and extracting watermark
def extract_watermark(scale_factor):
    # Simulate extraction quality (higher is better)
    return 1 - abs(scale_factor - 0.15)  # Pretend 0.15 faces more distortions but is still okay

# Objective function combining both embedding and extraction quality
def objective_function(scale_factor):
    quality_embedding = embed_watermark(scale_factor)
    quality_extraction = extract_watermark(scale_factor)
    # Our goal is to maximize the combined quality, so we return the negative sum
    return -(quality_embedding + quality_extraction)

# Bounds for the scale factor
bounds = [(0, 0.2)]

# Running the differential evolution algorithm
result = differential_evolution(objective_function, bounds)

# Results
print(f"Optimal scaling factor: {result.x[0]}")
print(f"Maximum combined quality: {-result.fun}")

# Plotting for visualization
scale_factors = np.linspace(0, 0.2, 100)
combined_quality = [-objective_function([sf]) for sf in scale_factors]

plt.plot(scale_factors, combined_quality, label='Combined Quality')
plt.axvline(x=result.x[0], color='r', linestyle='--', label='Optimal Scale Factor')
plt.xlabel('Scale Factor')
plt.ylabel('Combined Quality')
plt.legend()
plt.show()
