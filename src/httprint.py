import os

def run_httprint(server, signatures_file, output_dir):
    """
    Run Httprint analysis on a given server.

    Args:
        server (str): The URL of the server to analyze.
        signatures_file (str): Path to the signatures file for Httprint.
        output_dir (str): Output directory for reports.

    Returns:
        None
    """
    server_clean = server.translate(str.maketrans("", "", '[:punct:]'))
    print(f"Analyzing {server}...")

    # Run Httprint commands
    commands = [
        f"httprint -h {server} -s {signatures_file} > {output_dir}/{server_clean}_basic.txt",
        f"httprint -h {server} -s {signatures_file} -o {output_dir}/{server_clean}_report.html",
        f"httprint -h {server} -s {signatures_file} -oc {output_dir}/{server_clean}_report.csv",
        f"httprint -h {server} -s {signatures_file} -ox {output_dir}/{server_clean}_report.xml",
        f"httprint -h {server} -s {signatures_file} -noautossl > {output_dir}/{server_clean}_detailed.txt"
    ]

    for command in commands:
        os.system(command)

def main():
    # Take input for target servers
    servers_input = input("Enter target servers (separated by commas): ")
    servers = [server.strip() for server in servers_input.split(",")]

    # Path to signatures file
    signatures_file = "/usr/share/httprint/signatures.txt"  # Update this path if needed

    # Output directory for reports
    output_dir = "httprint_reports"
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each server and run Httprint
    for server in servers:
        run_httprint(server, signatures_file, output_dir)

    print("Httprint analysis completed for all servers.")

if __name__ == "__main__":
    main()
