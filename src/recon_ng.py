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

def main():
    while True:
        print("Choose an option:")
        print("1. Install a module from marketplace")
        print("2. Search the marketplace for modules")
        print("3. Create a workspace")
        print("4. Load a module")
        print("5. Show Hosts")
        print("6. Show Contacts")
        print("7. Add an API key")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            install_module()
        elif choice == '2':
            search_marketplace()
        elif choice == '3':
            create_workspace()
        elif choice == '4':
            load_module()
        elif choice == '5':
            show_hosts()
        elif choice == '6':
            show_contacts()
        elif choice == '7':
            add_api_key()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
