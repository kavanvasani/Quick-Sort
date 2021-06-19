def quick_sort(some):
  n = len(some)
  if n <= 1:
    return some
  else:
    pivot = some.pop()

  greater = []
  lesser = []

  for i in some:
    if i > pivot:
      greater.append(i)
    else:
      lesser.append(i)
  
  return quick_sort(lesser) + [pivot] + quick_sort(greater)


print('***Enter a letter to end list***\nEnter the list:')
try:

  new = []

  while True:
    new.append(int(input()))

except:
  pass

#ll1 = [5,4,3,7,1,9,2]
print('Sorted list is : ', quick_sort(new))

#print(f'Sorted list is : {new}')