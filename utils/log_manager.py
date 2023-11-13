from datetime import datetime
from os import mkdir
from os.path import exists

from loguru import logger

from errors.already_init import AlreadyInitException

__init = False

__GLOBAL_VERBOSE = False

__LOG_FILES_PATH = 'logs'

LOG_FORMAT = ' | '.join(
    [
        '{time:YYYY-MM-DD HH:mm:ss.SSS}',
        '{level: <10}',
        '{module: <15}',
        '{name: ^30}:{function: >20}:{line: <6}',
        '{message}',
    ],
)


@logger.catch
def init_log_record(log_level: str, log_file_extension: str, verbose: bool):
    global __init
    verbose = verbose or __GLOBAL_VERBOSE
    date = datetime.now().strftime('%Y-%m-%d')
    LOG_FILE_PATH = f'{__LOG_FILES_PATH}/{date}_{log_file_extension}.log'
    dir_created, file_created = not exists(__LOG_FILES_PATH), not exists(LOG_FILE_PATH)
    if not __init:
        if not verbose:
            logger.remove()

        if dir_created:
            mkdir(__LOG_FILES_PATH)

        # Center each log formatted string to center each section in the output file
        logger.add(LOG_FILE_PATH, level=log_level, format=LOG_FORMAT)

        logger.info(' LOGGER INITIALIZED '.center(50, '='))

        if dir_created:
            logger.info(f'{__LOG_FILES_PATH} directory created')

        if file_created:
            logger.info(f'Log file created -> {LOG_FILE_PATH}')

        logger.debug(f'Log level set to {log_level}')

        __init = True
    else:
        raise AlreadyInitException('Logger already initialized')
