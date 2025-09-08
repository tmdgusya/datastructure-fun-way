

import math


class Heap:
  
  def __init__(self) -> None:
    self.size = 100
    self.last_index = 0
    self.array = [None] * self.size
    
  def _grow(self):
    self.array += [None] * self.size
  
  def insert(self, value: int):
    if self.last_index == len(self.array) - 1:
      self._grow()
    
    self.last_index += 1
    self.array[self.last_index] = value
    
    curr = self.last_index
    parent = math.floor(curr / 2)
    
    while parent >= 1 and self.array[parent] < self.array[curr]:
      tmp = self.array[parent]
      self.array[parent] = self.array[curr]
      self.array[curr] = tmp
      curr = parent
      parent = math.floor(curr / 2)