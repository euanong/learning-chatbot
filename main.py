from chatbot import respond
from dbutils import store
import sys

#corpus = [[["do","you","like","fish"],["yes","i","like","fish"]], [["i","hate","potatoes"],["no","i","dont"]],[["i", "have", "to", "go", "to", "the", "bathroom"], ["you", "drink", "too", "much", "coffee"]], [["you", "drink", "too", "much", "coffee"], ["but", "i", "love", "coffee"]], [["but", "i", "love", "coffee"], ["well", "its", "your", "life"]], [["well", "its", "your", "life"], ["you", "eat", "too", "much", "chocolate"]], [["you", "eat", "too", "much", "chocolate"], ["i", "dont", "think", "so"]], [["i", "dont", "think", "so"], ["have", "you", "looked", "in", "the", "mirror"]], [["have", "you", "looked", "in", "the", "mirror"], ["do", "you", "think", "im", "getting", "fat"]], [["do", "you", "think", "im", "getting", "fat"], ["i", "didnt", "say", "that"]], [["i", "didnt", "say", "that"], ["what", "did", "you", "say"]], [["what", "did", "you", "say"], ["i", "said", "i", "have", "to", "go", "to", "the", "bathroom"]]]
#stored as words in array
#corpus [[[a],[b],[id]],[[c],[d],[id]]]
#corp {}
#olddict: dictionary = [["do",1],["you",1],["like",2],["fish",2],["yes",1],["i",3],["hate",1],["potatoes",1],["no",1],["dont",1]]
#dictionary = [['do', 1], ['you', 11], ['like', 2], ['fish', 2], ['yes', 1], ['i', 12], ['hate', 1], ['potatoes', 1], ['no', 1], ['dont', 3], ['have', 4], ['to', 4], ['go', 2], ['the', 4], ['bathroom', 2], ['drink', 2], ['too', 4], ['much', 4], ['coffee', 4], ['but', 2], ['love', 2], ['well', 2], ['its', 2], ['your', 2], ['life', 2], ['eat', 2], ['chocolate', 2], ['think', 4], ['so', 2], ['looked', 2], ['in', 2], ['mirror', 2], ['do', 1], ['im', 2], ['getting', 2], ['fat', 2], ['do', 1], ['didnt', 2], ['say', 4], ['that', 2], ['what', 2], ['did', 2], ['said', 1]]
#filecorpus: [corpus,lastid (this is last id used),corpfull]
#filedict: [dictarr]
def quit():
	print "Saving corpus..."
	picklecorpus = []
	picklecorpus.append(corpus)
	picklecorpus.append(fullcorp)
	picklecorpus.append(lastid)
	store.pickle(filecorpus,picklecorpus)
	print "Saved"
	print "Saving dict..."
	pickledict = []
	pickledict.append(dictionary)
	store.pickle(filedict,pickledict)
	print "Saved"
	print "Goodbye"


#CONFIG
filecorpus = "db/corpus.pkl"
filedict = "db/dict.pkl"

corparr = store.unpickle(filecorpus)
if corparr != False:
	lastid = corparr[2]
	corpus = corparr[0]
	fullcorp = corparr[1]
else:
	corpus = [[["hello"],["hi"],0],[["hi"],["hello"],1]]
	lastid = 1
	fullcorp = {0:["Hello","Hi"],1:["Hi","Hello"]}


dictarr = store.unpickle(filedict)
if dictarr != False:
	dictionary = dictarr[0]
else:
	dictionary = [["hello",2],["hi",2]]


while True:
	print corpus
	print dictionary
	responder = respond.Responder(corpus,dictionary)
	sentence = sys.stdin.readline()
	sentence = responder.listify(sentence)
	if sentence[0] == "quit":
		quit()
		break
	sentence = responder.response(sentence)
	sentid = sentence[0][2]
	print fullcorp[sentid][1]