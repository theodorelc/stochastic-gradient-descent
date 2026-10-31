import matplotlib.pyplot as plt
import numpy as np
import random


def main():
    sequence = input("Enter a sequence of heads and tails, i.e. HTTH: ")
    sequence = sequence.replace("H","0").replace("T","1")
    num = input("How many trials? ")
    trials = []

    for _ in range(int(num)):
        flips = ""
        while not flips.endswith(sequence):
            flips += str(random.randint(0, 1))
        trials.append(len(flips))

    average = np.mean(trials)
    print(f"Mean of coin flips: {average}")

    plt.figure(figsize=(8, 5))
    plt.hist(trials, bins=range(1, max(trials) + 2))
    plt.axvline(average, color="r")
    plt.xlabel("Flips until sequence")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    main()