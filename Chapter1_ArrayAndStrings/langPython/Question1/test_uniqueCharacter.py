from unittest import TestCase
from Chapter1_ArrayAndStrings.langPython.Question1.uniqueCharacter import isUnique


class Test_isUnique(TestCase):
    def test_return_empty_word(self):
        self.assertEqual(first=isUnique(''), second=True)

    def test_one_word(self):
        self.assertEqual(isUnique('a'), True)
        self.assertEqual(isUnique('b'), True)
        self.assertEqual(isUnique('d'), True)
        self.assertEqual(isUnique('z'), True)

        self.assertEqual(isUnique('1'), True)
        self.assertEqual(isUnique('3'), True)
        self.assertEqual(isUnique('0'), True)

        self.assertEqual(isUnique('*'), True)

    def test_two_word(self):
        self.assertEqual(isUnique('aa'), False)
        self.assertEqual(isUnique('ar'), True)

        self.assertEqual(isUnique('be'), True)
        self.assertEqual(isUnique('bb'), False)

        self.assertEqual(isUnique('zw'), True)
        self.assertEqual(isUnique('zz'), False)

        self.assertEqual(isUnique('11'), False)
        self.assertEqual(isUnique('31'), True)
        self.assertEqual(isUnique('0a'), True)

        self.assertEqual(isUnique('*!'), True)

    # def test_is_unique(self):
    #     self.fail()
