from Chapter1_ArrayAndStrings.langPython.Question4.isPalindromePermutation import is_palindromePermutation


class Test_isPalindromePermutation:

    def test_null_input(self):
        assert is_palindromePermutation('') == ValueError

    def test_one_word(self):
        assert is_palindromePermutation('ada') is True

        assert is_palindromePermutation('abc') is False

        assert is_palindromePermutation('aaa') is True

    def test_two_word(self):
        assert is_palindromePermutation('ada dd') is True

        assert is_palindromePermutation('Tact Coa') is True

        assert is_palindromePermutation('Tact Coaa') is False
