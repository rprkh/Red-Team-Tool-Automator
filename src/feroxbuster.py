def main():
    import subprocess
    
    # Initialize the command
    command = ""
    
    # Ask if the user has an input file containing URLs
    has_input_file = input("Do you have an input file containing URLs? (y/n): ").strip().lower()
    if has_input_file == "y":
        input_file = input("Please provide the path to the input file: ").strip()
        command += f"cat {input_file} | feroxbuster --stdin"
    else:
        url = input("Please provide the URL: ").strip()
        command += f"feroxbuster -u {url}"
    
    # Ask for the path to the wordlist
    wordlist = input("Please provide the path to the wordlist: ").strip()
    command += f" -w {wordlist}"
    
    # Ask if the user only wants URLs in the output
    silent = input("Do you want only URLs in the output? (y/n): ").strip().lower()
    if silent == "y":
        command += " --silent"
    
    # Ask if the user wants the scan to be recursive
    # recursive = input("Do you want the scan to be recursive? (y/n): ").strip().lower()
    # if recursive == "n":
    #     command += " -n"
    
    # Ask if the user wants to look for particular file extensions
    # extensions = input("Do you want to look for particular file extensions? (y/n): ").strip().lower()
    # if extensions == "y":
    #     exts = input("Please provide the file extensions separated by spaces (e.g., php js): ").strip()
    #     command += f" -x {exts}"
    
    # Ask if the user wants to look for only particular status codes
    # status_codes = input("Do you want to look for only particular status codes? (y/n): ").strip().lower()
    # if status_codes == "y":
    #     codes = input("Please provide the status codes separated by spaces (e.g., 200 301): ").strip()
    #     command += f" -s {codes}"
    
    # Ask if the user does not want particular status codes
    # exclude_codes = input("Do you want to exclude particular status codes? (y/n): ").strip().lower()
    # if exclude_codes == "y":
    #     ex_codes = input("Please provide the status codes to exclude separated by spaces (e.g., 200 404): ").strip()
    #     command += f" -C {ex_codes}"
    
    # Ask if the user wants to save the output
    # save_output = input("Do you want to save the output to a file? (y/n): ").strip().lower()
    # if save_output == "y":
    #     output_file = input("Please provide the output file name (e.g., feroxbuster_output.txt): ").strip()
    #     command += f" -o {output_file}"
    
    # Print the final command
    print(f"The final command is:\n{command}")
    
    # Execute the command
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
