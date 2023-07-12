import argparse

class Args:
    def __init__(self,
                 verbose: bool) -> None:
        self.verbose = verbose

    def __str__(self) -> str:
        return str({
            "verbose": self.verbose,
        })

    def parseArgs():
        parser = argparse.ArgumentParser(
            prog='Python advanced template',
            description="Remember to change this description to something useful for your project",)

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
        parser.add_argument("-v", "--verbose", action="store_true", dest="verbose",
                            help="Increase output verbosity")

        args = parser.parse_args()

        return Args(
            args.verbose,
        )
