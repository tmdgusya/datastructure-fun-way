import pytest

def string_equal(s1: str, s2: str):
  l1 = len(s1)
  l2 = len(s2)
  
  if l1 != l2:
    return False
  
  for i in range(l1):
    if s1[i] != s2[i]:
      return False
    
  return True

def test_raise_error_for_size():
  """When to stop iteration if the size of both are not the same
  """
  s1 = "hello"
  s2 = "h3"
  
  result = string_equal(s1, s2)

  assert result == False

def test_equality():
  s1 = "hello"
  s2 = "hello"

  result = string_equal(s1, s2)

  assert result == True


def test_equality2():
  s1 = "hello, world"
  s2 = "hellu, world"
  
  assert string_equal(s1, s2) == False