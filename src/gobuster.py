import subprocess

def directory_enum():
    website_url = input("Enter website URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'dir', '-u', website_url, '-w', wordlist_path])

def subdomain_enum():
    domain = input("Enter domain: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'dns', '-d', domain, '-w', wordlist_path, '--wildcard'])

def s3_enum():
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 's3', '-w', wordlist_path])

def vhost_enum():
    website_url = input("Enter website URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'vhost', '-u', website_url, '-w', wordlist_path])

def gcs_enum():
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'gcs', '-w', wordlist_path])

def tftp_enum():
    wordlist_path = input("Enter path to wordlist: ")
    tftp_server = input("Enter target TFTP server: ")
    subprocess.run(['gobuster', 'tftp', '-s', tftp_server, '-w', wordlist_path])

def directory_and_subdomain_enum():
    website_url = input("Enter website URL for directory enumeration: ")
    wordlist_path_dir = input("Enter path to wordlist for directory enumeration: ")
    subprocess.run(['gobuster', 'dir', '-u', website_url, '-w', wordlist_path_dir])

    domain = input("Enter domain for subdomain enumeration: ")
    wordlist_path_sub = input("Enter path to wordlist for subdomain enumeration: ")
    subprocess.run(['gobuster', 'dns', '-d', domain, '-w', wordlist_path_sub, '--wildcard'])

def main():
    while True:
        print("Select an option:")
        print("1. Directory Enumeration")
        print("2. Subdomain Enumeration")
        print("3. S3 Bucket Enumeration")
        print("4. VHost Enumeration")
        print("5. GCS Enumeration")
        print("6. TFTP Enumeration")
        print("7. Directory and Subdomain Enumeration")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            directory_enum()
        elif choice == '2':
            subdomain_enum()
        elif choice == '3':
            s3_enum()
        elif choice == '4':
            vhost_enum()
        elif choice == '5':
            gcs_enum()
        elif choice == '6':
            tftp_enum()
        elif choice == '7':
            directory_and_subdomain_enum()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a number from 1 to 8.")

if __name__ == "__main__":
    main()
