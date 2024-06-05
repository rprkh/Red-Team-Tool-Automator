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
    try:
      if option in ("-l", "-n", "-r"):
  
        return int(value)
      else:
        return value
    except ValueError:
      print("Invalid input. Please enter a valid value.")

def main():
  
  parser = argparse.ArgumentParser(description="metagoofil User Input Script")
  parser.add_argument("-d", "--domain", help="Domain to search")
  args = parser.parse_args()
  if not args.domain:
    args.domain = input("Enter domain to search: ")
  
  delay = get_user_input("set delay (seconds)")
  if delay:
    delay = get_flag_value("delay")

  save_file = get_user_input("save HTML links to a file")
  if save_file:
    save_file_choice = input("  - Don't save links (no -f)\n"
                             "  - Save links to default file (no argument to -f)\n"
                             "  - Save links to a custom file (-f <filename>)\n"
                             "Choose an option: ")
    if save_file_choice == "1":
      save_file = "-f"
    elif save_file_choice == "3":
      save_file = f"-f {get_flag_value('custom filename for links')}"
    else:
      save_file = ""

  url_timeout = get_user_input("set URL timeout (seconds)")
  if url_timeout:
    url_timeout = get_flag_value("URL timeout")

  search_max = get_user_input("set maximum search results")
  if search_max:
    search_max = get_flag_value("maximum search results")

  download_limit = get_user_input("set download file limit per type")
  if download_limit:
    download_limit = get_flag_value("download file limit")

  save_directory = get_user_input("set save directory for downloads")
  if save_directory:
    save_directory = get_flag_value("save directory")

  threads = get_user_input("set number of download threads")
  if threads:
    threads = get_flag_value("number of download threads")

  download_files = get_user_input("download files instead of viewing results")


  file_types = []
  file_type_options = ["pdf", "doc", "xls", "ppt", "odp", "ods", "docx", "xlsx", "pptx"]

  print("Select file types to download :")
  for i, option in enumerate(file_type_options):
      print(f"  {i+1}. {option}")
  choice = input("Enter your selections: ").lower().strip()

  selections = choice.split() 
  file_types.append(selections)
  file_types = [item for sublist in file_types for item in sublist]
  file_types = " ".join(file_types)


  command = "metagoofil"
  command += f" -d {args.domain}"
  if delay:
    command += f" -e {delay}"
  if save_file:
    command += f" {save_file}"
  if url_timeout:
    command += f" -i {url_timeout}"
  if search_max:
    command += f" -l {search_max}"
  if download_limit:
    command += f" -n {download_limit}"
  if save_directory:
    command += f" -o {save_directory}"
  if threads:
    command += f" -r {threads}"
  if download_files:
    command += " -w"
  if file_types:
    command += f" -t {file_types}"

  
  print(f"\nmetagoofil command based on your input:")
  print(command)
  print("\nThis may take some time. Please wait...\n")
  subprocess.run(command, shell=True)
  # os.system(command)

if __name__ == "__main__":
  main()