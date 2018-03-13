import re
from enum import Enum


class ChallengeType(Enum):
    write_in_english = 1
    write_in_german = 2
    select_in_german = 3


def decide_type_and_data(challenge):
    """ return challenge type and extracted data required for the solution """
    challenge = challenge.lower()

    # write in English
    if challenge == "write this in english":
        return ChallengeType.write_in_english, None

    # write in German
    wig_regex = re.match(r'write .(.*). in german', challenge)
    if wig_regex:
        return ChallengeType.write_in_german, wig_regex.group(1)

    # select in German
    sig_regex = re.match(r'select the word for .(.*).', challenge)
    if sig_regex:
        return ChallengeType.select_in_german, sig_regex.group(1)
    return None, None
