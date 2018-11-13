import nltk

path = nltk.data.path[0] + "/corpora/brown/brown_vocab_100.txt"

brown_dict = {}
with open(path, "r") as text_file:
	for index, word in enumerate(text_file):
		brown_dict[word.rstrip()] = index

# print brown_dict
with open("word_to_index_100.txt", "w") as write_file:
	write_file.write(str(brown_dict))
