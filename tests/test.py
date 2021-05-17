import unittest
from divide import *
from analyze import analyze


class TestValidator(unittest.TestCase):
    def test_word(self):
        word = Word('анекдот', 0.33, 'h')
        self.assertEqual(word.name, 'анекдот')
        self.assertEqual(word.value, 0.33)
        self.assertEqual(word.emotion, 'h')
        word = word.reverse()
        self.assertEqual(word.value, -0.33)
        self.assertEqual(word.emotion, 'i')

    def test_sentence(self):
        sent = Sentence('Він щасливий', 'ua')
        self.assertEqual(sent.emotion, 1.33)
        self.assertTrue('щасливий' in sent.happy_words)
        self.assertFalse(sent.sad_words)
        sent = Sentence('hello darkness my old friend', 'en')
        self.assertEqual(sent.emotion, 0.2439)

    def test_analyze(self):
        sent = Sentence('Він щасливий', 'ua')
        self.assertTrue('щасливий' in sent.happy_words)


if __name__ == '__main__':
    unittest.main()
