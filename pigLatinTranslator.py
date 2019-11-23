	newSentence = ''

	for i in range(len(words)):
		word = pigLatin(words[i])

		if i < len(words) - 1:
			newSentence += word + ' '
		else:
			newSentence += word

	return newSentence



#test run
test = ['a','latin','stupid','eat','the small brown dog jumps over the lazy fox', 'it was the best of times,,,, it was the worst of times!'] #should print away, atinlay, upidstay, eatway

for i in range(len(test)):
	print(pigLatinSentence(test[i]))