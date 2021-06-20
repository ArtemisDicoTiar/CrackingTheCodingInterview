from Chapter1_ArrayAndStrings.langPython.Question1.uniqueCharacter import isUnique


class Test_isUnique:
    def test_return_empty_word(self):
        assert isUnique('') is True

    def test_one_word(self):
        assert isUnique('a') is True
        assert isUnique('b') is True
        assert isUnique('d') is True
        assert isUnique('z') is True

        assert isUnique('1') is True
        assert isUnique('3') is True
        assert isUnique('0') is True

        assert isUnique('*') is True

    def test_two_word(self):
        assert isUnique('aa') is False
        assert isUnique('ar') is True

        assert isUnique('be') is True
        assert isUnique('bb') is False

        assert isUnique('zw') is True
        assert isUnique('zz') is False

        assert isUnique('11') is False
        assert isUnique('31') is True
        assert isUnique('0a') is True

        assert isUnique('*!') is True

    # def test_is_unique(self):
    #     self.fail()
