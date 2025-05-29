import argparse

from port_scanner import port_scanner
from vuln_scanner import vuln_scanner
from sqli import sqli
from xss import xss
from output_xls import output

def parse_args():
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
        help=""" Specify the targeted ip or subnet for host discovery (ex: 192.168.x)""",
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

    print("...Options and flags fetched...")
    args = Parser.parse_args()
    return args

def gui_logic(args):
    opt = ""

    match opt:
        case "port_scanner_ip":
            port_scanner(args.ip)

        case "port_scanner_port":
            port_scanner(args.ip, args.port)

        case "vuln_scanner":
            vuln_scanner(args.service, args.version)

        case "xss":
            xss(args.URL)

        case "sqli":
            sqli(args.URL)


def decide_option(args):
    opt = ""

    if args.select_script == "port_scanner" and args.service is None and args.version is None and args.URL is None:
        
        if args.ip is not None:
            opt = "port_scanner_ip"
        elif args.ip is not None and args.port is not None:
            opt = "port_scanner_port"
        else:
            print("eroare selectie flaguri port_scanner")
    
    elif args.select_script == "vuln_scanner" and args.ip is None and args.port is None and args.URL is None:
        
        if args.service is not None and args.version is not None:
            opt = "vuln_scanner"
        else:
            print("eroare selectie flaguri vuln_scanner")
    
    elif args.select_script == "xss" and args.ip is None and args.port is None and args.service is None and args.version is None:
       
        if args.URL is not None:
            opt = "xss"
        else:
            print("eroare selectie flaguri xss")
                     
    elif args.select_script == "sqli" and args.ip is None and args.port is None and args.service is None and args.version is None:
        
        if args.URL is not None:
            opt = "sqli"
        else:
            print("eroare selectie flaguri sqli")
   
    else:
        print("eroare scriptul selectat nu exista sau selectia flagurilor este gresita")

    return opt

def main():
    print("main")
    args = parse_args()
    print(args.select_script)
    print(args.ip)
    print(args.port)


if __name__ == '__main__':
    main()


