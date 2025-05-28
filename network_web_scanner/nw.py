import argparse

from port_scanner import port_scanner
from vuln_scanner import vuln_scanner
from sqli import sqli
from xss import xss
from output_xls import output

def parseArgs():
    print("...Waiting to fetch options and flags...")
    Parser = argparse.ArgumentParser(
        description=""" Utillity designed to distinguish between searcheable and non-searcheable pdf's in a directory.
                        by generating an output in the form of a csv/xlsx file, where the files are flagged as either,
                        searcheable or non-searcheable, located in the target directory.
                        """)
    Parser.add_argument(
        "output_filename",
        help=" Name of the output file, that stores the flagged vs non-flagged pdf files, as xlsx/csv. "
    )
    Parser.add_argument(
        "-p", "--path_target",
        metavar="PATH_OF_INPUT",
        help=""" Navigate to the given PATH_OF_INPUT of the target dir, where the utillity will sort the pdf files. If the
                 -p flag is not specified, the user will be prompted to choose from a window to select the dir.""",
        type=str,
        default=None
    )
    args = Parser.parse_args()
    return args

def main():
    print("main")
    args = parseArgs()
    print(args.output_filename)
    print(args.path_target)


if __name__ == '__main__':
    main()
