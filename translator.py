import logging
import re
from typing import List

_delimiters = [' ', ',', '.']

_g2e = {
    "bin": "am",
    "bist": "are",
    "ist": "is",
    "sind": "are",

    "ein": "a",
    "eine": "a",
    "der": "the",
    "die": "the",
    "das": "the",

    "und": "and",

    "ich": "i",
    "du": "you",
    "wir": "we",
    "er": "he",
    "sie": "she",
    "es": "it",

    "mann": "man",
    "frau": "woman",
    "kind": "child",
    "junge": "boy",
    "mädchen": "girl",
    "brot": "bread",
    "wasser": "water",

    "trinkt": "drinks",
    "trinkst": "drink",
    "esse": "eat",

    "lukas": "lukas",
    "anna": "anna",
    "maria": "maria",
    "david": "david",
    "julia": "julia",
}


def _translate_to_german(e_word: str) -> List[str]:
    if e_word.lower() not in _g2e.values():
        logging.error(f"unknown English word: [{e_word}]")
        return ['']

    if e_word[0].isupper():
        e_word = e_word.lower()

        def _format_return(s: str) -> str:
            return s[0].upper() + s[1:]
    else:
        def _format_return(s: str) -> str:
            return s

    options = []
    for g, e in _g2e.items():
        if e == e_word:
            options.append(g)
    return [_format_return(opt) for opt in options]


def _translate_to_english(g_word: str) -> str:
    if g_word.lower() not in _g2e:
        logging.error(f"unknown German word: [{g_word}]")
        return ''
    if g_word[0].isupper():
        res = _g2e[g_word.lower()]
        return res[0].upper() + res[1:]
    return _g2e[g_word]


def to_german(sentence: str) -> List[str]:
    tokens = re.split(r'(\W)', sentence)
    res = ['']
    for tok in tokens:
        if not tok:
            continue
        if tok in _delimiters:
            res = [r + tok for r in res]
        else:
            answers = _translate_to_german(tok)
            res = [r + a for r in res for a in answers]
    return res


def to_english(sentence: str) -> str:
    tokens = re.split(r'(\W)', sentence)
    res = ''
    for tok in tokens:
        if not tok:
            continue
        if tok in _delimiters:
            res += tok
        else:
            res += _translate_to_english(tok)
    return res


if __name__ == '__main__':
    import difflib

    assert to_english("Ein Kind trinkt.") == "A Child drinks."
    assert to_english("Ich bin ein Mann und du bist eine Frau.") == "I am a Man and you are a Woman."
    assert to_english("Ich esse Brot, du trinkst Wasser.") == "I eat Bread, you drink Water."

    assert len(to_german("he is a child.")) == 2
    assert difflib.get_close_matches("er ist ein kind.", to_german("he is a child."))[0] == "er ist ein kind."
    assert difflib.get_close_matches("Ich bin Anna.", to_german("I am Anna."))[0] == "Ich bin Anna."

    _test_question = "I am a Man and you are a Woman."
    _test_answer = "Ich bin ein Mann und du bist eine Frau."
    _test_suggestions = to_german(_test_question)
    assert len(_test_suggestions) == 8
    assert difflib.get_close_matches(_test_answer, _test_suggestions)[0] == _test_answer
