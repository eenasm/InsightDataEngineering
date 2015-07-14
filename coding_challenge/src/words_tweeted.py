#!/usr/bin/env python

import sys

try:
	# specify input and output files from command line 
	infile = sys.argv[1]
	outfile = sys.argv[2]
except IndexError:
	# default value for input and output files
	infile = "./tweet_input/tweets.txt"
	outfile = "./tweet_output/ft1.txt"

# open input file for reading
tweetfile = open(infile,"r")

# initialize dictionary for word count
wordcount = {}

# read and count words per tweet, assuming one tweet per line
for line in tweetfile:
	for word in line.split():
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] +=1
tweetfile.close

# sort words in dictionary
sortedwords = sorted(wordcount)

# write sorted words with corresponding word count to outfile
ft1 = open(outfile,"w")
for word in sortedwords:
	ft1.write( "%s\t\t\t%d\n" % ( word, wordcount[word]) )
ft1.close
