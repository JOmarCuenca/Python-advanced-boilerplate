from utils import getLogger, Args

args = Args.parseArgs()

logger = getLogger(debug=args.verbose)

logger.info(f"Args: {args}")

"""
I recommend the rest of the code is placed below this comment
so that proper init file for logs and args is in place.

Including other imports
"""