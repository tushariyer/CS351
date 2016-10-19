import requests
import threading

# Read keywords into a list stripping newlines
keywords = [keyword.rstrip('\n') for keyword in open('keywords.txt')]
fileOpen = open("output.txt", "a")
for k in keywords:
	fileOpen.write("@ATTRIBUTE\t" + k +  "\tNUMERIC\n")
fileOpen.write("\n\n")
fileOpen.close()


# Read URLs into a list stripping newlines
urls = [url.rstrip('\n') for url in open('links.txt')]


def processKeywords(inUrl):
	print inUrl
	matrix = []
	outputMatrix = []
	r = requests.get(inUrl)
	for word in keywords:
		if word in r.text:
			matrix.insert(0, (word, 1))
			outputMatrix.insert(0, '1');
		else:
			matrix.insert(0, (word, 0))
			outputMatrix.insert(0, '0');
	# print matrix
	fileOpen = open("output.txt", "a")
	outstr = ','.join(outputMatrix)
	fileOpen.write(outstr + "," + inUrl + "\n")
	fileOpen.close()
    

for url in urls:
	processKeywords(url)