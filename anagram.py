f = open("word_list.txt", "r")
all_words = [word.strip() for word in f.readlines()]

words = "complicated"


def count_letters(word):
    pass

def is_anagram(word1, word2):
    pass

counter_dict ={"a":0, "b":0, "c":0, "d":0, "e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,
        "r": 0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}

for letter in words:
    print(letter)
    counter_dict[letter] += 1

print(counter_dict)
