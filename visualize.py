import matplotlib.pyplot as plt
import numpy as np

datasets = ["small (6)", "medium (15)", "large (20)"]

runtime = {
    "basic":          [1.81e-05, 6.10e-05, 1.42e-03],
    "mrv_degree":     [7.18e-05, 6.37e-04, 1.13e-03],
    "mrv_degree_mac": [1.46e-04, 1.69e-03, 4.63e-03],
}

backtracks = {
    "basic":          [1, 12, 409],
    "mrv_degree":     [0, 0, 0],
    "mrv_degree_mac": [0, 0, 0],
}

x = np.arange(len(datasets))
width = 0.25
colors = ["#000000", "#3D3D3D", "#979898"]
labels = ["Basic Backtracking", "MRV + Degree", "MRV + Degree + MAC"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

for i, (mode, color, label) in enumerate(zip(runtime.keys(), colors, labels)):
    ax1.bar(x + i * width, runtime[mode], width, label=label, color=color)
ax1.set_xlabel("Dataset Size")
ax1.set_ylabel("Runtime (seconds)")
ax1.set_title("Runtime Comparison by Dataset Size")
ax1.set_xticks(x + width)
ax1.set_xticklabels(datasets)
ax1.legend()
ax1.grid(axis="y", linestyle="--", alpha=0.5)

for i, (mode, color, label) in enumerate(zip(backtracks.keys(), colors, labels)):
    ax2.bar(x + i * width, backtracks[mode], width, label=label, color=color)
ax2.set_xlabel("Dataset Size")
ax2.set_ylabel("Number of Backtracks")
ax2.set_title("Backtracks Comparison by Dataset Size")
ax2.set_xticks(x + width)
ax2.set_xticklabels(datasets)
ax2.legend()
ax2.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("results_graph.png", dpi=150)
plt.show()