https://edabit.com/challenge/nunJurLEibCyn8fzn




A=[1, 2, "a", "b"]

print([x for x in A if type(x)==int])



def filter_list(lst):
    newList = []
    for l in lst:
      if type(l) is int:
      	newList.append(l)


          

def filter_list(lst):
  num_lst =[]
  for item in lst:
    if not type(item) == str:
      num_lst.append(item)
  return num_lst




def filter_list(lst):
  all_num = []
  
  for i in lst:
    if type(i) == int:
      all_num.append(i)
    else:
      pass
  return all_num