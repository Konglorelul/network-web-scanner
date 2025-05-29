def port_scanner(ip, output, port=0):
    print("test port scanner")
    print("ip: "+ip)
    print("ot: "+str(output))
    print("port: "+str(port))

    if ip.split(".")[2] == "x":
        print("subnet")
    else:
        print("ip")

    if port != 0:
        if len(port.split("-")) == 1 and int(port.split("-")[0]) > 0 and int(port.split("-")[0]) < 65536:
            print("port")
        elif len(port.split("-")) == 2 and int(port.split("-")[0]) > 0 and int(port.split("-")[1]) < 65536 and int(port.split("-")[1]) > int(port.split("-")[0]):
            print("range")
        else:
            print("port/range invalid")
        