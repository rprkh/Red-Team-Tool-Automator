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
    parser = argparse.ArgumentParser(description="wfuzz User Input Script")
    args = parser.parse_args()

    use_colors = get_user_input("colors")
    if use_colors:
        use_colors = "-c"

    concurrent_connections = get_user_input("number of concurrent connections")
    if concurrent_connections:
        concurrent_connections = get_flag_value("number of concurrent connections")

    time_delay = get_user_input("time delay between requests")
    if time_delay:
        time_delay = get_flag_value("time delay")

    follow_redirects = get_user_input("follow HTTP redirections")
    if follow_redirects:
        follow_redirects = "-L"

    use_proxy = get_user_input("use proxy")
    if use_proxy:
        proxy_address = get_flag_value("proxy address")
        use_proxy = f"-p {proxy_address}"

    use_payload = get_user_input("use payload")
    if use_payload:
        payload = input("Enter payload (in the form of name[,parameter][,encoder]): ").strip()

    wordlist = get_user_input("use wordlist")
    if wordlist:
        wordlist_file = get_flag_value("wordlist file")
        wordlist = f"-w {wordlist_file}"

    dry_run = get_user_input("dry run")
    if dry_run:
        dry_run = "--dry-run"

    prev_requests = get_user_input("print the previous HTTP requests")
    if prev_requests:
        prev_requests = "--prev"

    hide_responses_code = get_user_input("hide responses with the specified code")
    if hide_responses_code:
        hide_responses_code_value = get_flag_value("hide responses with the specified code")
        hide_responses_code = f"--hc {hide_responses_code_value}"

    hide_responses_lines = get_user_input("hide responses with the specified lines")
    if hide_responses_lines:
        hide_responses_lines_value = get_flag_value("hide responses with the specified lines")
        hide_responses_lines = f"--hl {hide_responses_lines_value}"

    hide_responses_words = get_user_input("hide responses with the specified words")
    if hide_responses_words:
        hide_responses_words_value = get_flag_value("hide responses with the specified words")
        hide_responses_words = f"--hw {hide_responses_words_value}"

    hide_responses_chars = get_user_input("hide responses with the specified chars")
    if hide_responses_chars:
        hide_responses_chars_value = get_flag_value("hide responses with the specified chars")
        hide_responses_chars = f"--hh {hide_responses_chars_value}"

    show_responses_code = get_user_input("show responses with the specified code")
    if show_responses_code:
        show_responses_code_value = get_flag_value("show responses with the specified code")
        show_responses_code = f"--sc {show_responses_code_value}"

    show_responses_lines = get_user_input("show responses with the specified lines")
    if show_responses_lines:
        show_responses_lines_value = get_flag_value("show responses with the specified lines")
        show_responses_lines = f"--sl {show_responses_lines_value}"

    show_responses_words = get_user_input("show responses with the specified words")
    if show_responses_words:
        show_responses_words_value = get_flag_value("show responses with the specified words")
        show_responses_words = f"--sw {show_responses_words_value}"

    show_responses_chars = get_user_input("show responses with the specified chars")
    if show_responses_chars:
        show_responses_chars_value = get_flag_value("show responses with the specified chars")
        show_responses_chars = f"--sh {show_responses_chars_value}"

    show_hide_regex = get_user_input("show/hide responses with the specified regex within the content")
    if show_hide_regex:
        show_hide_regex_value = get_flag_value("show/hide responses with the specified regex within the content")
        show_hide_regex = f"--ss {show_hide_regex_value}"

    http_opt_method = get_user_input("Enter the HTTP method, if not already added as part of the payload")
    if http_opt_method:
        http_opt_method = get_flag_value("Enter the HTTP method, if not already added as part of the payload")

    command = "wfuzz"
    if use_colors:
        command += f" {use_colors}"
    if concurrent_connections:
        command += f" -t {concurrent_connections}"
    if time_delay:
        command += f" -s {time_delay}"
    if follow_redirects:
        command += f" {follow_redirects}"
    if use_proxy:
        command += f" {use_proxy}"
    if use_payload:
        command += f" -z {payload}"
    if wordlist:
        command += f" {wordlist}"
    if dry_run:
        command += f" {dry_run}"
    if prev_requests:
        command += f" {prev_requests}"
    if hide_responses_code:
        command += f" {hide_responses_code}"
    if hide_responses_lines:
        command += f" {hide_responses_lines}"
    if hide_responses_words:
        command += f" {hide_responses_words}"
    if hide_responses_chars:
        command += f" {hide_responses_chars}"
    if show_responses_code:
        command += f" {show_responses_code}"
    if show_responses_lines:
        command += f" {show_responses_lines}"
    if show_responses_words:
        command += f" {show_responses_words}"
    if show_responses_chars:
        command += f" {show_responses_chars}"
    if show_hide_regex:
        command += f" {show_hide_regex}"
    if http_opt_method:
        command += f" {http_opt_method}"

    print(f"\nwfuzz command based on your input: {command}")
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as subprocess_command_execution_error:
        print("Error executing command:", subprocess_command_execution_error)
        print("Please re-enter the command:")
    except UserWarning as user_warning:
        print("User warning:", user_warning)

if __name__ == "__main__":
    main()