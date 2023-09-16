from unittest import TestCase

from utils.log_manager import init_log_record


class LoggerMethodsTest(TestCase):
    def test_logger_init(self):
        PARAMS = {
            "log_level": "WARNING",
            "log_file_extension": "test",
            "verbose": False
        }
        # Calling this method 2 times shouldn't fail, but should register an exception
        init_log_record(**PARAMS)
        init_log_record(**PARAMS)
