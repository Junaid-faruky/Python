import subprocess

wifi_list = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
profiles = [line.split(":")[1].strip() for line in wifi_list.split('\n') if "All User Profile" in line]
for profile in profiles:
    result = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True).decode()
    for line in result.split('\n'):
        if "Key Content" in line:
            password = line.split(":")[1].strip()
            print(f"{profile}: {password}")
