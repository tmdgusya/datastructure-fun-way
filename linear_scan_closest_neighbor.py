
import dis
from typing import Callable, List


def linear_scan_closest_neighbor(array: List[int], target: int, dist: Callable[[int, int], int]) -> int:
  if len(array) == 0:
    return -1

  candidate = array[0]
  closest_distance = dist(target, candidate)  
  
  for neighbor in array[1:]:
    distance = dist(target, neighbor)
    
    if distance < closest_distance:
      closest_distance = distance
      candidate = neighbor
  
  return candidate