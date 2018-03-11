_g2e = {}
_e2g = {}


def train():
    learn_word("Mann", "Man")
    learn_word("Junge", "Boy")
    learn_word("Frau", "Woman")
    learn_word("Ein Mann", "A man")
    learn_word("Ein Junge", "A boy")
    learn_word("Eine Frau", "A woman")
    learn_word("Eine Frau ein Mann", "A woman a man")
    learn_word("Ich bin Anna", "I am Anna")


def learn_word(gword, eword):
    _g2e[gword.lower()] = eword
    _e2g[eword.lower()] = gword


def to_english(gword):
    return _g2e[gword.lower()]


def to_german(eword):
    return _e2g[eword.lower()]
