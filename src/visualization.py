import matplotlib.pyplot as plt
import numpy as np

def plot_forecasts(model_forecasts_for):
    for name, forecast in model_forecasts_for.items():
        plt.plot(np.arange(2023, 2029), forecast, marker='o', linestyle='--', label=f"{name} Forecast")
    plt.title("Foreign Forecast Comparison")
    plt.xlabel("Year")
    plt.ylabel("Foreign (Millions)")
    plt.legend()
    plt.grid(True)
    plt.show()
