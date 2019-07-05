mylist=['word1', 'word2', "word3"]

for word in mylist:
    print(word)

f = open("word_list.txt", "r")
all_words = [word.strip() for word in f.readlines()]

print(all_words)