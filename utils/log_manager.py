from datetime import datetime
from loguru import logger

from .file_manager import verify_dir, create_dir

__instance = None

__GLOBAL_VERBOSE = False

__LOG_FILES_PATH = "logs"

LOG_FORMAT = " | ".join([
    "{time:YYYY-MM-DD HH:mm:ss.SSS}",
    "{level: <10}",
    "{module: <15}",
    "{name: ^30}:{function: >15}:{line: <6}",
    "{message}",
])


def getLogger(debug=False):
    debug = debug or __GLOBAL_VERBOSE
    global __instance
    created = False
    if not __instance:
        if not (debug or __GLOBAL_VERBOSE):
            logger.remove()

        if not verify_dir(__LOG_FILES_PATH):
            create_dir(__LOG_FILES_PATH)
            created = True
        
        date = datetime.now().strftime("%Y-%m-%d")
        # Center each log formatted string to center each section in the output file
        logger.add(f"{__LOG_FILES_PATH}/{date}_run.log", level="DEBUG", format=LOG_FORMAT)
        if created:
            logger.error(f"{__LOG_FILES_PATH} directory created")
            
        logger.info(
            f"Log file created -> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        logger.info(" LOGGER INITIALIZED ".center(50, "="))

        __instance = logger

    return __instance


if __name__ == '__main__':
    logger = getLogger()
    logger.info("This is a test info")
    logger.debug("This is a test debug")
    logger.warning("This is a test warning")
    logger.error(Exception("This is a test error"))