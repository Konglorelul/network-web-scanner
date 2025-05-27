#!/usr/bin/python3

import vulners

def vuls_found(s,v):

    vulners_api = vulners.Vulners(api_key="K45YY3S4YYRSGVEGPL06HN8CHINRW21POS4Z950A82OIK2LRVX3WO0W0PP2MJH9G")
    results = vulners_api.softwareVulnerabilities(s, v)
    exploit_list = results.get('exploit')
    vulnerabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]
    print(vulnerabilities_list)

print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

service = str(input("Service: "))
version = str(input("Version: "))

print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

while (version != '0'):
    
    vuls_found(service, version)

    print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

    service = str(input("Service: "))
    version = str(input("Version: "))

    print("\n<---------------------------------------------------------------------------------------------------------------------->\n")