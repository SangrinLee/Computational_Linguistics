import numpy as np

# path_vocab = "/sscc/home/k/kob734/hw4materials/vocab.txt"
# path_lm = "/sscc/home/k/kob734/hw4materials/lm.txt"
# path_noise = nltk.data.path[0] + "/sscc/home/k/kob734/hw4materials/noise.txt"
path_vocab = "vocab.txt"
path_lm = "lm.txt"
path_noise = "noise.txt"

vocab_dict = {}
vocab_reverse_dict = {}
lm_dict = {}
noise_dict = {}

with open(path_vocab, "r") as text_file:
	for index, word in enumerate(text_file):
		vocab_dict[word.rstrip()] = index
		vocab_reverse_dict[index] = word.rstrip()

langprobs = np.zeros(len(vocab_dict))
noiseprobs = np.zeros(len(vocab_dict))

with open(path_lm, "r") as lm_file:
	for index, word, in enumerate(lm_file):
		langprobs[vocab_dict[word.split("\t")[0]]] = word.rstrip().split("\t")[1]

with open(path_noise, "r") as noise_file:
	for index, word, in enumerate(noise_file):
		noiseprobs[vocab_dict[word.split("\t")[0]]] = word.rstrip().split("\t")[1]

unnorm_posterior = langprobs * noiseprobs
posterior = unnorm_posterior / np.sum(unnorm_posterior)
max_idx = np.argmax(posterior)
result = np.where(posterior > 0.05)[0]

print vocab_reverse_dict[max_idx]
print posterior[max_idx]
for i in result:
	print i, vocab_reverse_dict[i], posterior[i]
