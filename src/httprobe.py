import os

def get_input(prompt, default=None):
    user_input = input(prompt)
    return user_input if user_input else default

def main():
    # Ask for the domains wordlist path
    wordlist_path = input("Enter the path to your domains wordlist: ")
    
    # Initialize the base command
    command = f"cat {wordlist_path} | httprobe"
    
    # Ask if user wants to set concurrency level
    # if get_input("Do you want to set concurrency level (default is 20)? (y/n): ").lower() == 'y':
    #     concurrency = get_input("Enter concurrency level: ")
    #     command += f" -c {concurrency}"
    
    # Ask if user wants to add additional probes
    # while get_input("Do you want to add additional probes? (y/n): ").lower() == 'y':
    #     additional_probe = get_input("Enter additional probe (e.g., http:81): ")
    #     command += f" -p {additional_probe}"
    
    # Ask if user wants to skip default probes
    # if get_input("Do you want to skip default probes (http:80 and https:443)? (y/n): ").lower() == 'y':
    #     command += " -s"
    
    # Ask if user wants to change the timeout
    # if get_input("Do you want to change the timeout (default is 10000 milliseconds)? (y/n): ").lower() == 'y':
    #     timeout = get_input("Enter timeout in milliseconds: ")
    #     command += f" -t {timeout}"
    
    # Ask if user wants to use any specific HTTP method
    # if get_input("Do you want to use any specific HTTP method? (y/n): ").lower() == 'y':
    #     http_method = get_input("Enter HTTP method: ")
    #     command += f" -method {http_method}"
    
    # Ask if user wants to try for HTTP only if HTTPS fails
    # if get_input("Do you want to try for HTTP only if HTTPS fails? (y/n): ").lower() == 'y':
    #     command += " -prefer-https"
    
    # Print the final command
    print("\nThe final httprobe command is:\n")
    print(command)
    
    # Execute the command
    os.system(command)

if __name__ == "__main__":
    main()
