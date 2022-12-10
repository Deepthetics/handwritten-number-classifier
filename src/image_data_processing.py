import numpy as np


def to_array(image):
    """Muuntaa 28x28 -resoluutioisen kuvan vektoriesityksen matriisiesitykseksi plottaamista varten.

    Args:
        image: pandas.Series -luokan olio, joka sisältää kuvadatan.

    Returns:
        array: numpy.ndarray -luokan olio, joka sisältää kuvadatan.
    """

    array = np.empty((28, 28))
    image = image.to_numpy()

    for i, j in enumerate(range(0, 784, 28)):
        array[i,:] = image[j:j+28]

    return array

def extract(df):
    """Purkaa MNIST-datasta kuvat ja niitä vastaavat luokat erilleen.

    Args:
        df: pandas.DataFrame-luokan olio.

    Returns:
        images: pandas.DataFrame -luokan olio, joka sisältää kuvat.
        labels: pandas.Series -luokan olio, joka sisältää kuvia vastaavat luokat.
    """

    images = df.iloc[:,1:]
    labels = df.iloc[:,0]
    return (images, labels)

def to_binary(df):
    """Muuntaa MNIST-datan sisältämät harmaaväriskaalaiset kuvat binääreiksi mustavalkoisiksi
    kuviksi.

    Args:
        df: pandas.DataFrame-luokan olio, joka sisältää harmaaväriskaalaiset kuvat.

    Returns:
        df: pandas.Dataframe -luokan olio, joka sisältää binäärit mustavalkoiset kuvat.
    """

    row_count = len(df.index)
    column_count = len(df.columns)

    for i in range(row_count):
        for j in range(column_count):
            if df.iloc[i, j] > 127:
                df.iat[i, j] = 1
                print(f'Row: {i}')
            else:
                df.iat[i, j] = 0
                print(f'Row: {i}')

    return df
