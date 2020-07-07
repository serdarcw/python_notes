Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis.
You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter of the sentence


word = input("Enter a sentance :")
word_list = list(word)
word_count = {}
for letter in word_list:
    if letter in word_count.keys():
        word_count.update({letter:word_count[letter]+1})
    else:
        word_count.update({letter:1})
print(word_count)