import nltk
import numpy as np
from sklearn.preprocessing import normalize

# path = nltk.data.path[0] + "/corpora/brown/brown_100_pos.txt"
# path_tags = nltk.data.path[0] + "/corpora/brown/brown_tags_hw3.txt"
# path_words = nltk.data.path[0] + "/corpora/brown/brown_words_hw3.txt"
# path_toy_corpus = nltk.data.path[0] + "/corpora/brown/toy_pos_corpus.txt"

path = "brown_100_pos.txt"
path_tags = "brown_tags_hw3.txt"
path_words = "brown_words_hw3.txt"
path_toy_corpus = "toy_pos_corpus.txt"
tags_dict = {}
words_dict = {}

with open(path_tags, "r") as tags_file:
	for index, tag in enumerate(tags_file):
		tags_dict[tag.rstrip()] = index

with open(path_words, "r") as words_file:
	for index, word in enumerate(words_file):
		words_dict[word.rstrip()] = index

transition_matrix = np.zeros((len(tags_dict), len(tags_dict)))
emission_matrix = np.zeros((len(tags_dict), len(words_dict)))

with open(path, "r") as text_file:
	for text in text_file:
		split = text.rstrip().lower().split()
		split.append("<end>/<end>")
		previous_tag = "<s>"
		t_col = 0
		t_row = 0
		e_col = 0
		e_row = 0

		for s in split:
			word = s.split("/", 1)[0]
			tag = s.split("/", 1)[1]

			for w, index in words_dict.iteritems():
				if w == word:
					e_col = index

			for t, index in tags_dict.iteritems():
				if t == tag:
					e_row = index
					t_col = index

				if t == previous_tag:
					t_row = index

			transition_matrix[t_row][t_col] += 1
			emission_matrix[e_row][e_col] += 1		
			previous_tag = tag

transition_probs = normalize(transition_matrix, norm='l1', axis=1)
emission_probs = normalize(emission_matrix, norm='l1', axis=1)

with open("emission.txt", "w") as write_file:
	write_file.write(str(emission_probs[tags_dict['nn']][words_dict['weekend']]) + "\n")
	write_file.write(str(emission_probs[tags_dict['np']][words_dict['texas']]) + "\n")
	write_file.write(str(emission_probs[tags_dict['to']][words_dict['to']]) + "\n")
	write_file.write(str(emission_probs[tags_dict['jj']][words_dict['old']]) + "\n")

with open("transition.txt", "w") as write_file:
	write_file.write(str(transition_probs[tags_dict['nn']][tags_dict['nn']]) + "\n")
	write_file.write(str(transition_probs[tags_dict['nn']][tags_dict['.']]) + "\n")
	write_file.write(str(transition_probs[tags_dict['.']][tags_dict['<end>']]) + "\n")
	write_file.write(str(transition_probs[tags_dict['to']][tags_dict['vb']]) + "\n")


with open(path_toy_corpus, "r") as toy_text:
	with open("pos_eval.txt", "w") as write_file:
		for text in toy_text:
			split = text.lower().rstrip().split()
			split.append("<end>/<end>")
			previous_tag = "<s>"
			t_col = 0
			t_row = 0
			e_col = 0
			e_row = 0
			prob = 1

			for s in split:
				word = s.split("/", 1)[0]
				tag = s.split("/", 1)[1]

				for w, index in words_dict.iteritems():
					if w == word:
						e_col = index

				for t, index in tags_dict.iteritems():
					if t == tag:
						e_row = index
						t_col = index

					if t == previous_tag:
						t_row = index

				prob *= transition_probs[t_row][t_col]
				prob *= emission_probs[e_row][e_col]
				previous_tag = tag
		
			write_file.write(str(prob) + "\n")
