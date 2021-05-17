from divide import *
from read_files import read_input
def analyze(path: str):
    divider = Divider()
    text = read_input(path)
    sentences = divider.div_into_sentences(text)
    sentences.make_summary()
    return sentences.acceptancy, sentences.emotional_words, \
    {'happy': sentences.happy_coef, 'sad': sentences.sad_coef, 'agressive': sentences.agressive_coef,
     'fear': sentences.fear_coef}
