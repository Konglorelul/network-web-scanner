import argparse

from port_scanner import port_scanner
from vuln_scanner import vuln_scanner
from sqli import sqli
from xss import xss
from output_xls import output

def parseArgs():
    print("...Waiting to fetch options and flags...")
    Parser = argparse.ArgumentParser(
        description=""" Network and Web Vulnerability Scanner
                        """)
    Parser.add_argument(
        "select_script",
        help=" Choose from port_scanner , vuln_scanner , xss , sqli to run desired script"
    )
    Parser.add_argument(
        "-i", "--ip",
        metavar="IP",
        help=""" Specify the targeted ip or subnet for host discovery (ex: 192.168.10.x)""",
        type=str,
        default=None
    )

    Parser.add_argument(
        "-p", "--port",
        metavar="PORT",
        help=""" Specify the targeted port """,
        type=str,
        default=None
    )

    Parser.add_argument(
        "-s", "--service",
        metavar="SERVICE",
        help=""" Specify the service used by the port """,
        type=str,
        default=None
    )

    Parser.add_argument(
        "-v", "--version",
        metavar="VERSION",
        help=""" Specify the version of the service """,
        type=str,
        default=None
    )

    Parser.add_argument(
        "-u", "--URL",
        metavar="URL",
        help=""" Specify the targeted URL for xss or URL+ injection placement character (ex: https://test.com/[*], https://test.com/arg=[*]  ) """,
        type=str,
        default=None
    )

    Parser.add_argument(
        "-o", "--output",
        action='store_true',
        help=""" Flag to specify if the output will be stored in an .xls document """
        
    )

    args = Parser.parse_args()
    return args

def main():
    print("main")
    args = parseArgs()
    print(args.select_script)
    print(args.ip)
    print(args.port)


if __name__ == '__main__':
    main()
