import math
from pprint import pprint 
"""
K-d tree

Every non-leaf node can be thought of as implicitly generating a splitting hyperplane that divides the space into two parts.


point = (x, y)
k = 2
"""

def kdtree(points, depth, k):
	if len(points) == 0:
		return None
	axis = depth % k

	sort = sorted(points, key=lambda x:x[axis]) 
	mid = len(points) // 2 

	median = sort[mid]

	return {
		"location": median,
		"leftChild": kdtree(sort[:mid], depth + 1, k),
		"rightChild": kdtree(sort[mid+1:], depth + 1, k)
	}

points = [
	(0, 0),
	(1, 0),
	(2, 2)
]

pprint(kdtree(points, 0, 2))
