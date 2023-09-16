from dotenv import dotenv_values, load_dotenv
from loguru import logger

from utils import Args
from utils.log_manager import init_log_record


@logger.catch(reraise=True)
def __init_logger_args() -> dict:
    args = Args.parseArgs()

    init_log_record(**args.__dict__)

    logger.debug(f"Args: {args}")

    return args


args = __init_logger_args()

"""
I recommend the rest of the code is placed below this comment
so that proper init file for logs and args is in place.

Including other imports
"""


@logger.catch(reraise=True)
def __load_env_values() -> dict:
    load_dotenv()

    config = dotenv_values(".env")

    logger.info("Dot env values loaded")

    logger.debug(f"Config: {config}")

    return config


__load_env_values()


@logger.catch()
def main():
    logger.info("Main function called")

    for i in range(1, 11):
        logger.debug(f"Attempt #{i}")
        init_log_record(**args.__dict__)


main()
