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
        value = input(f"Enter value for {option}: ")
        return value

def get_flag_value_with_options(option, valid_options):
    while True:
        value = input(f"Enter value for {option}: ").strip()
        if value.lower() in valid_options:
            return value.lower()
        else:
            print("Invalid input. Please enter a valid enumeration type.")

def main():
    parser = argparse.ArgumentParser(description="dnsrecon User Input Script")
    args = parser.parse_args()

    domain = get_user_input("target domain")
    if domain:
        domain = get_flag_value("target domain")

    ns_server = get_user_input("name server")
    if ns_server:
        ns_server = get_flag_value("name server")

    ip_range = get_user_input("IP range for reverse lookup brute force")
    if ip_range:
        ip_range = get_flag_value("IP range")

    dictionary = get_user_input("dictionary file")
    if dictionary:
        dictionary = get_flag_value("dictionary file")

    filter_brute_force = get_user_input("filter out of brute force domain lookup")
    if filter_brute_force:
        filter_brute_force = "-f"

    perform_axfr = get_user_input("perform AXFR with standard enumeration")
    if perform_axfr:
        perform_axfr = "-a"

    perform_reverse_lookup_ipv4 = get_user_input("perform a reverse lookup of IPv4 ranges in the SPF record with standard enumeration")
    if perform_reverse_lookup_ipv4:
        perform_reverse_lookup_ipv4 = "-s"

    perform_bing_enum = get_user_input("perform Bing enumeration with standard enumeration")
    if perform_bing_enum:
        perform_bing_enum = "-b"

    perform_yandex_enum = get_user_input("perform Yandex enumeration with standard enumeration")
    if perform_yandex_enum:
        perform_yandex_enum = "-y"

    perform_crt_enum = get_user_input("perform crt.sh enumeration with standard enumeration")
    if perform_crt_enum:
        perform_crt_enum = "-k"

    deep_whois_analysis = get_user_input("perform deep whois record analysis and reverse lookup of IP ranges found through Whois when doing a standard enumeration")
    if deep_whois_analysis:
        deep_whois_analysis = "-w"

    perform_dnssec_zone_walk = get_user_input("performs a DNSSEC zone walk with standard enumeration")
    if perform_dnssec_zone_walk:
        perform_dnssec_zone_walk = "-z"

    threads = get_user_input("number of threads")
    if threads:
        threads = get_flag_value("number of threads")

    lifetime = get_user_input("time to wait for a server to respond to a query")
    if lifetime:
        lifetime = get_flag_value("time to wait")

    use_tcp = get_user_input("use TCP protocol to make queries")
    if use_tcp:
        use_tcp = "--tcp"

    db = get_user_input("SQLite 3 file to save found records")
    if db:
        db = get_flag_value("SQLite 3 file")

    xml = get_user_input("XML file to save found records")
    if xml:
        xml = get_flag_value("XML file")

    csv = get_user_input("comma separated value file to save output")
    if csv:
        csv = get_flag_value("CSV file")

    json_output = get_user_input("JSON file to save output")
    if json_output:
        json_output = get_flag_value("JSON file")

    continue_brute_force = get_user_input("continue brute forcing a domain even if a wildcard record is discovered")
    if continue_brute_force:
        continue_brute_force = "--iw"

    disable_check_recursion = get_user_input("disable check for recursion on name servers")
    if disable_check_recursion:
        disable_check_recursion = "--disable_check_recursion"

    disable_check_bindversion = get_user_input("disable check for BIND version on name servers")
    if disable_check_bindversion:
        disable_check_bindversion = "--disable_check_bindversion"

    verbose = get_user_input("enable verbose")
    if verbose:
        verbose = "-v"

    valid_enumeration_types = ["std", "rvl", "brt", "srv", "axfr", "bing", "yand", "crt", "snoop", "tld", "zonewalk"]
    enumeration_type = get_flag_value_with_options("type of enumeration to perform (std, rvl, brt, srv, axfr, bing, yand, crt, snoop, tld, zonewalk)", valid_enumeration_types)
    
    command = "python dnsrecon/dnsrecon.py"
    
    if domain:
        command += f" --domain {domain}"    
    if ns_server:
        command += f" -n {ns_server}"
    if ip_range:
        command += f" -r {ip_range}"
    if dictionary:
        command += f" -D {dictionary}"
    if filter_brute_force:
        command += f" {filter_brute_force}"
    if perform_axfr:
        command += f" {perform_axfr}"
    if perform_reverse_lookup_ipv4:
        command += f" {perform_reverse_lookup_ipv4}"
    if perform_bing_enum:
        command += f" {perform_bing_enum}"
    if perform_yandex_enum:
        command += f" {perform_yandex_enum}"
    if perform_crt_enum:
        command += f" {perform_crt_enum}"
    if deep_whois_analysis:
        command += f" {deep_whois_analysis}"
    if perform_dnssec_zone_walk:
        command += f" {perform_dnssec_zone_walk}"
    if threads:
        command += f" --threads {threads}"
    if lifetime:
        command += f" --lifetime {lifetime}"
    if use_tcp:
        command += f" {use_tcp}"
    if db:
        command += f" --db {db}"
    if xml:
        command += f" -x {xml}"
    if csv:
        command += f" -c {csv}"
    if json_output:
        command += f" -j {json_output}"
    if continue_brute_force:
        command += f" {continue_brute_force}"
    if disable_check_recursion:
        command += f" {disable_check_recursion}"
    if disable_check_bindversion:
        command += f" {disable_check_bindversion}"
    if verbose:
        command += f" {verbose}"
    if enumeration_type:
        command += f" -t {enumeration_type}"

    print(f"\ndnsrecon command based on your input: {command}")
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as subprocess_command_execution_error:
        print("Error executing command:", subprocess_command_execution_error)
        print("Please re-enter the command:")

if __name__ == "__main__":
    main()