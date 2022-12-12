from math import sqrt


def euclidean_distance(a, b):
    """Laskee euklidisen etäisyyden kahden pisteen välillä.

    Args:
        a: (x, y)-koordinaatti (tuple).
        b: (x, y)-koordinaaatti (tuple).

    Returns:
        distance: euklidinen etäisyys (int).
    """

    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def generate_coordinates_by_distance():
    """Generoi dictionaryn, jonka avaimina ovat 28x28-resoluutioisten kuvien koordinaatit
     ja arvoina listat, jotka sisältävät kuvan muut koordinaatit sekä niihin lasketut etäisyydet
     avaimena olevasta koordinaatista järjestettynä etäisyyden mukaan pienimmästä suurimpaan.
     Kyseinen tietorakenne luodaan modifioidun Hausdorff -etäisyyden laskemisen tehostamista varten.

     Returns:
        coordinates_by_distances: dictionary, jossa avaimet muotoa (x, y) ja arvot muotoa [(x1, y1, etäisyys), ..., (x784, y784, etäisyys)].
    """

    coordinates_by_distance = {}

    for x1 in range(0, 28):
        for y1 in range(0, 28):
            coordinate_distances = []

            for x2 in range(0, 28):
                for y2 in range(0, 28):
                    coordinate_distances.append((x2, y2, euclidean_distance((x1, y1), (x2, y2))))

            coordinate_distances.sort(key=lambda x: x[2])
            coordinates_by_distance[(x1, y1)] = coordinate_distances

    return coordinates_by_distance
