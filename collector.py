import requests
import threading

# Read keywords into a list stripping newlines
keywords = [keyword.rstrip('\n') for keyword in open('keywords.txt')]
print keywords

# Read URLs into a list stripping newlines
urls = [url.rstrip('\n') for url in open('urls.txt')]
print urls

def processKeywords(inUrl):
    matrix = []
    r = requests.get(inUrl)
    for word in keywords:
        if word in r.text:
            matrix.insert(0, (word, 1))
        else:
            matrix.insert(0, (word, 0))
    print matrix
    

for url in urls:
    processKeywords(url)
    t = threading.Thread(target=processKeywords, args=(url,))
