class Divider:
    def __init__(self):
        pass

    def div_into_sentences(self, text):
        """
        return Text object - linked list with sentences from given text.
        """
        from nltk.tokenize import sent_tokenize
        sentences = Text()
        for sentence in sent_tokenize(text):
            sentences.add(Sentence(sentence))
        return sentences.reverse()


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Text:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def add(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            rest = self.head
            self.head = Node(value)
            self.head.next = rest

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data.text)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def reverse(self):
        current = self.head
        ms = Text()
        while current:
            ms.add(current.data)
            current = current.next
        return ms


class Sentence:
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
