from typing import Tuple

def euclidean_distance(
        pos_1 : Tuple[float, float],
        pos_2 : Tuple[float, float]
        ) -> float:
    distance_2 = (pos_1[0] - pos_2[0])**2 + (pos_1[1] - pos_2[1])**2
    return distance_2