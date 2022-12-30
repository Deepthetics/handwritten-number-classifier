import pandas as pd
from distance_measures import distance_d22, distance_d23, distance_d23_mod
from image_data_processing import to_array, extract, to_binary
from image_plotting import plot_two_images, plot_classification
from knn import classify_one, classify_many, classification_summary


class UI:
    def __init__(self, train_X, train_y, test_X, test_y):
        self.train_X = train_X
        self.train_y = train_y
        self.test_X = test_X
        self.test_y = test_y

    def start(self):
        while True:
            print()
            print('1: classify images')
            print('q: quit')
            print()

            command = input('command: ')
            print()

            if command == '1':
                train_index_start = int(input('train index start (0-59999): '))
                train_index_end = int(input('train index end (0-59999): '))
                test_index_start = int(input('test index start (0-9999): '))
                test_index_end = int(input('test index end (0-9999): '))
                k = int(input('k: '))
                distance_function = input('distance function (d22, d23, d23mod): ')
                plot = input('plot (true): ')

                if distance_function == 'd22':
                    distance_function = distance_d22
                elif distance_function == 'd23':
                    distance_function = distance_d23
                elif distance_function == 'd23mod':
                    distance_function = distance_d23_mod

                if plot == 'true':
                    plot = True
                else:
                    plot = False


                print()
                predicted_labels = classify_many(self.train_X.iloc[train_index_start:train_index_end+1],
                                                 self.train_y[train_index_start:train_index_end+1],
                                                 self.test_X.iloc[test_index_start:test_index_end+1],
                                                 k=k, distance_function=distance_function)

                real_labels = list(self.test_y.iloc[test_index_start:test_index_end+1].to_numpy())

                print()
                print(classification_summary(predicted_labels, real_labels))

                if plot:
                    for i, j in enumerate(range(test_index_start, test_index_end+1)):
                        plot_classification(to_array(self.test_X.iloc[j]), predicted_labels[i], self.test_y.iloc[j])

            if command == 'q':
                break
