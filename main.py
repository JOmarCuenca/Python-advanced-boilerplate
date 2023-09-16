from utils import Args
from utils.log_manager import init_log_record

from loguru import logger
from dotenv import load_dotenv, dotenv_values

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


