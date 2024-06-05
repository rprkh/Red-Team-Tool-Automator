import subprocess

def prompt_input(prompt):
    return input(f"{prompt}: ")

def run_command(command):
    print(f"Executing command: {command}")
    subprocess.run(command, shell=True)

def main():
    while True:
        service = prompt_input("Enter service (e.g., ftp, http-get, https-get, http-post-form, https-post-form)")

        if service in ["http-post-form", "https-post-form"]:
            website = prompt_input("Enter website/domain")
            username_field = prompt_input("Enter ID of username field")
            password_field = prompt_input("Enter ID of password field")
            submit_field = prompt_input("Enter ID of submit button")
            error_message = prompt_input("Enter error message for incorrect credentials")
            username_type = prompt_input("Enter username type (single or list)")

            if username_type == "list":
                username_file = prompt_input("Enter path to username file")
                username_param = f"-L {username_file}"
            else:
                username = prompt_input("Enter username")
                username_param = f"-l {username}"

            password_type = prompt_input("Enter password type (single or list)")

            if password_type == "list":
                password_file = prompt_input("Enter path to password file")
                password_param = f"-P {password_file}"
            else:
                password = prompt_input("Enter password")
                password_param = f"-p {password}"

            threads = prompt_input("Enter number of threads")
            command = f"hydra {service}://{website} \":{username_field}=^USER^&{password_field}=^PASS^&{submit_field}=Submit:{error_message}\" {username_param} {password_param} -V -t {threads}"

        elif service in ["http-get", "https-get"]:
            website = prompt_input("Enter website/domain")
            username_field = prompt_input("Enter ID of username field")
            password_field = prompt_input("Enter ID of password field")
            submit_field = prompt_input("Enter ID of submit button")
            username_type = prompt_input("Enter username type (single or list)")

            if username_type == "list":
                username_file = prompt_input("Enter path to username file")
                username_param = f"-L {username_file}"
            else:
                username = prompt_input("Enter username")
                username_param = f"-l {username}"

            password_type = prompt_input("Enter password type (single or list)")

            if password_type == "list":
                password_file = prompt_input("Enter path to password file")
                password_param = f"-P {password_file}"
            else:
                password = prompt_input("Enter password")
                password_param = f"-p {password}"

            threads = prompt_input("Enter number of threads")
            command = f"hydra {username_param} {password_param} {service}://{website} \":{username_field}=^USER^&{password_field}=^PASS^&{submit_field}=Submit\" -V -t {threads}"

        else:
            host_option = prompt_input("Enter 'single' for one host or 'multiple' for multiple hosts")
            command = f"hydra {service}"

            if host_option == "single":
                host_ip = prompt_input("Enter host IP")
                port = prompt_input("Enter port")
                command += f"://{host_ip}:{port}"

            username_type = prompt_input("Enter username type (single or list)")

            if username_type == "list":
                username_file = prompt_input("Enter path to username file")
                username_param = f"-L {username_file}"
            else:
                username = prompt_input("Enter username")
                username_param = f"-l {username}"

            password_type = prompt_input("Enter password type (single or list)")

            if password_type == "list":
                password_file = prompt_input("Enter path to password file")
                password_param = f"-P {password_file}"
            else:
                password = prompt_input("Enter password")
                password_param = f"-p {password}"

            threads = prompt_input("Enter number of threads")
            command += f" {username_param} {password_param} -V -t {threads}"

            if host_option == "multiple":
                host_file = prompt_input("Enter path to host file")
                command += f" -M {host_file}"

        run_command(command)

        choice = prompt_input("Do you want to execute another command? (yes/no)")
        if choice.lower() not in ["yes", "y"]:
            break

if __name__ == "__main__":
    main()
