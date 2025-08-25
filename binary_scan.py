
from math import floor
from turtle import up

def binary_scan(arr, target):
  upper_bound = len(arr) - 1
  lower_bound = 0

  while lower_bound < upper_bound:
    median = floor((upper_bound - lower_bound) / 2)
    if target == arr[median]:
      return median
    if target > arr[median]:
      lower_bound = median + 1
    if target < arr[median]:
      upper_bound = median - 1
  
  return -1


def test_binary_scan():
  arr = [1,2,3,4,5]
  target = 1

  assert binary_scan(arr, target) == 0
  
def test_binary_scan2():
  arr = [1,2,3,4,5,6]
  target = 1

  assert binary_scan(arr, target) == 0