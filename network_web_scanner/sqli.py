def sqli(URL, output):
    print("test sqli")
    print("URL: "+URL)
    print("ot: "+str(output))

    payload = "1=1"
    injected_url = ""
    payload_index = URL.find("[*]")
    injected_url = URL[0:payload_index] + payload #+ URL[payload_index+3:len(URL)]
    print(injected_url)
