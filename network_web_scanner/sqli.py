import requests
import xlwt
from datetime import datetime

def sqli(URL, output):
    if "[*]" not in URL:
        print("URL-ul needs to have [*] as injection marker")
        return

    payload = "'"
    url = URL.replace("[*]", payload)

    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://localhost/vulnerabilities/sqli/",
        "Connection": "keep-alive"
    }

    
    cookies = {
        "PHPSESSID": "utvtq4rm217uu7984ma9l30ag1",
        "security": "low"
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)

        print(f"Sent payload to: {response.url}")
        print(f"HTTP Status: {response.status_code}")

        if "error in your SQL syntax" in response.text.lower():
            print("\nNo suspicious behaviour detected")
            result = "No"
        else:
            print("\nPossible SQLi detected!")
            result = "Yes"

        if output:
            wb = xlwt.Workbook()
            sh = wb.add_sheet("SQLi_Result")
            sh.write(0, 0, "URL")
            sh.write(0, 1, "Payload")
            sh.write(0, 2, "Status")
            sh.write(0, 3, "Possible Injection")

            sh.write(1, 0, response.url)
            sh.write(1, 1, payload)
            sh.write(1, 2, response.status_code)
            sh.write(1, 3, result)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            wb.save(f"SQLi_Result_{timestamp}.xls")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error sending the request: {e}")
