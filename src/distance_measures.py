from calculation_utilities import generate_coordinates_by_distance
from image_data_processing import to_array


COORDINATES_BY_DISTANCE = generate_coordinates_by_distance()

def distance_d6(image1, image2):
    point_count = 0
    aux_sum = 0

    image1 = to_array(image1)
    image2 = to_array(image2)

    for i in range(0, 28):
        for j in range(0, 28):

            if image1[i, j] == 0:
                point_count += 1

                for x, y, distance in COORDINATES_BY_DISTANCE[(i, j)]:

                    if image2[x, y] == 0:
                        aux_sum += distance
                        break

    return 1/point_count*aux_sum

def distance_d6_mod(image1, image2):
    point_count = 0
    aux_sum = 0

    image1 = to_array(image1)
    image2 = to_array(image2)

    for i in range(0, 28):
        for j in range(0, 28):

            if image1[i, j] == 0:
                point_count += 1

                for x, y, distance in COORDINATES_BY_DISTANCE[(i, j)]:

                    if image2[x, y] == 0:
                        aux_sum += distance
                        break

    return aux_sum

def distance_f2(distance1, distance2):
    return max(distance1, distance2)

def distance_f3(distance1, distance2):
    return (distance1+distance2)/2

def distance_d22(image1, image2):
    distance1 = distance_d6(image1, image2)
    distance2 = distance_d6(image2, image1)
    return distance_f2(distance1, distance2)

def distance_d23(image1, image2):
    distance1 = distance_d6(image1, image2)
    distance2 = distance_d6(image1, image2)
    return distance_f3(distance1, distance2)

def distance_d23_mod(image1, image2):
    distance1 = distance_d6_mod(image1, image2)
    distance2 = distance_d6_mod(image1, image2)
    return distance_f3(distance1, distance2)
