import socket
import multiprocessing
import os
import subprocess
import threading 
from queue import Queue
import xlwt
from datetime import datetime

def porthost_scanner(ip, output, port=None):
    if subnet(ip):
        subnet_scan(ip, output)

    elif full_ip(ip) and port is None:
        scan_ports(ip, output)

    elif full_ip(ip) and "-" in str(port):
        scan_range(ip, port, output)

    elif full_ip(ip) and port:
        scan_port(ip, int(port), output)

    else:
        print("Eroare format IP sau port/range invalid")

def subnet(ip):
    return ip.count(".") == 2

def full_ip(ip):
    return ip.count(".") == 3

def ping_command(job_queue, result_queue):
    DEVNULL = open(os.devnull, 'w')
    while True:
        ip_addr = job_queue.get()
        if ip_addr is None:
            break

        try:
            subprocess.check_call(['ping','-c1', ip_addr], stdout=DEVNULL, stderr=DEVNULL)
            result_queue.put(ip_addr)
        except:
            pass

def port_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
    
def open_state(ip, queue, open_ports):
    while not queue.empty():
        port = queue.get()
        if port_scan(ip, port):
            open_ports.append(port)

def serv_vers(ip, queue, results):
    while not queue.empty():
        port = queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, port))
            s.send(b'\r\n')
            version = s.recv(2048).decode(errors="ignore").strip()
            s.close()
            service = socket.getservbyport(port, "tcp") if port < 1024 else "Unknown"
            results.append((ip, port, service, version))
            print(f"{ip}:{port} Service: {service} Version: {version}")
        except:
            results.append((ip, port, "Unknown", "Unknown"))
            print(f"{ip}:{port} Service: Unknown Version: Unknown")


def subnet_scan(ip, output):
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()
    processes = [multiprocessing.Process(target=ping_command, args=(jobs, results))
                  for p in range(100)]
    
    for p in processes:
        p.start()

    for i in range(1,255):
        jobs.put(f"{ip}.{i}")

    for p in processes:
        jobs.put(None)

    for p in processes:
        p.join()

    up = []

    while not results.empty():
        ip = results.get()
        up.append(ip)
        print(f"Host is up: {ip}")

    if output and up:
        wb = xlwt.Workbook()
        sh = wb.add_sheet("Hosts")
        sh.write(0, 0, "Active Hosts")
        for i, ip in enumerate(up, 1):
            sh.write(i, 0, ip)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        wb.save(f"Active_Hosts_{ip}_{timestamp}.xls")


def scan_ports(ip, output):
    all_ports = Queue()
    open_ports = []
    results = []
    threads = []

    for port in range(1, 65536):
        all_ports.put(port)

    for i in range(200):
        thread = threading.Thread(target=open_state, args=(ip, all_ports, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    open_ports.sort()
    print(f"\n{ip} has the following open ports: {open_ports}\n")

    for port in open_ports:
        all_ports.put(port)

    threads = []

    for i in range(100):
        thread = threading.Thread(target=serv_vers, args=(ip, all_ports, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    if output and results:
        wb = xlwt.Workbook()
        sh = wb.add_sheet("All_Ports")
        sh.write(0, 0, "Target_IP")
        sh.write(0, 1, "Port")
        sh.write(0, 2, "Service")
        sh.write(0, 3, "Version")
        for i, (ip, port, service, version) in enumerate(results, 1):
            sh.write(i, 0, ip)
            sh.write(i, 1, port)
            sh.write(i, 2, service)
            sh.write(i, 3, version)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        wb.save(f"Scanned_Ports_For_{ip}_{timestamp}.xls")
        
def scan_range(ip, port, output):
    if len(port.split("-")) == 2 and int(port.split("-")[0]) > 0 and int(port.split("-")[1]) < 65536 and int(port.split("-")[1]) > int(port.split("-")[0]):
        first_port = int(port.split("-")[0])
        last_port = int(port.split("-")[1])
        port_range = range(first_port, last_port + 1)
        ports = Queue()
        open_ports = []
        results = []
        threads = []

        for p in port_range:
            ports.put(p)

        for i in range(200):
            thread = threading.Thread(target=open_state, args=(ip, ports, open_ports))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        open_ports.sort()
        print(f"\n{ip} has the following open ports: {open_ports}\n")

        for p in open_ports:
            ports.put(p)

        threads = []

        for i in range(100):
            thread = threading.Thread(target=serv_vers, args=(ip, ports, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if output and results:
            wb = xlwt.Workbook()
            sh = wb.add_sheet("Port_Range")
            sh.write(0, 0, "Target_IP")
            sh.write(0, 1, "Port")
            sh.write(0, 2, "Service")
            sh.write(0, 3, "Version")
            for i, (ip, port, service, version) in enumerate(results, 1):
                sh.write(i, 0, ip)
                sh.write(i, 1, port)
                sh.write(i, 2, service)
                sh.write(i, 3, version)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            wb.save(f"Scanned_Range_For_{ip}_{timestamp}.xls")

def scan_port(ip, port, output):
    open_ports = []
    results = []

    if port_scan(ip, port):
        open_ports.append(port)

    if open_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((ip, port))
            s.send(b'\r\n')
            version = s.recv(2048).decode(errors="ignore").strip()
            s.close()
            service = socket.getservbyport(port, "tcp") if port < 1024 else "Unknown"
            results.append((ip, port, service, version))
            print(f"{ip}:{port} Service: {service} Version: {version}")
        except:
            results.append((ip, port, "Unknown", "Unknown"))
            print(f"{ip}:{port} Service: Unknown Version: Unknown")

    if output and results:
        wb = xlwt.Workbook()
        sh = wb.add_sheet("Single_Port")
        sh.write(0, 0, "IP")
        sh.write(0, 1, "Port")
        sh.write(0, 2, "Service")
        sh.write(0, 3, "Version")
        for i, (ip, port, service, version) in enumerate(results, 1):
            sh.write(i, 0, ip)
            sh.write(i, 1, port)
            sh.write(i, 2, service)
            sh.write(i, 3, version)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        wb.save(f"Scanned_Port_{port}_For_{ip}_{timestamp}.xls")    