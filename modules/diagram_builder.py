
import os , errno
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from analyze import analyze
import random

def generate_diagram(emotions: dict):
    """
    Builds a diagram and saves it in directory /diagrams/ as diagram.jpg
    :param emotions: dict with emotions and their values.
    """
    try:
        os.makedirs(os.path.realpath('../modules/static'))
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
    name = '../modules/static/diagram'
    number = str(random.randint(0, 1000000))
    path = name + number + ".jpg"
    plt.savefig(os.path.realpath(path))
    plt.switch_backend('agg')
    return '/static/diagram' + number + ".jpg"


def generate_wordcloud(words):
    """
    Builds a word cloud diagram and saves it in directory /diagrams/ as wordcloud.jpg.
    :param words: list of words to be displayed in the word cloud.
    """
    try:
        os.makedirs(os.path.realpath('../modules/static'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    text = ' '.join(words)
    if len(text) == 0:
        text = 'nothing particular'
    cloud = WordCloud(width=400,
                      height=330,
                      max_words=150,
                      background_color='white',
                      colormap='tab20c',
                      collocations=True).generate_from_text(text)
    plt.figure(figsize=(5,6))
    plt.imshow(cloud)
    plt.axis('off')
    name = '../modules/static/wordcloud'
    number = str(random.randint(0, 1000000))
    path = name + number + ".jpg"
    plt.savefig(os.path.realpath(path))
    plt.switch_backend('agg')
    return '/static/wordcloud' + number + ".jpg"

def create_diagrams(path):
    """
    Builds a diagram and wordcloud and saves it in
    directory /diagrams/ as diagram.jpg and wordcloud.jpg.
    """
    results = analyze(path)
    words = results[1]
    emotions = results[2]
    h = emotions['happy']
    s = emotions['sad']
    f = emotions['fear']
    a = emotions['agressive']
    # if emotions['sad'] != 0:
    #     sad_per = emotions['sad'] / (emotions['happy'] + emotions['sad'] +emotions['agressive'] + emotions['fear'])
    # else:
    #     sad_per = 0
    # if emotions['fear'] != 0:
    #     fear_per = emotions['fear'] / (emotions['happy'] + emotions['sad'] +emotions['agressive'] + emotions['fear'])
    # else:
    #     fear_per = 0
    # if emotions['agressive'] != 0:
    #     agressive_per = emotions['agressive'] / (emotions['happy'] + emotions['sad'] +emotions['agressive'] + emotions['fear'])
    # else:
    #     agressive_per = 0
    path_1 = generate_diagram(emotions)
    path_2 = generate_wordcloud(words)
    if (results[0]) and (s < 0.3 * (h+s+f+a)) and (f < 0.3 * (h+s+f+a)) and (a < 0.3 * (h+s+f+a)):
        msg = "???? ?????????????? ?????????????????????????? ????????????????"
    else: msg = "?????????????????????????????? ??????????"
    return path_1, path_2, msg
