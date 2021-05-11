import matplotlib.pyplot as plt
import text2emotion as te


def analyzer(text):
    emotions = te.get_emotion(text)
    labels = emotions.keys()
    sizes = emotions.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, normalize=True)
    ax1.axis('equal')
    plt.show()
    return emotions

if __name__ == '__main__':
    print(analyzer("I was asked to sign a third party contract a week out from stay."
                   " If it wasn't an 8 person group that took a lot of wrangling "
                   "I would have cancelled the booking straight away. Bathrooms "
                   "- there are no stand alone bathrooms. Please consider this -"
                   " you have to clear out the main bedroom to use that bathroom."
                   " Other option is you walk through a different bedroom to get "
                   "to its en-suite. Signs all over the apartment - there are signs"
                   " everywhere - some helpful - some telling you rules. Perhaps "
                   "some people like this but It negatively affected our enjoyment"
                   " of the accommodation. Stairs - lots of them - some had slightly"
                   " bending wood which caused a minor injury."))