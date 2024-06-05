import os

def run_command(command):
    result = os.system(command)
    if result != 0:
        print(f"Error executing command: {command}")

def main():
    # Define target networks
    networks = ["192.168.1.5/24"]

    # Output directory for reports
    output_dir = "unicornscan_reports"
    os.makedirs(output_dir, exist_ok=True)

    for network in networks:
        network_clean = network.translate(str.maketrans("", "", '[:punct:]'))
        print(f"Scanning network {network}...")

        # Run Unicornscan with sudo and output results to files
        run_command(f"sudo unicornscan -i eth0 {network} > {output_dir}/{network_clean}_results.txt")

    print("Unicornscan analysis completed for all networks.")

if __name__ == "__main__":
    main()
