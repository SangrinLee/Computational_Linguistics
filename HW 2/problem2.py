import nltk
import numpy as np

path_vocab = nltk.data.path[0] + "/corpora/brown/brown_vocab_100.txt"
path = nltk.data.path[0] + "/corpora/brown/brown_100.txt"
path_toy_corpus = nltk.data.path[0] + "/corpora/brown/toy_corpus.txt"

counts = np.zeros(813)
words = []
brown_dict = {}

with open(path_vocab, "r") as text_file:
	for index, word in enumerate(text_file):
		brown_dict[word.rstrip()] = index

with open(path, "r") as text_file:
	for text in text_file:
		split = text.lower().rstrip().split()
		split.append("</s>")

		for word, index in brown_dict.iteritems():
			for s in split:
				if word == s:
					counts[index] += 1
		
probs = counts / np.sum(counts)

with open("unigram_probs.txt", "w") as write_file:
	write_file.write(str(probs))

with open(path_toy_corpus, "r") as toy_text:
	with open("unigram_eval.txt", "w") as write_file:
		for text in toy_text:
			split = text.lower().rstrip("\n").split(" ")
			split.append("</s>")

			sentprob = 1.0
			sent_len = len(split)
			for s in split:
				wordprob = probs[brown_dict[s]]
				sentprob *= wordprob
			
			perplexity = 1/(pow(sentprob, 1.0/sent_len))
			write_file.write(str(perplexity) + "\n")
