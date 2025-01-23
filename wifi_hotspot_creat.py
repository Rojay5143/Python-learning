# import subprocess
# subprocess.call('netsh wlan show drivers', shell=True)
# wifi_name = "rojay python"
# wifi_password = "Rojay@123"

# subprocess.call(f"netsh wlan set hostednetwork mode=allow ssid={wifi_name} key={wifi_password}",shell=True)
# subprocess.call("netsh wlan start hostednetwork", shell=True)

import subprocess

subprocess.call('netsh wlan show drivers',shell=True)

wifi_name = "R_wifi"
wifi_password = "@123ramhari"

subprocess.call(f"netsh wlan set hostednetwork mode=allow ssid={wifi_name} key={wifi_password}",shell=True)
subprocess.call("netsh wlan start hostednetwork",shell=True)