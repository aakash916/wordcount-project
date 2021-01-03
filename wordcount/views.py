from django.http import HttpResponse
from django.shortcuts import render 
import operator


def home(request):
	return render(request, 'home.html') 

def eggs(request):
	return HttpResponse('<h2>EggS!!!</h2>') 

def count(request):
	fulltext= request.GET['fulltext']
	wordlist = fulltext.split()
	wordDict = {}

	for word in wordlist:
		if word not in wordDict.keys():
			wordDict[word] = 1
		else:
			wordDict[word] += 1

	sortedwords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords}) 


def about(request):
	return HttpResponse('<h2>Welcome to my site!</h2>')