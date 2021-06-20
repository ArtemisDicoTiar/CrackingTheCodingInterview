from Chapter1_ArrayAndStrings.langPython.Question2.checkPermutation import is_permutation


class Test_checkPermutation:
    def test_null_inputs(self):
        assert is_permutation('', '...') is ValueError
        assert is_permutation('...', '') is ValueError

    def test_one_word(self):
        assert is_permutation('abc', 'a') is True
        assert is_permutation('abc', 'b') is True
        assert is_permutation('abc', 'd') is False

    def test_two_words(self):
        assert is_permutation('abc', 'ab') is True
        assert is_permutation('abc', 'cb') is True
        assert is_permutation('abc', 'da') is False

        assert is_permutation('apples', 'le') is True
        assert is_permutation('apples', 'lz') is False
