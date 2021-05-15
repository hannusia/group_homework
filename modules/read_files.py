def read_input(path='text.txt') -> str:
    with open(path) as file:
        text = file.read()
    return text


def read_stopwords(path: str) -> set:
    with open(path) as file:
        stopwords = file.read().splitlines()
    return set(stopwords)


def read_emotions(path: str):
    result = {}
    with open(path) as file:
        lines = file.read().splitlines()
    for line in lines:
        line = line.split('\t')
        result[line[0]] = (float(line[1]), line[-1])
    return result

