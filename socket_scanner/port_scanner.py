#!/usr/bin/python3 

import socket
import multiprocessing
import os
import subprocess
import threading 
from queue import Queue #lista care stocheaza alte tipuri de date (ex: porturile deschise) 


def portscan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #conectarea la retea (IPV4, TCP)
        s.connect((target, port))
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def state():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port: {}/tcp => State: open".format(port))
            open_ports.append(port)

def version():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            try:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #conectarea la retea (IPV4, TCP)
                s.connect((target, port))
                #socket.setdefaulttimeout(5)
                #s.send(b'GET HTTP/1.1 \r\n')
                s.send(b'ICMP\r\n') #request pentru serviciul http
                s.settimeout(5)
                service = socket.getservbyport(port)
                print("Port: {}/tcp => State: open => Service name: {} => Version: {}\n".format(port,service,str(s.recv(2048)).strip('b')))
            except:
                print('Port: {}/tcp => State: open => Service name: unknown => Version: unknown\n'.format(port))  
            open_ports.append(port)

def pinger( job_q, results_q ):
    DEVNULL = open(os.devnull,'w')
    while True:
        ip = job_q.get()
        if ip is None: break

        try:
            subprocess.check_call(['ping','-c1',ip],
                                  stdout=DEVNULL)
            results_q.put(ip)
        except:
            pass

print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

op=int(input("[*] Available options: \n"
        "\n1. Discovered hosts in a subnet (run only on linux distributions)\n"
        "2. Scan a selected range of ports\n"
        "3. Scan selected ports (with service/version)\n"
        "4. Scan common ports in range 1-1024 (with service/version)\n"
        "5. Scan all ports in range 1-65535 (with service/version)\n"
        "\n[*] Please insert a valid option: "))

print('\n<----------------------------------------------------------------------------------------------------------------------->\n')

while (op <= 6):

    if (op == 1):      

        sub = str((input("[*] Insert a subnet (ex: 192.168.x): ")))

        print('\n<-------------------------------------------------------------------------------------------------------------------->\n')

        if __name__ == '__main__':
            pool_size = 255

        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()

        pool = [ multiprocessing.Process(target=pinger, args=(jobs,results))
            for i in range(pool_size) ]

        for p in pool:
            p.start()

        for i in range(1,255):
            jobs.put("{}.{}".format(sub,i))

        for p in pool:
            jobs.put(None)

        for p in pool:
            p.join()

        while not results.empty():
            ip = results.get()
            print(ip)
            
    if (op == 2):
            
        target = input("[*] Insert a ip adress or site you want to scan: ")
        print("[*] The ip a inserted target is: {}".format(socket.gethostbyname(target)))

        print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

        queue = Queue()
        open_ports= []

        start_port = int(input('[*] Insert start port: '))
        stop_port = int(input('[*] Insert stop port: '))

        print("\n<------------------------------------------------------------------------------------------------------------------------->")
        
        port_list = range(start_port,stop_port)
        
        print('\n')

        fill_queue(port_list)
            
        thread_list = []
            
        for t in range(2000):
            thread = threading.Thread(target=state)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            
        for thread in thread_list: 
            thread.join() #wait for all threads

        print ("\nOpen ports are:",open_ports)

        print("\n")

        fill_queue(port_list)

        thread_list = []
            
        for t in range(1000):
            thread = threading.Thread(target=version)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            
        for thread in thread_list: 
            thread.join() #wait for all threads



    if (op == 3):

        target = input("[*] Insert a ip adress or site you want to scan: ")
        print("[*] The ip a inserted target is: {}".format(socket.gethostbyname(target)))

        print("\n<------------------------------------------------------------------------------------------------------------------------>\n")

        ports_specified= []

        ans = str(0)

        while ans != 'n':
                p= int(input("[*] Insert a port you want to scan: "))
                ports_specified.append(p)
                ans = input("[*] Do you want to insert more? (y/n): ")

        print("\nPorts list for scan: ",ports_specified)
        print("\n<--------------------------------------------------------------------------------------------------------------------------->\n")

        for i in ports_specified:    
            try:    
                if portscan(i):
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    s.connect((target, i))
                    #s.send(b'GET HTTP/1.1 \r\n')
                    s.send(b'WhoAreYou\r\n') #request pentru serviciul http
                    print("Port: {}/tcp => State: open => Service name: {} => Version: {}\n".format(i,socket.getservbyport(i),s.recv(10000)))
                else:
                    print("Port: {}/tcp => State: close\n".format(i))
            except:
                print('Port: {}/tcp => State: open => Service name: unknown => Version: unknown\n'.format(i))  
                s.close()
                

    if (op == 4):

        target = input("[*] Insert a ip adress or site you want to scan: ")
        print("[*] The ip a inserted target is: {}".format(socket.gethostbyname(target)))

        print("\n<----------------------------------------------------------------------------------------------------------------------------->\n")

        queue = Queue()
        open_ports= []

        port_list = range(1,1024)

        fill_queue(port_list)
            
        thread_list = []
            
        for t in range(1000):
            thread = threading.Thread(target=state)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            
        for thread in thread_list: 
            thread.join() #wait for all threads

        print ("\nOpen ports are:",open_ports)

        print("\n")

        fill_queue(port_list)

        thread_list = []
            
        for t in range(1000):
            thread = threading.Thread(target=version)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            
        for thread in thread_list: 
            thread.join() #wait for all threads

    
    if (op == 5):

        target = input("[*] Insert a ip adress or site you want to scan: ")
        print("[*] The ip a inserted target is: {}".format(socket.gethostbyname(target)))

        print("\n<---------------------------------------------------------------------------------------------------------------------------->\n")
            
        queue = Queue()
        open_ports= []

        port_list = range(1,65535)

        fill_queue(port_list)
            
        thread_list = []
            
        for t in range(2000):
            thread = threading.Thread(target=state)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list: 
            thread.join() 

        print ("\nOpen ports are: ",open_ports)

        print("\n")

        fill_queue(port_list)

        thread_list = []
            
        for t in range(1000):
            thread = threading.Thread(target=version)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()
            
        for thread in thread_list: 
            thread.join() #wait for all threads
                

        if (op >= 6):
            print("[*] Please insert a valid option")

    print("\n<----------------------------------------------------------------------------------------------------------------------->\n")

    op=int(input("[*] Available options: \n"
        "\n1. Discovered hosts in a subnet (run only on linux distributions)\n"
        "2. Scan a selected range of ports\n"
        "3. Scan selected ports (with service/version)\n"
        "4. Scan common ports in range 1-1024 (with service/version)\n"
        "5. Scan all ports in range 1-65535 (with service/version)\n"
        "\n[*] Please insert a valid option: "))

    print('\n<---------------------------------------------------------------------------------------------------------------------->\n')



