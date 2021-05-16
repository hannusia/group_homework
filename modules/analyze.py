from divide import *
from read_files import read_input
def analyze(path: str):
    divider = Divider()
    text = read_input(path)
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
    return emotion, acceptancy, all_words, {'happy': len(happy_words), 'sad': len(sad_words), 'agressive': len(agressive_words), 'fear': len(fear_words)}
print(analyze('text.txt'))