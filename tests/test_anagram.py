from anagram import count_letters, is_anagram


def test_count_letters():
    text = "hello"

    result = count_letters(text)

    assert result['h'] == 1
    assert result['e'] == 1
    assert result['l'] == 2
    assert result['o'] == 1


def test_is_anagram():
    text1 = "hello"
    text2 = "holle"
    text3 = "hell"

    assert is_anagram(text1, text2)
    assert is_anagram(text2, text1)
    assert not is_anagram(text2, text3)
    assert not is_anagram(text1, text3)

