from turtle import reset
import pytest

def insertion_sort(arr):
  size = len(arr)
  i = 1

  while i < size:
    current = arr[i]
    j = i - 1
    while j >= 0 and current < arr[j]:
      arr[j + 1] = arr[j]
      j = j - 1
      
    arr[j + 1] = current
    i = i + 1

  return arr
    
def test_insertion_sort_1():
  arry = [61, 82, 67, 4, 98, 20, 37, 85]

  result = insertion_sort(arry)

  print(result)

  assert result[0] == 4
  