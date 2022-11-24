from statistics import mode
import pandas as pd
from distance_measures import distance_d22
from image_plotting import plot_classification


def classify(train_X, train_y, image, real_label, k):
    """Luokittelee kuvan k-NN-menetelmällä

    Args:
        train_X: pandas.DataFrame -luokan olio, joka sisältää harjoitusdatan kuvat.
        train_y: pandas.Series -luokan olio, joka sisältää harjoitusdatan kuvia vastaavat luokat.
        image: pandas.Series -luokan olio, joka vastaa luokiteltavaa kuvaa.
        real_label: luokiteltavan kuvan todellinen luokka (int).
        k: naapureiden lukumäärä k-NN-menetelmää varten (int).
    """

    # neighbors: list of neighbors as tuples of length two
    # where the first element of the tuple is the distance to the neighor
    # and the second element of the tuple is the label of the neighbor
    neighbors = []

    for i in range(len(train_X)):
        print(f'Calculating distance to image {i} in the training data')
        distance = distance_d22(train_X.iloc[i], image)
        neighbors.append((distance, train_y.iloc[i]))

    neighbors.sort(key=lambda x: x[0])

    # labels: list of labels that belong to the k nearest neighbors
    labels = []

    for i in range(k):
        labels.append(neighbors[i][1])

    predicted_label = mode(labels)

    plot_classification(image, predicted_label, real_label)
