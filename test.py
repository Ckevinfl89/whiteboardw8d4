from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase(TestCase):
    def test_example_onet(self):
        self.assertEqual(solution('Pig latin is cool'),'igPay atinlay siay oolcay')
    def test_example_two(self):
        self.assertEqual(solution('This is my string'),'hisTay siay ymay tringsay')
    def test_hello_world(self):
        self.assertEqual(solution('Hello world !'),'elloHay orldway !')
    def test_empty(self):
        self.assertEqual(solution(""), "")
    def test_nonsense(self):
        self.assertEqual(solution('Acta est fabula'), 'ctaAay steay abulafay')