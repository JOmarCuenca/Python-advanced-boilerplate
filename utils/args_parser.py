import argparse
from dataclasses import dataclass

LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


@dataclass(frozen=True, repr=True, eq=True)
class Args:
    verbose: bool
    log_level: str
    log_file_extension: str

    def __str__(self) -> str:
        return str(
            {
                'verbose': self.verbose,
                'log_level': self.log_level,
                'log_file_extension': self.log_file_extension,
            },
        )

    def parseArgs():
        parser = argparse.ArgumentParser(
            prog='Python advanced template',
            description='Remember to change this description to something useful for your project',
        )

        # parser.add_argument("--key", dest="keyPath",
        #                     help="Path to the '.key' file")
        # parser.add_argument("--cer", dest="cerPath",
        #                     help="Path to the '.cer' file")
        # parser.add_argument("--password", dest="pwdPath",
        #                     help="Path to the '.txt' file that holds the password")
        # parser.add_argument("--storePath", dest="downloadPath",
        #                     help="Path to the directory where everything will be downloaded")
        # parser.add_argument("--date-file", dest="datesPath", nargs='?',
        #                     help="Path to the file of date collection to download")
        # parser.add_argument("--date-range", dest="dateRange",
        #                     nargs='?', help="Date string of the dates to download")
        parser.add_argument(
            '-v',
            '--verbose',
            action='store_true',
            dest='verbose',
            help='Increase output verbosity',
        )
        parser.add_argument(
            '--log_level',
            dest='log_level',
            default='info',
            help='Set log level to debug, info, warning, error, critical',
            choices=LOG_LEVELS,
            type=str.upper,
            metavar='LOG_LEVEL',
        )
        parser.add_argument(
            '--log_file_extension',
            dest='log_file_extension',
            default='run',
            help='Set log file extension path',
            type=str,
            metavar='LOG_FILE_EXTENSION_PATH',
        )

        args = parser.parse_args()

        return Args(**args.__dict__)
