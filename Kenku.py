phrase = ''
coppendium = [line.rstrip('\n') for line in open("kenku.txt")]

while(phrase != 'stop'):
	speakable = True
	phrase = raw_input('Enter desired sentence:')
	speech = phrase.split()
	unknown_words = []	
	for word in speech:
		if word not in coppendium: 
			speakable = False
			unknown_words.append(word)
	if(speakable):
		print("Can speak that phrase")
	else:
		print("Cannot speak that phrase due to:")
		print(unknown_words)
		




		


