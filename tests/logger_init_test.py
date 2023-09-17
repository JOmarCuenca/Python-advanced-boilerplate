from tests import PARAMS, CommonTestCase
from utils.log_manager import init_log_record


class LoggerMethodsTest(CommonTestCase):
    def test_logger_init(self):

        # Calling this method 2 times shouldn't fail, but should register an exception
        init_log_record(**PARAMS)
