
import re

# there is a bug.
# If there is a sentence annotate by '', it will recognize the ' as part of the word.

with open(r'C:\Users\12104\OneDrive\desktop\word.txt') as wordfile:
    wordtxt = wordfile.read()
    wordlist = re.split(r"[^a-zA-z\-']+", wordtxt)
    wordlist.remove('')
    worddict = {}
    for word in wordlist:
        worddict[word] = worddict.setdefault(word, 0) + 1
    print(wordlist)
    print(worddict)
    print('the whole word number: %s' % len(worddict))
