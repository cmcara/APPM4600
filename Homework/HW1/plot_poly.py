import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.920, 2.081, 0.001)
coeffs = [1, -18, 144, -672, 2016, -4032, 5376, -4608, 2304, -512]

p_expanded = np.polyval(coeffs, x)
p_factored = (x - 2) ** 9

plt.figure(figsize=(10, 5))
plt.plot(x, p_factored, label="Factored Plot", color="blue", linewidth=2)
plt.xlabel("x", fontsize=11)
plt.ylabel("p(x)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
