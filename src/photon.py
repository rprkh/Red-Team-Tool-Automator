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
    parser = argparse.ArgumentParser(description="Photon User Input Script")
    args = parser.parse_args()

    url = get_flag_value("root URL")

    # use_cookie = get_user_input("cookie")
    # if use_cookie:
    #     cookie = get_flag_value("cookie")
    #     use_cookie = f"-c {cookie}"

    # use_regex = get_user_input("regex pattern")
    # if use_regex:
    #     regex = get_flag_value("regex pattern")
    #     use_regex = f"-r {regex}"

    # use_export = get_user_input("export format (csv/json)")
    # if use_export:
    #     export = get_flag_value("export format")
    #     use_export = f"-e {export}"

    # use_output = get_user_input("output directory")
    # if use_output:
    #     output = get_flag_value("output directory")
    #     use_output = f"-o {output}"

    # use_level = get_user_input("levels to crawl")
    # if use_level:
    #     level = get_flag_value("levels to crawl")
    #     use_level = f"-l {level}"

    # use_threads = get_user_input("number of threads")
    # if use_threads:
    #     threads = get_flag_value("number of threads")
    #     use_threads = f"-t {threads}"

    # use_delay = get_user_input("delay between requests")
    # if use_delay:
    #     delay = get_flag_value("delay between requests")
    #     use_delay = f"-d {delay}"

    # verbose = get_user_input("verbose output")
    # if verbose:
    #     verbose = "-v"

    # use_seeds = get_user_input("additional seed URLs")
    # if use_seeds:
    #     seeds = get_flag_value("additional seed URLs")
    #     use_seeds = f"-s {seeds}"

    # use_stdout = get_user_input("send variables to stdout")
    # if use_stdout:
    #     stdout = get_flag_value("send variables to stdout")
    #     use_stdout = f"--stdout {stdout}"

    # use_user_agent = get_user_input("custom user agent(s)")
    # if use_user_agent:
    #     user_agent = get_flag_value("custom user agent(s)")
    #     use_user_agent = f"--user-agent {user_agent}"

    # use_exclude = get_user_input("exclude URLs matching this regex")
    # if use_exclude:
    #     exclude = get_flag_value("exclude URLs matching this regex")
    #     use_exclude = f"--exclude {exclude}"

    # use_timeout = get_user_input("HTTP request timeout")
    # if use_timeout:
    #     timeout = get_flag_value("HTTP request timeout")
    #     use_timeout = f"--timeout {timeout}"

    # use_proxy = get_user_input("proxy server")
    # if use_proxy:
    #     proxy = get_flag_value("proxy server IP:PORT or DOMAIN:PORT")
    #     use_proxy = f"-p {proxy}"

    # clone = get_user_input("clone the website locally")
    # if clone:
    #     clone = "--clone"

    # add_headers = get_user_input("add headers")
    # if add_headers:
    #     add_headers = "--headers"

    # enumerate_dns = get_user_input("enumerate subdomains and DNS data")
    # if enumerate_dns:
    #     enumerate_dns = "--dns"

    # find_keys = get_user_input("find secret keys")
    # if find_keys:
    #     find_keys = "--keys"

    # update_photon = get_user_input("update photon")
    # if update_photon:
    #     update_photon = "--update"

    # only_urls = get_user_input("only extract URLs")
    # if only_urls:
    #     only_urls = "--only-urls"

    # use_wayback = get_user_input("fetch URLs from archive.org as seeds")
    # if use_wayback:
    #     use_wayback = "--wayback"

    command = f"python3 Photon/photon.py -u {url}"

    # if use_cookie:
    #     command += f" {use_cookie}"
    # if use_regex:
    #     command += f" {use_regex}"
    # if use_export:
    #     command += f" {use_export}"
    # if use_output:
    #     command += f" {use_output}"
    # if use_level:
    #     command += f" {use_level}"
    # if use_threads:
    #     command += f" {use_threads}"
    # if use_delay:
    #     command += f" {use_delay}"
    # if verbose:
    #     command += f" {verbose}"
    # if use_seeds:
    #     command += f" {use_seeds}"
    # if use_stdout:
    #     command += f" {use_stdout}"
    # if use_user_agent:
    #     command += f" {use_user_agent}"
    # if use_exclude:
    #     command += f" {use_exclude}"
    # if use_timeout:
    #     command += f" {use_timeout}"
    # if use_proxy:
    #     command += f" {use_proxy}"
    # if clone:
    #     command += f" {clone}"
    # if add_headers:
    #     command += f" {add_headers}"
    # if enumerate_dns:
    #     command += f" {enumerate_dns}"
    # if find_keys:
    #     command += f" {find_keys}"
    # if update_photon:
    #     command += f" {update_photon}"
    # if only_urls:
    #     command += f" {only_urls}"
    # if use_wayback:
    #     command += f" {use_wayback}"

    print(f"\nPhoton command based on your input: {command}")

    try:
        subprocess.run(command + " -t 2 -v --keys", shell=True, check=True)
        subprocess.run(command + " -e json -l 2 -t 4", shell=True, check=True)
    except subprocess.CalledProcessError as subprocess_command_execution_error:
        print("Error executing command:", subprocess_command_execution_error)
        print("Please re-enter the command:")

if __name__ == "__main__":
    main()
