

class Queue():
  
  def __init__(self) -> None:
    self.arr = [None] * 10
    self.front = 0
    self.back = 0
  
  def dequeue(self):
    ele = None
    if self.back > self.front: 
      ele = self.arr[self.front]
      self.front += 1
    
    return ele
  
  
  def enqueue(self, ele):
    if self.back >= len(self.arr):
      self.arr += ([None] * len(self.arr))
    
    self.arr[self.back] = ele
    self.back += 1
    return None


def test_queue():
  
  queue = Queue()
  arr = [1,2,3,4,5,6,7,8,9,10,11]

  for ele in arr:
    queue.enqueue(ele)
  
  for ele in arr:
    assert ele == queue.dequeue()
  