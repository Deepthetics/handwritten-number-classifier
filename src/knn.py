from statistics import mode


def classify_one(train_X, train_y, image, k, distance_function):
    """Luokittelee kuvan k-NN-menetelmällä.

    Args:
        train_X: pandas.DataFrame -luokan olio, joka sisältää harjoitusdatan kuvat.
        train_y: pandas.Series -luokan olio, joka sisältää harjoitusdatan kuvia vastaavat luokat.
        image: pandas.Series -luokan olio, joka vastaa luokiteltavaa kuvaa.
        real_label: luokiteltavan kuvan todellinen luokka (int).
        k: naapureiden lukumäärä k-NN-menetelmää varten (int).
        distance_function: etäisyysfunktio.

    Returns:
        predicted_label: ennustettu luokka (int).
    """

    # neighbors: list of neighbors as tuples of length two
    # where the first element of the tuple is the distance to the neighor
    # and the second element of the tuple is the label of the neighbor
    neighbors = []

    for i in range(len(train_X)):
        #print(f'Calculating distance to image {i} in the training data...')
        distance = distance_function(train_X.iloc[i], image)
        neighbors.append((distance, train_y.iloc[i]))

    neighbors.sort(key=lambda x: x[0])

    # labels: list of labels that belong to the k nearest neighbors
    labels = []

    for i in range(k):
        labels.append(neighbors[i][1])

    predicted_label = mode(labels)

    return predicted_label

def classify_many(train_X, train_y, images, k, distance_function):
    """Luokittelee kuvat k-NN-menetelmällä.

    Args:
        train_X: pandas.DataFrame -luokan olio, joka sisältää harjoitusdatan kuvat.
        train_y: pandas.Series -luokan olio, joka sisältää harjoitusdatan kuvia vastaavat luokat.
        images: pandas.DataFrame -luokan olio, joka vastaa luokiteltavia kuvia.
        k: naapureiden lukumäärä k-NN-menetelmää varten (int).
        distance_function: etäisyysfunktio.

    Returns:
        predicted_labels: ennustetut luokat (list).
    """

    predicted_labels = []

    for i in range(len(images.index)):
        print(f'Classifying image {i+1} of test data...')
        predicted_labels.append(classify_one(train_X, train_y, images.iloc[i], k, distance_function))

    return predicted_labels

def error_rate(predicted_labels, real_labels):
    """Laskee luokitteluvirheen.

    Args:
        predicted_labels: ennustetut luokat (list).
        real_labels: todelliset luokat (list).

    Returns:
        error: luokitteluvirhe (int).
    """

    error_count = 0
    label_count = len(predicted_labels)

    for i in range(label_count):
        if predicted_labels[i] != real_labels[i]:
            error_count += 1

    error = error_count / label_count
    return error

def classification_summary(predicted_labels, real_labels):
    """Muodostaa yhteenvedon useamman kuvan luokittelusta.

    Args:
        predicted_labels: ennustetut luokat (list).
        real_labels: todelliset luokat (list).

    Returns:
        summary: Yhteenveto luokittelusta (string).
    """

    error = error_rate(predicted_labels, real_labels)
    summary = f'Classified {len(predicted_labels)} images.\nPredicted labels: {predicted_labels}\nReal labels: {real_labels}\nError rate: {error*100}%'
    return summary
