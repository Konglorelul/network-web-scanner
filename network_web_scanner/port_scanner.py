import socket
import multiprocessing
import os
import subprocess
import threading 
from queue import Queue

def port_scanner(ip, output, port=0):
    print("test port scanner")
    print("ip: "+ip)
    print("ot: "+str(output))
    print("port: "+str(port))

    def ping_command( ip, result_q):
        DEVNULL = open(os.devnull, 'w')
        subprocess.check_call(['ping', '-c1', ip], stdout = DEVNULL)
        result_q


    if ip.count(".") == 3:
        print("ip")
    elif ip.count(".") == 2:
        print("subnet") 
    else:
        print("eroare format ip")
        



 #   if ip.split(".")[2] == "x": #needs change, logic error
 #       print("subnet")
 #   else:
 #       print("ip")

    if port != 0:
        if len(port.split("-")) == 1 and int(port.split("-")[0]) > 0 and int(port.split("-")[0]) < 65536:
            print("port")
        elif len(port.split("-")) == 2 and int(port.split("-")[0]) > 0 and int(port.split("-")[1]) < 65536 and int(port.split("-")[1]) > int(port.split("-")[0]):
            print("range")
        else:
            print("port/range invalid")

