
def linear_scan(arr, target):
  for i, v in enumerate(arr):
    print(i, v, )
    if v == target:
      return i 
    
  return -1
  
def test_linear_scan():
  arr = [1, 2, 3, 4, 5]
  target = 5
  
  index = linear_scan(arr, target)
  
  assert index is 4
  
def test_linear_scan2():
  arr = [1, 2, 3, 4, 5]
  target = 6
  
  index = linear_scan(arr, target)
  
  assert index is -1