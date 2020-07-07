Test.assert_equals(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]), 5)
Test.assert_equals(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]), 10)
Test.assert_equals(missing_num([7, 2, 3, 9, 4, 5, 6, 8, 10]), 1)
Test.assert_equals(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]), 7)
Test.assert_equals(missing_num([1, 7, 2, 4, 8, 10, 5, 6, 9]), 3)

#1 den 10 a kadar olan listede çıkarılan sayıyı bulma

def missing_num(lst):lst = input()
  return 55 - sum(lst)




#benim çözümüm
  def missing_num(lst):
	count = 0
	for i in lst:
		count += i
	return (55-count)
