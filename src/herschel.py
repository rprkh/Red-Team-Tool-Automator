import subprocess
import time
import os
import urllib.request

def run_nmap():
    target = input("Enter the target for Nmap: ")

    print("\n--- Starting Nmap SYN Scan (-sS) ---")
    subprocess.run(["nmap", "-sS", target])
    time.sleep(15)

    print("\n--- Starting Nmap Version Detection (-sV) ---")
    subprocess.run(["nmap", "-sV", target])
    time.sleep(15)

    print("\n--- Starting Nmap OS Detection (-O) ---")
    subprocess.run(["nmap", "-O", target])
    time.sleep(15)

    print("\n--- Starting Nmap All Scans (-A) ---")
    subprocess.run(["nmap", "-A", target])
    time.sleep(15)

def run_nikto():
    target_url = input("Enter the target URL for Nikto: ")

    print("\n--- Starting Nikto Scan ---")
    subprocess.run(["nikto", "-h", target_url])
    time.sleep(15)

def run_sqlmap():
    target_url = input("Enter the target URL for SQLMap: ")

    print("\n--- Starting SQLMap Basic SQL Injection ---")
    subprocess.run(["sqlmap", "-u", target_url])
    time.sleep(15)

    print("\n--- Starting SQLMap Crawl and Scan ---")
    subprocess.run(["sqlmap", "-u", target_url, "--crawl=1"])
    time.sleep(15)

    print("\n--- Starting SQLMap DBMS-specific (MySQL) ---")
    subprocess.run(["sqlmap", "-u", target_url, "--dbms=mysql"])
    time.sleep(15)

def run_dnsrecon():
    domain = input("Enter the domain for DNSRecon: ")

    print("\n--- Starting DNSRecon Standard Enumeration ---")
    subprocess.run(["dnsrecon", "-d", domain])
    time.sleep(15)

    print("\n--- Starting DNSRecon Zone Transfer (-t axfr) ---")
    subprocess.run(["dnsrecon", "-d", domain, "-t", "axfr"])
    time.sleep(15)

    wordlist_path = "/usr/share/wordlists/dnsrecon/subdomains-top1million-110000.txt"
    if not os.path.exists(wordlist_path):
        print("\n--- Downloading wordlist for DNSRecon Brute Force ---")
        os.makedirs("/usr/share/wordlists/dnsrecon", exist_ok=True)
        urllib.request.urlretrieve("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-110000.txt", wordlist_path)

    print("\n--- Starting DNSRecon Brute Force (-D [wordlist] -t brt) ---")
    subprocess.run(["dnsrecon", "-d", domain, "-D", wordlist_path, "-t", "brt"])
    time.sleep(15)

def run_dnsenum():
    domain = input("Enter the domain for DNSEnum: ")

    print("\n--- Starting DNSEnum Standard Enumeration ---")
    subprocess.run(["dnsenum", domain])
    time.sleep(15)

    print("\n--- Starting DNSEnum Extended Enumeration (--enum) ---")
    subprocess.run(["dnsenum", domain, "--enum"])
    time.sleep(15)

def run_dirsearch():
    url = input("Enter the URL for Dirsearch: ")

    wordlist_path = "/usr/share/wordlists/dirsearch/dicc.txt"
    if not os.path.exists(wordlist_path):
        print("\n--- Downloading wordlist for Dirsearch ---")
        os.makedirs("/usr/share/wordlists/dirsearch", exist_ok=True)
        urllib.request.urlretrieve("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/dicc.txt", wordlist_path)

    print("\n--- Starting Dirsearch Default Scan ---")
    subprocess.run(["dirsearch", "-u", url, "-w", wordlist_path])
    time.sleep(15)

    print("\n--- Starting Dirsearch Recursive Scan (-r) ---")
    subprocess.run(["dirsearch", "-u", url, "-w", wordlist_path, "-r"])
    time.sleep(15)

    print("\n--- Starting Dirsearch Scan with Threads (-t 10) ---")
    subprocess.run(["dirsearch", "-u", url, "-w", wordlist_path, "-t", "10"])
    time.sleep(15)
