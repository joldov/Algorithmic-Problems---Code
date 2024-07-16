import math

# func that finds euclidean distance between 2 points
def euclDist(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# def align(seriesA: list[(int, int)], seriesB: list[(int, int)]):
def align(seriesA, seriesB):
    # initializing matrix:
    n = len(seriesA)
    m = len(seriesB)
    # using list comprehension to created 2d list, initializing it w positive infinity bc any other positive number would be less than infinity
    # i.e its useful to find minimum value 
    dp = [[float('inf')] * m for _ in range(n)] 

    # base case: distance from the start to the start is simply the distance between the first points
    dp[0][0] = euclDist(seriesA[0], seriesB[0])

    # filling in the matrix with the min distances:
    for i in range(n):
        for j in range(m):
            if i > 0 or j > 0: #skipping first cell bc we alr set it on line 17
                min_prev_dist = float('inf') 
                if i > 0:
                    min_prev_dist = min(min_prev_dist, dp[i-1][j]) # reach current cell from the top
                if j > 0:
                    min_prev_dist = min(min_prev_dist, dp[i][j-1]) # reach current cell from the left
                if i > 0 and j > 0:
                    min_prev_dist = min(min_prev_dist, dp[i-1][j-1]) #reach current cell diagonally from top-left
                
                # current cells value is dist from current point in A to current point in B + prev min dist
                dp[i][j] = euclDist(seriesA[i], seriesB[j]) + min_prev_dist
    #last point of A must map to last point of B
    return dp[-1][-1]
# seriesA = [(0, 0), (1, 0), (2, 1)]
# seriesB = [(0, 0), (2, 0), (3, 1)]
# print(align(seriesA, seriesB))