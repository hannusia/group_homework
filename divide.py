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
        sentences = TextADT()
        for sentence in sent_tokenize(text):
            sentences.add(Sentence(sentence))
        return sentences.reverse()

    def div_into_words(self, sentence) -> list:
        """
        return list with all words from given sentence
        """
        import re
        sentence = re.sub('[^а-яі ]', '', sentence)
        words = sentence.split(' ')
        return words


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
    def __init__(self) -> None:
        self.head = None
        self.emotion = 0

    def empty(self) -> bool:
        """
        Check if linked list is empty.
        """
        return self.head == None

    def add(self, value) -> None:
        """
        Add new value to linked list.
        """
        if self.head is None:
            self.head = Node(value)
        else:
            rest = self.head
            self.head = Node(value)
            self.head.next = rest

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

    def reverse(self):
        current = self.head
        ms = TextADT()
        while current:
            ms.add(current.data)
            current = current.next
        return ms

    def __iter__(self):
        list_item = self.head
        while list_item is not None:
            yield list_item
            list_item = list_item.next


class Sentence:
    STOPWORDS = {}
    EMOTIONAL_WORDS = {}

    def __init__(self, text: str):
        if text[-1] == '!':
            self.sentiment = 1.2
        elif text[-1] in {'?', '...'}:
            self.sentiment = 1.1
        else:
            self.sentiment = 1
        text = text[:-1]
        while not text[0].isalpha():
            text = text[1:]
        self.text = text.lower()
        self.emotion = 0
        self.words = self.clean_words()

    def clean_words(self) -> list:
        """
        Return list with normalized words from sentence
        and without stopwords.
        """
        import pymorphy2
        morph = pymorphy2.MorphAnalyzer(lang='uk')
        all_words = Divider().div_into_words(self.text)
        all_words = list(map(lambda x: morph.parse(x)
                         [0].normal_form, all_words))
        all_words = list(filter(lambda x: x not in self.STOPWORDS, all_words))
        words = []
        for i in range(len(all_words)):
            if all_words[i] == 'не':
                if all_words[i+1] in self.EMOTIONAL_WORDS:
                    tpl = self.EMOTIONAL_WORDS[all_words[i+1]]
                    words.append(
                        Word(all_words[i+1], tpl[0], tpl[1]).reverse())
            else:
                if all_words[i] in self.EMOTIONAL_WORDS:
                    tpl = self.EMOTIONAL_WORDS[all_words[i]]
                    words.append(Word(all_words[i], tpl[0], tpl[1]))
        return words

    def __str__(self):
        """
        Return string representation of sentence.
        """
        result = ''
        for word in self.words:
            result += str(word) + '\n'
        return result

    def count_emotion(self):
        pass


class Word:
    def __init__(self, name: str, value: float, emotion: str) -> None:
        self.name = name
        self.value = value
        self.emotion = emotion

    def reverse(self):
        """
        Return word with opposite sentiment to given word.
        """
        if self.emotion in {'s', 'a', 'f'}:
            reversed_emotion = 'h'
        else:
            reversed_emotion = 's'
        reversed_word = Word(f'не {self.name}', - self.value, reversed_emotion)
        return reversed_word

    def __str__(self):
        """
        Return string representation of given word.
        """
        return f'word {self.name} has value of {str(self.value)} and has {self.emotion} emotion'
