import matplotlib.pyplot as plt

def plot_evolution(entropy_history, wisdom_density_history):
    plt.plot(entropy_history, label="Entropy", color="red")
    plt.plot(wisdom_density_history, label="Wisdom Density", color="blue")
    plt.xlabel("Time Steps")
    plt.ylabel("Values")
    plt.title("智慧進化模擬")
    plt.legend()
    plt.show()
