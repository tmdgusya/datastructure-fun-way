
class Stack():
  
  def __init__(self, size) -> None:
    self.size = size
    self.top: int = -1
    self.array = [None] * size
  
  
  def push(self, ele) -> bool:
    if self.top == (self.size - 1):
      self.size = self.size * 2
      self.array = self.array + ([None] * (self.size * 2))
    
    self.top = self.top + 1
    self.array[self.top] = ele
    return True
  
  def is_empty(self) -> bool:
    return self.top == -1
  
  def pop(self):
    value = None
    if self.top > -1:
      value = self.array[self.top]
      self.top = self.top - 1
    return value

  
def test_stack():
  
  arr = [1,2,3,4,5]
  stack = Stack(len(arr))

  answer_set = [5,4,3,2,1,None]

  for ele in arr:
    stack.push(ele)

  for ele in answer_set:
    assert ele == stack.pop()

  
  