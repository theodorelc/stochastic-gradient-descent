import matplotlib.pyplot as plt
import numpy as np
import random


def main():
    num = int(input("How many dice? "))
    rolls = []

    for _ in range(num):
        rolls.append(random.randint(1, 6))

    average = np.mean(rolls)
    print(f"Mean of dice rolls: {average}")

    plt.figure(figsize=(8, 5))
    plt.hist(rolls, bins=6)
    plt.show()


if __name__ == "__main__":
    main()