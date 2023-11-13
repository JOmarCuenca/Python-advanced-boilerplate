from unittest import TestCase

from loguru import logger

from utils.log_manager import init_log_record

PARAMS = {'log_level': 'WARNING', 'log_file_extension': 'test', 'verbose': False}


class CommonTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        init_log_record(**PARAMS)
        logger.debug('Test logger initialized')
