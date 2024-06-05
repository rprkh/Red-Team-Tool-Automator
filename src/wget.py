import subprocess

def main():
  """Prompts user for URL and flags, builds wget command, and executes it."""
  url = input("Enter the URL to download: ")
  recursive = input("Enable recursive download (-r)? (y/N): ").lower() == 'y'
  mirror = input("Enable mirroring (-m)? (y/N): ").lower() == 'y'
  wait_time = input("Set wait time between retries (-w)? (seconds, default: no wait): ")
  limit_rate = input("Set download rate limit (--limit-rate)? (kbps, default: no limit): ")
  verbose = input("Enable verbose output (-v)? (y/N): ").lower() == 'y'

  # Error handling for mutually exclusive flags
  if recursive and mirror:
    print("Error: -r and -m flags cannot be used together.")
    return

  # Build wget command string
  command = ["wget"]
  if recursive:
    command.append("-r")
  elif mirror:
    command.append("-m")
  if wait_time:
    command.append(f"-w {wait_time}")
  if limit_rate:
    command.append(f"--limit-rate={limit_rate}k")
  if verbose:
    command.append("-v")
  command.append(url)

  # Execute the wget command
  try:
    subprocess.run(command, check=True)
    print("Download complete!")
  except subprocess.CalledProcessError as e:
    print(f"Error: wget command failed - {e}")

if __name__ == "__main__":
  main()
