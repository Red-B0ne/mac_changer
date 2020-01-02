import subprocess
import time
import re

print("""

______         _  ______  _____
| ___ \       | | | ___ \|  _  |
| |_/ /___  __| | | |_/ /| |/' |_ __   ___
|    // _ \/ _` | | ___ \|  /| | '_ \ / _ 
| |\ \  __/ (_| | | |_/ /\ |_/ / | | |  __/
\_| \_\___|\__,_| \____/  \___/|_| |_|\___|
              ______
             |______|

             """)

time.sleep(1)

interface = input("[+] What interface would you like to change? ")
new_mac = input("[+] What is the new MAC address? ")

if not interface:
    print("[-] You must specify an interface")
    exit()
elif not new_mac:
    print("[-] You must specify a MAC address")
    exit()

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

output = subprocess.check_output(["ifconfig", interface]).decode('utf-8')

mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)

if mac_result:
    print("[+] The current MAC address is " + mac_result.group(0))
else:
    print("[-] Could not read MAC address")
