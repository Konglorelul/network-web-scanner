#!/usr/bin/python3

import vulners

def vuls_found(s,v):

    vulners_api = vulners.Vulners(api_key="O0NDUGEAUMB2NJ04GG2MQNMKTBJGI965Z1JRHPS30AO0H0AHTR6DX9ZGIMP0CG95")
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