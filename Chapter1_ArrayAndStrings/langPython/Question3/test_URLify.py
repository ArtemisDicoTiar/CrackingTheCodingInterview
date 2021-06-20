from Chapter1_ArrayAndStrings.langPython.Question3.URLify import urlify


class Test_URLify:
    def test_null_input(self):
        assert urlify('', 0) == ValueError
        assert urlify('...', 0) == ValueError
        assert urlify('', 3) == ValueError

    def test_one_word(self):
        assert urlify('hello    ', 5) == 'hello'
        assert urlify('equation    ', 8) == 'equation'

    def test_two_word(self):
        assert urlify('one dark    ', 8) == 'one%20dark'
        assert urlify('python console    ', 14) == 'python%20console'

    def test_three_word(self):
        assert urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
