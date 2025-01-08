def binSearchIter(lst, item):
  low = 0
  high = len(lst) - 1

  while low <= high:
    mid = (high + low) // 2
    x = lst[mid]
    
    if x == item:
      return True
    elif x < item:          # Cannot be on left side
      low = mid + 1
    else:                   # x > item, cannot be on right side
      high = mid - 1
  
  return False


def binSearchRecur(lst, item):
  high = len(lst) - 1

  if high < 0:              # The list is empty
    return False
  
  mid = high // 2

  if lst[mid] == item:
    return True
  elif lst[mid] < item:
    # We already know that item is not at mid, so we exclude mid
    return binSearchRecur(lst[mid + 1:], item) 
  else:
    return binSearchRecur(lst[:mid], item) 


l = [1, 4, 5, 6, 8, 9, 10]
print(binSearchIter(l, 4))
print(binSearchRecur(l, 4))