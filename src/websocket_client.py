import argparse
import subprocess

def get_user_input(option, default=False):
    while True:
        response = input(f"Use {option}? (y/n) [default: {'Yes' if default else 'No'}] ").lower().strip()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_flag_value(option):
    while True:
        value = input(f"Enter value for {option}: ").strip()
        return value

def main():
    parser = argparse.ArgumentParser(description="WebSocket User Input Script")
    args = parser.parse_args()

    ws_url = get_user_input("ws based URL")
    if ws_url:
        ws_url = get_flag_value("ws based URL")

    proxy = get_user_input("proxy")
    if proxy:
        proxy = get_flag_value("proxy")

    verbose = get_user_input("verbose")
    if verbose:
        verbose = get_flag_value("verbose")

    ignore_invalid_ssl_certificate_flag = get_user_input("ignoring SSL certificate")

    raw_output = get_user_input("raw output")

    text = get_user_input("text")
    if text:
        text = get_flag_value("text")

    eof_wait_time = get_user_input("EOF wait time")
    if eof_wait_time:
        eof_wait_time = get_flag_value("EOF wait time")

    timings = get_user_input("timings")

    command = "python websocket_client/wsdump.py"

    if ws_url:
        command += f" {ws_url}"

    if proxy:
        command += f" -p {proxy}"

    if verbose:
        command += f" -v {verbose}"

    if ignore_invalid_ssl_certificate_flag:
        command += f" -n"

    if raw_output:
        command += f" -r"

    if text:
        command += f" -t {text}"

    if eof_wait_time:
        command += f" --eof-wait {eof_wait_time}"

    if timings:
        command += f" --timings"

    print(f"\nwebsocket-client command based on your input: {command}")

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as subprocess_command_execution_error:
        print("Error executing command:", subprocess_command_execution_error)
        print("Please re-enter the command:")
    except KeyboardInterrupt:
        print("\nExiting the websocket-client.")

if __name__ == "__main__":
    main()