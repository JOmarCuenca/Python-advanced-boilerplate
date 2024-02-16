from dotenv import dotenv_values, load_dotenv
from loguru import logger

from utils import init_log_record
from utils.args_parser import Args

from tqdm import tqdm
from time import sleep


@logger.catch(reraise=True)
def __init_logger_args() -> dict:
    args = Args.parse_args()

    init_log_record(**args.__dict__)

    logger.debug(f'Args: {args}')

    return args


args = __init_logger_args()
"""I recommend the rest of the code is placed below this comment so that proper
init file for logs and args is in place.

Including other imports
"""


@logger.catch(reraise=True)
def __load_env_values() -> dict:
    load_dotenv()

    config = dotenv_values('.env')

    logger.info('Dot env values loaded')

    logger.debug(f'Config: {config}')

    return config


__load_env_values()


@logger.catch()
def main():
    args = Args.parse_args()
    init_log_record(args.log_level, args.log_file_extension, args.verbose)

    logger.info('Main function called')

    for i in tqdm(range(100), unit=' oper'):
        sleep(0.1)


if __name__ == '__main__':
    main()
