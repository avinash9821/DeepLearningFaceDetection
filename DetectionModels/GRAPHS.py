import matplotlib.pyplot as plt
import numpy as np


def plots(history):
    plt.plot(np.arange(len(np.array(history.history["accuracy"]))), np.array(history.history["accuracy"]),
             label="Accuracy")
    plt.plot(np.arange(len(np.array(history.history["loss"]))), np.array(history.history["loss"]),
             label="Loss")

    plt.legend()
    plt.savefig("AccuracyPlots")

    plt.plot(np.arange(len(np.array(history.history["val_accuracy"]))), np.array(history.history["val_accuracy"]),
             label="validation Accuracy")

    plt.plot(np.arange(len(np.array(history.history["val_loss"]))), np.array(history.history["val_loss"]),
             label="validation Loss")
    plt.legend()
    plt.savefig("LossPlots")

