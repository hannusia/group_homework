
import os , errno
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from analyze import analyze


def generate_diagram(emotions: dict):
    """
    Builds a diagram and saves it in directory /diagrams/ as diagram.jpg
    :param emotions: dict with emotions and their values.
    """
    try:
        os.makedirs(os.path.realpath('../diagrams'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    entries_to_remove = []
    for i in emotions.keys():
        if emotions[i] == 0.0:
            entries_to_remove.append(i)
    for i in entries_to_remove:
        emotions.pop(i, None)
    labels = emotions.keys()
    sizes = emotions.values()
    patches, texts, a = plt.pie(sizes,
                                autopct='%1.1f%%',
                                startangle=90,
                                normalize=True)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.savefig(os.path.realpath('../diagrams/diagram.jpg'))


def generate_wordcloud(words):
    """
    Builds a word cloud diagram and saves it in directory /diagrams/ as wordcloud.jpg.
    :param words: list of words to be displayed in the word cloud.
    """
    try:
        os.makedirs(os.path.realpath('../diagrams'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    text = ' '.join(words)
    cloud = WordCloud(width=400,
                      height=330,
                      max_words=150,
                      background_color='white',
                      colormap='tab20c',
                      collocations=True).generate_from_text(text)
    plt.figure(figsize=(5,6))
    plt.imshow(cloud)
    plt.axis('off')
    plt.savefig(os.path.realpath('../diagrams/wordcloud.jpg'))


def create_diagrams(path):
    """
    Builds a diagram and wordcloud and saves it in
    directory /diagrams/ as diagram.jpg and wordcloud.jpg.
    """
    results = analyze(path)
    words = results[2]
    emotions = results[3]
    generate_diagram(emotions)
    generate_wordcloud(words)
