import os

def get_input(prompt, choices=None):
    if choices:
        prompt += " (" + "/".join(choices) + "): "
    else:
        prompt += ": "
    return input(prompt)

def main():
    command = "sudo docker run gospider"

    # Ask user if they want to input a single URL or a list
    url_choice = get_input("Do you want to input a single URL or have a list", ["single", "list"])
    if url_choice == "single":
        url = input("Enter the URL: ")
        command += f' -s "{url}"'
    else:
        list_path = input("Enter the path to the list: ")
        command += f' -S {list_path}'

    # Ask if the user wants only URLs in the output
    # only_urls = get_input("Do you want only URLs in output", ["y", "n"])
    # if only_urls == "y":
    #     command += " -q"

    # Ask for maximum concurrent requests
    # max_concurrent_requests = input("Enter the maximum number of concurrent requests for each site: ")
    # command += f" -c {max_concurrent_requests}"

    # Ask for depth
    # depth = input("Enter the depth: ")
    # command += f" -d {depth}"

    # Ask for the number of threads
    # threads = input("Enter the number of threads: ")
    # command += f" -t {threads}"

    # Ask if the user wants URLs from 3rd party sources
    # third_party_urls = get_input("Do you want URLs from 3rd party sources", ["y", "n"])
    # if third_party_urls == "y":
    #     command += " --other-source"
    #     include_subs = get_input("Do you want to include subdomains from 3rd parties", ["y", "n"])
    #     if include_subs == "y":
    #         command += " --include-subs"

    command += " --other-source --include-subs"

    # Ask if the user wants to save the output
    # save_output = get_input("Do you want to save the output", ["y", "n"])
    # if save_output == "y":
    #     filename = input("Enter the filename: ")
    #     command += f" -o {filename}"

    # Ask if the user wants to blacklist certain extensions
    # blacklist = get_input("Do you want to blacklist certain extensions", ["y", "n"])
    # if blacklist == "y":
    #     extensions = input("Enter the extensions to blacklist (separated by |, e.g., 'jpg|png|gif'): ")
    #     command += f' --blacklist ".({extensions})"'

    # Print and run the command
    print(f"Running command: {command}")
    os.system(command)

if __name__ == "__main__":
    main()
