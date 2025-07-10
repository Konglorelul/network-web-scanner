from vulners import VulnersApi
from datetime import datetime
import xlwt

API_KEY = "NYEZ6HH8GPY9D2MEYHCIZSBN23ENXN7SVWFF7448MW7IZ4IC2RBQE7J3IGLYDZ7Z"

def vuln_scanner(service, version, output=False):
    vulners_api = VulnersApi(api_key=API_KEY)
    query = f'{service} {version}'
    results = vulners_api.search.search_bulletins_all(query)

    if not results:
        print("[-] No results found.")
        return

    print(f"[+] Found {len(results)} results for {service} {version}:\n")

    for item in results[:5]:
        print(f"ID: {item.get('id')}")
        print(f"Title: {item.get('title')}")
        print(f"Type: {item.get('type')}")
        print(f"Severity: {item.get('cvss', {}).get('score', 'N/A')}")
        print("-" * 40)

    if output:
        wb = xlwt.Workbook()
        sh = wb.add_sheet("Vulnerabilities")
        sh.write(0, 0, "ID")
        sh.write(0, 1, "Title")
        sh.write(0, 2, "Type")
        sh.write(0, 3, "Severity")

        for i, item in enumerate(results[:10], start=1):
            sh.write(i, 0, item.get("id", "N/A"))
            sh.write(i, 1, item.get("title", "N/A"))
            sh.write(i, 2, item.get("type", "N/A"))
            sh.write(i, 3, item.get("cvss", {}).get("score", "N/A"))

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Vulners_{service}_{version}_{timestamp}.xls"
        wb.save(filename)
        
