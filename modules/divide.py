from read_files import *
emotional_words = read_emotions('positive.tsv')
sad_words = read_emotions('negative.tsv')
emotional_words.update(sad_words)
stopwords = read_stopwords('stopwords.txt')
cusswords_en = read_stopwords('cusswords.txt')


class Divider:
    """
    Helper class which can divide text into sentences and sentence into words.
    """

    def __init__(self) -> None:
        pass

    def div_into_sentences(self, text):
        """
        return Text object - linked list with sentences from given text.
        """
        from nltk.tokenize import sent_tokenize
        sentences = TextADT(self.detect_language(text))
        for sentence in sent_tokenize(text):
            new_sent = Sentence(sentence, sentences.lang)
            sentences.add(new_sent)
        sentences.emotion = sentences.count_emotion()
        sentences.acceptancy = sentences.is_aceptable()
        return sentences

    def div_into_words(self, sentence) -> list:
        """
        return list with all words from given sentence
        """
        import re
        sentence = re.sub('[^а-яіa-z ]', '', sentence)
        words = sentence.split(' ')
        return words

    def detect_language(self, text: str):
        for i in text:
            if i.isalpha():
                if 97 <= ord(i.lower()) <= 122:
                    return 'en'
        return 'ua'


class Node:
    """
    Helper class - node for TextADT.
    """

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data.text)


class TextADT:
    """
    Linked list to keep text.
    """

    def __init__(self, lang: str) -> None:
        self.head = None
        self.lang = lang
        self.emotion = 0
        self.acceptancy = True
        self.happy_words = {}
        self.sad_words = {}
        self.agressive_words = {}
        self.fear_words = {}

    def empty(self) -> bool:
        """
        Check if linked list is empty.
        """
        return self.head == None

    def add(self, value):
        NewNode = Node(value)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while laste.next:
            laste = laste.next
        laste.next = NewNode

    def __repr__(self) -> str:
        """
        Return sring representation of TextADT.
        """
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data.text)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        list_item = self.head
        while list_item is not None:
            yield list_item
            list_item = list_item.next

    def __len__(self):
        counter = 0
        for i in self:
            counter += 1
        return counter

    def count_emotion(self) -> float:
        result = 0
        for sentence in self:
            result += sentence.data.emotion
        if len(self) != 0:
            return round(result/len(self), 2)
        return 0

    def is_aceptable(self):
        for sentence in self:
            if sentence:
                if not sentence.data.acceptancy:
                    return False
        return True

    def make_dict(self):
        curr = self.head
        self.happy_words = curr.data.happy_words
        self.sad_words = curr.data.sad_words
        self.agressive_words = curr.data.agressive_words
        self.fear_words = curr.data.fear_words
        curr = curr.next
        while curr is not None:
            self.happy_words.update(curr.data.happy_words)
            self.sad_words.update(curr.data.sad_words)
            self.agressive_words.update(curr.data.agressive_words)
            self.fear_words.update(curr.data.fear_words)
            curr = curr.next


class Sentence:
    STOPWORDS = stopwords
    EMOTIONAL_WORDS = emotional_words
    FORBIDDEN_WORDS = {}

    def __init__(self, text: str, lang: str):
        self.lang = lang
        if lang == 'en':
            self.FORBIDDEN_WORDS = cusswords_en
        self.text = text.lower()
        self.sentiment = self.find_sentiment(text)
        self.words = self.clean_words()
        self.acceptancy = self.is_aceptable()
        self.emotion = self.count_emotion() * self.sentiment
        self.happy_words = {}
        self.sad_words = {}
        self.agressive_words = {}
        self.fear_words = {}
        self.make_dict()

    def find_sentiment(self, text):
        if text[-1] == '!':
            sentiment = 1.2
        elif text[-1] in {'?', '...'}:
            sentiment = 1.1
        else:
            sentiment = 1
        return sentiment

    def clean_words(self) -> list:
        """
        Return list with normalized words from sentence
        and without stopwords.
        """
        all_words = Divider().div_into_words(self.text)
        words = []
        if self.lang == 'ua':
            import pymorphy2
            morph = pymorphy2.MorphAnalyzer(lang='uk')
            all_words = list(map(lambda x: morph.parse(x)
                                 [0].normal_form, all_words))
            all_words = list(
                filter(lambda x: x not in self.STOPWORDS, all_words))
            for i in range(len(all_words)):
                if all_words[i] == 'не':
                    if i < len(all_words) - 1:
                        if all_words[i+1] in self.EMOTIONAL_WORDS:
                            tpl = self.EMOTIONAL_WORDS[all_words[i+1]]
                            words.append(
                                Word(all_words[i+1], tpl[0], tpl[1]).reverse())
                else:
                    if all_words[i] in self.EMOTIONAL_WORDS:
                        tpl = self.EMOTIONAL_WORDS[all_words[i]]
                        words.append(Word(all_words[i], tpl[0], tpl[1]))
        else:
            from nltk.sentiment import SentimentIntensityAnalyzer
            import text2emotion as te
            analyzer = SentimentIntensityAnalyzer()
            for i in range(len(all_words)):
                val = analyzer.polarity_scores(all_words[i])['compound'] * 2
                if val != 0:
                    dct = te.get_emotion(all_words[i])
                    if dct['Happy'] != 0.0:
                        words.append(Word(all_words[i], val, 'h'))
                    elif dct['Angry'] != 0.0:
                        words.append(Word(all_words[i], val, 'a'))
                    elif dct['Sad'] != 0.0:
                        words.append(Word(all_words[i], val, 's'))
                    elif dct['Fear'] != 0.0:
                        words.append(Word(all_words[i], val, 'f'))
                    else:
                        words.append(Word(all_words[i], val, 'i'))
        return words

    def __str__(self):
        """
        Return string representation of sentence.
        """
        result = ''
        for word in self.words:
            result += str(word) + '\n'
        return result

    def is_aceptable(self):
        for word in self.FORBIDDEN_WORDS:
            if word in self.text:
                return False
        return True

    def count_emotion(self):
        result = 0
        counter = 0
        for word in self.words:
            result += word.value
            counter += 1
        if counter != 0:
            return result/counter
        return 0

    def make_dict(self):
        for word in self.words:
            emotion = word.emotion
            name = word.name
            if emotion == 'h':
                if name in self.happy_words:
                    self.happy_words[name] += 1
                else:
                    self.happy_words[name] = 1
            elif emotion == 's':
                if name in self.sad_words:
                    self.sad_words[name] += 1
                else:
                    self.sad_words[name] = 1
            elif emotion == 'a':
                if name in self.agressive_words:
                    self.agressive_words[name] += 1
                else:
                    self.agressive_words[name] = 1
            elif emotion == 'f':
                if name in self.fear_words:
                    self.fear_words[name] += 1
                else:
                    self.fear_words[name] = 1


class Word:
    def __init__(self, name: str, value: float, emotion: str) -> None:
        self.name = name
        self.value = value
        self.emotion = emotion

    def reverse(self):
        """
        Return word with opposite sentiment to given word.
        """
        reversed_word = Word(f'не {self.name}', - self.value, 'i')
        return reversed_word

    def __str__(self):
        """
        Return string representation of given word.
        """
        return f'word {self.name} has value of {str(self.value)} and has {self.emotion} emotion'
