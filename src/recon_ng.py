import subprocess

def run_recon_ng_commands(commands):
    with open('/tmp/recon_ng_commands.txt', 'w') as f:
        f.write(commands)
    subprocess.run(['recon-ng', '-r', '/tmp/recon_ng_commands.txt'])
    subprocess.run(['rm', '/tmp/recon_ng_commands.txt'])

def install_module():
    module_name = input("Enter module name: ")
    commands = f"marketplace install {module_name}\nexit"
    run_recon_ng_commands(commands)

def install_multiple_modules():
    modules = ["profiles", "hackertarget", "brute_hosts", "whois_pocs", "interesting_files"]
    commands = "\n".join([f"marketplace install {module}" for module in modules])
    commands += "\nexit"
    run_recon_ng_commands(commands)

def search_marketplace():
    commands = "marketplace search\nexit"
    run_recon_ng_commands(commands)

def create_workspace():
    workspace_name = input("Enter workspace name: ")
    commands = f"workspaces create {workspace_name}\nexit"
    run_recon_ng_commands(commands)

def load_module():
    module_name = input("Enter module name: ")
    source_name = input("Enter source: ")
    commands = f"modules load {module_name}\noptions set SOURCE {source_name}\nrun\nexit"
    run_recon_ng_commands(commands)

def run_all_modules():
    source_name = input("Enter source: ")
    modules = ["profiler", "hackertarget", "brute_hosts", "whois_pocs", "interesting_files"]
    commands = ""
    for module in modules:
        commands += f"modules load {module}\noptions set SOURCE {source_name}\nrun\n"
    commands += "exit"
    run_recon_ng_commands(commands)

def add_api_key():
    api_name = input("Enter API name: ")
    api_key = input("Enter API key: ")
    commands = f"keys add {api_name} {api_key}\nexit"
    run_recon_ng_commands(commands)

def show_hosts():
    commands = "show hosts\nexit"
    run_recon_ng_commands(commands)

def show_contacts():
    commands = "show contacts\nexit"
    run_recon_ng_commands(commands)

def show_profiles():
    commands = "show profiles\nexit"
    run_recon_ng_commands(commands)

def show_gathered_information():
    commands = "show hosts\nshow contacts\nshow profiles\nexit"
    run_recon_ng_commands(commands)

def main():
    while True:
        print("Choose an option:")
        print("1. Install a module from marketplace")
        print("2. Install multiple modules (profiles, hackertarget, brute_hosts, whois_pocs, interesting_files)")
        print("3. Search the marketplace for modules")
        print("4. Create a workspace")
        print("5. Load a module")
        print("6. Run all specified modules")
        print("7. Show Hosts")
        print("8. Show Contacts")
        print("9. Show Profiles")
        print("10. Show Gathered Information")
        print("11. Add an API key")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            install_module()
        elif choice == '2':
            install_multiple_modules()
        elif choice == '3':
            search_marketplace()
        elif choice == '4':
            create_workspace()
        elif choice == '5':
            load_module()
        elif choice == '6':
            run_all_modules()
        elif choice == '7':
            show_hosts()
        elif choice == '8':
            show_contacts()
        elif choice == '9':
            show_profiles()
        elif choice == '10':
            show_gathered_information()
        elif choice == '11':
            add_api_key()
        elif choice == '12':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
