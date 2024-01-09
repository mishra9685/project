#All install software's list

import winreg

# Open the registry key where software information is stored
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")

# Function to get installed software list
def get_installed_software(key):
    software_list = []
    index = 0
    while True:
        try:
            subkey_name = winreg.EnumKey(key, index)
            subkey = winreg.OpenKey(key, subkey_name)
            displayName, _ = winreg.QueryValueEx(subkey, 'DisplayName')
            software_list.append(displayName)
            index += 1
        except FileNotFoundError:
            break
    return software_list

installed_software = get_installed_software(key)

# Print the list of installed software
for software in installed_software:
    print("All installed file:-", software)


# import speedtest

# def test_internet_speed():
#     st = speedtest.Speedtest()
#     st.get_best_server()
#     download_speed = st.download() / 1_000_000  # in Mbps
#     upload_speed = st.upload() / 1_000_000  # in Mbps
#     ping = st.results.ping  # in ms

#     print(f"Download Speed: {download_speed:.2f} Mbps")
#     print(f"Upload Speed: {upload_speed:.2f} Mbps")
#     print(f"Ping: {ping} ms")

# if __name__ == "__main__":
#     test_internet_speed()

#check screen resolution

import pyautogui

# Get the screen resolution
screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution: {screen_width}x{screen_height}")


#cpu model

import platform

cpu_model = platform.processor()
print(f"CPU Model: {cpu_model}")

#no of core and threads of cpu

import psutil

# Get CPU information
cpu_info = psutil.cpu_count()

# Extract number of CPU cores and threads
num_cores = psutil.cpu_count(logical=False)  # Physical cores
num_threads = psutil.cpu_count(logical=True)  # Total threads (including hyperthreading)

print(f"Number of CPU Cores: {num_cores}")
print(f"Number of Threads (including hyperthreading): {num_threads}")


#gpu model(if exist)

import wmi

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0]
        gpu_model = gpu_info.Name
        return gpu_model
    except Exception as e:
        print(f"Error retrieving GPU information: {e}")
        return None

gpu_model = get_gpu_info()
if gpu_model:
    print(f"GPU Model: {gpu_model}")
else:
    print("GPU information not available")


#Ram size (in gb)

import psutil

# Get total RAM size in bytes
total_ram = psutil.virtual_memory().total

# Convert bytes to gigabytes
total_ram_gb = total_ram / (1024 ** 3)  # 1 GB = 1024^3 bytes

print(f"Total RAM: {total_ram_gb:.2f} GB")


#screen size (like, 15 inch, 21 inch)

# import subprocess

# def get_screen_size():
#     try:
#         command = "xrandr | grep -w 'connected primary'"
#         output = subprocess.check_output(command, shell=True, text=True)
#         size_info = output.split()[2]  # Extracts the size portion from xrandr output
#         return size_info
#     except Exception as e:
#         print(f"Error retrieving screen size: {e}")
#         return None

# screen_size = get_screen_size()
# if screen_size:
#     print(f"Screen Size: {screen_size}")
# else:
#     print("Screen size information not available")


#public ip address

import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException as e:
        print(f"Error retrieving public IP address: {e}")
        return None

public_ip = get_public_ip()
if public_ip:
    print(f"Public IP Address: {public_ip}")
else:
    print("Public IP address not found")

    #windows version

import platform

windows_version = platform.win32_ver()
print(f"Windows Version: {windows_version[0]}")


    #wifi/ethernet mac address

import psutil

def get_mac_addresses():
    interfaces = psutil.net_if_addrs()
    mac_addresses = {}
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == psutil.AF_LINK:
                mac_addresses[interface_name] = address.address
    return mac_addresses

mac_addresses = get_mac_addresses()
for interface, mac_address in mac_addresses.items():
    print(f"Interface: {interface}, MAC Address: {mac_address}")

#Window sizes
#     from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#internet speed in widow

import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000  # in Mbps
    ping = st.results.ping  # in ms

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    test_internet_speed()

