import subprocess

def get_target():
    target = input("Enter target(s) (URL, hostname, IP address, filename, or IP range): ")
    return target

def get_input_file():
    input_file = input("Enter input file (or press Enter to skip): ")
    if input_file:
        return f"-i {input_file}"
    return ""

def get_url_prefix():
    url_prefix = input("Enter URL prefix (or press Enter to skip): ")
    if url_prefix:
        return f"--url-prefix {url_prefix}"
    return ""

def get_url_suffix():
    url_suffix = input("Enter URL suffix (or press Enter to skip): ")
    if url_suffix:
        return f"--url-suffix {url_suffix}"
    return ""

def get_url_pattern():
    url_pattern = input("Enter URL pattern (or press Enter to skip): ")
    if url_pattern:
        return f"--url-pattern {url_pattern}"
    return ""

def get_aggression_level():
    aggression_level = input("Enter aggression level (1, 3, or 4) [default: 1]: ")
    if aggression_level:
        return f"-a {aggression_level}"
    return "-a 1"

def get_user_agent():
    user_agent = input("Enter user agent (or press Enter to skip): ")
    if user_agent:
        return f"-U {user_agent}"
    return ""

def get_header():
    header = input("Enter HTTP header (or press Enter to skip): ")
    if header:
        return f"-H {header}"
    return ""

def get_follow_redirects():
    follow_redirects = input("Enter follow redirects option (never, http-only, meta-only, same-site, or always) [default: always]: ")
    if follow_redirects:
        return f"--follow-redirect={follow_redirects}"
    return "--follow-redirect=always"

def get_max_redirects():
    max_redirects = input("Enter maximum redirects [default: 10]: ")
    if max_redirects:
        return f"--max-redirects={max_redirects}"
    return "--max-redirects=10"

def get_auth():
    auth = input("Enter HTTP basic authentication (username:password) [or press Enter to skip]: ")
    if auth:
        return f"-u {auth}"
    return ""

def get_cookie():
    cookie = input("Enter cookies (name=value; name2=value2) [or press Enter to skip]: ")
    if cookie:
        return f"-c {cookie}"
    return ""

def get_proxy():
    proxy = input("Enter proxy hostname and port (or press Enter to skip): ")
    if proxy:
        return f"--proxy {proxy}"
    return ""

def get_plugins():
    plugins = input("Enter plugins (comma-delimited list) [or press Enter to skip]: ")
    if plugins:
        return f"-p {plugins}"
    return ""

def get_grep():
    grep = input("Enter search string or regular expression [or press Enter to skip]: ")
    if grep:
        return f"-g {grep}"
    return ""

def get_custom_plugin():
    custom_plugin = input("Enter custom plugin definition [or press Enter to skip]: ")
    if custom_plugin:
        return f"--custom-plugin={custom_plugin}"
    return ""

def get_output_options():
    verbose = input("Enable verbose output? (y/n) [default: n]: ")
    if verbose.lower() == 'y':
        return "-v"
    colour = input("Enable colour output? (y/n) [default: auto]: ")
    if colour.lower() == 'y':
        return "--colour=always"
    quiet = input("Suppress brief logging to STDOUT? (y/n) [default: n]: ")
    if quiet.lower() == 'y':
        return "-q"
    return ""

def get_logging_options():
    log_brief = input("Enter log brief file [or press Enter to skip]: ")
    if log_brief:
        return f"--log-brief={log_brief}"
    log_verbose = input("Enter log verbose file [or press Enter to skip]: ")
    if log_verbose:
        return f"--log-verbose={log_verbose}"
    return ""

def get_performance_options():
    max_threads = input("Enter maximum threads [default: 25]: ")
    if max_threads:
        return f"-t {max_threads}"
    open_timeout = input("Enter open timeout [default: 15]: ")
    if open_timeout:
        return f"--open-timeout={open_timeout}"
    read_timeout = input("Enter read timeout [default: 30]: ")
    if read_timeout:
        return f"--read-timeout={read_timeout}"
    wait = input("Enter wait time between connections [default: 0]: ")
    if wait:
        return f"--wait={wait}"
    return ""

def build_command():
    target = get_target()
    input_file = get_input_file()
    url_prefix = get_url_prefix()
    url_suffix = get_url_suffix()
    url_pattern = get_url_pattern()
    aggression_level = get_aggression_level()
    user_agent = get_user_agent()
    header = get_header()
    follow_redirects = get_follow_redirects()
    max_redirects = get_max_redirects()
    auth = get_auth()
    cookie = get_cookie()
    proxy = get_proxy()
    plugins = get_plugins()
    grep = get_grep()
    custom_plugin = get_custom_plugin()
    output_options = get_output_options()
    logging_options = get_logging_options()
    performance_options = get_performance_options()

    command = f"whatweb {target} {input_file} {url_prefix} {url_suffix} {url_pattern} {aggression_level} {user_agent} {header} {follow_redirects} {max_redirects} {auth} {cookie} {proxy} {plugins} {grep} {custom_plugin} {output_options} {logging_options} {performance_options}"
    return command

def execute_command(command):
    subprocess.run(command, shell=True)

def main():
    command = build_command()
    print(f"Executing command: {command}")
    execute_command(command)

if __name__ == "__main__":
  main()