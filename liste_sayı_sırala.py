
#Given a list of numbers, write a function that returns a list that...
#
#Has all duplicate elements removed.
#Is sorted from least to greatest value.
#Examples
#unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
#
#unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
#
#unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]
#
#return sorted(list(set(lst)))




#ef unique_sort(lst):
#  purgedList = []
#  for i in sorted(lst):
#    if i not in purgedList:
#      purgedList.append(i)
#  return purgedList
#
#
#
#
#
#
#
#  def unique_sort(lst):
#    lst = set(lst)
#    lst = list(lst)
#    lst.sort()
#    return lst
#
#
#
#
#
#    def unique_sort(lst):
#    unique = []
#    for num in lst:
#        if num not in unique:
#            unique.append(num)
#
#    return sorted(unique)