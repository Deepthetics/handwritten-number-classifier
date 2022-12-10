from matplotlib import pyplot as plt
from image_data_processing import to_array


def plot_two_images(image1, image2, image1_title, image2_title):
    """Plottaa kaksi kuvaa vierekkäin.

    Args:
        image1: pandas.Series -luokan olio, joka sisältää kuvadatan.
        image2: pandas.Series -luokan olio, joka sisältää kuvadatan.
        image1_title: ensimmäisen kuvan otsikko (str).
        image2_title: toisen kuvan otsikko (str).
    """

    image1 = to_array(image1)
    image2 = to_array(image2)

    fig = plt.figure()
    fig.suptitle('Comparison')
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)
    plt.imshow(image1, cmap='Greys')
    plt.title(image1_title)

    fig.add_subplot(rows, columns, 2)
    plt.imshow(image2, cmap='Greys')
    plt.title(image2_title)

    plt.show()

def plot_classification(image, predicted_label, real_label):
    """Plottaa kuvan ja tiedot sen ennustetusta luokasta sekä todellisesta luokasta.

    Args:
        image: pandas.Series -luokan olio, joka sisältää kuvadatan.
        predicted_label: ennustettu luokka (int).
        real_label: todellinen luokka (int).
    """

    image = to_array(image)
    plt.imshow(image, cmap="Greys")
    plt.title(f'Predicted label: {predicted_label}\nReal label:{real_label}', loc='left')
    plt.show()
