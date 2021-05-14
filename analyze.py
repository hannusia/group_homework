from divide import *
divider = Divider()
text = ""
sentences = divider.div_into_sentences(text)

emotion = sentences.emotion
acceptancy = sentences.acceptancy

sentences.make_dict()
happy_words = sentences.happy_words
sad_words = sentences.sad_words
agressive_words = sentences.agressive_words
fear_words = sentences.fear_words
all_words = set(happy_words.keys())
all_words.update(set(sad_words.keys()))
all_words.update(set(agressive_words.keys()))
all_words.update(set(fear_words.keys()))

# print(emotion, acceptancy, all_words, happy_words)
