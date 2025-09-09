

import math
from turtle import left


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
      
  def _find_larger_child_index(self, index: int) -> int:
    """주어진 노드의 자식 중 더 큰 값을 가진 자식의 인덱스를 반환"""
    left_child = index * 2
    right_child = index * 2 + 1
    largest = index
    
    # 왼쪽 자식이 존재하고 현재 노드보다 크면
    if left_child <= self.last_index and self.array[left_child] > self.array[largest]:
      largest = left_child
    
    # 오른쪽 자식이 존재하고 현재 largest보다 크면
    if right_child <= self.last_index and self.array[right_child] > self.array[largest]:
      largest = right_child
    
    return largest
  
  def _heapify_down(self, index: int):
    """아래쪽으로 힙 속성을 복원하는 메서드"""
    while True:
      largest = self._find_larger_child_index(index)
      
      # 현재 노드가 이미 가장 크면 종료
      if largest == index:
        break
      
      # 더 큰 자식과 교환
      self.array[index], self.array[largest] = self.array[largest], self.array[index]
      index = largest
    
  def delete(self, index: int) -> bool:
    """특정 인덱스의 노드를 삭제"""
    # 유효성 검사
    if index < 1 or index > self.last_index:
      return False
    
    # 삭제할 노드가 마지막 노드인 경우
    if index == self.last_index:
      self.array[self.last_index] = None
      self.last_index -= 1
      return True
    
    # 마지막 노드의 값을 삭제할 위치로 이동
    self.array[index] = self.array[self.last_index]
    self.array[self.last_index] = None
    self.last_index -= 1
    
    # 힙이 비어있으면 종료
    if self.last_index == 0:
      return True
    
    # 부모와 비교해서 위로 올라가야 하는지 확인
    parent = math.floor(index / 2)
    if parent >= 1 and self.array[index] > self.array[parent]:
      # 위로 올라가는 heapify (insert와 동일한 로직)
      curr = index
      while parent >= 1 and self.array[parent] < self.array[curr]:
        self.array[parent], self.array[curr] = self.array[curr], self.array[parent]
        curr = parent
        parent = math.floor(curr / 2)
    else:
      # 아래로 내려가는 heapify
      self._heapify_down(index)
    
    return True
  
  def delete_root(self):
    """루트 노드(최대값)를 삭제하고 반환"""
    if self.last_index == 0:
      return None
    
    root_value = self.array[1]
    self.delete(1)
    return root_value
  
  def peek(self):
    """루트 노드(최대값)를 반환 (삭제하지 않음)"""
    if self.last_index == 0:
      return None
    return self.array[1]
    