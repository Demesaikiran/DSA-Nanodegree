import heapq
from math import pow, sqrt
from collections import namedtuple

cost = namedtuple('Cost', ['total', 'journey', 'to_goal'])
path = namedtuple('Path', ['cost', 'intersections', 'previous', 'frontier'])

def euclidean_distance(origin_point: [float, float], destinaiton_point: [float, float]) -> float:
    """
    Given two poitns origin and destination returns their euclidean distance
    :param origin_point: It's the origin point in the 2D cartesian space
    :param destination_point: IT's the destination point in the 2D cartesian space
    :return: It returns the Euclidean distance between the two points
    """
    
    return sqrt(pow((oringin_point[0] - destination_point[0]), 2) + pow((origin_point[1] - destination_point[1]), 2))


def estimated_distance(path_frontier_point: [float, float], goal_point: [float, float]) -> float:
    




def shortest_path(M,start,goal):
    print("shortest path called")
    return