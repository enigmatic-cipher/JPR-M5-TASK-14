"""
Given an array of numbers as input, move the negatives numbers to the end of the array. Note that the order of no-negative and negative numbers should be the same. You can create another array to solve this problem.
Input-> [2,-5,4,12,-7,-9,6,3,-10]
Output-> [2,4,12,6,3,-5,-7,-9,-10]
"""

def arr(ls):
  new_list = []
  for i in range(0,len(ls)):
    e = ls[i]
    if e > 0:
      new_list.append(e)
  for j in range(0,len(ls)):
    e1 = ls[j]
    if e1 < 0:
      new_list.append(e1)
  print(new_list)

li = [2,-5,4,12,-7,-9,6,3,-10]
arr(li)