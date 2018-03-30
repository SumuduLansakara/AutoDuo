import logging
import time


def init_logging(enable_console_log, enable_file_log):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if enable_console_log:
        logger.addHandler(_get_stream_handler())

    if enable_file_log:
        logger.addHandler(_get_file_handler('autoduo.log'))
    logger.debug("Starting AutoDuo: {}".format(time.strftime("%Y-%m-%d [%H:%M:%S]")))


def _get_stream_handler():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%H:%M:%S')
    handler.setFormatter(formatter)
    return handler


def _get_file_handler(logfile_path):
    handler = logging.FileHandler(logfile_path)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%H:%M:%S')
    handler.setFormatter(formatter)
    return handler
