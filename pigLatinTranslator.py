

def pigLatin(word):
	index = first_vowel(word)
	index2 = last_non_letter(word)
	print(index2)

	if index == 0:
		if index2 < 0:
			return word + 'way'
		else:
			return word[:index2] + 'way' + word[index2:]
	else:
		if index2 < 0:
			return word[index:] + word[:index] + 'ay'
		else:
			return word[index:index2] + word[:index] + 'ay' + word[index2:]


def first_vowel(s):
	for i in range(len(s)):
		if s[i] in 'aeiou':
			return i

def last_non_letter(word):
	for i in range(len(word)):
		if word[i] not in 'abcdefghijklmnopqrstuvwxyz':
			return i
	return -1


def pigLatinSentence(sentence):
	words = sentence.split(' ')

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