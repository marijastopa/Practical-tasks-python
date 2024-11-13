import argparse
import psutil
import platform
import socket
import getpass

def get_distro_info():
    return platform.platform()

def get_memory_info():
    memory = psutil.virtual_memory()
    return f"Total: {memory.total}, Used: {memory.used}, Free: {memory.free}"

def get_cpu_info():
    cpu_info = platform.processor()
    return f"CPU: {cpu_info}, Cores: {psutil.cpu_count(logical=False)}, Speed: {psutil.cpu_freq().current} MHz"

def get_user_info():
    return getpass.getuser()

def get_load_average():
    return psutil.getloadavg()

def get_ip_address():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "IP Address information unavailable. Please check your network connection."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="System Info Script")
    parser.add_argument("-d", action="store_true", help="Show distro info")
    parser.add_argument("-m", action="store_true", help="Show memory info")
    parser.add_argument("-c", action="store_true", help="Show CPU info")
    parser.add_argument("-u", action="store_true", help="Show user info")
    parser.add_argument("-l", action="store_true", help="Show load average")
    parser.add_argument("-i", action="store_true", help="Show IP address")
    args = parser.parse_args()

    if args.d:
        print("Distro Info:", get_distro_info())
    if args.m:
        print("Memory Info:", get_memory_info())
    if args.c:
        print("CPU Info:", get_cpu_info())
    if args.u:
        print("User Info:", get_user_info())
    if args.l:
        print("Load Average:", get_load_average())
    if args.i:
        print("IP Address:", get_ip_address())

