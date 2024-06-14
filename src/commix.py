import subprocess

def get_user_input(prompt, flag, command, is_required=False):
    value = input(prompt)
    if value or is_required:
        return f'{command} {flag}="{value}"'
    return command

def main():
    print("Refer https://docs.google.com/document/d/1P_whor_76MX8dZYPRxul5Lx14QrLlCby/edit?usp=sharing&ouid=106471594549028288584&rtpof=true&sd=true to know how to use the tool")
    command = "commix"
    
    # Target URL
    url = input("Enter target URL: ")
    command += f' --url="{url}"'
    
    # HTTP Cookie
    cookie_needed = input("Do you want to enter the HTTP cookie? (y/n): ").strip().lower()
    if cookie_needed == 'y':
        cookie = input("Enter the HTTP cookie: ")
        command += f' --cookie="{cookie}"'
    
    # Data string to be sent through POST
    data_needed = input("Do you want to enter a Data string to be sent through POST? (y/n): ").strip().lower()
    if data_needed == 'y':
        data = input("Enter the Data string: ")
        command += f' --data="{data}"'
    
    # Web server document root directory
    # command = get_user_input("Enter web server document root directory (leave blank if not needed): ", "--web-root", command)
    
    # Injection payload prefix string
    # command = get_user_input("Enter Injection payload prefix string (leave blank if not needed): ", "--prefix", command)
    
    # Injection payload suffix string
    # command = get_user_input("Enter Injection payload suffix string (leave blank if not needed): ", "--suffix", command)
    
    # Extra headers
    # command = get_user_input("Enter Extra headers (leave blank if not needed): ", "--headers", command)
    
    # Proxy to connect to the target URL
    # command = get_user_input("Enter proxy to connect to the target URL (leave blank if not needed): ", "--proxy", command)
    
    # Alternative OS shell
    # command = get_user_input("Enter alternative OS shell (leave blank if not needed): ", "--alter-shell", command)
    
    # Injection technique(s) to use
    # command = get_user_input("Enter injection technique(s) to use (leave blank if not needed): ", "--technique", command)
    
    # Shellshock injection module
    # shellshock_needed = input("Do you want to use the Shellshock injection module? (y/n): ").strip().lower()
    # if shellshock_needed == 'y':
    #     command += ' --shellshock'
    
    # Level of tests to perform
    # level = input("Enter the level of tests to perform (1-3, Default: 1): ").strip()
    # if level:
    #     command += f' --level={level}'
    
    # Additional flags
    # additional_flags_needed = input("Do you want to enter additional flags? (y/n): ").strip().lower()
    # if additional_flags_needed == 'y':
    #     additional_flags = input("Enter additional flags: ")
    #     command += f' {additional_flags}'

    print(f"Generated command: {command}")
    
    # Execute the command
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
