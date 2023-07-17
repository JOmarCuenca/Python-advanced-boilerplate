from utils import getLogger, Args
from dotenv import load_dotenv, dotenv_values

args = Args.parseArgs()

logger = getLogger(debug=args.verbose)

logger.info(f"Args: {args}")

"""
I recommend the rest of the code is placed below this comment
so that proper init file for logs and args is in place.

Including other imports
"""

load_dotenv()

config = dotenv_values(".env")

logger.info(f"Config: {config}")

logger.info(config["val"])