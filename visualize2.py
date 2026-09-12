import matplotlib.pyplot as plt
import numpy as np

unsolvable_runtime = [9.71e-04, 1.90e-04, 2.63e-04]
unsolvable_backtracks = [316, 5, 1]

x = np.arange(3)
colors = ["#070707", "#555555", "#CDCDCD"]
labels = ["Basic", "MRV + Degree", "MRV + Degree + MAC"]

fig, ax = plt.subplots(figsize=(7, 6))
ax_twin = ax.twinx()

ax.bar(x, unsolvable_backtracks, 0.5, color=colors, alpha=0.85)
line, = ax_twin.plot(x, unsolvable_runtime, color="black", marker="o", linewidth=2, label="Runtime (s)")

ax.set_xlabel("Algorithm")
ax.set_ylabel("Number of Backtracks")
ax_twin.set_ylabel("Runtime (seconds)")
ax.set_title("Unsolvable Dataset (Backtracks & Runtime)")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=10, ha="right")
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.legend([plt.Rectangle((0,0),1,1, color=c) for c in colors], labels, loc="upper right", fontsize=9)
ax_twin.legend([line], ["Runtime (s)"], loc="upper center", fontsize=9)

plt.tight_layout()
plt.savefig("unsolvable_graph.png", dpi=150)
plt.show()