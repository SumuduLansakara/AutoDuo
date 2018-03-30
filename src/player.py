import logging
import re
from enum import Enum

from selenium.common import exceptions

import lesson_page
import translator

MAX_LOAD_ATTEMPTS = 10


def do_all_challenges():
    cid = 0
    prev_header = None
    prev_data = 0
    while True:
        try:
            challenge_header = lesson_page.get_challenge_header().strip()
            challenge_load_attempts = 0
            while challenge_load_attempts < MAX_LOAD_ATTEMPTS:
                challenge_load_attempts += 1
                if challenge_header:
                    if challenge_header != prev_header:
                        break
                    type_, _ = _decide_type_and_data(challenge_header)
                    if type_ == ChallengeType.write_in_english:
                        hint = lesson_page.get_hint_sentence(challenge_load_attempts / 2)
                        hint = translator.sanitize(hint)
                        if hint != prev_data:
                            break
                challenge_header = lesson_page.get_challenge_header().strip()
            else:
                logging.getLogger().debug("challenge completed: max attempts reached")
                return cid
        except exceptions.StaleElementReferenceException:
            logging.getLogger().debug("challenge completed: StaleElementReferenceException")
            return cid
        except exceptions.TimeoutException:
            logging.getLogger().debug("challenge completed: TimeoutException")
            return cid
        except Exception:
            logging.getLogger().debug("challenge completed: Generic")
            return cid
        cid += 1
        type_, data = _decide_type_and_data(challenge_header)
        if type_ == ChallengeType.write_in_english:
            hint = lesson_page.get_hint_sentence()
            hint = translator.sanitize(hint)
            logging.getLogger().info("challenge {}: {} [{}]".format(cid, challenge_header, hint))
            prev_data = hint
            lesson_page.type_english(translator.g2e(hint))
        else:
            logging.getLogger().info("challenge {}: {}".format(cid, challenge_header))
            prev_data = data
            if type_ == ChallengeType.write_in_german:
                lesson_page.type_german(translator.e2g(data))
            elif type_ == ChallengeType.select_in_german:
                lesson_page.select_radio(translator.e2g(data))
        lesson_page.click_next()
        lesson_page.click_next()
        lesson_page.wait_till_header_changed(challenge_header, 1)
        prev_header = challenge_header


class ChallengeType(Enum):
    write_in_english = 1
    write_in_german = 2
    select_in_german = 3


def _decide_type_and_data(challenge):
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
