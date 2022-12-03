import numpy as np
import pandas as pd

def distance_d6(points1, points2):
    # NOTE: Laske etäisyys lähimpään samanväriseen (musta tai valkoinen) pisteeseen
    n = 784
    distance = np.sum(np.abs(points1-points2))

    return 1/n*distance

def distance_d6_mod(points1, points2):
    pass

def distance_f2(distance1, distance2):
    return max(distance1, distance2)

def distance_f3(distance1, distance2):
    return (distance1+distance2)/2

def distance_d22(points1, points2):
    distance1 = distance_d6(points1, points2)
    distance2 = distance_d6(points2, points1)
    return distance_f2(distance1, distance2)

def distance_d23(points1, points2):
    distance1 = distance_d6(points1, points2)
    distance2 = distance_d6(points2, points1)
    return distance_f3(distance1, distance2)

def distance_d23_mod(points1, points2):
    distance1 = distance_d6_mod(points1, points2)
    distance2 = distance_d6_mod(points2, points1)
    return distance_f3(distance1, distance2)
