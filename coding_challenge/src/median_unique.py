#!/usr/bin/env python

import sys
import numpy

try: 
	# command line to specify input and output files
	infile = sys.argv[1]
	outfile = sys.argv[2]
except IndexError:
	# default input and output files
	infile = "./tweet_input/tweets.txt"
	outfile = "./tweet_output/ft2.txt"

# read tweets.txt file

# open input file for reading and output file for writing
tweetfile = open(infile,"r")
ft2 = open(outfile,"w")

# initialize list for unique word count per tweet
unique_word_cnt = []

# read each tweet in tweet file, assuming one tweet per line 
for line in tweetfile:
	# initialize dictionary for word count
	wordcount = {}

	# count words in line 
	for word in line.split():
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] +=1
	unique_word = len(wordcount)

	# append unique word count to list of word counts per tweet
	unique_word_cnt.append(unique_word)

	# calculate running median and write to output file
	median_unique = numpy.median(unique_word_cnt)
	ft2.write(str(median_unique) + '\n')
tweetfile.close
ft2.close
