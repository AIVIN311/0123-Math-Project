from math_models.model_0123 import logistic_wisdom_growth, adaptive_entropy_growth
import matplotlib.pyplot as plt

class EvolutionSimulator:
    def __init__(self):
        self.stage = 0
        self.entropy = 1.0
        self.wisdom_density = 1.0
        self.time = 0
        self.history = {"time": [], "entropy": [], "wisdom": []}

    def simulate_step(self):
        self.entropy = adaptive_entropy_growth(self.entropy, self.stage)
        self.wisdom_density = logistic_wisdom_growth(self.time, 5, 0.3, 5, self.entropy, self.stage)
        self.history["time"].append(self.time)
        self.history["entropy"].append(self.entropy)
        self.history["wisdom"].append(self.wisdom_density)
        self.time += 1
        self.stage = (self.stage + 1) % 4  # 0 → 1 → 2 → 3 → 0

    def run_simulation(self, steps=20):
        for _ in range(steps):
            self.simulate_step()

    def plot_results(self):
        plt.plot(self.history["time"], self.history["entropy"], label="Entropy", color="red")
        plt.plot(self.history["time"], self.history["wisdom"], label="Wisdom Density", color="blue")
        plt.xlabel("Time Steps")
        plt.ylabel("Values")
        plt.title("0123 理論智慧進化模擬")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    sim = EvolutionSimulator()
    sim.run_simulation(50)
    sim.plot_results()
