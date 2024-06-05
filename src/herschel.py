import subprocess

def run_nmap():
    target = input("Enter target: ")
    print("Select scan type:")
    print("1. SYN Scan (-sS)")
    print("2. Version Detection (-sV)")
    print("3. OS Detection (-O)")
    print("4. All Scans (-A)")
    print("5. Custom")
    scan_choice = input("Enter your choice: ")
    
    if scan_choice == "5":
        custom_scan = input("Enter custom Nmap scan options: ")
        scan_type = custom_scan
    else:
        scan_options = {
            "1": "-sS",
            "2": "-sV",
            "3": "-O",
            "4": "-A"
        }
        scan_type = scan_options.get(scan_choice, "-sS")
    
    command = ["nmap", scan_type, target]
    subprocess.run(command)

def run_nikto():
    target_url = input("Enter target URL: ")
    options = input("Enter additional options (or press Enter for none): ").split()
    command = ["nikto", "-h", target_url] + options
    subprocess.run(command)

def run_sqlmap():
    target_url = input("Enter target URL: ")
    print("Select technique:")
    print("1. Basic SQL Injection")
    print("2. Crawl and Scan")
    print("3. DBMS-specific (MySQL)")
    print("4. Custom")
    sqlmap_choice = input("Enter your choice: ")

    if sqlmap_choice == "4":
        custom_technique = input("Enter custom SQLMap options: ")
        technique = custom_technique
    else:
        scan_options = {
            "1": "",
            "2": "--crawl=1",
            "3": "--dbms=mysql"
        }
        technique = scan_options.get(sqlmap_choice, "")

    command = ["sqlmap", "-u", target_url] + technique.split()
    subprocess.run(command)

def run_dnsrecon():
    domain = input("Enter domain: ")
    print("Select scan type:")
    print("1. Standard Enumeration")
    print("2. Zone Transfer (-t axfr)")
    print("3. Brute Force (-D [wordlist] -t brt)")
    print("4. Custom")
    dnsrecon_choice = input("Enter your choice: ")

    if dnsrecon_choice == "4":
        custom_scan = input("Enter custom DNSRecon options: ")
        scan_type = custom_scan
    elif dnsrecon_choice == "3":
        wordlist_path = input("Enter path to wordlist: ")
        scan_type = f"-D {wordlist_path} -t brt"
    else:
        scan_options = {
            "1": "",
            "2": "-t axfr",
            "3": f"-D {wordlist_path} -t brt"
        }
        scan_type = scan_options.get(dnsrecon_choice, "")

    command = ["dnsrecon", "-d", domain] + scan_type.split()
    subprocess.run(command)

def run_dnsenum():
    domain = input("Enter domain: ")
    print("Select scan type:")
    print("1. Standard Enumeration")
    print("2. Extended Enumeration (--enum)")
    print("3. Custom")
    dnsenum_choice = input("Enter your choice: ")

    if dnsenum_choice == "3":
        custom_options = input("Enter custom DNSEnum options: ")
        options = custom_options
    else:
        scan_options = {
            "1": "",
            "2": "--enum"
        }
        options = scan_options.get(dnsenum_choice, "")

    command = ["dnsenum", domain] + options.split()
    subprocess.run(command)

def run_dirsearch():
    url = input("Enter URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    print("Select additional options:")
    print("1. Default")
    print("2. Recursive (-r)")
    print("3. Threads (-t)")
    print("4. Custom")
    dirsearch_choice = input("Enter your choice: ")

    if dirsearch_choice == "4":
        custom_options = input("Enter custom Dirsearch options: ")
        options = custom_options
    elif dirsearch_choice == "3":
        threads = input("Enter number of threads: ")
        options = f"-t {threads}"
    else:
        scan_options = {
            "1": "",
            "2": "-r",
            "3": f"-t {threads}"
        }
        options = scan_options.get(dirsearch_choice, "")

    command = ["dirsearch", "-u", url, "-w", wordlist_path] + options.split()
    subprocess.run(command)
