import nltk
import numpy as np
from sklearn.preprocessing import normalize

path_vocab = nltk.data.path[0] + "/corpora/brown/brown_vocab_100.txt"
path = nltk.data.path[0] + "/corpora/brown/brown_100.txt"
path_toy_corpus = nltk.data.path[0] + "/corpora/brown/toy_corpus.txt"

counts = np.zeros((813,813))
words = []
brown_dict = {}

with open(path_vocab, "r") as text_file:
	for index, word in enumerate(text_file):
		brown_dict[word.rstrip()] = index

with open(path, "r") as text_file:
	for text in text_file:
		split = text.lower().rstrip().split()
		split.append("</s>")
		previous_word = "<s>"
		col = 0
		row = 0
		for s in split:
			for word, index in brown_dict.iteritems():
				if previous_word == word:
					col = index
				if s == word:
					row = index

			counts[col][row] += 1
			previous_word = s

probs = normalize(counts, norm='l1', axis=1)

with open("bigram_probs.txt", "w") as write_file:
	write_file.write(str(probs[brown_dict['all']][brown_dict['the']]) + "\n")
	write_file.write(str(probs[brown_dict['the']][brown_dict['jury']]) + "\n")
	write_file.write(str(probs[brown_dict['the']][brown_dict['campaign']]) + "\n")
	write_file.write(str(probs[brown_dict['anonymous']][brown_dict['calls']]) + "\n")

with open(path_toy_corpus, "r") as toy_text:
	with open("bigram_eval.txt", "w") as write_file:
		for text in toy_text:
			split = text.lower().rstrip("\n").split(" ")
			split.append("</s>")

			sentprob = 1.0
			sent_len = len(split)
			
			previous_word = "<s>"
			col = 0
			row = 0
			for s in split:
				for word, index in brown_dict.iteritems():
					if previous_word == word:
						col = index
					if s == word:
						row = index
					
				previous_word = s
				wordprob = probs[col][row]
				sentprob *= wordprob

			perplexity = 1/(pow(sentprob, 1.0/sent_len))
			write_file.write(str(perplexity) + "\n")
