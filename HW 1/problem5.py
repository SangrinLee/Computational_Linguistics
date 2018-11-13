import re
import nltk

path = nltk.data.path[0] + "/corpora/brown/brown_all.txt"
path = "brown_all.txt"
text_file = open(path, "r")
write_file = open('browncaps.txt', "w")

result = []

for text in text_file:
	split = text.split(" ")
	
	m = re.search(r"(\b[A-Z][a-z0-9'.-]* ).*(\b[A-Z][a-z0-9'.-]* ).*(\b[A-Z][a-z0-9'.-]*\b)", text)

	if m:
		write_file.write(text)
