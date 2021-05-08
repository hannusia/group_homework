"""
abstract data types to be used in the project
"""

from collections import Counter
import re
import string
import json

class SVParser:
    """
    class represents native language words with according values
    in either Valence, Arousal or Dominance

    class object is aquired through a comma or tab separated file

    Attributes
    ----------
    dct : dict
        the dictionary of keywords and their property values

    Methods
    -------
    file_reader : dict
        reads separated values file and returns dct
    """

    def __init__(self, path, separator=','):
        """
        :param path: file_path for separated values file
        :param separator: separator used in file
        """
        self.dct = self.file_reader(path, separator)

    @staticmethod
    def file_reader(path, separator):
        """
        reads file dictionary

        :param separator: separator used in file
        """
        with open('new.tsv', 'r', encoding='utf-8') as f:
            lines_lst = f.readlines()
            dct = {x.split(separator)[0] : x.split(separator)[1].strip('\n')
                   for x in lines_lst}

        return dct

    def __getitem__(self, idx):
        """
        gets property value by word index or returns 0
        if the word is not present in SVParser object

        :param idx: signifies an index of desired value
        """
        try:
            return float(self.dct[idx])
        except KeyError:
            return 0.0


class TextAnalysis:
    """
    Analyzes text using tsv tables with according word values

    Attributes
    ----------
    text : str
        text to be analyzed
    valence : float
        valence indicator of the text
    arousal : float
        arousal indicator of the text
    dominance : float
        dominance indicator of the text

    Methods
    -------
    find_common_word : list
        returns most common words in the text fragment
    clear_punctuation : str
        returns text without punctuation
    clear_text : str
        return text without punctuation or common words
    analyze_text
        calculates specified property of the text
    """

    def __init__(self, text):
        """
        :param text: text fragment to be analyzed
        """
        self.text = text
        self.valence = 0.0
        self.arousal = 0.0
        self.dominance = 0.0

    def find_common_words(self, common_words_counter, text):
        """
        finds specified amount of most common words in text

        :param common_words_counter: the amount of common words to be found
        :param text: the text to be analyzed
        """
        words = re.findall(r'\w+', text)
        return Counter(words).most_common(common_words_counter)

    def clear_puntuation(self, text):
        """
        returns text without punctuation

        :param text: the text to be modified
        """
        for i in string.punctuation:
                text = text.replace(i, '')

        return text

    def clear_text(self, counter=1):
        """
        clears text of common words and punctuation

        :param counter: the amount of common words to be found
        """
        text = self.text

        for word in self.find_common_words(counter, text):
            text = text.replace(word[0], '')

        text = self.clear_puntuation(text)

        return text

    def analyze_text(self, sv_obj, property):
        """
        analyzes the text by given property

        :param sv_obj: SVParser object that contains data on given property
        :param property: string name of property to be changed
        """
        assert type(sv_obj) == SVParser

        self.text = self.clear_text()
        text = self.text

        value = 0.0

        for word in text.split(' '):
            value += sv_obj[word]

        setattr(self, property, value)

    def get_property(self, property):
        """
        returns text assessment on specified property

        :param property: string name of needed property
        """
        return getattr(self, property)


class JSONParser:
    """
    helps user navigate through json files

    Attributes
    ----------
    json : json
        json data

    Methods
    -------
    get_value : str
        returns value by given path
    """

    @staticmethod
    def get_json_from_file(path):
        """
        reads json data from path file

        :param path: path to json file
        """
        with open(path, 'r') as json_file:
            data = json.load(json_file)

        return data

    def __init__(self, json_data):
        if not isinstance(json_data, dict):
            json_data = self.get_json_from_file(json_data)
        self.json = json_data

    def get_value(self, *keys):
        """
        gets value by given path

        :param *keys: keys to needed data sorted in order
        """
        obj = self.json

        for key in keys:
            obj = obj[key]

        return obj
