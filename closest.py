import math

# func that finds euclidean distance between 2 points
def euclDist(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# helper func to find the minimum distance in the strip
def stripClosest(strip, d):
    # this function will find the minimum distance in the strip where d is the minimum distance calculated so far
    min_dist = d  # initializing
    strip.sort(key=lambda point: point[1])  # sort the strip according to the y coordinate

    # loop through the strip and check for closer points. this is a linear operation
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] < min_dist:
                dist = euclDist(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist # set that to be new min distance
    return min_dist

# recursive func to find the minimum distance
def closestUtil(points):
    # if there are 2 or 3 points, use the brute force method
    if len(points) <= 3:
        return bruteForce(points)
    
    # find middle point
    mid = len(points) // 2
    midPoint = points[mid]

    # consider the vertical line passing through the middle point
    # calculate the smallest distance dl on left of middle point and dr on right side
    dl = closestUtil(points[:mid])
    dr = closestUtil(points[mid:])

    # find the smaller of two distances
    d = min(dl, dr)

    # build an array strip[] that contains points close to the line passing through the mid point
    strip = [p for p in points if abs(p[0] - midPoint[0]) < d]

    # find the closest points in strip. Return the minimum of d and closest distance in strip[]
    return min(d, stripClosest(strip, d))

# the main function that finds the smallest distance
def minimum_distance(points):
    points.sort(key=lambda point: point[0])  # sort the points based on the x coordinate
    return closestUtil(points)

# brute force func that calculates distance between all pairs (for small points array)
def bruteForce(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclDist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist


#points = [(0, 0), (2, 2.5), (3, 1.5), (1, 1)]
#min_dist = minimum_distance(points)
#print(f"Minimum Euclidean distance is: {min_dist}")
