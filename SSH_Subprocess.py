import subprocess
from CSV_Functions import get_ssh_command

file_name = "" 

ssh_command = get_ssh_command(file_name, 1)

subprocess.run(ssh_command, shell=True)

