#https://edabit.com/challenge/WS6hR6b9EZzuDTD26
#
#Words With Duplicate Letters
#Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
#
#Examples
#no_duplicate_letters("Fortune favours the bold.") ➞ True
#
#no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
#
#no_duplicate_letters("Look before you leap.") ➞ False
## Duplicate letters in "Look" and "before".
#
#no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
## Duplicate letters in "apple", "keeps", "doctor", and "away".
#Notes
#Letter matches are case-insensitive.
#
#
#def no_duplicate_letters(phrase):
#    return not any([len(set(i))!=len(i) for i in phrase.split()])


print(all([1,1, 1, 1]))






















#def no_duplicate_letters(phrase):
#    return not len([i.count(x) for i in phrase.split(" ") for x in i if i.count(x)>1 ]) >1
#
#
#def no_duplicate_letters(phrase):
#    f=[i.count(x) for i in phrase.split(" ") for x in i if i.count(x)>1 ]
#    if len(f)>1:
#        return False
#    else:
#        return True
#    
#def no_duplicate_letters(phrase):
#    l = phrase.split()
#    for word in l:
#        for letter in set(word):
#            if word.count(letter) > 1:
#                return False
#    return True
#
#
#def no_duplicate_letters(phrase):
#    for i in phrase.split(sep=" "):
#        for j in i:
#            if i.count(j) >= 2:
#                return False
#    return True
#
#
#def no_duplicate_letters(phrase):
#	for word in list(phrase.split(" ")):
#		for letter in word:
#			if word.count(letter) > 1:
#				return False
#	return True


