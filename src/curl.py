# curl_commands.py
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def curl_operations():
    # Basic HTTP GET request
    print("Performing basic HTTP GET request...")
    run_command('curl https://www.instagram.com')

    # Analyzing robots.txt
    print("Analyzing robots.txt...")
    run_command('curl https://www.instagram.com/robots.txt')

    # Retrieving meta tags
    print("Retrieving meta tags...")
    run_command('curl -i https://www.instagram.com')

    # Inspecting comments and code metadata
    print("Inspecting comments and code metadata...")
    run_command('curl -s https://www.instagram.com | grep "<!--"')

    # Analyzing WAF: Observe response headers and behavior for WAF indications
    print("Analyzing WAF...")
    run_command('curl -I https://www.instagram.com')

    # Proxy usage (uncomment and replace <proxy_host> and <proxy_port> with actual values)
    # print("Using proxy...")
    # run_command('curl -x <proxy_host>:<proxy_port> https://www.instagram.com')

    # Backend database detection: Manual analysis required
    print("Backend database detection requires manual analysis.")

    # Creating a local copy of the website
    print("Creating a local copy of the website...")
    run_command('curl -o instagram.html https://www.instagram.com')

    # Analyzing HTTP methods
    print("Analyzing HTTP methods...")
    run_command('curl -X OPTIONS https://www.instagram.com')

    # Checking security headers
    print("Checking security headers...")
    run_command('curl -I https://www.instagram.com')

    print("Curl commands executed successfully.")
