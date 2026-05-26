# %%
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# %%
# --- Escalier de Cantor (fonction du diable) ---
#
# Définition récursive sur [0, 1] :
#   f(x) = f(3x) / 2          si x ∈ [0, 1/3]
#   f(x) = 1/2                si x ∈ [1/3, 2/3]
#   f(x) = 1/2 + f(3x−2) / 2 si x ∈ [2/3, 1]


def _cantor_scalar(x: float, depth: int) -> float:
    if depth == 0:
        return x
    if x < 1 / 3:
        return _cantor_scalar(3 * x, depth - 1) / 2
    elif x > 2 / 3:
        return 0.5 + _cantor_scalar(3 * x - 2, depth - 1) / 2
    else:
        return 0.5


cantor = np.vectorize(lambda x: _cantor_scalar(x, depth=15))

# %%
x = np.linspace(0, 1, 2000)
y = cantor(x)
# %%
fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(x, y, color="steelblue", linewidth=1.5)

ax.set_title("Escalier de Cantor", fontsize=14)
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")

# Graduations en fractions propres
ax.xaxis.set_major_locator(ticker.MultipleLocator(1 / 3))
ax.xaxis.set_major_formatter(
    ticker.FuncFormatter(
        lambda v, _: {0: "0", 1 / 3: "1/3", 2 / 3: "2/3", 1: "1"}.get(
            round(v, 10), f"{v:.2f}"
        )
    )
)
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.25))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(True, alpha=0.3)
ax.set_aspect("equal")

plt.tight_layout()
plt.savefig("cantor_staircase.png", dpi=150)
# plt.show()
